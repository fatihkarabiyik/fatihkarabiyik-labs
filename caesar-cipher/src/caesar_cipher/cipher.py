"""Caesar cipher: encrypt and decrypt text by shifting alphabet characters."""


def encrypt(text: str, shift: int) -> str:
    """Encrypt plaintext using a Caesar cipher with the given shift.

    Args:
        text:  The plaintext string to encrypt.
        shift: Number of positions to shift each letter (can be negative).

    Returns:
        The encrypted ciphertext. Non-alphabetic characters are unchanged.

    Examples:
        >>> encrypt("Hello, World!", 3)
        'Khoor, Zruog!'
        >>> encrypt("abc", 1)
        'bcd'
    """
    return _shift_text(text, shift)


def decrypt(text: str, shift: int) -> str:
    """Decrypt ciphertext that was encrypted with the given shift.

    Args:
        text:  The ciphertext string to decrypt.
        shift: The shift value that was used during encryption.

    Returns:
        The original plaintext. Non-alphabetic characters are unchanged.

    Examples:
        >>> decrypt("Khoor, Zruog!", 3)
        'Hello, World!'
        >>> decrypt("bcd", 1)
        'abc'
    """
    return _shift_text(text, -shift)


def brute_force(text: str) -> list[tuple[int, str]]:
    """Return all 25 possible decryptions of ciphertext.

    Useful when the shift value is unknown.

    Args:
        text: The ciphertext string to brute-force.

    Returns:
        A list of (shift, plaintext) tuples for shifts 1 through 25.

    Examples:
        >>> results = brute_force("Khoor!")
        >>> results[2]
        (3, 'Hello!')
    """
    return [(shift, decrypt(text, shift)) for shift in range(1, 26)]


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _shift_text(text: str, shift: int) -> str:
    """Shift every alphabetic character in *text* by *shift* positions."""
    shift = shift % 26  # normalise to 0-25
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)
