# Caesar Cipher

A beginner Python project implementing the classic Caesar cipher — encrypt and decrypt text by shifting each letter a fixed number of positions in the alphabet.

## Features

- Encrypt plaintext with any integer shift
- Decrypt ciphertext back to plaintext
- Brute-force all 25 possible shifts when the key is unknown
- Clean CLI (`encrypt`, `decrypt`, `brute-force` subcommands)
- Fully tested with pytest

## Quick start

```bash
# Install dependencies (requires uv)
uv sync

# Encrypt
python main.py encrypt "Hello, World!" 3
# → Khoor, Zruog!

# Decrypt
python main.py decrypt "Khoor, Zruog!" 3
# → Hello, World!

# Brute force
python main.py brute-force "Khoor!"
```

Or use the shortcuts in the Justfile:

```bash
just encrypt "Hello, World!" 3
just decrypt "Khoor, Zruog!" 3
just test
```

## Project structure

```
caesar-cipher/
├── assets/          # Screenshots and demo GIF
├── learn/           # Beginner notes and walkthroughs
├── src/
│   └── caesar_cipher/
│       ├── __init__.py
│       └── cipher.py
├── tests/
│   └── test_cipher.py
├── main.py
├── pyproject.toml
├── Justfile
└── DEMO.md
```

## How it works

Each letter is shifted forward (encryption) or backward (decryption) by the key value, wrapping around at Z → A. Non-alphabetic characters (spaces, punctuation, digits) pass through unchanged. Case is preserved.

## License

MIT
