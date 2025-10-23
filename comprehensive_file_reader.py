#!/usr/bin/env python3
"""
Comprehensive File Reader
=========================

A comprehensive utility for reading and analyzing lots of files with various approaches.
This demonstrates different techniques for handling multiple file I/O operations.
"""

import os
import sys
import glob
import time
import json
import hashlib
import mimetypes
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import asyncio
import aiofiles
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional, Union
import argparse

@dataclass
class FileStats:
    """Statistics for a single file."""
    path: str
    size: int
    lines: int
    words: int
    chars: int
    mime_type: str
    extension: str
    hash_md5: str
    read_time: float
    error: Optional[str] = None

@dataclass
class ProjectStats:
    """Overall project statistics."""
    total_files: int
    total_size: int
    total_lines: int
    total_words: int
    total_chars: int
    file_types: Dict[str, int]
    largest_files: List[FileStats]
    processing_time: float
    method_used: str

class FileReader:
    """Base class for file reading operations."""
    
    def __init__(self, max_workers: int = 4):
        self.max_workers = max_workers
        self.supported_extensions = {
            '.txt', '.md', '.tex', '.py', '.js', '.ts', '.html', '.css', 
            '.json', '.yaml', '.yml', '.csv', '.log', '.cfg', '.ini', 
            '.conf', '.sh', '.bash', '.zsh', '.fish', '.ps1', '.c', '.cpp', 
            '.h', '.hpp', '.java', '.go', '.rs', '.php', '.rb', '.pl', 
            '.lua', '.r', '.m', '.swift', '.kt', '.scala', '.bib', '.sty', 
            '.cls', '.xml', '.sql', '.dockerfile', '.gitignore', '.gitattributes'
        }
    
    def get_files(self, patterns: List[str] = None) -> List[str]:
        """Get list of files to process."""
        if patterns:
            files = []
            for pattern in patterns:
                if os.path.isfile(pattern):
                    files.append(pattern)
                else:
                    files.extend(glob.glob(pattern, recursive=True))
            return sorted(list(set(files)))
        else:
            # Default: find all supported files
            files = []
            for root, dirs, filenames in os.walk('.'):
                for filename in filenames:
                    file_path = os.path.join(root, filename)
                    if Path(file_path).suffix.lower() in self.supported_extensions:
                        files.append(file_path)
            return sorted(files)
    
    def read_file_sync(self, file_path: str) -> FileStats:
        """Read a single file synchronously."""
        start_time = time.time()
        
        try:
            # Get file info
            stat = os.stat(file_path)
            size = stat.st_size
            
            # Get MIME type
            mime_type, _ = mimetypes.guess_type(file_path)
            mime_type = mime_type or 'application/octet-stream'
            
            # Get extension
            extension = Path(file_path).suffix.lower()
            
            # Read content
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Calculate hash
            hash_md5 = hashlib.md5(content.encode('utf-8')).hexdigest()
            
            # Count lines, words, chars
            lines = content.splitlines()
            words = content.split()
            
            read_time = time.time() - start_time
            
            return FileStats(
                path=file_path,
                size=size,
                lines=len(lines),
                words=len(words),
                chars=len(content),
                mime_type=mime_type,
                extension=extension,
                hash_md5=hash_md5,
                read_time=read_time
            )
            
        except Exception as e:
            read_time = time.time() - start_time
            return FileStats(
                path=file_path,
                size=0,
                lines=0,
                words=0,
                chars=0,
                mime_type='unknown',
                extension=Path(file_path).suffix.lower(),
                hash_md5='',
                read_time=read_time,
                error=str(e)
            )

class SequentialReader(FileReader):
    """Sequential file reader."""
    
    def read_files(self, file_paths: List[str]) -> List[FileStats]:
        """Read files one by one."""
        print(f"Reading {len(file_paths)} files sequentially...")
        start_time = time.time()
        
        results = []
        for i, file_path in enumerate(file_paths):
            if i % 10 == 0:
                print(f"  Progress: {i}/{len(file_paths)} files")
            result = self.read_file_sync(file_path)
            results.append(result)
        
        total_time = time.time() - start_time
        print(f"  Completed in {total_time:.2f} seconds")
        return results

class ThreadedReader(FileReader):
    """Threaded file reader."""
    
    def read_files(self, file_paths: List[str]) -> List[FileStats]:
        """Read files using thread pool."""
        print(f"Reading {len(file_paths)} files with {self.max_workers} threads...")
        start_time = time.time()
        
        results = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_path = {
                executor.submit(self.read_file_sync, path): path 
                for path in file_paths
            }
            
            for i, future in enumerate(as_completed(future_to_path)):
                if i % 10 == 0:
                    print(f"  Progress: {i}/{len(file_paths)} files")
                result = future.result()
                results.append(result)
        
        total_time = time.time() - start_time
        print(f"  Completed in {total_time:.2f} seconds")
        return results

class ProcessReader(FileReader):
    """Multiprocess file reader."""
    
    def read_files(self, file_paths: List[str]) -> List[FileStats]:
        """Read files using process pool."""
        print(f"Reading {len(file_paths)} files with {self.max_workers} processes...")
        start_time = time.time()
        
        with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
            results = list(executor.map(self.read_file_sync, file_paths))
        
        total_time = time.time() - start_time
        print(f"  Completed in {total_time:.2f} seconds")
        return results

class AsyncReader(FileReader):
    """Async file reader."""
    
    async def read_file_async(self, file_path: str) -> FileStats:
        """Read a single file asynchronously."""
        start_time = time.time()
        
        try:
            # Get file info
            stat = os.stat(file_path)
            size = stat.st_size
            
            # Get MIME type
            mime_type, _ = mimetypes.guess_type(file_path)
            mime_type = mime_type or 'application/octet-stream'
            
            # Get extension
            extension = Path(file_path).suffix.lower()
            
            # Read content
            async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = await f.read()
            
            # Calculate hash
            hash_md5 = hashlib.md5(content.encode('utf-8')).hexdigest()
            
            # Count lines, words, chars
            lines = content.splitlines()
            words = content.split()
            
            read_time = time.time() - start_time
            
            return FileStats(
                path=file_path,
                size=size,
                lines=len(lines),
                words=len(words),
                chars=len(content),
                mime_type=mime_type,
                extension=extension,
                hash_md5=hash_md5,
                read_time=read_time
            )
            
        except Exception as e:
            read_time = time.time() - start_time
            return FileStats(
                path=file_path,
                size=0,
                lines=0,
                words=0,
                chars=0,
                mime_type='unknown',
                extension=Path(file_path).suffix.lower(),
                hash_md5='',
                read_time=read_time,
                error=str(e)
            )
    
    async def read_files(self, file_paths: List[str]) -> List[FileStats]:
        """Read files asynchronously."""
        print(f"Reading {len(file_paths)} files asynchronously (max {self.max_workers} concurrent)...")
        start_time = time.time()
        
        # Create semaphore to limit concurrent operations
        semaphore = asyncio.Semaphore(self.max_workers)
        
        async def read_with_semaphore(file_path):
            async with semaphore:
                return await self.read_file_async(file_path)
        
        # Read all files concurrently
        tasks = [read_with_semaphore(path) for path in file_paths]
        results = await asyncio.gather(*tasks)
        
        total_time = time.time() - start_time
        print(f"  Completed in {total_time:.2f} seconds")
        return results

class FileAnalyzer:
    """Analyzer for file statistics."""
    
    @staticmethod
    def analyze_files(file_stats: List[FileStats], method_used: str) -> ProjectStats:
        """Analyze file statistics and return project stats."""
        start_time = time.time()
        
        # Basic statistics
        successful = [f for f in file_stats if f.error is None]
        failed = [f for f in file_stats if f.error is not None]
        
        total_files = len(file_stats)
        total_size = sum(f.size for f in successful)
        total_lines = sum(f.lines for f in successful)
        total_words = sum(f.words for f in successful)
        total_chars = sum(f.chars for f in successful)
        
        # File type distribution
        file_types = Counter(f.extension for f in successful)
        
        # Largest files
        largest_files = sorted(successful, key=lambda f: f.size, reverse=True)[:10]
        
        processing_time = time.time() - start_time
        
        return ProjectStats(
            total_files=total_files,
            total_size=total_size,
            total_lines=total_lines,
            total_words=total_words,
            total_chars=total_chars,
            file_types=dict(file_types),
            largest_files=largest_files,
            processing_time=processing_time,
            method_used=method_used
        )
    
    @staticmethod
    def print_summary(stats: ProjectStats):
        """Print a summary of the analysis."""
        print(f"\n{'='*60}")
        print(f"FILE READING SUMMARY - {stats.method_used.upper()}")
        print(f"{'='*60}")
        
        print(f"Total files processed: {stats.total_files}")
        print(f"Total size: {stats.total_size:,} bytes ({stats.total_size/1024/1024:.2f} MB)")
        print(f"Total lines: {stats.total_lines:,}")
        print(f"Total words: {stats.total_words:,}")
        print(f"Total characters: {stats.total_chars:,}")
        print(f"Processing time: {stats.processing_time:.2f} seconds")
        
        print(f"\nFile type distribution:")
        for ext, count in sorted(stats.file_types.items(), key=lambda x: x[1], reverse=True):
            print(f"  {ext or 'no extension'}: {count} files")
        
        print(f"\nLargest files:")
        for i, file_stat in enumerate(stats.largest_files[:5], 1):
            size_mb = file_stat.size / 1024 / 1024
            print(f"  {i}. {file_stat.path} ({size_mb:.2f} MB, {file_stat.lines} lines)")
    
    @staticmethod
    def export_results(stats: ProjectStats, file_stats: List[FileStats], output_file: str):
        """Export results to JSON."""
        export_data = {
            'summary': asdict(stats),
            'files': [asdict(f) for f in file_stats]
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        print(f"Results exported to {output_file}")

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description='Comprehensive file reader')
    parser.add_argument('patterns', nargs='*', help='File patterns to read')
    parser.add_argument('--method', '-m', choices=['sequential', 'threaded', 'process', 'async'], 
                       default='async', help='Reading method to use')
    parser.add_argument('--workers', '-w', type=int, default=4, help='Number of workers')
    parser.add_argument('--export', '-e', help='Export results to JSON file')
    parser.add_argument('--compare', '-c', action='store_true', help='Compare all methods')
    
    args = parser.parse_args()
    
    # Get files to process
    reader = FileReader()
    files = reader.get_files(args.patterns)
    
    if not files:
        print("No files found matching the patterns.")
        return
    
    print(f"Found {len(files)} files to process")
    
    if args.compare:
        # Compare all methods
        methods = [
            ('Sequential', SequentialReader()),
            ('Threaded', ThreadedReader(args.workers)),
            ('Process', ProcessReader(args.workers)),
            ('Async', AsyncReader(args.workers))
        ]
        
        results = {}
        for method_name, method_reader in methods:
            print(f"\n{'-'*50}")
            print(f"Testing {method_name} method")
            print(f"{'-'*50}")
            
            if method_name == 'Async':
                file_stats = asyncio.run(method_reader.read_files(files))
            else:
                file_stats = method_reader.read_files(files)
            
            stats = FileAnalyzer.analyze_files(file_stats, method_name)
            results[method_name] = (stats, file_stats)
            FileAnalyzer.print_summary(stats)
        
        # Performance comparison
        print(f"\n{'='*60}")
        print("PERFORMANCE COMPARISON")
        print(f"{'='*60}")
        for method_name, (stats, _) in results.items():
            print(f"{method_name:12}: {stats.processing_time:.3f} seconds")
    
    else:
        # Use single method
        if args.method == 'sequential':
            reader = SequentialReader()
        elif args.method == 'threaded':
            reader = ThreadedReader(args.workers)
        elif args.method == 'process':
            reader = ProcessReader(args.workers)
        elif args.method == 'async':
            reader = AsyncReader(args.workers)
        
        # Read files
        if args.method == 'async':
            file_stats = asyncio.run(reader.read_files(files))
        else:
            file_stats = reader.read_files(files)
        
        # Analyze results
        stats = FileAnalyzer.analyze_files(file_stats, args.method)
        FileAnalyzer.print_summary(stats)
        
        # Export if requested
        if args.export:
            FileAnalyzer.export_results(stats, file_stats, args.export)

if __name__ == "__main__":
    main()