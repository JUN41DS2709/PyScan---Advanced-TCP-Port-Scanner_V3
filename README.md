# PyScan - Advanced TCP Port Scanner - V3

PyScan is a fast, multithreaded TCP port scanner built with Python. It allows users to scan custom port ranges, configure the number of threads, enable verbose output, and measure scan execution time.

## Features

* Multithreaded TCP port scanning
* Custom port ranges
* Configurable thread count
* Verbose scanning mode
* Scan time measurement
* Command-line interface
* No external dependencies

## Usage

### Basic Scan

```bash
python pyscan.py 192.168.1.2
```

### Custom Port Range

```bash
python pyscan.py -s 20 -e 1000 192.168.1.2
```

### Custom Thread Count

```bash
python pyscan.py -t 500 192.168.1.2
```

### Verbose Mode

```bash
python pyscan.py -V 192.168.1.2
```

### Combine Options

```bash
python pyscan.py -s 20 -e 40000 -t 500 -V 192.168.1.2
```

## Options

| Option          | Description           | Default  |
| --------------- | --------------------- | -------- |
| `-s, --start`   | Starting port         | 1        |
| `-e, --end`     | Ending port           | 65535    |
| `-t, --threads` | Number of threads     | 500      |
| `-V, --verbose` | Enable verbose output | Disabled |
| `-v, --version` | Display version       | 3.0      |

## Technologies

* Python
* Socket
* Threading
* Argparse

## Screenshots

### Basic Usage

### Advanced Usage

## Disclaimer

PyScan is intended for educational purposes and authorized security testing only. Do not scan systems without proper authorization.

## Version

PyScan V3.0
