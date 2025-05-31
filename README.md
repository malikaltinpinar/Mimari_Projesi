Hamming SEC-DED Code Simülatörü

# Hamming SEC-DED Kod Simülatörü

Bu proje, tek bitlik hataların düzeltilmesi (SEC - Single Error Correction) ve çift bitlik hataların algılanması (DED - Double Error Detection) amacıyla kullanılan Hamming kodlama yöntemini Python dili ile gerçekleştiren grafik arayüzlü bir simülatördür.

## 📌 Amaç

- Hamming algoritmasını uygulamalı olarak öğrenmek
- Kullanıcı dostu bir GUI (tkinter) üzerinden kodlama, hata üretimi ve düzeltme işlemlerini simüle etmek
- Hata tespit ve düzeltme süreçlerini adım adım görselleştirmek

## 🧠 Temel Bilgiler

Hamming SEC-DED algoritması, parite bitleri ekleyerek hata konumlarını tespit eder. Eğer sendrom sonucu 0’dan farklı ise hata vardır ve pozisyonu hesaplanarak düzeltilebilir.

## 📁 Proje Yapısı

HammingSimulator/
├── hamming.py # Hamming kodlama, hata üretimi, sendrom ve düzeltme
├── memory.py # Bellek listesi simülasyonu
├── gui.py # tkinter tabanlı grafik arayüz
├── main.py # Komut satırı ile çalıştırılabilir versiyon
└── README.md # Bu dosya


## 🚀 Kurulum

Python 3.10+ sürümüyle uyumludur.

1. Depoyu klonlayın veya dosyaları indirin:
   ```bash
   git clone https://github.com/kullanici/hamming-simulator.git
   cd hamming-simulator
2. Gerekli modülleri yükleyin (yalnızca standart kütüphaneler kullanılmıştır):
   python3 gui.py
   
🖥️ Kullanım
GUI Arayüzü:
8, 16 veya 32 bitlik bir veri girin (örnek: 10110011)

“Belleğe Yaz” ile kod oluşturulup belleğe eklenir

Listeden veri seçin, hata pozisyonunu girin (örn. 3)

“Hata Ekle ve Düzelt” butonu ile işlem gerçekleştirilir

Terminal (CLI) Kullanımı:
python3 main.py

📊 Örnek Çıktı (GUI Terminal Log)

- HATA ANALİZ LOG -
Orijinal Kod     : 101101100011
Hatalı Kod       : 100101100011
Hata Pozisyonu   : 3
Sendrom          : 3
Düzeltilmiş Kod  : 101101100011


✅ Özellikler
8 / 16 / 32 bit veri girişi desteği

Manuel hata pozisyonu girişi

Sendrom tabanlı hata tespiti

Anında düzeltme işlemi

tkinter GUI desteği

🔧 Bilinen Sorunlar
Şu an için yalnızca tek bit hataları düzeltilebilmektedir

Çoklu hata durumları sadece “algılanabilir” ancak düzeltilmez

🌱 Geliştirme Olanakları
Rastgele hata üretici entegrasyonu

Belleği dosyaya kaydetme / okuma

Çift bit düzeltme destekli ileri algoritmalar

Mobil arayüz (Kivy) veya web tabanlı GUI (Flask)

👨‍💻 Geliştirici
Enes Malik Altınpınar
Bursa Teknik Üniversitesi – Bilgisayar Mühendisliği
Öğrenci No: 22360859323
Video Bağlantısı:•	https://youtu.be/Tx19rb27SdA

📚 Kaynakça
Hamming, R. W. (1950). Error Detecting and Error Correcting Codes.

Mano, M. M. (2001). Computer System Architecture.

Stallings, W. (2021). Computer Organization and Architecture.

https://en.wikipedia.org/wiki/Hamming_code

https://www.geeksforgeeks.org/hamming-code/
