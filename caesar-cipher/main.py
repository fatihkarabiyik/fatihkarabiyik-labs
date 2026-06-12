"""Command-line interface for the Caesar cipher."""

import argparse
import sys

from caesar_cipher import brute_force, decrypt, encrypt


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="caesar-cipher",
        description="Encrypt or decrypt text with a Caesar cipher.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- encrypt ---
    enc = subparsers.add_parser("encrypt", aliases=["e"], help="Encrypt plaintext")
    enc.add_argument("text", help="Text to encrypt")
    enc.add_argument("shift", type=int, help="Shift amount (integer)")

    # --- decrypt ---
    dec = subparsers.add_parser("decrypt", aliases=["d"], help="Decrypt ciphertext")
    dec.add_argument("text", help="Text to decrypt")
    dec.add_argument("shift", type=int, help="Shift amount used during encryption")

    # --- brute-force ---
    bf = subparsers.add_parser("brute-force", aliases=["bf"], help="Try all 25 shifts")
    bf.add_argument("text", help="Ciphertext to brute-force")

    args = parser.parse_args()

    if args.command in ("encrypt", "e"):
        print(encrypt(args.text, args.shift))
    elif args.command in ("decrypt", "d"):
        print(decrypt(args.text, args.shift))
    elif args.command in ("brute-force", "bf"):
        for shift, plaintext in brute_force(args.text):
            print(f"[shift {shift:>2}] {plaintext}")


if __name__ == "__main__":
    sys.exit(main())
