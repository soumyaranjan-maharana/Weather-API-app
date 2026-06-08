import requests as rq

api_key = "3806d8e45ebc87c04a04bc9bd4573bbd"

city_name = input("enter city name : ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

response = rq.get(url)
data = response.json()

if data["cod"] == 200:
    weather = data["weather"][0]["main"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["main"]
else:
    print("Somthing, Wrong!")

def main():
    print(f"Weather : {weather}, Temperature : {temp}, description : {description}, these are the Weather info of {city_name}")

if __name__ == "__main__":
    main()
