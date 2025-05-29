import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit,
    QRadioButton, QButtonGroup, QPushButton, QMessageBox
)
from PyQt5.QtGui import QIntValidator


class HammingCodeSimulator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hamming Kodu Simülasyonu")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.hamming_code = None

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # Hamming kodu uzunluğunu seçmek için düğmeler
        length_label = QLabel("Hamming Kodu Uzunluğu:")
        main_layout.addWidget(length_label)

        self.length_group = QButtonGroup(self)
        self.length_group.buttonClicked[int].connect(self.update_bit_boxes)

        for length in [4, 8, 16]:
            radio_button = QRadioButton(f"{length} bit")
            self.length_group.addButton(radio_button, length)
            main_layout.addWidget(radio_button)
        
        self.bit_layout = QHBoxLayout()
        main_layout.addLayout(self.bit_layout)

        # Kodlamayı başlatma
        self.encode_button = QPushButton("Kodlamayı Başlat")
        self.encode_button.clicked.connect(self.start_encoding)
        main_layout.addWidget(self.encode_button)

        # Sonuç alanı
        self.result_label = QLabel("Sonuç:")
        main_layout.addWidget(self.result_label)

        self.central_widget.setLayout(main_layout)

        self.encoded_bit_layout = QHBoxLayout()
        main_layout.addLayout(self.encoded_bit_layout)

        # Hata oluşturma
        self.error_button = QPushButton("Hata Oluştur")
        self.error_button.clicked.connect(self.create_error)
        self.error_button.setEnabled(False)
        main_layout.addWidget(self.error_button)

        self.error_apply_button = QPushButton("Hata Uygula")
        self.error_apply_button.clicked.connect(self.apply_error)
        main_layout.addWidget(self.error_apply_button)

        # Başlangıçta 4 bitlik giriş kutularını otomatik oluşturma
        self.update_bit_boxes(4)

    def update_bit_boxes(self, length):
        # Giriş kutularını temizleme
        for i in reversed(range(self.bit_layout.count())):
            widget = self.bit_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()

        # Yeni giriş kutularını oluşturma
        self.bit_entries = []
        for i in range(length):
            bit_entry = QLineEdit()
            bit_entry.setFixedSize(60, 60)  # Giriş kutusu boyutunu ayarlama 
            bit_entry.setMaxLength(1)  # Sadece tek bir karakter girişine izin verme
            bit_entry.setValidator(QIntValidator(0, 1))  # Sadece 0 ve 1 değerlerini kabul etme
            self.bit_layout.addWidget(bit_entry)
            self.bit_entries.append(bit_entry)

    def start_encoding(self):
        # Kullanıcıdan bit dizisini alma işlemi
        self.data = ''.join([entry.text() for entry in self.bit_entries])
        if len(self.data) != len(self.bit_entries):
            QMessageBox.warning(self, "Eksik Giriş", "Lütfen tüm kutulara 0 veya 1 girin.")
            return

        self.encoded_data, parities = self.encode_data(self.data)
        parity_text = '\n'.join([f"P{i+1} = {parities[i]}" for i in range(len(parities))])
        encoded_text = ''.join(map(str, self.encoded_data))

        # Hamming kodu hesaplama 
        self.hamming_code = self.calculate_hamming_code(self.encoded_data)

        self.result_label.setText(f"Parite Bitleri:\n{parity_text}\n\nKodlanmış Veri: {encoded_text}\n\n")

        # Parite bitleri ve verinin birleşimi olan kodlanmış veriyi giriş kutularına yerleştirme
        self.display_encoded_bits()

    def display_encoded_bits(self):
        # Kodlanmış veri kutularını temizleme
        for i in reversed(range(self.encoded_bit_layout.count())):
            widget = self.encoded_bit_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()

        # Kodlanmış veri giriş kutularını oluşturma
        self.encoded_bit_entries = []
        for bit in self.encoded_data:
            bit_entry = QLineEdit()
            bit_entry.setFixedSize(60, 60)
            bit_entry.setMaxLength(1)
            bit_entry.setValidator(QIntValidator(0, 1))
            bit_entry.setText(str(bit))
            bit_entry.setReadOnly(True)
            self.encoded_bit_layout.addWidget(bit_entry)
            self.encoded_bit_entries.append(bit_entry)

        self.error_button.setEnabled(True)

    def create_error(self):
        for entry in self.encoded_bit_entries:
            entry.setReadOnly(False)

        self.error_button.setEnabled(False)

        # Kullanıcıya uyarı
        self.result_label.setText("(LÜTFEN SADECE 1 BİT DEĞİŞTİRİNİZ)")

        self.encoded_bit_entries[0].setFocus()

    def calculate_hamming_code(self, encoded_data):
        hamming_code = 0
        for i in range(len(encoded_data)):
            hamming_code ^= (i + 1) * encoded_data[i]
        # Hamming kodunu doğru uzunlukta binary string olarak döndürür
        hamming_code_length = len(bin(len(encoded_data))[2:])
        return bin(hamming_code)[2:].zfill(hamming_code_length)


    def encode_data(self, data):
        data_length = len(data)
         
        hamming_length = 2
        while 2 ** hamming_length - 1 < data_length + hamming_length:
            hamming_length += 1

        data_list = list(data)

        # Parite bitlerini ekleme
        encoded_data = []
        index = 0
        for i in range(1, hamming_length + data_length + 1):
            if i == 2 ** index:
                encoded_data.append(0)
                index += 1
            else:
                encoded_data.append(int(data_list.pop(0)))

        parities = []
        for i in range(hamming_length):
            parity_index = 2 ** i - 1
            parities.append(self.calculate_parity(encoded_data, parity_index))

        for i in range(hamming_length):
            parity_index = 2 ** i - 1
            encoded_data[parity_index] = parities[i]
        return encoded_data, parities

    def calculate_parity(self, encoded_data, parity_index):
        parity = 0
        i = parity_index
        while i < len(encoded_data):
            for j in range(parity_index + 1):
                if i + j < len(encoded_data):
                    parity ^= encoded_data[i + j]
            i += 2 * (parity_index + 1)
        return parity

    def apply_error(self):
        # Kodlanmış verideki 1 değerine sahip indislerin konumlarını bulma
        error_indices = [i for i, entry in enumerate(self.encoded_bit_entries) if entry.text() == '1']

        # İndislerin binary karşılıklarını XOR'layarak hatalı bitin konumunu bulma
        error_position = 0
        for index in error_indices:
            error_position ^= index + 1

        error_position_binary = bin(error_position)[2:]

        if error_position == 0:
            QMessageBox.warning(self, "Hata Yok", "Herhangi bir hata bulunmuyor.")
            return
        else:
            self.find_invert_error_position(error_position_binary)

    def find_invert_error_position(self, error_position_binary):
        error_position = int(error_position_binary, 2)

        # Hata bulunan bitin değerini tersine çevirme
        error_bit_entry = self.encoded_bit_entries[error_position - 1]
        current_value = int(error_bit_entry.text())
        new_value = 1 if current_value == 0 else 0
        error_bit_entry.setText(str(new_value))

        # Verinin doğru halini oluşturma
        new_data = ''.join(entry.text() for entry in self.encoded_bit_entries)

        # Yapılan değişiklikleri kullanıcıya bildirme
        QMessageBox.information(self, "Hata Düzeltildi", f"Hata bulunan bitin değeri tersine çevrildi: {error_position}\n\nVerinin doğru hali: {new_data}")

def main():
    app = QApplication(sys.argv)
    simulator = HammingCodeSimulator()
    simulator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

