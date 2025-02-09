from src.data_fetcher import fetch_stock_data

if __name__ == "__main__":
    ticker = "AAPL"  # 애플 주식 데이터 가져오기
    data = fetch_stock_data(ticker, period="1mo", interval="1d")

    print("📈 주식 데이터 가져오기 성공!")
    print(data.head())  # 상위 5개 데이터 출력