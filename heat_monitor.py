import datetime
import json

today = datetime.date.today()

data = {
    "2026-06-14": {"arpa": 32, "ministero": 2},
    "2026-06-15": {"arpa": 35, "ministero": 3},
    "2026-06-16": {"arpa": 37, "ministero": 3},
}

html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Milano Heat Dashboard</title>

<style>
body {{
    font-family: Arial;
    background: #0f172a;
    color: white;
    margin: 0;
    padding: 0;
}}

.header {{
    padding: 20px;
    background: #111827;
    text-align: center;
}}

.container {{
    padding: 20px;
    max-width: 900px;
    margin: auto;
}}

.card {{
    background: #1f2937;
    padding: 20px;
    border-radius: 12px;
    margin-top: 15px;
}}

.big {{
    font-size: 40px;
    font-weight: bold;
}}

.select {{
    padding: 10px;
    font-size: 16px;
    border-radius: 8px;
    margin-top: 10px;
}}
</style>

</head>

<body>

<div class="header">
    <h1>🌡 Milano Heat Dashboard</h1>
    <p>Only Milan real-time risk overview</p>

    <select id="daySelect" class="select" onchange="update()">
        <option value="2026-06-14">2026-06-14</option>
        <option value="2026-06-15">2026-06-15</option>
        <option value="2026-06-16" selected>2026-06-16</option>
    </select>
</div>

<div class="container">

    <div class="card">
        <h2>ARPA Lombardia (Humidex)</h2>
        <div class="big" id="arpa">--</div>
    </div>

    <div class="card">
        <h2>Ministero della Salute (HHWWS)</h2>
        <div class="big" id="ministero">--</div>
    </div>

</div>

<script>
const data = {json.dumps(data)};

function update() {{
    const day = document.getElementById("daySelect").value;

    document.getElementById("arpa").innerText =
        data[day].arpa + "°C";

    document.getElementById("ministero").innerText =
        "Level " + data[day].ministero;
}}

update();
</script>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Milano Heat Dashboard generated successfully")
