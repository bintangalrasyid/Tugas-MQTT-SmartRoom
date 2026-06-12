# Tugas-MQTT-SmartRoom
# Implementasi Komunikasi MQTT - Smart Room Monitoring

Proyek ini adalah implementasi sistem komunikasi berbasis MQTT menggunakan Python (`paho-mqtt`) dan Mosquitto Broker. Studi kasus yang digunakan adalah pemantauan suhu dan kelembapan ruangan.

## Kebutuhan Sistem
* Python 3.x
* Mosquitto Broker terpasang dan berjalan di lokal (port 1883)
* Library `paho-mqtt` v2.0+

## Instalasi
1. Pastikan Mosquitto Broker sudah berjalan di komputer Anda.
2. Install library yang dibutuhkan dengan menjalankan perintah:
   ```bash
   pip install paho-mqtt

## Cara Menjalankan Program
Program ini terdiri dari dua file utama: publisher.py (simulasi sensor) dan subscriber.py (pemantauan).

Buka dua terminal (Command Prompt/PowerShell/VS Code Terminal).

Di Terminal 1, jalankan subscriber terlebih dahulu agar siap mendengarkan data:

python subscriber.py
Di Terminal 2, jalankan publisher untuk mulai mengirimkan data:

python publisher.py

## Catatan Pengujian:
Untuk mengubah topik yang didengarkan (menguji Wildcard + atau #) dan mengubah tingkat QoS (0, 1, 2), silakan ubah variabel TOPIC_TO_SUBSCRIBE dan QOS_LEVEL di dalam file subscriber.py sebelum menjalankan ulang program.
