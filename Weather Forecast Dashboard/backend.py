import requests

API_KEY="14b698cab7b32b58ccacfbdda71cd3e0"

def get_data(place,days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = int(8 * days)
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Lisbon",days = 3))
