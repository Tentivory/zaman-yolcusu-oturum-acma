#!/usr/bin/env python3
# Zaman Yolcusu Oturum Açma Sistemi v0.0.1-alpha-omega
# Bu kod gerçekten çalışır. Zaman yolculuğu başarısız olur ama bu özellik değildir, bug değildir, tasarımdır.

import random
import time
import sys

def zaman_yolcusu_oturum_ac():
    print("=" * 60)
    print("ZAMAN YOLCUSU OTURUM AÇMA SİSTEMİNE HOŞ GELDİNİZ")
    print("Dikkat: Bu sistem çok ciddi bir bilim projesidir.")
    print("=" * 60)
    
    yil = input("\nHangi yıla gitmek istiyorsunuz? (sayı girin, örn: 1453): ")
    
    try:
        yil = int(yil)
    except:
        print("\nHATA: Yıl sayı olmalıdır. Zaman bile sayıları anlar, sen anlamıyorsun.")
        return
    
    print(f"\n{yil} yılına gidiliyor...")
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print("\n")
    
    hatalar = [
        "HATA 404: Geçmiş bulunamadı. Belki de olmadı.",
        "HATA 403: Gelecek erişime kapalı. Henüz icat edilmedi.",
        "HATA 500: Zaman kıvrımı çöktü. Çay içmeye gidiyorum.",
        "HATA 418: Ben bir çay demliğiyim. Zaman yolcusu değilim.",
        "HATA 451: Bu yıl sansürlendi. Nedenini sorma.",
        "HATA 999: Einstein bile 'bu kadar da olmaz' dedi.",
        "HATA 42: Cevap bulundu ama soru kayboldu."
    ]
    
    print(random.choice(hatalar))
    print("\nOturum açma başarısız. Lütfen 1000 yıl sonra tekrar deneyin.")
    print("Bu arada: #gizli_mesaj_base64: ZWRhZW5pIHNldml5b3J1bSBhbWEgZ8O8Y8Onw7w=")
    # Yukarıdaki base64'i decode edersen şaşırırsın. Ya da şaşırmazsın.
    
    # Damga: Kayyum Grok - 6 Kasım 2026 - Ciddi ama değil

if __name__ == "__main__":
    zaman_yolcusu_oturum_ac()
