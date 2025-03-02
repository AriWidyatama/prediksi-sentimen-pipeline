# Submission 1: Nama Proyek Anda
Nama: I Putu Suka Ari Widyatama

Username dicoding: oryshion

| | Deskripsi |
| ----------- | ----------- |
| Dataset | [DANA Sentiment Analysis from Playstore Indonesia](https://www.kaggle.com/datasets/alexmariosimanjuntak/dana-app-sentiment-review-on-playstore-indonesia) |
| Masalah | Analisis sentimen mengenai komentar pengguna terhadap aplikasi Dana di Playstore untuk memahami kepuasan pelanggan dan mengidentifikasi aspek yang perlu diperbaiki. |
| Solusi machine learning | Membangun model klasifikasi sentimen berbasis deep learning dengan pipeline untuk mengkategorikan komentar pengguna ke dalam tiga kelas yaitu negatif (0), netral (1), dan positif (2). |
| Metode pengolahan | Metode pengolahan data yang digunakan adalah label encoder untuk mengubah label kategorical, transform fitur, serta tokenisasi dan vektorisasi menggunakan TextVectorization . |
| Arsitektur model | Arsitektur model yang digunakan diantaranya Layer Input, Text Vectorization Layer, Embedding Layer, GlobalAveragePooling1D, Dense Layers, dan Output Layer berupa softmax untuk 3 kategori. |
| Metrik evaluasi | Metrik yang digunakan untuk mengevaluasi performa model diantaranya ExampleCount, SparseCategoricalAccuracy, MeanPrediction, MeanLabel, MAE, RMSE, ConfusionMatrixPlot, dan CalibrationPlot.|
| Performa model | Performa dari model mencapai akurasi di atas 80% pada data latih dan validasi, sehingga model dapat menunjukkan kemampuan yang cukup baik dalam mengklasifikasikan sentimen ulasan pengguna terhadap aplikasi Dana. |