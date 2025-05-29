# gui.py

import tkinter as tk
from tkinter import messagebox, Listbox
from hamming import generate_hamming_code, introduce_error, calculate_syndrome, correct_error
from memory import yaz_bellege, bellegi_goster, oku_bellekten

class HammingApp:
    def __init__(self, master):
        self.master = master
        master.title("Hamming SEC-DED Simülatörü")

        # === VERİ GİRİŞİ ===
        self.label = tk.Label(master, text="8, 16 veya 32 bitlik veri girin:")
        self.label.pack()

        self.veri_entry = tk.Entry(master, width=40)
        self.veri_entry.pack()

        self.yaz_button = tk.Button(master, text="Belleğe Yaz", command=self.belgeye_yaz)
        self.yaz_button.pack()

        # === BELLEK LİSTESİ ===
        self.bellek_listbox = Listbox(master, width=50)
        self.bellek_listbox.pack()

        self.refresh_button = tk.Button(master, text="Belleği Göster", command=self.bellegi_guncelle)
        self.refresh_button.pack()

        # === HATA EKLEME & DÜZELTME ===
        self.hata_entry = tk.Entry(master, width=20)
        self.hata_entry.pack()
        self.hata_entry.insert(0, "Hata pozisyonu gir (1'den başlayarak)")

        self.hata_button = tk.Button(master, text="Hata Ekle ve Düzelt", command=self.hata_ekle_duzelt)
        self.hata_button.pack()

        self.sonuc_label = tk.Label(master, text="")
        self.sonuc_label.pack()

    def belgeye_yaz(self):
        veri = self.veri_entry.get()
        if len(veri) not in [8, 16, 32]:
            messagebox.showerror("Hata", "Sadece 8, 16 veya 32 bitlik veri girebilirsiniz.")
            return
        hamming_kod = generate_hamming_code(veri)
        yaz_bellege(hamming_kod)
        messagebox.showinfo("Başarılı", f"Hamming Kodu belleğe yazıldı:\n{hamming_kod}")
        self.bellegi_guncelle()

    def bellegi_guncelle(self):
        self.bellek_listbox.delete(0, tk.END)
        for i, kod in bellegi_goster():
            self.bellek_listbox.insert(tk.END, f"{i}: {kod}")

    def hata_ekle_duzelt(self):
        try:
            secili = self.bellek_listbox.curselection()
            if not secili:
                raise Exception("Lütfen bir veri seçin.")
            index = secili[0]
            kod = oku_bellekten(index)

            poz = int(self.hata_entry.get())
            hatali = introduce_error(kod, poz)
            sendrom = calculate_syndrome(hatali)

            # DEBUG logları
            print("------ HATA ANALİZ LOG ------")
            print(f"Orijinal Kod     : {kod}")
            print(f"Hatalı Kod       : {hatali}")
            print(f"Hata Pozisyonu   : {poz}")
            print(f"Sendrom          : {sendrom}")

            if sendrom == 0:
                sonuc = f"Hata yok.\nKod: {hatali}"
            else:
                duzeltilmis = correct_error(hatali, sendrom)
                print(f"Düzeltilmiş Kod  : {duzeltilmis}")
                print("----------------------------")
                sonuc = f"Hata Pozisyonu: {sendrom}\nDüzeltilmiş Kod: {duzeltilmis}"

            self.sonuc_label.config(text=sonuc)

        except Exception as e:
            messagebox.showerror("Hata", str(e))


# === UYGULAMA BAŞLAT ===
if __name__ == "__main__":
    root = tk.Tk()
    app = HammingApp(root)
    root.mainloop()
