# bplus

[![Build Status](https://travis-ci.org/k2uhl/bplus.svg?branch=master)](https://travis-ci.org/k2uhl/bplus)
[![Coverage](https://coveralls.io/repos/github/k2uhl/bplus/badge.svg)](https://coveralls.io/github/k2uhl/bplus)
[![Documentation](https://readthedocs.org/projects/bplus/badge/?version=latest)](https://bplus.readthedocs.org/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/bplus.svg)](https://pypi.python.org/pypi/bplus)
[![PyPI Pythons](https://img.shields.io/pypi/pyversions/bplus.svg)](https://pypi.python.org/pypi/bplus)
[![License](https://img.shields.io/pypi/l/bplus.svg)](https://github.com/k2uhl/bplus/blob/master/LICENSE)

The database shell with a passing grade.

## Features

* What it do?

## Usage

* TODO

## Install

```console
pip install bplus
```

## Documentation
See https://bplus.readthedocs.org/en/latest/

## Development
```console
pip install poetry
cd bplus
poetry install
```
### Run
To run cli entrypoint:
```console
poetry run bplus --help
```

### Tests
```console
poetry run tox
```

### Docker
To run with docker
```console
docker build -t bplus .
docker run bplus:latest bplus --help
```
