import datetime
import json

today = str(datetime.date.today())

# SAHTE VERİ (sonra gerçek yapacağız)
data = {
    today: {
        "arpa": 37,
        "ministero": 3
    }
}

html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Milano Heat Dashboard</title>

<style>
body {{
    margin: 0;
    font-family: Arial;
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}}

.header {{
    text-align: center;
    padding: 25px;
    background: #111827;
    font-size: 22px;
    font-weight: bold;
}}

.grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    padding: 20px;
    max-width: 900px;
    margin: auto;
}}

.card {{
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 16px;
}}

.big {{
    font-size: 48px;
    font-weight: bold;
    margin-top: 10px;
}}

.badge {{
    padding: 8px 12px;
    border-radius: 10px;
    display: inline-block;
    margin-top: 10px;
    background: #f97316;
}}
</style>
</head>

<body>

<div class="header">
🌡 MILANO HEAT MONITORING DASHBOARD
<br>
{today}
</div>

<div class="grid">

<div class="card">
<h2>ARPA Lombardia</h2>
<div class="big">{data[today]["arpa"]}°C</div>
<div class="badge">Humidex</div>
</div>

<div class="card">
<h2>Ministero della Salute</h2>
<div class="big">Level {data[today]["ministero"]}</div>
<div class="badge">HHWWS</div>
</div>

</div>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("OK")
