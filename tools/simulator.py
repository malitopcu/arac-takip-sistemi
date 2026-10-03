import json
import time
import random
import paho.mqtt.client as mqtt

BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "proje_arac_takip/arac_01/telemetri"

# Başlangıç konumu (Konya Merkez)
lat = 37.8714
lng = 32.4846

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, keepalive=60)
client.loop_start()

print(f"Simülatör başlatıldı. Broker: {BROKER}, Topic: {TOPIC}")

try:
   while True:
      # Konumu hafifçe ilerlet (rota simülasyonu)
      lat += random.uniform(-0.0003, 0.0003)
      lng += random.uniform(-0.0003, 0.0003)

      payload = {
         "device_id": "CAR_01",
         "lat": round(lat, 6),
         "lng": round(lng, 6),
         "speed": round(random.uniform(30.0, 70.0), 1),
         "temp": round(random.uniform(22.0, 26.0), 1),
         "timestamp": int(time.time())
      }

      client.publish(TOPIC, json.dumps(payload), qos=0)
      print(f"Veri gönderildi: {payload}")
      time.sleep(2)
except KeyboardInterrupt:
   print("Durduruldu.")
   client.loop_stop()
   client.disconnect()