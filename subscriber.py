import paho.mqtt.client as mqtt

# Konfigurasi Broker
broker_address = "localhost"
port = 1883

TOPIC_TO_SUBSCRIBE = "smartroom/#"  # Ubah sesuai skenario
QOS_LEVEL = 1                       # Ubah sesuai skenario (0, 1, atau 2)
# ==========================================

# Fungsi callback saat pesan masuk
def on_message(client, userdata, message):
    payload = message.payload.decode('utf-8')
    print(f"[Pesan Diterima] Topik: {message.topic} | Data: {payload} | QoS: {message.qos}")

# Inisialisasi Client (Sudah ditambah Callback API Version 2)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "SmartRoom_Subscriber")
client.on_message = on_message

# Koneksi dan Subscribe
client.connect(broker_address, port)
client.subscribe(TOPIC_TO_SUBSCRIBE, qos=QOS_LEVEL)

print(f"Subscriber berjalan...")
print(f"Mendengarkan topik: '{TOPIC_TO_SUBSCRIBE}' dengan QoS: {QOS_LEVEL}")
print("Tekan Ctrl+C untuk berhenti.\n")

# Looping agar terus mendengarkan pesan
client.loop_forever()