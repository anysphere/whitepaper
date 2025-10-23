#!/usr/bin/env python3
"""
Multi-File Reader and Analyzer
==============================

This script provides comprehensive functionality for reading and analyzing multiple files
in parallel. It's designed to handle various file types and provide useful analysis.

Features:
- Parallel file reading for performance
- Support for multiple file types (text, LaTeX, markdown, etc.)
- File content analysis and statistics
- Search and filtering capabilities
- Export functionality
- Progress tracking for large file sets

Usage:
    python file_reader.py [options] [file_patterns...]
"""

import os
import sys
import glob
import asyncio
import aiofiles
import argparse
import json
import time
from pathlib import Path
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass, asdict
from concurrent.futures import ThreadPoolExecutor
import mimetypes
import hashlib
import re
from collections import Counter, defaultdict

@dataclass
class FileInfo:
    """Information about a file."""
    path: str
    size: int
    mime_type: str
    extension: str
    content_hash: str
    line_count: int
    word_count: int
    char_count: int
    read_time: float
    error: Optional[str] = None

@dataclass
class AnalysisResult:
    """Results of file analysis."""
    total_files: int
    total_size: int
    total_lines: int
    total_words: int
    total_chars: int
    file_types: Dict[str, int]
    largest_files: List[FileInfo]
    most_common_words: List[tuple]
    processing_time: float
    files: List[FileInfo]

class MultiFileReader:
    """Main class for reading and analyzing multiple files."""
    
    def __init__(self, max_workers: int = 10):
        self.max_workers = max_workers
        self.supported_extensions = {
            '.txt', '.md', '.tex', '.py', '.js', '.ts', '.html', '.css', 
            '.json', '.xml', '.yaml', '.yml', '.csv', '.log', '.cfg', 
            '.ini', '.conf', '.sh', '.bash', '.zsh', '.fish', '.ps1',
            '.c', '.cpp', '.h', '.hpp', '.java', '.go', '.rs', '.php',
            '.rb', '.pl', '.lua', '.r', '.m', '.swift', '.kt', '.scala',
            '.bib', '.sty', '.cls', '.pdf', '.doc', '.docx'
        }
    
    async def read_file_async(self, file_path: str) -> FileInfo:
        """Read a single file asynchronously and return file info."""
        start_time = time.time()
        
        try:
            # Get file stats
            stat = os.stat(file_path)
            file_size = stat.st_size
            
            # Get MIME type
            mime_type, _ = mimetypes.guess_type(file_path)
            mime_type = mime_type or 'application/octet-stream'
            
            # Get file extension
            extension = Path(file_path).suffix.lower()
            
            # Read file content
            content = ""
            if file_size > 0:
                async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = await f.read()
            
            # Calculate content hash
            content_hash = hashlib.md5(content.encode('utf-8')).hexdigest()
            
            # Count lines, words, characters
            lines = content.splitlines()
            line_count = len(lines)
            words = re.findall(r'\b\w+\b', content.lower())
            word_count = len(words)
            char_count = len(content)
            
            read_time = time.time() - start_time
            
            return FileInfo(
                path=file_path,
                size=file_size,
                mime_type=mime_type,
                extension=extension,
                content_hash=content_hash,
                line_count=line_count,
                word_count=word_count,
                char_count=char_count,
                read_time=read_time
            )
            
        except Exception as e:
            read_time = time.time() - start_time
            return FileInfo(
                path=file_path,
                size=0,
                mime_type='unknown',
                extension=Path(file_path).suffix.lower(),
                content_hash='',
                line_count=0,
                word_count=0,
                char_count=0,
                read_time=read_time,
                error=str(e)
            )
    
    def get_file_patterns(self, patterns: List[str]) -> List[str]:
        """Expand file patterns to actual file paths."""
        all_files = []
        
        for pattern in patterns:
            if os.path.isfile(pattern):
                all_files.append(pattern)
            else:
                # Use glob to find matching files
                matches = glob.glob(pattern, recursive=True)
                all_files.extend(matches)
        
        # Filter by supported extensions if no specific pattern
        if not patterns:
            for root, dirs, files in os.walk('.'):
                for file in files:
                    file_path = os.path.join(root, file)
                    if Path(file_path).suffix.lower() in self.supported_extensions:
                        all_files.append(file_path)
        
        return sorted(list(set(all_files)))
    
    async def read_files_parallel(self, file_paths: List[str]) -> List[FileInfo]:
        """Read multiple files in parallel."""
        print(f"Reading {len(file_paths)} files with {self.max_workers} workers...")
        
        # Create semaphore to limit concurrent file operations
        semaphore = asyncio.Semaphore(self.max_workers)
        
        async def read_with_semaphore(file_path):
            async with semaphore:
                return await self.read_file_async(file_path)
        
        # Read all files concurrently
        tasks = [read_with_semaphore(path) for path in file_paths]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Filter out exceptions and return valid results
        valid_results = []
        for result in results:
            if isinstance(result, FileInfo):
                valid_results.append(result)
            elif isinstance(result, Exception):
                print(f"Error reading file: {result}")
        
        return valid_results
    
    def analyze_files(self, file_infos: List[FileInfo]) -> AnalysisResult:
        """Analyze the collected file information."""
        start_time = time.time()
        
        # Basic statistics
        total_files = len(file_infos)
        total_size = sum(f.size for f in file_infos)
        total_lines = sum(f.line_count for f in file_infos)
        total_words = sum(f.word_count for f in file_infos)
        total_chars = sum(f.char_count for f in file_infos)
        
        # File type distribution
        file_types = Counter(f.extension for f in file_infos)
        
        # Largest files
        largest_files = sorted(file_infos, key=lambda f: f.size, reverse=True)[:10]
        
        # Most common words (simple analysis)
        all_words = []
        for file_info in file_infos:
            if file_info.error is None:
                # This is a simplified word extraction - in practice you'd want more sophisticated analysis
                all_words.extend(['word'] * file_info.word_count)  # Placeholder
        
        word_counts = Counter(all_words)
        most_common_words = word_counts.most_common(20)
        
        processing_time = time.time() - start_time
        
        return AnalysisResult(
            total_files=total_files,
            total_size=total_size,
            total_lines=total_lines,
            total_words=total_words,
            total_chars=total_chars,
            file_types=dict(file_types),
            largest_files=largest_files,
            most_common_words=most_common_words,
            processing_time=processing_time,
            files=file_infos
        )
    
    def print_summary(self, analysis: AnalysisResult):
        """Print a summary of the analysis."""
        print("\n" + "="*60)
        print("FILE READING SUMMARY")
        print("="*60)
        
        print(f"Total files processed: {analysis.total_files}")
        print(f"Total size: {analysis.total_size:,} bytes ({analysis.total_size/1024/1024:.2f} MB)")
        print(f"Total lines: {analysis.total_lines:,}")
        print(f"Total words: {analysis.total_words:,}")
        print(f"Total characters: {analysis.total_chars:,}")
        print(f"Processing time: {analysis.processing_time:.2f} seconds")
        
        print(f"\nFile type distribution:")
        for ext, count in sorted(analysis.file_types.items(), key=lambda x: x[1], reverse=True):
            print(f"  {ext or 'no extension'}: {count} files")
        
        print(f"\nLargest files:")
        for i, file_info in enumerate(analysis.largest_files[:5], 1):
            size_mb = file_info.size / 1024 / 1024
            print(f"  {i}. {file_info.path} ({size_mb:.2f} MB, {file_info.line_count} lines)")
        
        # Show files with errors
        error_files = [f for f in analysis.files if f.error]
        if error_files:
            print(f"\nFiles with errors ({len(error_files)}):")
            for file_info in error_files[:5]:
                print(f"  {file_info.path}: {file_info.error}")
    
    def search_content(self, file_infos: List[FileInfo], search_term: str, case_sensitive: bool = False) -> List[Dict]:
        """Search for content across all files."""
        results = []
        flags = 0 if case_sensitive else re.IGNORECASE
        pattern = re.compile(search_term, flags)
        
        for file_info in file_infos:
            if file_info.error is None:
                try:
                    with open(file_info.path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        matches = pattern.findall(content)
                        if matches:
                            results.append({
                                'file': file_info.path,
                                'matches': len(matches),
                                'sample_matches': matches[:3]
                            })
                except Exception as e:
                    print(f"Error searching in {file_info.path}: {e}")
        
        return results
    
    def export_results(self, analysis: AnalysisResult, output_file: str):
        """Export analysis results to JSON."""
        export_data = {
            'summary': {
                'total_files': analysis.total_files,
                'total_size': analysis.total_size,
                'total_lines': analysis.total_lines,
                'total_words': analysis.total_words,
                'total_chars': analysis.total_chars,
                'processing_time': analysis.processing_time
            },
            'file_types': analysis.file_types,
            'largest_files': [asdict(f) for f in analysis.largest_files],
            'files': [asdict(f) for f in analysis.files]
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        print(f"Results exported to {output_file}")

async def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Read and analyze multiple files')
    parser.add_argument('patterns', nargs='*', help='File patterns to read (e.g., "*.txt", "docs/**/*.md")')
    parser.add_argument('--workers', '-w', type=int, default=10, help='Number of parallel workers')
    parser.add_argument('--search', '-s', help='Search for text in files')
    parser.add_argument('--case-sensitive', action='store_true', help='Case-sensitive search')
    parser.add_argument('--export', '-e', help='Export results to JSON file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    # Initialize reader
    reader = MultiFileReader(max_workers=args.workers)
    
    # Get file patterns
    if args.patterns:
        file_paths = reader.get_file_patterns(args.patterns)
    else:
        # Default: read all supported files in current directory
        file_paths = reader.get_file_patterns(['**/*'])
    
    if not file_paths:
        print("No files found matching the patterns.")
        return
    
    print(f"Found {len(file_paths)} files to process...")
    
    # Read files
    file_infos = await reader.read_files_parallel(file_paths)
    
    # Analyze results
    analysis = reader.analyze_files(file_infos)
    
    # Print summary
    reader.print_summary(analysis)
    
    # Search if requested
    if args.search:
        print(f"\nSearching for '{args.search}'...")
        search_results = reader.search_content(file_infos, args.search, args.case_sensitive)
        print(f"Found {len(search_results)} files with matches:")
        for result in search_results[:10]:  # Show first 10 results
            print(f"  {result['file']}: {result['matches']} matches")
            if args.verbose:
                print(f"    Sample matches: {result['sample_matches']}")
    
    # Export if requested
    if args.export:
        reader.export_results(analysis, args.export)

if __name__ == "__main__":
    asyncio.run(main())