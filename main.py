from hamming import generate_hamming_code, introduce_error, calculate_syndrome, correct_error
from memory import yaz_bellege, oku_bellekten, bellegi_goster

def main():
    while True:
        print("\n--- Hamming SEC-DED Simülatörü ---")
        print("1. Veri gir ve belleğe yaz")
        print("2. Belleği görüntüle")
        print("3. Bellekten oku ve hata ekle")
        print("4. Çıkış")

        secim = input("Seçiminiz (1-4): ")

        if secim == "1":
            veri = input("8, 16 veya 32 bitlik veri girin (örnek: 10110011): ")
            kod = generate_hamming_code(veri)
            yaz_bellege(kod)
            print(f"Hamming Kodu belleğe yazıldı: {kod}")

        elif secim == "2":
            print("--- Bellek ---")
            for i, v in bellegi_goster():
                print(f"{i}: {v}")

        elif secim == "3":
            index = int(input("Bellekten hangi veriyi okumak istiyorsunuz? (index girin): "))
            veri = oku_bellekten(index)
            if veri is None:
                print("Geçersiz index.")
                continue

            print(f"Seçilen veri: {veri}")
            pos = int(input("Hangi bit'e hata eklemek istersiniz? (1'den başlayarak): "))
            hatali = introduce_error(veri, pos)
            sendrom = calculate_syndrome(hatali)

            print(f"Hatalı Kod: {hatali}")
            print(f"Sendrom: {sendrom}")

            if sendrom == 0:
                print("Hata yok.")
            else:
                print(f"Hata tespit edildi. Pozisyon: {sendrom}")
                duzeltilmis = correct_error(hatali, sendrom)
                print(f"Düzeltilmiş Kod: {duzeltilmis}")

        elif secim == "4":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim.")
if __name__ == "__main__":
    main()
