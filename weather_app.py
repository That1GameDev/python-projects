import requests

API_KEY = "d624d7ee57a4626dd76ed435f234973b"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        
        print(f"\n=== Weather in {name}, {country} ===")
        print(f"Temperature: {temp}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {description.capitalize()}")
    else:
        print("City not found. Please try again.")

def main():
    print("=== Weather App ===")
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ")
        if city.lower() == "quit":
            print("Goodbye!")
            break
        get_weather(city)

main()