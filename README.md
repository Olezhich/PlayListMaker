[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)  
[![Python](https://img.shields.io/badge/python-3.12%2B-blue)](https://python.org)  

## Description:  
A lightweight CLI tool to generate playlists using Python. Designed as part of a microservice architecture with Swift-based frontend control.  
## Technologies:
- **Python** (version 3.12+)
- **toml** — for working with TOML configs
- Standard Python library (`os`, `sys`, `subprocess`, etc.)
## Features:
- **Flexible generation rules**: Support for custom templates in TOML config.
- **Cross-platform**: Works on Windows, Linux and macOS.
- **Rejection of unnecessary dependencies**: Only `toml` + standard Python library.
- **Recursive folder traversal**: Automatically finds all audio files in the specified directory and its subfolders.
- **Format support**: Correctly handles both `cue` sheets and `flac`, `wav`, `mp3`, etc.
- **Flexibility**: You can exclude/include certain folders and files via config like .gitignore.
