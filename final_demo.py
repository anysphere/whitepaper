#!/usr/bin/env python3
"""
Final Demo: Reading Lots of Files
=================================

This script demonstrates various approaches to reading multiple files efficiently.
It shows different methods and their trade-offs for different scenarios.
"""

import os
import time
import asyncio
import aiofiles
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from collections import Counter
import json

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

def method_sequential(files):
    """Method 1: Sequential reading."""
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
    print(f"  Completed in {end_time - start_time:.3f} seconds")
    return results

def method_threaded(files, max_workers=4):
    """Method 2: Threaded reading."""
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
    print(f"  Completed in {end_time - start_time:.3f} seconds")
    return results

def method_multiprocess(files, max_workers=4):
    """Method 3: Multiprocess reading."""
    print(f"Method 3: Multiprocess Reading ({max_workers} workers)")
    print("-" * 40)
    
    start_time = time.time()
    
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(read_file_sync, files))
    
    end_time = time.time()
    print(f"  Completed in {end_time - start_time:.3f} seconds")
    return results

async def method_async(files, max_concurrent=10):
    """Method 4: Async reading."""
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
    print(f"  Completed in {end_time - start_time:.3f} seconds")
    return results

def analyze_results(results, method_name):
    """Analyze and print results."""
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
        for result in failed[:3]:
            print(f"    {result['path']}: {result.get('error', 'Unknown error')}")

def create_large_test_files():
    """Create some large test files for demonstration."""
    print("Creating test files...")
    
    # Create a large text file
    with open('large_test.txt', 'w') as f:
        for i in range(10000):
            f.write(f"This is line {i} of a large test file. " * 10 + "\n")
    
    # Create multiple smaller files
    for i in range(20):
        with open(f'test_file_{i:02d}.txt', 'w') as f:
            for j in range(100):
                f.write(f"Test file {i}, line {j}: Some content here.\n")
    
    print("Test files created.")

def cleanup_test_files():
    """Clean up test files."""
    print("Cleaning up test files...")
    
    test_files = ['large_test.txt'] + [f'test_file_{i:02d}.txt' for i in range(20)]
    
    for file in test_files:
        try:
            if os.path.exists(file):
                os.remove(file)
        except:
            pass
    
    print("Test files cleaned up.")

def main():
    """Main demonstration function."""
    print("Reading Lots of Files - Final Demo")
    print("=" * 50)
    
    # Get all files
    print("Discovering files...")
    files = get_all_files()
    print(f"Found {len(files)} files to read")
    
    if not files:
        print("No files found. Creating test files...")
        create_large_test_files()
        files = get_all_files()
        print(f"Now found {len(files)} files to read")
    
    # Show some example files
    print(f"\nExample files:")
    for file_path in files[:5]:
        print(f"  {file_path}")
    if len(files) > 5:
        print(f"  ... and {len(files) - 5} more")
    
    print(f"\n{'='*50}")
    print("Testing Different Methods")
    print(f"{'='*50}")
    
    # Test all methods
    methods = [
        ("Sequential", lambda: method_sequential(files)),
        ("Threaded (2 workers)", lambda: method_threaded(files, 2)),
        ("Threaded (4 workers)", lambda: method_threaded(files, 4)),
        ("Multiprocess (2 workers)", lambda: method_multiprocess(files, 2)),
        ("Multiprocess (4 workers)", lambda: method_multiprocess(files, 4)),
        ("Async (5 concurrent)", lambda: asyncio.run(method_async(files, 5))),
        ("Async (10 concurrent)", lambda: asyncio.run(method_async(files, 10))),
    ]
    
    results_by_method = {}
    
    for method_name, method_func in methods:
        print(f"\n{'-'*50}")
        print(f"Testing: {method_name}")
        print(f"{'-'*50}")
        
        try:
            results = method_func()
            results_by_method[method_name] = results
            analyze_results(results, method_name)
        except Exception as e:
            print(f"Error with {method_name}: {e}")
    
    # Performance comparison
    print(f"\n{'='*50}")
    print("Performance Comparison")
    print(f"{'='*50}")
    
    # This is a simplified comparison - in practice you'd want more sophisticated timing
    print("Note: Performance depends on file sizes, disk speed, and system resources.")
    print("For I/O bound tasks like file reading, threading or async often works well.")
    print("For CPU bound tasks, multiprocessing is usually better.")
    
    # Clean up test files
    cleanup_test_files()
    
    print(f"\n{'='*50}")
    print("Summary")
    print(f"{'='*50}")
    print("This demonstration showed different approaches to reading lots of files:")
    print("1. Sequential: Simple but slow for many files")
    print("2. Threaded: Good for I/O bound tasks, limited by GIL in Python")
    print("3. Multiprocess: Good for CPU bound tasks, but more overhead")
    print("4. Async: Very efficient for I/O bound tasks, especially with many files")
    print("\nChoose the method that best fits your specific use case!")

if __name__ == "__main__":
    main()