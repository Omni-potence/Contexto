from setuptools import setup, find_packages

setup(
    name="contexto",
    version="0.1.0",
    author="Contexto Team",
    author_email="example@example.com",
    description="A context engine for AI coding assistants",
    long_description=open("contexto/README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/contexto",
    packages=find_packages(include=["contexto", "contexto.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "tree-sitter>=0.20.0",
        "typer>=0.7.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "contexto=contexto.cli.src.main:app",
        ],
    },
)
