# stellar-xdr

XDR for the Stellar Network.

# Stellar XDR Library

## Overview

The Stellar XDR library provides tools for encoding and decoding Stellar XDR (External Data Representation) data structures, enabling seamless interaction with the Stellar network.

## Features

- Encoding and decoding of Stellar transactions and data structures.
- Cryptographic functions for signing and verifying transactions.
- Command-line interface for easy usage.
- Graphical user interface for user-friendly interaction.

## Installation

To install the library, clone the repository and install the required dependencies:

```bash
1 git clone https://github.com/KOSASIH/stellar-xdr.git
2 cd stellar-xdr
3 pip install -r requirements.txt
```

Alternatively, you can install the package using setup.py:

```bash
1 python setup.py install
```

## Usage
For detailed usage examples, please refer to the Usage section of the documentation.

## Running Tests
To run the tests, use the following command:

```bash
1 python -m unittest discover -s tests
```

## Running Benchmarks
To run the benchmarks, execute the following commands:

```bash
1 python benchmarks/benchmark_encoder.py
2 python benchmarks/benchmark_decoder.py
```

## Contributing
We welcome contributions! Please see our Contributing Guidelines for more information.
