# Contexto

Contexto is a powerful context engine for AI coding assistants. It indexes and retrieves richly structured code context from repositories, providing semantic understanding of code to improve AI assistance.

## Features

- **Multi-language Support**: Parse and index code in Python, JavaScript, TypeScript, Go, and more
- **Semantic Code Search**: Find relevant code based on natural language queries
- **Structured Code Understanding**: Extract functions, classes, methods, and their relationships
- **Fast Retrieval**: Optimized for low-latency responses
- **Caching**: Efficient caching system to avoid re-parsing unchanged files
- **Configurable**: Customize behavior through `.contexto.toml` configuration

## Installation

```bash
# Install from source
git clone https://github.com/yourusername/contexto.git
cd contexto
pip install -e ".[dev,embedding,index,server]"

# Run setup to build Tree-sitter language libraries
python -m contexto.tools.setup
```

## Usage

### Indexing a Repository

```bash
python -m contexto.cli.src.main index /path/to/your/repo
```

### Querying for Context

```bash
python -m contexto.cli.src.main query "How is authentication implemented?"
```

### Managing the Cache

```bash
# Get cache information
python -m contexto.cli.src.main cache info

# Clear the cache
python -m contexto.cli.src.main cache clear
```

### Running the API Server

```bash
python -m contexto.cli.src.main server
```

## Configuration

Create a `.contexto.toml` file in your project root:

```toml
[general]
cache_dir = ".contexto_cache"
data_dir = "data"

[parser]
chunk_overlap = 0
max_chunk_tokens = 1000

[parser.languages]
python = true
javascript = true
typescript = true
go = true

[embeddings]
model = "microsoft/codebert-base"
device = "auto"  # "cpu", "cuda", or "auto"

[index]
vector_index_type = "qdrant"
lexical_index_type = "tantivy"
rerank_results = true

[server]
host = "127.0.0.1"
port = 8000
```

## Project Structure

```
contexto/
├── cli/            # Command-line interface
├── config/         # Configuration handling
├── embeddings/     # Code embedding generation
├── index/          # Vector and lexical indexing
├── parser/         # Code parsing and chunk extraction
├── retriever/      # Context retrieval and ranking
├── server/         # API server
├── tests/          # Shared test utilities
└── tools/          # Development tools
```

## Development

### Running Tests

```bash
pytest contexto
```

### Building Documentation

```bash
cd docs
make html
```

## License

MIT License
