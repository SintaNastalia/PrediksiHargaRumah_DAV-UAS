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
