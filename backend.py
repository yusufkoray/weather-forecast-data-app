import requests

API_KEY="fbface564d5591fbf286daad81522d0a"


def get_data(place,foreceast_day=None,kind=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response=requests.get(url)
    data=response.json()
    filtered_data=data["list"]
    nr_values=8*foreceast_day  #24/3 = 8  8*5 = 40
    filtered_data=data["list"][:nr_values]
    match kind:
        case "Temperature":
            filtered_data=[a["main"]["temp"] for a in filtered_data] # filtered_data'nin icerisinda a bir dictionary donuyor. Sonucta filtered datamiz dictionary.
            #donen dictionary icerisindeki main key'inin icerisindeki "temp" key'ine erisiyoruz. Bunun icerisindeki temperature value'leri yeni bir lit olarak filtered_data
            #icerisine aktariyoruz.
            #yani aslinda her defasinda filtered_data[0]['main']['temp'] yapiyoruz. 0 bittikten sonra 1'e 1 'den sonra 2'ye geciyor.
        case "Sky":
            filtered_data=[b["weather"][0]["main"] for b in filtered_data] #Bu kisimda da [0] yazmamizin sebebi ['main'] ' in yani erismek istedigimiz
        #degerin ['weather'] LISTESI icerisinde olmasindan kaynaklanir. Liste de sadece 1 eleman iceriyor.

    return filtered_data

if __name__=="__main__":
    print(get_data("Tokyo",foreceast_day=3,kind="Temperature"))