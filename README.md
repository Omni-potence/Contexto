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
# Clone the repository
git clone https://github.com/yourusername/contexto.git
cd contexto

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package in development mode
pip install -e .
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

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
