import streamlit as st
import appdirs as ad
ad.user_cache_dir = lambda *args: "/tmp"
import yfinance as yf
import matplotlib.pyplot as plt

# Create a Streamlit app
st.title("Stock Price Analysis")

# Create a text input for entering a stock symbol
stock_symbol = st.text_input("Enter a stock symbol:")

# Get the historical price data for the entered stock
if stock_symbol:
    try:
        stock_data = yf.download(stock_symbol, start="2020-01-01", end="2022-12-31")
        # Create a line chart of the stock's closing prices
        fig, ax = plt.subplots()
        ax.plot(stock_data.index, stock_data["Close"])
        ax.set_title(f"{stock_symbol} Closing Prices")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (USD)")
        st.pyplot(fig)
    except Exception as e:
        st.error(f"Error: {e}")

# Run the app
if __name__ == "__main__":
    st.write("Stock Price Analysis App")
    st.write("Enter a stock symbol to view its historical price data.")