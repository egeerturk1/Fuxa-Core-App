from fastapi import APIRouter
from app.core.database import get_db_connection

router = APIRouter()

@router.get("/test")
def test_okuma():
    return {"mesaj": "API Çalışıyor, Üretim Hattı dinleniyor!"}

@router.get("/oee")
def get_oee_skoru():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Otoyoldan gelen en taze veriyi (son satırı) çekiyoruz
        cur.execute("""
            SELECT motor_sicaklik, enerji_kw, toplam_uretim, hatali_uretim 
            FROM uretim_hatti 
            ORDER BY kayit_zamani DESC 
            LIMIT 1
        """)
        row = cur.fetchone()
        cur.close()
        conn.close()

        if not row or row[2] == 0:
            return {"mesaj": "Yeterli üretim verisi bekleniyor..."}

        motor_sicaklik = row[0]
        enerji_kw = row[1]
        toplam = row[2]
        hatali = row[3]

        # 1. Kalite Oranı: (Sağlam Ürün / Toplam Ürün)
        saglam_uretim = toplam - hatali
        kalite_yuzdesi = (saglam_uretim / toplam) * 100

        # 2. Kullanılabilirlik ve Performans (Demo için endüstriyel standartlarda sabit kabul ediyoruz)
        kullanilabilirlik = 98.5  # %98.5
        performans = 95.0         # %95.0

        # 3. Nihai OEE Skoru Hesabı
        oee_skoru = (kullanilabilirlik / 100) * (performans / 100) * (kalite_yuzdesi / 100) * 100

        # Endüstriyel Dashboard'un (FUXA) tüketeceği API Yanıtı
        return {
            "anlik_durum": {
                "motor_sicaklik_c": round(motor_sicaklik, 1),
                "enerji_tuketimi_kw": round(enerji_kw, 1)
            },
            "uretim_verileri": {
                "toplam_parca": toplam,
                "hatali_parca": hatali,
                "saglam_parca": saglam_uretim
            },
            "oee_metrikleri": {
                "kullanilabilirlik": kullanilabilirlik,
                "performans": performans,
                "kalite": round(kalite_yuzdesi, 2),
                "genel_oee": round(oee_skoru, 2)
            }
        }
    except Exception as e:
        return {"hata": str(e)}
    
from fastapi import APIRouter
from app.core.database import get_db_connection

router = APIRouter()

@router.get("/history/{sensor_adi}")
def get_sensor_history(sensor_adi: str, limit: int = 100):
    conn = get_db_connection()
    cur = conn.cursor()
    query = f"SELECT {sensor_adi}, kayit_zamani FROM uretim_hatti ORDER BY kayit_zamani DESC LIMIT %s"
    cur.execute(query, (limit,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    # KRİTİK DEĞİŞİKLİK: Veriyi bir 'history_pack' anahtarı içine koyuyoruz
    # Böylece FUXA 200 satır değil, tek bir paket görecek
    history_list = [{"x": r[1].isoformat(), "y": r[0]} for r in rows]
    return {"history_pack": history_list}