import datetime

today = datetime.date.today()

# SAHTE VERİ (şimdilik test)
arpa_level = "molto forte"
ministero_level = "3"

html = f"""
<html>
<head>
<title>Heat Monitor Milano</title>
</head>
<body>
<h1>Milano Heat Monitoring</h1>

<p><b>Date:</b> {today}</p>

<h2>ARPA Lombardia (Humidex)</h2>
<p>{arpa_level}</p>

<h2>Ministero della Salute (HHWWS)</h2>
<p>Livello {ministero_level}</p>

<h2>Comparison</h2>
<p>System comparison placeholder</p>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML generated")
