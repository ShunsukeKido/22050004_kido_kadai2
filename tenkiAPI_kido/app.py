import streamlit as st

import pandas as pd

from weather import get_weather
 
def main():

    st.title("🌤 天気予報アプリ")

    city = st.text_input("都市名を入力してください (例: Tokyo, Osaka)")
 
    if st.button("天気を取得"):

        if city:

            forecast = get_weather(city)

            if forecast:

                st.subheader(f"📍 {city} の天気予報")

                df = pd.DataFrame(list(forecast.items()), columns=["日付", "気温(℃)"])

                st.dataframe(df)
 
                # CSV保存ボタン

                if st.button("CSVに保存"):

                    df["都市名"] = city  # 都市名を追加

                    try:

                        old_df = pd.read_csv("forecast.csv")

                        df = pd.concat([old_df, df], ignore_index=True)

                    except FileNotFoundError:

                        pass  # 初回はファイルがないので新規作成
 
                    df.to_csv("forecast.csv", index=False, encoding="utf-8-sig")

                    st.success("CSVに保存しました！")

            else:

                st.error("データを取得できませんでした。")

        else:

            st.warning("都市名を入力してください。")
 
if __name__ == "__main__":

    main()

 
