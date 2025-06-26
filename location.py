import requests

def get_coords_from_ip():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        lat, lon = map(float, data['loc'].split(','))
        return lat, lon
    except Exception as e:
        print("Error:", e)
        return None, None

LAT, LON = get_coords_from_ip()
print(f"Latitude: {LAT}, Longitude: {LON}")
