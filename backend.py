import requests

API_KEY="fbface564d5591fbf286daad81522d0a"


def get_data(place="Adana",foreceast_day=1):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response=requests.get(url)
    data=response.json()
    nr_values=8*foreceast_day  #24/3 = 8  8*5 = 40
    filtered_data=data["list"][:nr_values]
    return filtered_data

if __name__=="__main__":
    print(get_data("Tokyo",3))