import requests

# 都市名から緯度経度を取得する関数
def get_coordinates(city: str):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        if "results" in data and len(data["results"]) > 0:
            lat = data["results"][0]["latitude"]
            lon = data["results"][0]["longitude"]
            return lat, lon
    return None, None

# 緯度経度から天気予報を取得する関数
def get_weather(city: str):
    lat, lon = get_coordinates(city)
    if lat is None or lon is None:
        return None
    
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max&timezone=auto"
    res = requests.get(url)
    
    if res.status_code == 200:
        data = res.json()
        forecast = {}
        for date, temp in zip(data["daily"]["time"], data["daily"]["temperature_2m_max"]):
            forecast[date] = temp
        return forecast
    return None
