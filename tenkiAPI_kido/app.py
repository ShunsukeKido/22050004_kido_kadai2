import streamlit as st
from weather import get_weather
 
def main():
    st.title("🌤 天気予報アプリ")
    city = st.text_input("都市名を入力してください (例: Tokyo, Osaka)")
 
    if st.button("天気を取得"):
        if city:
            forecast = get_weather(city)
            if forecast:
                st.subheader(f"📍 {city} の天気予報")
                for day, temp in forecast.items():
                    st.write(f"{day}: {temp}°C")
            else:
                st.error("データを取得できませんでした。")
        else:
            st.warning("都市名を入力してください。")
 
if __name__ == "__main__":
    main()
