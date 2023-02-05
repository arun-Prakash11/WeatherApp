import requests
import json

with open('../api_key.json') as file:
    api_key = json.load(file)["api_key"]

def get_owm_req_by_city_name(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    return url 

def get_owm_req_by_lat_lon(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat},lon{lon}&appid={api_key}&units=metric"
    return url

def weather_app():
    
    while True:
        try:
            print("Hello!\n")
            print("\t1. Get weather by city name\n")
            print("\t2. Get weather by latitude and longitude\n")
            print("\t3. Exit\n")
            
            while True:
                try:
                    choice = int(input("\nEnter Your choice: "))
                    if(choice<1 or choice>3):
                        print()
                        print("\n[ ] Enter a number b/w [1, 3]")
                        continue
                    if(choice == 3):
                        print("\n[ ] Program Stopped.")
                        exit(0)
                    break
                except ValueError:
                    print("\n[ ] Enter a number b/w [1, 3]")
                    continue

            if(choice == 1):
                city = input("\nEnter city name: ")
                url = get_owm_req_by_city_name(city)
            elif(choice == 2):
                while True:
                    try:
                        lat = float(input("\nEnter latitude: "))
                        break
                    except ValueError:
                        print("\n[ ] Enter Correct Coordinates.")
                        continue
                while True:
                    try:
                        lon = float(input("\nEnter longitude: "))
                        break
                    except ValueError:
                        print("\n[ ] Enter Correct Coordinates.")
                        continue
                url = get_owm_req_by_lat_lon(lat, lon)

            
            response = requests.get(url)

            wd = response.json() # Weather data
            
            if (str(wd['cod']) == str(200)):
                print()
                print(f"Weather report of city {wd['name']}, lon: {wd['coord']['lon']} lat: {wd['coord']['lat']}")
                print(f"\tWeather: {wd['weather'][0]['description']}")
                print(f"\tTemperature: {wd['main']['temp']}")
                print(f"\tTemperature range: {wd['main']['temp_min']}-{wd['main']['temp_max']}")
                print(f"\tPressure: {wd['main']['pressure']}")
                print(f"\tHumidity: {wd['main']['humidity']}")
                print(f"\tWind Speed: {wd['wind']['speed']}")
            elif (wd['cod'] == str(400)):
                print("\nLocation of the place is invalid.")
            elif (wd['cod'] == str(404)):
                print("\nCity not found.")
            else:
                print(f"\nError: {wd['message']}, {wd['cod']}")
            print()
            cont = input("\nEnter any key to Continue, '0' to Exit: ")
            if(cont == '0'):
                exit(0)
            print()
            print()
        except KeyboardInterrupt: 
            print("\n[ ] Program Stopped.")
            break

weather_app()

