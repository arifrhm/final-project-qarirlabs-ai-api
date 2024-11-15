
# AI Engineering Service

Layanan AI Engineering menggunakan FastAPI dan Roboflow untuk prediksi gambar.

## Deskripsi

Proyek ini adalah sebuah service AI Engineering yang menggunakan arsitektur bersih (clean architecture) dengan FastAPI sebagai framework web dan integrasi Roboflow untuk prediksi gambar. Layanan ini dirancang dengan prinsip decoupling, memungkinkan fleksibilitas untuk beralih ke layanan AI lain di masa depan jika diperlukan.

## Fitur

- Prediksi gambar menggunakan model Roboflow
- API RESTful dengan FastAPI
- Arsitektur bersih untuk memudahkan pemeliharaan dan pengembangan
- Konfigurasi berbasis environment variables

## Persyaratan

- Python 3.7+
- FastAPI
- Uvicorn
- Roboflow
- Python-dotenv

## Instalasi

1. Clone repositori ini:
   ```
   git clone https://github.com/username/ai-engineering-service.git
   cd ai-engineering-service
   ```

2. Buat virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # Untuk Unix atau MacOS
   venv\Scripts\activate  # Untuk Windows
   ```

3. Install dependensi:
   ```
   pip install -r requirements.txt
   ```

4. Salin file `.env.example` ke `.env` dan isi dengan konfigurasi yang sesuai:
   ```
   cp .env.example .env
   ```

## Penggunaan

1. Jalankan server:
   ```
   uvicorn app.main:app --reload
   ```

2. Akses API dokumentasi di `http://localhost:8000/docs`

3. Gunakan endpoint `/api/v1/predict` untuk melakukan prediksi gambar

## Struktur Proyek

```
.
├── app/
│   ├── api/
│   │   └── routes/
│   ├── core/
│   ├── models/
│   ├── services/
│   └── main.py
├── tests/
├── .env
├── requirements.txt
└── README.md
```

## Pengembangan

Untuk menambahkan layanan AI baru:

1. Buat kelas baru di `app/services/` yang mengimplementasikan `PredictionService`
2. Update `app/api/routes/prediction.py` untuk menggunakan layanan baru

## Kontribusi

Kontribusi selalu diterima. Silakan buka issue atau submit pull request.

## Lisensi

[MIT License](https://opensource.org/licenses/MIT)