# Install RUST

TODO:

This is a working in progress.

## Install Python RUST

```bash
$ git clone https://github.com/RustPython/RustPython.git
$ cd RustPython
$ rustyp update
$ rustup target add wasm32-unknown-unknown
$ rustup target add wasm32-wasi
$ cargo build --release --target wasm32-unknown-unknown
