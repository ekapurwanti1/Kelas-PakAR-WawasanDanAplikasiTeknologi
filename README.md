
# Model Prediksi Diabetes dengan Regresi Logistik

Repository ini berisi skrip Python untuk memprediksi kemungkinan seseorang menderita diabetes menggunakan model regresi logistik. Dataset yang digunakan berisi informasi medis pasien, dan model ini dilatih untuk memprediksi apakah seseorang memiliki diabetes berdasarkan data tersebut.

## Persyaratan:
- Python 3.x
- Pandas
- scikit-learn

## Cara Menjalankan:
1. **Clone repository ini:**
   Untuk mengunduh proyek ini ke komputer lokal Anda, buka terminal atau command prompt, lalu jalankan perintah berikut:
   ```bash
   git clone https://github.com/ekapurwanti1/Kelas-PakAR-WawasanDanAplikasiTeknologi
   ```

2. **Instalasi dependensi:**
   Setelah repository di-clone anda juga bisa menginstal paket secara manual menggunakan pip:
   ```bash
   pip install pandas scikit-learn
   ```

4. **Menyiapkan dataset:**
   Dataset yang digunakan dalam proyek ini berada di folder `dataset/diabetes.csv`. Pastikan Anda memiliki file dataset yang sesuai di folder yang tepat, atau Anda dapat menggantinya dengan dataset Anda sendiri yang sesuai formatnya.

5. **Menjalankan skrip:**
   Jalankan skrip `diabetes_prediction.py` untuk melatih dan mengevaluasi model prediksi diabetes. Skrip ini akan memuat data, melatih model menggunakan regresi logistik, dan kemudian menampilkan laporan evaluasi model.
   ```bash
   python diabetes_prediction.py
   ```

   Model ini akan melakukan pemisahan data menjadi data latih dan data uji (80-20), melatih model regresi logistik, dan menampilkan hasil evaluasi menggunakan classification report.

## Struktur Proyek:
- **diabetes_prediction.py**: Skrip utama untuk melatih dan menguji model prediksi diabetes.
- **dataset/diabetes.csv**: Dataset yang berisi informasi medis untuk memprediksi diabetes.
- **requirements.txt**: Daftar dependensi yang diperlukan untuk menjalankan proyek ini.

## Hasil Evaluasi Model:
Skrip ini menggunakan regresi logistik untuk memprediksi apakah seseorang akan mengembangkan diabetes berdasarkan fitur-fitur seperti usia, tekanan darah, BMI, dll. Evaluasi model akan ditampilkan dalam format classification report yang mencakup precision, recall, f1-score, dan akurasi.
