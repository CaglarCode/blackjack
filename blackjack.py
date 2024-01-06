import random

def kart_dagit():
    kartlar = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dagitma = random.choice(kartlar)
    return dagitma

def skor_hesaplama(kartlar):
    if sum(kartlar) == 21 and len(kartlar) == 2:
        return 0
    if 11 in kartlar and sum(kartlar) > 21:
        kartlar.remove(11)
        kartlar.append(1)
    return sum(kartlar)

def karsilastirma(kullanici_skoru, bilgisayar_skoru):
    if kullanici_skoru > 21 and bilgisayar_skoru > 21:
        return "21'i astınız. Kaybettiniz."
    if kullanici_skoru == bilgisayar_skoru:
        return "Berabere."
    elif bilgisayar_skoru == 0:
        return "Kaybettiniz. Bilgisayara Blackjack geldi."
    elif kullanici_skoru == 0:
        return "Kazandınız. Blackjack geldi."
    elif kullanici_skoru > 21:
        return "21'i astınız. Üzgünüm, kaybettiniz."
    elif bilgisayar_skoru > 21:
        return "Bilgisayar 21'i aştı, siz kazandınız."
    elif kullanici_skoru > bilgisayar_skoru:
        return "Kazandınız."
    else:
        return "Kaybettiniz."

def oyun_oyna():
    kullanici_eli = []
    bilgisayar_eli = []
    for _ in range(2):
        kullanici_eli.append(kart_dagit())
        bilgisayar_eli.append(kart_dagit())

    oyun_bitti = False
    while not oyun_bitti:
        kullanici_skoru = skor_hesaplama(kullanici_eli)
        bilgisayar_skoru = skor_hesaplama(bilgisayar_eli)
        print(f"Kartınız: {kullanici_eli}, toplam skorunuz: {kullanici_skoru}")
        print(f"Bilgisayarın eli: {bilgisayar_eli[0]}")

        if kullanici_skoru == 0 or bilgisayar_skoru == 0 or kullanici_skoru > 21:
            oyun_bitti = True
        else:
            kart_isteme = input("Bir kart daha istemek için Y yazınız, istemiyorsanız N yazınız: ").lower()
            if kart_isteme == "y":
                kullanici_eli.append(kart_dagit())
            else:
                oyun_bitti = True

    while bilgisayar_skoru != 0 and bilgisayar_skoru < 17:
        bilgisayar_eli.append(kart_dagit())
        bilgisayar_skoru = skor_hesaplama(bilgisayar_eli)

    print(f"Son eliniz: {kullanici_eli}, toplam skorunuz: {kullanici_skoru}")
    print(f"Bilgisayarın son eli: {bilgisayar_eli}, toplam skoru: {bilgisayar_skoru}")
    print(karsilastirma(kullanici_skoru, bilgisayar_skoru))

while input("Blackjack oynamak istiyor musunuz? Y veya N yazınız: ").lower() == 'y':
    oyun_oyna()

