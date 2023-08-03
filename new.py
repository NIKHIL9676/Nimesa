import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def send_request():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_weather_data():
    date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
    data = send_request()
    if data:
        for forecast in data['list']:
            if forecast['dt_txt'] == date:
                print(f" {forecast['main']['temp']} °F")
                return
        print("Weather data not found for the given date.")
    else:
        print("Failed to retrieve weather data.")

def get_wind_speed():
    date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
    data = send_request()
    if data:
        for forecast in data['list']:
            if forecast['dt_txt'] == date:
                print(f"{forecast['wind']['speed']} m/s")
                return
        print("Wind speed data not found for the given date.")
    else:
        print("Failed to retrieve wind speed data.")

def get_pressure():
    date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
    data = send_request()
    if data:
        for forecast in data['list']:
            if forecast['dt_txt'] == date:
                print(f"{forecast['main']['pressure']} hPa")
                return
        print("Pressure data not found for the given date.")
    else:
        print("Failed to retrieve pressure data.")

def main():
    while True:
        print("Select an option:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = int(input())

        if choice == 1:
            get_weather_data()
        elif choice == 2:
            get_wind_speed()
        elif choice == 3:
            get_pressure()
        elif choice == 0:
            
            print("Program Terminated")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
