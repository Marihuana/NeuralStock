import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def plot_stock_chart(ticker: str, period: str = "3mo"):
    """
    특정 종목의 주식 가격을 그래프로 출력하는 함수.
    
    :param ticker: 주식 심볼 (예: "AAPL", "005930.KQ")
    :param period: 조회할 기간 (예: "1mo", "3mo", "1y", "max")
    """
    # 주식 데이터 가져오기
    stock = yf.Ticker(ticker)
    df = stock.history(period=period)

    # 이동 평균선 추가 (20일, 50일)
    df["SMA_20"] = df["Close"].rolling(window=20).mean()
    df["SMA_50"] = df["Close"].rolling(window=50).mean()

    # 그래프 그리기
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="종가", color="blue")
    plt.plot(df.index, df["SMA_20"], label="20일 이동 평균", linestyle="dashed", color="red")
    plt.plot(df.index, df["SMA_50"], label="50일 이동 평균", linestyle="dotted", color="green")
    
    plt.title(f"{ticker} 주가 차트 ({period})")
    plt.xlabel("날짜")
    plt.ylabel("가격")
    plt.legend()
    plt.grid()
    plt.show()

import numpy as np

def add_bollinger_bands(df: pd.DataFrame, window: int = 20):
    """
    볼린저 밴드 계산 (20일 이동 평균 ± 2표준편차)
    :param df: 주가 데이터 (Pandas DataFrame)
    :param window: 이동 평균 기간 (기본값: 20일)
    """
    df["SMA_20"] = df["Close"].rolling(window=window).mean()
    df["STD_20"] = df["Close"].rolling(window=window).std()
    df["Upper_Band"] = df["SMA_20"] + (df["STD_20"] * 2)
    df["Lower_Band"] = df["SMA_20"] - (df["STD_20"] * 2)
    return df

def plot_stock_chart_with_bollinger(ticker: str, period: str = "3mo"):
    df = yf.Ticker(ticker).history(period=period)
    df = add_bollinger_bands(df)  # 볼린저 밴드 계산

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="종가", color="blue")
    plt.plot(df.index, df["SMA_20"], label="20일 이동 평균", linestyle="dashed", color="red")
    plt.fill_between(df.index, df["Upper_Band"], df["Lower_Band"], color="gray", alpha=0.3, label="볼린저 밴드")

    plt.title(f"{ticker} 주가 차트 + 볼린저 밴드 ({period})")
    plt.xlabel("날짜")
    plt.ylabel("가격")
    plt.legend()
    plt.grid()
    plt.show()


def add_rsi(df: pd.DataFrame, window: int = 14):
    """
    RSI (Relative Strength Index) 계산
    :param df: 주가 데이터 (Pandas DataFrame)
    :param window: RSI 계산 기간 (기본값: 14일)
    """
    delta = df["Close"].diff(1)
    gain = np.where(delta > 0, delta, 0)
    loss = np.where(delta < 0, -delta, 0)

    avg_gain = pd.Series(gain).rolling(window=window, min_periods=1).mean()
    avg_loss = pd.Series(loss).rolling(window=window, min_periods=1).mean()

    rs = avg_gain / avg_loss
    df["RSI"] = 100 - (100 / (1 + rs))
    return df

def plot_rsi_chart(ticker: str, period: str = "3mo"):
    df = yf.Ticker(ticker).history(period=period)
    df = add_rsi(df)  # RSI 계산

    plt.figure(figsize=(12, 4))
    plt.plot(df.index, df["RSI"], label="RSI", color="purple")
    plt.axhline(70, linestyle="dashed", color="red", label="과매수 (70)")
    plt.axhline(30, linestyle="dashed", color="green", label="과매도 (30)")

    plt.title(f"{ticker} RSI 지표 ({period})")
    plt.xlabel("날짜")
    plt.ylabel("RSI 값")
    plt.legend()
    plt.grid()
    plt.show()

# 한글 폰트 설정 (Mac, Windows, Linux에 맞게 자동 설정)
def set_korean_font():
    plt.rcParams["axes.unicode_minus"] = False  # 마이너스 기호 깨짐 방지
    
    # MacOS (애플 기본 폰트)
    if fm.findSystemFonts(fontpaths=["/System/Library/Fonts/Supplemental"]):
        plt.rcParams["font.family"] = "AppleGothic"

    # Windows (맑은 고딕)
    elif fm.findSystemFonts(fontpaths=["C:/Windows/Fonts"]):
        plt.rcParams["font.family"] = "Malgun Gothic"

    # Linux (나눔고딕)
    else:
        plt.rcParams["font.family"] = "NanumGothic"

# 한글 폰트 적용
set_korean_font()

# 테스트 실행
if __name__ == "__main__":
    plot_stock_chart("AAPL", "3mo")  # 애플 3개월 주가 차트 출력