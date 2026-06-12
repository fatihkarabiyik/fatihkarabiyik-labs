"""Tests for the caesar_cipher package."""

import pytest

from caesar_cipher import brute_force, decrypt, encrypt


# ---------------------------------------------------------------------------
# encrypt
# ---------------------------------------------------------------------------

class TestEncrypt:
    def test_basic_shift(self):
        assert encrypt("abc", 1) == "bcd"

    def test_wraps_around(self):
        assert encrypt("xyz", 3) == "abc"

    def test_preserves_case(self):
        assert encrypt("Hello", 3) == "Khoor"

    def test_preserves_non_alpha(self):
        assert encrypt("Hello, World!", 3) == "Khoor, Zruog!"

    def test_shift_zero(self):
        assert encrypt("abc", 0) == "abc"

    def test_shift_26_is_identity(self):
        assert encrypt("Caesar", 26) == "Caesar"

    def test_negative_shift(self):
        assert encrypt("bcd", -1) == "abc"

    def test_large_shift_normalised(self):
        assert encrypt("abc", 27) == encrypt("abc", 1)

    def test_empty_string(self):
        assert encrypt("", 5) == ""

    def test_digits_unchanged(self):
        assert encrypt("abc123", 1) == "bcd123"


# ---------------------------------------------------------------------------
# decrypt
# ---------------------------------------------------------------------------

class TestDecrypt:
    def test_basic_decrypt(self):
        assert decrypt("Khoor, Zruog!", 3) == "Hello, World!"

    def test_roundtrip(self):
        original = "The Quick Brown Fox"
        for shift in range(1, 26):
            assert decrypt(encrypt(original, shift), shift) == original

    def test_shift_zero(self):
        assert decrypt("abc", 0) == "abc"


# ---------------------------------------------------------------------------
# brute_force
# ---------------------------------------------------------------------------

class TestBruteForce:
    def test_returns_25_results(self):
        results = brute_force("Khoor!")
        assert len(results) == 25

    def test_correct_shift_recovers_plaintext(self):
        results = brute_force("Khoor!")
        shift_map = dict(results)
        assert shift_map[3] == "Hello!"

    def test_shifts_are_1_through_25(self):
        shifts = [s for s, _ in brute_force("test")]
        assert shifts == list(range(1, 26))
