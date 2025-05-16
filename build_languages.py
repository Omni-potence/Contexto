"""Build Tree-sitter language libraries."""

from tree_sitter import Language

# Build the language library
Language.build_library(
    'build/languages.so',
    [
        'build/languages/tree-sitter-python',
    ]
)
