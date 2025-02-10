import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def fetch_stock_data(ticker: str, period: str = "6mo"):
    """
    주가 데이터를 가져와서 머신러닝 모델 훈련을 위한 데이터프레임 반환.
    :param ticker: 주식 심볼 (예: "AAPL", "005930.KQ")
    :param period: 조회할 기간 (기본값: 6개월)
    :return: 전처리된 주가 데이터 (DataFrame)
    """
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)

    # 특징 생성 (전일 대비 변동률)
    df["Return"] = df["Close"].pct_change()
    df["SMA_20"] = df["Close"].rolling(window=20).mean()
    df["SMA_50"] = df["Close"].rolling(window=50).mean()
    df["Volatility"] = df["Close"].rolling(window=20).std()

    # 결측치 제거
    df = df.dropna()

    return df

def train_predict_stock_model(ticker: str):
    """
    주가 데이터를 기반으로 랜덤 포레스트 회귀 모델을 훈련하고 예측 수행.
    :param ticker: 주식 심볼
    """
    df = fetch_stock_data(ticker)

    # 입력(X) & 출력(y) 데이터 정의
    feature_columns = ["Open", "High", "Low", "Close", "Volume", "SMA_20", "SMA_50", "Volatility"]
    X = df[feature_columns]
    y = df["Close"].shift(-1)  # 하루 뒤 주가 예측

    # 학습/테스트 데이터 분할
    X_train, X_test, y_train, y_test = train_test_split(X[:-1], y[:-1], test_size=0.2, random_state=42)

    # 랜덤 포레스트 모델 훈련
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 예측 수행
    y_pred = model.predict(X_test)

    # 성능 평가
    mae = mean_absolute_error(y_test, y_pred)
    print(f"📈 {ticker} 주가 예측 모델 성능 (MAE): {mae:.2f}")

    # 예측 수행 (마지막 데이터로 미래 주가 예측)
    last_input = pd.DataFrame([X.iloc[-1]], columns=feature_columns)  # DataFrame 유지
    last_pred = model.predict(last_input)[0]
    print(f"🔮 {ticker} 예상 종가: {last_pred:.2f}")

    # 실제값 vs 예측값 저장
    df_test = df.iloc[-len(y_test):].copy()
    df_test["Predicted_Close"] = y_pred

    return df_test

# 📌 예측 결과 시각화 함수
def plot_predicted_vs_actual(df, ticker):
    """
    실제 주가와 예측 주가를 비교하는 그래프를 출력.
    :param df: 예측 결과가 포함된 DataFrame
    :param ticker: 주식 심볼
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="Actual Close Price", color="blue")
    plt.plot(df.index, df["Predicted_Close"], label="Predicted Close Price", linestyle="dashed", color="red")

    plt.title(f"{ticker} 실제 주가 vs 예측 주가")
    plt.xlabel("날짜")
    plt.ylabel("가격")
    plt.legend()
    plt.grid()
    plt.show()

# 테스트 실행
if __name__ == "__main__":
    train_predict_stock_model("AAPL")  # 애플 주가 예측 실행