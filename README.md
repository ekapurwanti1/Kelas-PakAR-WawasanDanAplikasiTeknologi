📘 Sistem Deteksi Diabetes Menggunakan Artificial Intelligence (AI)
Proyek ini merupakan bagian dari tugas mata kuliah Wawasan dan Aplikasi Teknologi, dengan fokus pada penggunaan Artificial Intelligence (AI) di bidang kesehatan. Sistem ini menggunakan Logistic Regression untuk memprediksi apakah seorang pasien berpotensi mengidap diabetes, berdasarkan data kesehatan dari dataset Pima Indian.

🧠 Fitur Utama
Input data kesehatan pasien (glukosa, tekanan darah, BMI, dll)

Algoritma Machine Learning (Logistic Regression)

Evaluasi akurasi model (precision, recall, f1-score)

Deteksi otomatis potensi diabetes berdasarkan data

🛠️ Teknologi yang Digunakan
Python 3

Pandas

Scikit-learn

Dataset: Kaggle – Pima Indian Diabetes

🚀 Cara Menjalankan
Clone repository ini.

Install dependensi:

bash
Copy
Edit
pip install pandas scikit-learn
Pastikan file diabetes.csv tersedia di folder dataset/.

Jalankan program:

bash
Copy
Edit
python diabetes_prediction.py
📄 Panduan Pengguna
Dokumentasi lengkap dan buku panduan pengguna tersedia di dalam repository. Panduan ini mencakup:

Deskripsi sistem

Alur proses

Penjelasan output

Etika penggunaan

📊 Output Program (Contoh)
diff
Copy
Edit
=== Hasil Evaluasi Model ===
              precision    recall  f1-score   support
           0       0.76      0.87      0.81       107
           1       0.69      0.52      0.59        47
    accuracy                           0.74       154
📌 Catatan Etis
⚠️ Model ini tidak untuk digunakan dalam diagnosa medis nyata. Tujuan proyek ini adalah edukatif dan eksploratif.
