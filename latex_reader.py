#!/usr/bin/env python3
"""
LaTeX Project Reader
====================

Specialized script for reading and analyzing LaTeX projects.
"""

import os
import re
import glob
from pathlib import Path
from collections import defaultdict, Counter
import json

class LaTeXReader:
    """Reader specialized for LaTeX projects."""
    
    def __init__(self, project_dir="."):
        self.project_dir = Path(project_dir)
        self.latex_extensions = {'.tex', '.sty', '.cls', '.bib'}
        self.files = {}
        self.structure = {}
        self.citations = set()
        self.references = set()
        self.commands = Counter()
        self.packages = set()
        
    def find_latex_files(self):
        """Find all LaTeX-related files in the project."""
        latex_files = []
        
        for ext in self.latex_extensions:
            pattern = f"**/*{ext}"
            files = list(self.project_dir.glob(pattern))
            latex_files.extend(files)
        
        return sorted(latex_files)
    
    def read_file(self, file_path):
        """Read a LaTeX file and extract information."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            file_info = {
                'path': str(file_path),
                'size': len(content),
                'lines': len(content.splitlines()),
                'content': content,
                'sections': self.extract_sections(content),
                'citations': self.extract_citations(content),
                'references': self.extract_references(content),
                'commands': self.extract_commands(content),
                'packages': self.extract_packages(content),
                'includes': self.extract_includes(content),
                'success': True
            }
            
            return file_info
            
        except Exception as e:
            return {
                'path': str(file_path),
                'size': 0,
                'lines': 0,
                'content': '',
                'sections': [],
                'citations': set(),
                'references': set(),
                'commands': Counter(),
                'packages': set(),
                'includes': [],
                'success': False,
                'error': str(e)
            }
    
    def extract_sections(self, content):
        """Extract section headings from LaTeX content."""
        section_pattern = r'\\(?:sub)*section\*?\{([^}]+)\}'
        sections = re.findall(section_pattern, content)
        return sections
    
    def extract_citations(self, content):
        """Extract citations from LaTeX content."""
        citation_pattern = r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}'
        citations = re.findall(citation_pattern, content)
        return set(citations)
    
    def extract_references(self, content):
        """Extract references from LaTeX content."""
        ref_pattern = r'\\ref\{([^}]+)\}'
        references = re.findall(ref_pattern, content)
        return set(references)
    
    def extract_commands(self, content):
        """Extract custom LaTeX commands."""
        command_pattern = r'\\(?:newcommand|renewcommand|providecommand|DeclareRobustCommand)\*?\{([^}]+)\}'
        commands = re.findall(command_pattern, content)
        return Counter(commands)
    
    def extract_packages(self, content):
        """Extract package imports."""
        package_pattern = r'\\usepackage(?:\[[^\]]*\])?\{([^}]+)\}'
        packages = re.findall(package_pattern, content)
        return set(packages)
    
    def extract_includes(self, content):
        """Extract file includes."""
        include_pattern = r'\\(?:input|include|subfile)\{([^}]+)\}'
        includes = re.findall(include_pattern, content)
        return includes
    
    def read_all_files(self):
        """Read all LaTeX files in the project."""
        print("Discovering LaTeX files...")
        latex_files = self.find_latex_files()
        print(f"Found {len(latex_files)} LaTeX files")
        
        print("Reading files...")
        for i, file_path in enumerate(latex_files):
            print(f"  Reading {i+1}/{len(latex_files)}: {file_path.name}")
            file_info = self.read_file(file_path)
            self.files[str(file_path)] = file_info
            
            # Aggregate information
            if file_info['success']:
                self.citations.update(file_info['citations'])
                self.references.update(file_info['references'])
                self.commands.update(file_info['commands'])
                self.packages.update(file_info['packages'])
        
        return self.files
    
    def analyze_structure(self):
        """Analyze the structure of the LaTeX project."""
        print("\nAnalyzing project structure...")
        
        # Find main file (usually main.tex or the one with \documentclass)
        main_files = []
        for file_path, file_info in self.files.items():
            if file_info['success'] and '\\documentclass' in file_info['content']:
                main_files.append(file_path)
        
        if main_files:
            main_file = main_files[0]
            print(f"Main file: {main_file}")
            self.structure['main_file'] = main_file
            
            # Build dependency tree
            self.structure['dependencies'] = self.build_dependency_tree(main_file)
        else:
            print("No main LaTeX file found")
            self.structure['main_file'] = None
        
        # Analyze sections
        all_sections = []
        for file_info in self.files.values():
            if file_info['success']:
                all_sections.extend(file_info['sections'])
        
        self.structure['sections'] = all_sections
        self.structure['total_sections'] = len(all_sections)
        
        return self.structure
    
    def build_dependency_tree(self, main_file, visited=None):
        """Build a dependency tree starting from the main file."""
        if visited is None:
            visited = set()
        
        if main_file in visited:
            return {}  # Circular dependency
        
        visited.add(main_file)
        dependencies = {}
        
        if main_file in self.files:
            file_info = self.files[main_file]
            if file_info['success']:
                for include in file_info['includes']:
                    # Try to find the actual file
                    include_path = self.find_include_file(include)
                    if include_path:
                        dependencies[include] = self.build_dependency_tree(include_path, visited.copy())
        
        return dependencies
    
    def find_include_file(self, include_name):
        """Find the actual file for an include."""
        # Try different extensions
        for ext in ['.tex', '.sty', '.cls']:
            full_name = include_name + ext
            for file_path in self.files:
                if file_path.endswith(full_name):
                    return file_path
        return None
    
    def print_summary(self):
        """Print a summary of the LaTeX project."""
        print("\n" + "="*60)
        print("LATEX PROJECT SUMMARY")
        print("="*60)
        
        successful_files = [f for f in self.files.values() if f['success']]
        failed_files = [f for f in self.files.values() if not f['success']]
        
        print(f"Total files: {len(self.files)}")
        print(f"Successful: {len(successful_files)}")
        print(f"Failed: {len(failed_files)}")
        
        if successful_files:
            total_size = sum(f['size'] for f in successful_files)
            total_lines = sum(f['lines'] for f in successful_files)
            print(f"Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")
            print(f"Total lines: {total_lines:,}")
        
        print(f"\nProject structure:")
        if self.structure.get('main_file'):
            print(f"  Main file: {self.structure['main_file']}")
        print(f"  Total sections: {self.structure.get('total_sections', 0)}")
        
        print(f"\nCitations: {len(self.citations)}")
        if self.citations:
            print("  Sample citations:", list(self.citations)[:5])
        
        print(f"\nReferences: {len(self.references)}")
        if self.references:
            print("  Sample references:", list(self.references)[:5])
        
        print(f"\nPackages used: {len(self.packages)}")
        if self.packages:
            print("  Packages:", sorted(list(self.packages)))
        
        print(f"\nCustom commands: {len(self.commands)}")
        if self.commands:
            print("  Most common commands:")
            for cmd, count in self.commands.most_common(10):
                print(f"    \\{cmd}: {count} times")
        
        print(f"\nSections found:")
        for i, section in enumerate(self.structure.get('sections', [])[:10], 1):
            print(f"  {i}. {section}")
        if len(self.structure.get('sections', [])) > 10:
            print(f"  ... and {len(self.structure['sections']) - 10} more")
    
    def export_analysis(self, output_file="latex_analysis.json"):
        """Export the analysis to a JSON file."""
        export_data = {
            'project_info': {
                'total_files': len(self.files),
                'successful_files': len([f for f in self.files.values() if f['success']]),
                'failed_files': len([f for f in self.files.values() if not f['success']]),
                'main_file': self.structure.get('main_file'),
                'total_sections': self.structure.get('total_sections', 0)
            },
            'files': {
                path: {
                    'size': info['size'],
                    'lines': info['lines'],
                    'sections': info['sections'],
                    'citations': list(info['citations']),
                    'references': list(info['references']),
                    'packages': list(info['packages']),
                    'includes': info['includes'],
                    'success': info['success']
                }
                for path, info in self.files.items()
            },
            'global_analysis': {
                'citations': list(self.citations),
                'references': list(self.references),
                'packages': list(self.packages),
                'commands': dict(self.commands),
                'sections': self.structure.get('sections', [])
            }
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        print(f"Analysis exported to {output_file}")

def main():
    """Main function."""
    print("LaTeX Project Reader")
    print("=" * 50)
    
    # Initialize reader
    reader = LaTeXReader()
    
    # Read all files
    reader.read_all_files()
    
    # Analyze structure
    reader.analyze_structure()
    
    # Print summary
    reader.print_summary()
    
    # Export analysis
    reader.export_analysis()

if __name__ == "__main__":
    main()