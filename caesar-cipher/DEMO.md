# Demo

## Encrypt

```
$ python main.py encrypt "Hello, World!" 3
Khoor, Zruog!
```

## Decrypt

```
$ python main.py decrypt "Khoor, Zruog!" 3
Hello, World!
```

## Brute force (unknown shift)

```
$ python main.py brute-force "Khoor!"
[shift  1] Jgnnq!
[shift  2] Ifmmp!
[shift  3] Hello!
[shift  4] Gdkkn!
...
```

## Run tests

```
$ just test
========================= test session starts =========================
collected 16 items

tests/test_cipher.py ................                            [100%]
========================== 16 passed in 0.05s =========================
```
