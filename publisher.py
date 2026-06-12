import paho.mqtt.client as mqtt
import time
import random

# Konfigurasi Broker
broker_address = "localhost" 
port = 1883
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "SmartRoom_Publisher")
client.connect(broker_address, port)

print("Publisher berjalan... Mengirim data simulasi. Tekan Ctrl+C untuk berhenti.")

try:
    while True:
        # Generate data dummy
        temp_living = round(random.uniform(24.0, 30.0), 1)
        hum_living = round(random.uniform(50.0, 65.0), 1)
        temp_bed = round(random.uniform(22.0, 28.0), 1)
        hum_bed = round(random.uniform(45.0, 60.0), 1)

        qos_level = 1

        client.publish("smartroom/livingroom/temperature", temp_living, qos=qos_level)
        client.publish("smartroom/livingroom/humidity", hum_living, qos=qos_level)
        client.publish("smartroom/bedroom/temperature", temp_bed, qos=qos_level)
        client.publish("smartroom/bedroom/humidity", hum_bed, qos=qos_level)

        print(f"Data Terkirim [QoS {qos_level}] -> LivingRoom(T:{temp_living}, H:{hum_living}) | BedRoom(T:{temp_bed}, H:{hum_bed})")
        
        time.sleep(3) # Jeda pengiriman 3 detik

except KeyboardInterrupt:
    print("\nPublisher dihentikan.")
    client.disconnect()