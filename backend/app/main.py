from fastapi import FastAPI
from app.core.database import init_db
from app.services.mqtt_service import start_mqtt
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware

# 1. Veritabanını Başlat
init_db()

# 2. Arka Plan MQTT Dinleyicisini Başlat
start_mqtt()

# 3. FastAPI Web Sunucusunu Kur
app = FastAPI(
    title="Endüstriyel IoT & OEE Platformu",
    description="Üretim hattı sensör verileri ve verimlilik analizi API'si",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Geliştirme aşamasında her şeye izin veriyoruz
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotaları Uygulamaya Bağla
app.include_router(router)
@app.get("/")
def health_check():
    return {"status": "ok", "message": "IIoT Backend is alive!"}