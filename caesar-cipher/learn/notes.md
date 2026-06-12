# Caesar Cipher — öğrenme notları

## Temel kavram

Caesar cipher, her harfi alfabe üzerinde sabit bir sayı kadar kaydırarak çalışan en basit şifreleme yöntemlerinden biridir.

```
Düz metin:  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Kaydırma 3: D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
```

## Algoritma adımları

1. Her karakter için:
   - Harf değilse olduğu gibi bırak
   - Harfse ASCII değerini al
   - Büyük/küçük harf tabanını belirle (`A` = 65, `a` = 97)
   - `(ord(ch) - base + shift) % 26 + base` formülünü uygula
2. Sonuçları birleştir

## Neden `% 26`?

Modülo işlemi kaydırmanın alfabenin sonuna gelince başa dönmesini sağlar.
`Z` + 3 = `C` (25 + 3 = 28 → 28 % 26 = 2 → `C`)

## Egzersizler

1. `cipher.py` dosyasını okuyun ve `_shift_text` fonksiyonunu anlayın.
2. `encrypt("python", 13)` çıktısını elle hesaplayın, ardından programla doğrulayın.
3. ROT13 özel bir Caesar cipher mıdır? Neden?
4. `brute_force` fonksiyonunu kullanarak `"Gur dhvpx oebja sbk"` metnini çözün.
