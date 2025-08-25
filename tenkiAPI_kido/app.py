from weather import get_weather

def main():
    print("=== 天気予報アプリ ===")
    city = input("都市名を入力してください (例: Tokyo, Osaka): ")
    
    forecast = get_weather(city)
    
    if forecast:
        print(f"\n📍 {city} の天気予報")
        for day, temp in forecast.items():
            print(f"{day}: {temp}°C")
    else:
        print("データを取得できませんでした。")

if __name__ == "__main__":
    main()
