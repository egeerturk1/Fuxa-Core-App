# 🏭 Industrial IoT & OEE Monitoring Stack

Bu proje; endüstriyel sensör verilerinin gerçek zamanlı takibi, veritabanı arşivlemesi ve OEE (Toplam Ekipman Verimliliği) metriklerinin otomatik hesaplanarak bir SCADA arayüzünde görselleştirilmesini sağlayan tam kapsamlı bir IIoT (Industrial Internet of Things) altyapısıdır.

> [!IMPORTANT]
> Sistem, modern mikroservis mimarisi kullanılarak Docker üzerinde konteynerize edilmiştir ve endüstriyel OT (Operational Technology) standartlarına uygun olarak tasarlanmıştır.

---

## 🚀 Öne Çıkan Özellikler

- 📡 **Real-time Data Acquisition:** MQTT protokolü üzerinden milisaniyelik gecikmeyle sensör verisi toplama.
- 📊 **Automated OEE Calculation:** Üretim hattı verileri üzerinden Kullanılabilirlik, Performans ve Kalite metriklerinin anlık hesabı.
- 🗄️ **Database Persistence:** Tüm sensör verilerinin PostgreSQL üzerinde zaman damgalı (Time-series) olarak saklanması.
- 🌉 **History Data Bridge:** Veritabanındaki geçmiş verilerin SCADA grafiklerine Node-RED tabanlı bir Proxy üzerinden paketlenerek aktarılması.
- 🖥️ **Modern SCADA Interface:** FUXA platformu üzerinde endüstriyel standartlarda dashboard tasarımı.

---

## 🏗️ Sistem Mimarisi

Sistem birbirine entegre **5 ana katmandan** oluşmaktadır:

| Katman | Bileşen | Açıklama |
|--------|---------|----------|
| **Simulation Layer** | Node-RED | PLC/Sensör verilerini simüle eden ve MQTT üzerinden yayınlayan katman |
| **Messaging Layer** | Mosquitto MQTT | Servisler arası haberleşmeyi sağlayan yüksek performanslı mesaj broker'ı |
| **Application Layer** | FastAPI / Python | Verileri işleyen, veritabanına kaydeden ve OEE analizlerini gerçekleştiren backend servisi |
| **Storage Layer** | PostgreSQL | Endüstriyel verilerin güvenli ve düzenli saklandığı ilişkisel veritabanı |
| **Visualization Layer** | FUXA SCADA | Operatör ve mühendis panellerinin yer aldığı görselleştirme arayüzü |

---

## 🛠️ Kullanılan Teknolojiler

| Bileşen | Teknoloji | Görev |
|---------|-----------|-------|
| Backend | Python 3.10+, FastAPI | Veri işleme ve API yönetimi |
| Database | PostgreSQL | Zaman serisi veri depolama |
| Messaging | MQTT (Mosquitto) | Cihazlar arası iletişim |
| Integration | Node-RED | Veri akış yönetimi ve Proxy |
| Visualization | FUXA SCADA | Endüstriyel Dashboard |
| Infrastructure | Docker, Docker Compose | Konteynerizasyon ve Orkestrasyon |

---

## 📦 Kurulum ve Çalıştırma

Sistemi ayağa kaldırmak için bilgisayarınızda **Docker** ve **Docker Compose**'un yüklü olması yeterlidir.

**1. Projeyi klonlayın:**

```bash
git clone https://github.com/kullaniciadi/industrial-oee-stack.git
cd industrial-oee-stack
```

**2. Docker konteynerlerini başlatın:**

```bash
docker compose up -d --build
```

**3. Arayüzlere erişin:**

| Servis | URL |
|--------|-----|
| 🌐 FUXA SCADA | http://localhost:1881 |
| 🔄 Node-RED | http://localhost:1880 |
| 🔌 FastAPI Docs | http://localhost:8000/docs |

---

## 📂 Proje Yapısı

```
├── backend/
│   ├── app/
│   │   ├── api/          # OEE ve History API Rotaları
│   │   ├── core/         # DB Bağlantısı ve Konfigürasyon
│   │   ├── services/     # MQTT Listener ve İş Mantığı
│   │   └── main.py       # Uygulama Giriş Noktası
│   └── Dockerfile
├── mosquitto/            # MQTT Broker Konfigürasyonu
├── docker-compose.yml    # Tüm Sistemin Orkestrasyonu
└── README.md
```

---

## 👨‍💻 Geliştirici

**Ege Ertürk**  
Software Engineering Student | IIoT & OT Enthusiast
