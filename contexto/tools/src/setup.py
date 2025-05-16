"""Setup script for Contexto.

This script sets up the required dependencies and builds the Tree-sitter language libraries.
"""

import os
import sys
import subprocess
from pathlib import Path


def setup_tree_sitter():
    """Set up Tree-sitter language libraries."""
    try:
        import tree_sitter
    except ImportError:
        print("Tree-sitter not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tree-sitter"])
        import tree_sitter

    # Create build directory
    build_dir = Path("build")
    languages_dir = build_dir / "languages"
    languages_dir.mkdir(parents=True, exist_ok=True)

    # Clone language repositories if they don't exist
    languages = {
        "python": "https://github.com/tree-sitter/tree-sitter-python",
        "javascript": "https://github.com/tree-sitter/tree-sitter-javascript",
        "typescript": "https://github.com/tree-sitter/tree-sitter-typescript",
        "go": "https://github.com/tree-sitter/tree-sitter-go",
    }

    for lang_name, repo_url in languages.items():
        lang_dir = languages_dir / f"tree-sitter-{lang_name}"
        if not lang_dir.exists():
            print(f"Cloning {lang_name} grammar...")
            subprocess.check_call(["git", "clone", repo_url, str(lang_dir)])

    # Build language library
    language_paths = []
    for lang_name in languages:
        lang_dir = languages_dir / f"tree-sitter-{lang_name}"
        if lang_name == "typescript":
            # TypeScript has two parsers: typescript and tsx
            language_paths.append(str(lang_dir / "typescript"))
            language_paths.append(str(lang_dir / "tsx"))
        else:
            language_paths.append(str(lang_dir))

    print("Building language library...")
    tree_sitter.Language.build_library(
        str(build_dir / "languages.so"),
        language_paths
    )
    print("Language library built successfully.")


def main():
    """Run the setup script."""
    print("Setting up Contexto...")
    setup_tree_sitter()
    print("Setup completed successfully.")


if __name__ == "__main__":
    main()
