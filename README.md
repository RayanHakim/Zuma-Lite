🐸 ZUMA LITE: ARCADE PUZZLE SHOOTER
Zuma Lite adalah sebuah permainan arcade-puzzle berbasis Python dan Pygame yang terinspirasi dari game klasik Zuma. Pemain bertugas menghentikan deretan bola berwarna agar tidak mencapai lubang akhir dengan cara menembakkan bola dan mencocokkan tiga warna yang sama atau lebih.

🎮 Fitur Utama & Mekanik
Aplikasi ini mengimplementasikan logika chain-reaction yang kompleks untuk menciptakan pengalaman bermain yang menantang:

⛓️ Dynamic Chain Logic: Bola bergerak mengikuti jalur (path) yang telah ditentukan secara otomatis menggunakan sistem koordinat jarak tempuh.

🎯 Precision Shooting: Mekanisme penembakan bola dari bawah layar dengan kontrol gerakan horizontal (kiri-kanan) yang responsif.

💥 Match-3 System: Penghancuran bola secara otomatis menggunakan algoritma pencarian batas jika terdapat 3 atau lebih warna yang sama bersentuhan.

🔮 Predictive Bullet: Indikator warna peluru berikutnya (Next Bullet) untuk membantu pemain menyusun strategi tembakan.

🏆 Data Persistence: Sistem penyimpanan skor tertinggi (High Score) dan menu pengaturan yang tersimpan secara lokal.

⏸️ Simpel Pause: Fitur jeda permainan menggunakan tombol ESC untuk kenyamanan sesi bermain yang fleksibel.

🧪 Arsitektur Proyek (Modular Structure)
Kode dirancang secara modular agar logika permainan, data, dan antarmuka terpisah dengan rapi:

📜 main.py: Pusat kendali aplikasi yang mengatur main menu dan game loop utama.

⚙️ config.py: Pusat konfigurasi global yang berisi data jalur (Path Points), warna, dan kecepatan game.

🛠️ utils.py: Fungsi pembantu untuk menangani perhitungan jarak matematis dan posisi bola pada jalur.

💾 high_score.py: Menangani sistem penyimpanan dan pembacaan data skor tertinggi dari file eksternal.

🔧 setting.py: Antarmuka untuk memodifikasi pengaturan tingkat kesulitan dan konfigurasi game.

🚪 keluar.py: Menangani tampilan menu Game Over dan manajemen pilihan navigasi setelah sesi berakhir.

🛠️ Tech Stack
Language: Python 3.x

Library: Pygame (Graphics & Input Handling)

Algorithm: Linear Path Interpolation & Chain Deletion Algorithm.

📂 Struktur Proyek
Plaintext
/Zuma-Lite
  ├── main.py          <-- Pusat Kontrol Game
  ├── config.py        <-- Pengaturan Jalur & Konstanta
  ├── utils.py         <-- Perhitungan Matematika & Render Teks
  ├── high_score.py    <-- Sistem Simpan Skor
  ├── setting.py       <-- Menu Pengaturan
  ├── keluar.py        <-- Menu Keluar & Game Over
  └── README.md        <-- Dokumentasi Proyek
🚀 Panduan Instalasi
Persiapan: Pastikan library Pygame sudah terpasang di komputer Anda. Jika belum, instal melalui terminal:
pip install pygame

Jalankan Permainan: Eksekusi file utama untuk memulai sesi permainan:
python main.py
