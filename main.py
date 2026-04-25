from flask import Flask, jsonify
from flask_cors import CORS
from waitress import serve
import requests
import time
import json
import os

app = Flask(__name__)
CORS(app)

STOPS_FILE = os.path.join(os.path.dirname(__file__), 'stops.json')
API_URL = "https://www.stops.lt/rigaapp/read.php"

HEADERS = {
    "Origin-Custom": "stops.lt",
    "Referer": "https://stops.lt/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}

def load_stops():
    with open(STOPS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)['stops']

def seconds_from_midnight():
    now = time.localtime()
    return now.tm_hour * 3600 + now.tm_min * 60 + now.tm_sec

def parse_departures(raw_text):
    lines   = raw_text.strip().split('\n')
    now_sec = seconds_from_midnight()
    departures = []

    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        parts = line.split(',')
        if len(parts) < 6:
            continue

        transport_type = parts[0]          # bus, trol, tram, train
        route = parts[1]
        direction = parts[2]
        scheduled_sec = int(parts[3])
        realtime_sec = int(parts[4])
        destination = parts[5]

        sched_min = round((scheduled_sec - now_sec) / 60)
        if sched_min < -1:
            continue

        has_realtime = realtime_sec > 3600
        real_min = round((realtime_sec - now_sec) / 60) if has_realtime else None
        delay_sec = (realtime_sec - scheduled_sec) if has_realtime else None
        delay_min = round(delay_sec / 60) if delay_sec is not None and abs(delay_sec) < 1800 else None

        departures.append({
            "type": transport_type,
            "route": route,
            "direction": direction,
            "destination": destination,
            "scheduled_min": sched_min,
            "realtime_min": real_min,
            "delay_min": delay_min,
            "scheduled_sec": scheduled_sec,
            "realtime_sec": realtime_sec if has_realtime else None,
        })

    departures.sort(key=lambda x: x['scheduled_sec'])
    return departures[:10]

def fetch_stop(stop_id):
    params = {
        "stopid": stop_id,
        "time": str(int(time.time() * 1000)),
    }
    try:
        resp = requests.get(API_URL, params=params, headers=HEADERS, timeout=5)
        resp.raise_for_status()
        return parse_departures(resp.text)
    except Exception as e:
        return {"error": str(e)}

# ── Routes ──────────────────────────────────────────────

@app.route('/api/stops', methods=['GET'])
def get_stops():
    return jsonify(load_stops())

@app.route('/api/departures/<stop_id>', methods=['GET'])
def get_departures(stop_id):
    return jsonify({
        "stop_id":   stop_id,
        "timestamp": int(time.time()),
        "now_sec":   seconds_from_midnight(),
        "departures": fetch_stop(stop_id),
    })

@app.route('/api/all', methods=['GET'])
def get_all():
    stops = load_stops()
    result = []
    for stop in stops:
        if stop.get('id') is None:
            result.append({"stop": stop, "departures": []})
            continue
        departures = fetch_stop(stop['id'])
        result.append({"stop": stop, "departures": departures})
    return jsonify({
        "timestamp": int(time.time()),
        "now_sec": seconds_from_midnight(),
        "stops": result,
    })

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"status": "ok", "time": int(time.time())})

if __name__ == '__main__':
    print("Transit Board API → http://localhost:5000")
    serve(app, host='0.0.0.0', port=5000)