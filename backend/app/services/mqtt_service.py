# MQTT Listening and data insertion service for IIoT application

import json
import paho.mqtt.client as mqtt
from app.core.config import settings
from app.core.database import get_db_connection
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    print("MQTT Broker'a Bağlanıldı!")
    client.subscribe("fabrika/hat1/veriler")

def on_message(client, userdata, msg):
    if msg.topic == "fabrika/hat1/veriler":
        try:
            payload = json.loads(msg.payload.decode('utf-8'))
            
            # 1. Zamanı Python tarafında "ŞİMDİ" olarak al
            # Docker'da TZ=Europe/Istanbul olduğu için bu doğru saati verecek
            kayit_zamani = datetime.now() 

            conn = get_db_connection()
            cur = conn.cursor()
            
            # 2. SQL sorgusuna kayit_zamani'nı biz gönderiyoruz
            cur.execute("""
                INSERT INTO uretim_hatti (kayit_zamani, motor_sicaklik, enerji_kw, toplam_uretim, hatali_uretim)
                VALUES (%s, %s, %s, %s, %s)
            """, (kayit_zamani, payload['motor_sicaklik'], payload['enerji_kw'], payload['toplam_uretim'], payload['hatali_uretim']))
            
            conn.commit()
            cur.close()
            conn.close()

            # 2. OEE HESAPLA (Analiz)
            toplam = payload['toplam_uretim']
            hatali = payload['hatali_uretim']
            
            if toplam > 0:
                kalite = ((toplam - hatali) / toplam)
                kullanilabilirlik = 0.98 # Sabit varsayılan
                performans = 0.95        # Sabit varsayılan
                oee_skoru = kullanilabilirlik * performans * kalite * 100
                
                # 3. HESAPLANMIŞ VERİYİ OTOYOLA GERİ GÖNDER
                analiz_paketi = {
                    "anlik_oee": round(oee_skoru, 2),
                    "kalite_orani": round(kalite * 100, 2)
                }
                client.publish("fabrika/hat1/analiz", json.dumps(analiz_paketi))
                
        except Exception as e:
            print(f"Hata: {e}")

def start_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    try:
        client.connect(settings.MQTT_BROKER, settings.MQTT_PORT, 60)
        client.loop_start()
    except Exception as e:
        print("MQTT Bağlantı Hatası:", e)