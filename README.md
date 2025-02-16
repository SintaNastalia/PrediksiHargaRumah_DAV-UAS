# Prediksi Harga Properti di Bali

Proyek ini adalah sebuah website prediksi harga properti di Bali yang dikembangkan menggunakan D3.JS. Website ini memungkinkan pengguna untuk menginput data properti dan memilih model prediksi yang diinginkan untuk mendapatkan estimasi harga properti di berbagai daerah di Bali. Tiga model prediksi yang digunakan adalah Linear Regression, Random Forest, dan Gradient Boosting.

## Fitur

1. **Input Data Properti**:
   - Tipe Rumah
   - Jumlah Kamar Mandi
   - Luas Tanah
   - Jumlah Kamar Tidur
   - Jumlah Carport
   - Luas Bangunan

2. **Pemilihan Model Prediksi**:
   - Linear Regression
   - Random Forest
   - Gradient Boosting

3. **Hasil Prediksi**:
   - Menampilkan estimasi harga properti berdasarkan daerah di Bali.
   - Membandingkan hasil prediksi dari ketiga model yang dipilih.

4. **Evaluasi Kinerja Model**:
   - Menggunakan Mean Squared Error (MSE) untuk menilai keakuratan dan kinerja model.
   - Menampilkan hasil perbandingan MSE dari ketiga model yang digunakan.

## Hasil dan Pembahasan

Berdasarkan hasil perbandingan Mean Squared Error (MSE) dari ketiga model yang diuji, yaitu Linear Regression, Random Forest, dan Gradient Boosting, dapat disimpulkan bahwa model Gradient Boosting memberikan hasil terbaik dengan nilai MSE terkecil. Model Random Forest menempati posisi kedua, sementara model Linear Regression menunjukkan performa terburuk. Dengan demikian, untuk prediksi yang lebih akurat dalam konteks dataset yang digunakan, model Gradient Boosting adalah pilihan yang paling optimal dibandingkan dengan dua model lainnya.


## Cara Menjalankan

### 1. Clone Repository
Clone repository ini ke komputer:
```bash
git clone https://github.com/SintaNastalia/PrediksiHargaRumah_DAV-UAS.git
cd PrediksiHargaRumah_DAV-UAS
```


### 2. Buat Virtual Environment (Opsional)
Disarankan untuk menjalankan aplikasi dalam virtual environment:
```bash
python -m venv venv
source venv/bin/activate      # Untuk Mac/Linux
venv\Scripts\activate         # Untuk Windows
```


### 3. Install Dependency
Install semua dependency Python yang tercatat dalam requirements.txt:
```bash
pip install -r requirements.txt
```


### 4. Jalankan Aplikasi Flask (Backend)
Jalankan aplikasi Flask:
```bash
python app.py
```
Aplikasi backend akan berjalan di http://127.0.0.1:5000. Jangan tutup terminal ini selama aplikasi digunakan.


### 5. Jalankan Frontend
Untuk menjalankan frontend, buka folder yang berisi file frontend, lalu jalankan perintah berikut:
```bash
python -m http.server
```
Server frontend akan berjalan di http://127.0.0.1:8000. Buka URL tersebut di browser untuk mengakses frontend.


### 6. Akses Aplikasi
```bash
Frontend: http://127.0.0.1:8000
Backend: http://127.0.0.1:5000
```



## Catatan
Python Version: Pastikan menggunakan Python versi 3.7 atau lebih tinggi.
Model: File .pkl adalah model machine learning yang sudah dilatih.


## Kontribusi
Jika memiliki saran atau ingin menambahkan fitur baru, silakan buat pull request atau buka issue baru di repository ini.
