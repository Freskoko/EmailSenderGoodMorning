import requests

def get_weather():

    latitude = 60.3
    longitude = 5.3


    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m,cloudcover,rain"
    
    data = requests.get(url)
    response = data.json()

    g = list(zip(response['hourly']["temperature_2m"],response['hourly']['time'], response['hourly']['rain']     ))
    g = g[8:25]

    return g


if __name__ == "__main__":
    response = get_weather()

    for i in response:

        print(i)
