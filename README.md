# Benchmarco - The Benchmarking Bot

Benchmarco is a bot that runs benchmarks on your code and reports the results.

## Usage

Simple usage should be as follows:

```yml
name: Benchmark

on:
    pull_requests: [main]

jobs:
    benchmark:
        runs-on: ubuntu-latest

        steps:
        - uses: actions/benchmarco@v1
          with:
            script: run.sh
            compare: main
```

## Configuration

### `compare` - Compare with previous results

It can assume the following values:

* `main` - Compare with the main branch.
* `tag` - Compare with the latest tag.

### `script` - Script to run

This is the path to the script to run e.g. `run.sh` . The root path is the root of the repository.
