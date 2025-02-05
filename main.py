import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place=st.text_input("Place:")
days=st.slider("Forecast Days",min_value=1,max_value=5,help="Select the number of forecasted days")
option=st.selectbox("Selact data to view",("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


if place:
    try:
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperature_data = [a["main"]["temp"] for a in filtered_data]
                                # filtered_data'nin icerisinda a bir dictionary donuyor. Sonucta filtered datamiz dictionary.
                                # donen dictionary icerisindeki main key'inin icerisindeki "temp" key'ine erisiyoruz.
                                #Bunun icerisindeki temperature value'leri yeni bir lit olarak filtered_data
                                # icerisine aktariyoruz. Yani aslinda her defasinda filtered_data[0]['main']['temp'] yapiyoruz.
                                #0 bittikten sonra 1'e 1 'den sonra 2'ye geciyor.
            c_temperatures_data = [i-273 for i in temperature_data]

            # Create a temperature plot.
            days=[b["dt_txt"] for b in filtered_data]
            figure=px.line(x=days,y=c_temperatures_data,labels={'x':"Date",'y':"Temperature(C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            filtered_data = [b["weather"][0]["main"] for b in filtered_data]
                            # Bu kisimda da [0] yazmamizin sebebi ['main'] ' in yani erismek istedigimiz
                            # degerin ['weather'] LISTESI icerisinde olmasindan kaynaklanir. Liste de sadece 1 eleman iceriyor.

            #My Solution:
            #filtered_data = ["images/" + str(c)[:1].lower() + str(c)[1:] + ".png" for c in filtered_data]

            #Teacher Solution:
            images={"Celar":"images/clear.png","Clouds":"images/clouds.png","Rain":"images/rain.png","Snow":"images/snow.png"}
            image_paths=[images[condition] for condition in filtered_data]
            # Create a sky image.
            st.image(image_paths,width=115),
    except KeyError:
        st.info("This city is not accesable now. Please try another city :)")


