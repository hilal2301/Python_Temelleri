

import random

print("Sayı Tahmini Oyununa Hoş Geldiniz")
rastgele_sayi = random.randint(1, 100)  # Rastgele bir sayı üret

while True:
    tahmin = int(input("1 ile 100 arasında bir sayı tahmin et: "))  # Kullanıcıdan giriş al
    if tahmin < rastgele_sayi:
        print("Daha büyük bir sayı tahmin edin")  # Tahmin küçükse yönlendirme
    elif tahmin > rastgele_sayi:
        print("Daha küçük bir sayı tahmin edin")  # Tahmin büyükse yönlendirme
    else:
        print("Tebrikler, doğru tahmin!")  # Doğru tahmin
        break  # Döngüyü sonlandır

