import yfinance as yf
import streamlit as st

# Define tickers and industry for demonstration
tickers = ["AAPL", "MSFT"]
industry = "Technology"

# Function to fetch financial data and calculate ratios
def get_financial_data(ticker):
    financial_data = {}
    ratios = {}
    try:
        data = yf.Ticker(ticker).info
        financial_data = {
            "Total Revenue": data.get("totalRevenue", None),
            "Cost Of Revenue": data.get("costOfRevenue", None),
            "Net Income": data.get("netIncome", None),
            "Total Stockholders' Equity": data.get("totalStockholdersEquity", None),
        }

        # Profit Margin
        revenue = financial_data.get("Total Revenue")
        cost_of_goods_sold = financial_data.get("Cost Of Revenue")
        if revenue is not None and cost_of_goods_sold is not None:
            profit_margin = (revenue - cost_of_goods_sold) / revenue
            ratios["Profit Margin"] = profit_margin
        else:
            st.write(f"Profit Margin data not available ({ticker})")

        # Return on Equity (ROE)
        net_income = financial_data.get("Net Income")
        total_stockholders_equity = financial_data.get("Total Stockholders' Equity")
        if net_income is not None and total_stockholders_equity is not None:
            roe = net_income / total_stockholders_equity
            ratios["ROE"] = roe
        else:
            st.write(f"ROE data not available ({ticker})")

    except (KeyError, ValueError) as e:
        st.error(f"Error retrieving data for {ticker}: {e}")
    return ratios

# Streamlit dashboard layout
st.title(f"Financial Ratio Analysis ({industry})")

# User selection for company
selected_ticker = st.selectbox("Select a company:", tickers)

# Download data and calculate ratios
ratios = get_financial_data(selected_ticker)

# Display ratios if available
if ratios:
    st.header(f"{selected_ticker} Ratios")
    for ratio, value in ratios.items():
        if value is not None:
            st.write(f"- {ratio}: {value:.2f}")

# Industry averages (replace with actual industry averages)
industry_avg = {"Profit Margin": 0.15, "ROE": 0.2}

# Display industry averages
st.header("Industry Averages")
for ratio, value in industry_avg.items():
    st.write(f"- {ratio}: {value:.2f}")

# Profit Margin comparison (if both data and industry average are available)
if "Profit Margin" in ratios and "Profit Margin" in industry_avg:
    profit_margin = ratios["Profit Margin"]
    industry_profit_margin = industry_avg["Profit Margin"]
    comparison = "Lower" if profit_margin < industry_profit_margin else ("Higher" if profit_margin > industry_profit_margin else "Equal")
    st.subheader(f"Profit Margin Comparison")
    st.write(f"{selected_ticker}'s Profit Margin ({profit_margin:.2f}) is {comparison} than the industry average ({industry_profit_margin:.2f}).")

# Sentiment Score Integration (placeholder)
sentiment_score = 0.35  # Placeholder for sentiment score (replace with actual logic)
st.header("Sentiment Score")
st.write(f"{selected_ticker}'s sentiment score is {sentiment_score:.2f} (higher score is more positive).")

# Findings Compilation
st.header("Findings Compilation")
st.write("Based on the analysis, it can be concluded that... (provide summary of findings)")

# Recommendations
st.header("Recommendations")
st.write("Based on the findings, the following recommendations are suggested... (provide recommendations)")

