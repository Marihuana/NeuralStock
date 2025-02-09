import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, period: str = "1mo", interval: str = "1d") -> pd.DataFrame:
    """
    특정 종목의 주식 데이터를 가져오는 함수.
    
    :param ticker: 주식 심볼 (예: "AAPL", "005930.KQ" - 삼성전자)
    :param period: 조회할 기간 (예: "1d", "5d", "1mo", "3mo", "1y", "max")
    :param interval: 데이터 간격 (예: "1m", "5m", "1h", "1d", "1wk", "1mo")
    :return: 주식 데이터 (DataFrame)
    """
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    return data

# 테스트 실행
if __name__ == "__main__":
    ticker = "AAPL"  # 애플 주식
    stock_data = fetch_stock_data(ticker, period="5d", interval="1d")
    print(stock_data.head())  # 데이터 출력