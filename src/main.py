from src.data_fetcher import fetch_stock_data
from src.data_analyzer import plot_stock_chart, plot_stock_chart_with_bollinger, plot_rsi_chart
from src.strategy import train_model, plot_predicted_vs_actual
from src.utils.enums import ModelType


if __name__ == "__main__":
    ticker = "AAPL"  # 애플 주식
    # data = fetch_stock_data(ticker, period="1mo", interval="1d")

    # print("📈 주식 데이터 가져오기 성공!")
    # print(data.head())  # 상위 5개 데이터 출력

    # plot_stock_chart(ticker, "3mo")  # 3개월 데이터 시각화
    # plot_stock_chart_with_bollinger(ticker, "3mo")  # 볼린저 밴드 포함 차트
    # print("📈 주식 차트 + 볼린저 밴드 출력 완료!")

    # plot_rsi_chart(ticker, "3mo")  # RSI 차트
    # print("📈 RSI 차트 출력 완료!")

    model_type = ModelType.XGBOOST  # 사용할 모델 선택 (ModelType.XGBOOST, ModelType.LSTM)
    
    df_test, mae, last_pred = train_model(ticker, model_type)  # ✅ df_test 포함
    plot_predicted_vs_actual(df_test, ticker)  # ✅ 이제 `df_test`에 예측값이 포함됨!

