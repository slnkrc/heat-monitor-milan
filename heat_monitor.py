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
    backdrop-filter: blur(10px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
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
}}

.red {{ background: #ef4444; }}
.orange {{ background: #f97316; }}
.green {{ background: #22c55e; }}

select {{
    padding: 10px;
    border-radius: 10px;
    margin-top: 10px;
}}
</style>
</head>

<body>

<div class="header">
🌡 MILANO HEAT MONITORING DASHBOARD
<br>
<select id="day" onchange="update()">
    <option>2026-06-14</option>
    <option>2026-06-15</option>
    <option selected>2026-06-16</option>
</select>
</div>

<div class="grid">

<div class="card">
<h2>ARPA Lombardia</h2>
<div class="big" id="arpa"></div>
<div class="badge orange">Humidex</div>
</div>

<div class="card">
<h2>Ministero della Salute</h2>
<div class="big" id="ministero"></div>
<div class="badge red">HHWWS</div>
</div>

</div>

<script>
const data = {json.dumps(data)};

function update() {{
    const day = document.getElementById("day").value;

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
