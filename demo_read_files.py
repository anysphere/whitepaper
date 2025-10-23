#!/usr/bin/env python3
"""
Demo: Reading Lots of Files
===========================

This script demonstrates different approaches to reading multiple files efficiently.
"""

import os
import time
import glob
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import asyncio
import aiofiles

def get_all_files(directory=".", extensions=None):
    """Get all files with specified extensions."""
    if extensions is None:
        extensions = {'.txt', '.md', '.tex', '.py', '.js', '.html', '.css', '.json', '.yaml', '.yml', '.bib', '.sty', '.cls'}
    
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if Path(file_path).suffix.lower() in extensions:
                all_files.append(file_path)
    
    return sorted(all_files)

def read_file_sync(file_path):
    """Read a single file synchronously."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        return {
            'path': file_path,
            'size': len(content),
            'lines': len(content.splitlines()),
            'words': len(content.split()),
            'success': True
        }
    except Exception as e:
        return {
            'path': file_path,
            'size': 0,
            'lines': 0,
            'words': 0,
            'success': False,
            'error': str(e)
        }

async def read_file_async(file_path):
    """Read a single file asynchronously."""
    try:
        async with aiofiles.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = await f.read()
        return {
            'path': file_path,
            'size': len(content),
            'lines': len(content.splitlines()),
            'words': len(content.split()),
            'success': True
        }
    except Exception as e:
        return {
            'path': file_path,
            'size': 0,
            'lines': 0,
            'words': 0,
            'success': False,
            'error': str(e)
        }

def method_1_sequential(files):
    """Method 1: Read files one by one (sequential)."""
    print("Method 1: Sequential Reading")
    print("-" * 40)
    
    start_time = time.time()
    results = []
    
    for i, file_path in enumerate(files):
        if i % 5 == 0:
            print(f"  Progress: {i}/{len(files)} files")
        result = read_file_sync(file_path)
        results.append(result)
    
    end_time = time.time()
    print(f"  Completed in {end_time - start_time:.2f} seconds")
    return results

def method_2_threaded(files, max_workers=4):
    """Method 2: Read files using threads."""
    print(f"Method 2: Threaded Reading ({max_workers} workers)")
    print("-" * 40)
    
    start_time = time.time()
    results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_file = {executor.submit(read_file_sync, file_path): file_path for file_path in files}
        
        for i, future in enumerate(future_to_file):
            if i % 5 == 0:
                print(f"  Progress: {i}/{len(files)} files")
            result = future.result()
            results.append(result)
    
    end_time = time.time()
    print(f"  Completed in {end_time - start_time:.2f} seconds")
    return results

def method_3_multiprocess(files, max_workers=4):
    """Method 3: Read files using multiple processes."""
    print(f"Method 3: Multiprocess Reading ({max_workers} workers)")
    print("-" * 40)
    
    start_time = time.time()
    
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(read_file_sync, files))
    
    end_time = time.time()
    print(f"  Completed in {end_time - start_time:.2f} seconds")
    return results

async def method_4_async(files, max_concurrent=10):
    """Method 4: Read files asynchronously."""
    print(f"Method 4: Async Reading (max {max_concurrent} concurrent)")
    print("-" * 40)
    
    start_time = time.time()
    
    # Create semaphore to limit concurrent operations
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def read_with_semaphore(file_path):
        async with semaphore:
            return await read_file_async(file_path)
    
    # Read all files concurrently
    tasks = [read_with_semaphore(file_path) for file_path in files]
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"  Completed in {end_time - start_time:.2f} seconds")
    return results

def analyze_results(results, method_name):
    """Analyze and print results for a method."""
    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]
    
    total_size = sum(r['size'] for r in successful)
    total_lines = sum(r['lines'] for r in successful)
    total_words = sum(r['words'] for r in successful)
    
    print(f"\n{method_name} Results:")
    print(f"  Files processed: {len(results)}")
    print(f"  Successful: {len(successful)}")
    print(f"  Failed: {len(failed)}")
    print(f"  Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")
    print(f"  Total lines: {total_lines:,}")
    print(f"  Total words: {total_words:,}")
    
    if failed:
        print(f"  Failed files: {len(failed)}")
        for result in failed[:3]:  # Show first 3 failures
            print(f"    {result['path']}: {result.get('error', 'Unknown error')}")

def main():
    """Main demonstration function."""
    print("Reading Lots of Files - Demonstration")
    print("=" * 50)
    
    # Get all files to read
    print("Discovering files...")
    files = get_all_files()
    print(f"Found {len(files)} files to read")
    
    if not files:
        print("No files found. Make sure you're in a directory with supported files.")
        return
    
    # Show some example files
    print(f"\nExample files:")
    for file_path in files[:5]:
        print(f"  {file_path}")
    if len(files) > 5:
        print(f"  ... and {len(files) - 5} more")
    
    print(f"\n{'='*50}")
    print("Testing Different Methods")
    print(f"{'='*50}")
    
    # Test Method 1: Sequential
    results1 = method_1_sequential(files)
    analyze_results(results1, "Sequential")
    
    # Test Method 2: Threaded
    results2 = method_2_threaded(files, max_workers=2)
    analyze_results(results2, "Threaded")
    
    # Test Method 3: Multiprocess
    results3 = method_3_multiprocess(files, max_workers=2)
    analyze_results(results3, "Multiprocess")
    
    # Test Method 4: Async
    print(f"\n{'-'*50}")
    print("Method 4: Async Reading")
    print("-" * 40)
    results4 = asyncio.run(method_4_async(files, max_concurrent=5))
    analyze_results(results4, "Async")
    
    # Summary
    print(f"\n{'='*50}")
    print("Summary")
    print(f"{'='*50}")
    print("Different methods have different trade-offs:")
    print("  - Sequential: Simple, but slow for many files")
    print("  - Threaded: Good for I/O bound tasks, limited by GIL in Python")
    print("  - Multiprocess: Good for CPU bound tasks, but more overhead")
    print("  - Async: Good for I/O bound tasks, very efficient for many files")
    print("\nFor reading lots of files, async or threaded approaches usually work best.")

if __name__ == "__main__":
    main()