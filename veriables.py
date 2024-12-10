import random

print("Taş-Kağıt-Makas Oyununa Hoş Geldiniz!")
print("Seçenekler: Taş, Kağıt, Makas")

while True:
    kullanici_secimi = input("Seçiminizi yapın (taş, kağıt, makas): ").lower()
    
    # Geçersiz seçim kontrolü
    if kullanici_secimi not in ["taş", "kağıt", "makas"]:
        print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")
        continue
    
    # Bilgisayarın seçimi
    bilgisayar_secimi = random.choice(["taş", "kağıt", "makas"])
    print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")
    
    # Sonuç kontrolü
    if kullanici_secimi == bilgisayar_secimi:
        print("Berabere!")
    elif (
        (kullanici_secimi == "taş" and bilgisayar_secimi == "makas") or
        (kullanici_secimi == "kağıt" and bilgisayar_secimi == "taş") or
        (kullanici_secimi == "makas" and bilgisayar_secimi == "kağıt")
    ):
        print("Tebrikler, kazandınız!")
    else:
        print("Bilgisayar kazandı!")
    
    # Oyuna devam etme seçeneği
    devammi = input("Tekrar oynamak ister misin? (e/h): ").lower()
    if devammi != "e":
        print("Oyundan çıkılıyor. Görüşmek üzere!")
        break
