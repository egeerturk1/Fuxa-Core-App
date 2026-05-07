#Environment variables and configuration settings for the application

import os

class Settings:
    MQTT_BROKER = os.getenv("MQTT_BROKER", "mosquitto")
    MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
    DB_URL = os.getenv("DATABASE_URL", "postgresql://ege_admin:iiot_password@db/iiot_data")

settings = Settings()