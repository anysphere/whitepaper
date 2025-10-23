#!/usr/bin/env python3
"""
Simple Multi-File Reader
========================

A simple script to read lots of files and demonstrate different approaches.
"""

import os
import glob
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import multiprocessing as mp

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

def read_files_sequential(file_paths):
    """Read files one by one (sequential approach)."""
    print("Reading files sequentially...")
    start_time = time.time()
    results = []
    
    for i, file_path in enumerate(file_paths):
        if i % 10 == 0:
            print(f"  Progress: {i}/{len(file_paths)} files")
        result = read_file_sync(file_path)
        results.append(result)
    
    end_time = time.time()
    print(f"Sequential reading completed in {end_time - start_time:.2f} seconds")
    return results

def read_files_threaded(file_paths, max_workers=4):
    """Read files using thread pool (parallel approach)."""
    print(f"Reading files with {max_workers} threads...")
    start_time = time.time()
    results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all tasks
        future_to_path = {executor.submit(read_file_sync, path): path for path in file_paths}
        
        # Collect results as they complete
        for i, future in enumerate(as_completed(future_to_path)):
            if i % 10 == 0:
                print(f"  Progress: {i}/{len(file_paths)} files")
            result = future.result()
            results.append(result)
    
    end_time = time.time()
    print(f"Threaded reading completed in {end_time - start_time:.2f} seconds")
    return results

def read_files_multiprocess(file_paths, max_workers=4):
    """Read files using multiprocessing (parallel approach)."""
    print(f"Reading files with {max_workers} processes...")
    start_time = time.time()
    
    with mp.Pool(max_workers) as pool:
        results = pool.map(read_file_sync, file_paths)
    
    end_time = time.time()
    print(f"Multiprocess reading completed in {end_time - start_time:.2f} seconds")
    return results

def analyze_results(results):
    """Analyze the results of file reading."""
    successful = [r for r in results if r['success']]
    failed = [r for r in results if not r['success']]
    
    total_size = sum(r['size'] for r in successful)
    total_lines = sum(r['lines'] for r in successful)
    total_words = sum(r['words'] for r in successful)
    
    print(f"\nAnalysis Results:")
    print(f"  Total files: {len(results)}")
    print(f"  Successful: {len(successful)}")
    print(f"  Failed: {len(failed)}")
    print(f"  Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")
    print(f"  Total lines: {total_lines:,}")
    print(f"  Total words: {total_words:,}")
    
    if failed:
        print(f"\nFailed files:")
        for result in failed[:5]:  # Show first 5 failures
            print(f"  {result['path']}: {result.get('error', 'Unknown error')}")

def get_all_files(directory=".", extensions=None):
    """Get all files matching the given extensions."""
    if extensions is None:
        extensions = {'.txt', '.md', '.tex', '.py', '.js', '.html', '.css', '.json', '.yaml', '.yml'}
    
    all_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if Path(file_path).suffix.lower() in extensions:
                all_files.append(file_path)
    
    return sorted(all_files)

def main():
    """Main function to demonstrate different file reading approaches."""
    print("Multi-File Reader Demo")
    print("=" * 50)
    
    # Get all files to read
    print("Discovering files...")
    file_paths = get_all_files()
    print(f"Found {len(file_paths)} files to read")
    
    if not file_paths:
        print("No files found. Make sure you're in a directory with supported files.")
        return
    
    # Show some example files
    print(f"\nExample files:")
    for path in file_paths[:5]:
        print(f"  {path}")
    if len(file_paths) > 5:
        print(f"  ... and {len(file_paths) - 5} more")
    
    # Test different approaches
    approaches = [
        ("Sequential", lambda: read_files_sequential(file_paths)),
        ("Threaded (2 workers)", lambda: read_files_threaded(file_paths, 2)),
        ("Threaded (4 workers)", lambda: read_files_threaded(file_paths, 4)),
        ("Multiprocess (2 workers)", lambda: read_files_multiprocess(file_paths, 2)),
        ("Multiprocess (4 workers)", lambda: read_files_multiprocess(file_paths, 4)),
    ]
    
    results_by_approach = {}
    
    for approach_name, approach_func in approaches:
        print(f"\n{'-' * 50}")
        print(f"Testing: {approach_name}")
        print(f"{'-' * 50}")
        
        try:
            results = approach_func()
            results_by_approach[approach_name] = results
            analyze_results(results)
        except Exception as e:
            print(f"Error with {approach_name}: {e}")
    
    # Compare performance
    print(f"\n{'=' * 50}")
    print("Performance Comparison")
    print(f"{'=' * 50}")
    
    # This is a simplified comparison - in practice you'd want more sophisticated timing
    print("Note: Actual performance depends on file sizes, disk speed, and system resources.")
    print("For I/O bound tasks like file reading, threading often works well.")
    print("For CPU bound tasks, multiprocessing is usually better.")

if __name__ == "__main__":
    main()