# --------------------- Beginning of Practice ----------------------------
# print("Hello InvestIQ")

# portfolio_value = 65000
# print(portfolio_value)

# stock_prices = [150, 200, 75]
# print(stock_prices[1])

# portfolio = {"AAPL": 150, "GOOG": 200, "TSLA": 75}
# print(portfolio["TSLA"])

# for ticker in portfolio:
#     print(ticker, portfolio[ticker])

# def show_portfolio():
#     for ticker in portfolio:
#         print(ticker, portfolio[ticker])

# show_portfolio()

# watchlist = {"NFLX": 400, "AMZN": 130}

# def show_holdings(holdings):
#     for ticker in holdings:
#         print(ticker, holdings[ticker])

# show_holdings(portfolio)
# show_holdings(watchlist)

# tsla_price = portfolio["TSLA"]

# if tsla_price < 50:
#     print("Strong Buy")
# elif tsla_price < 100:
#     print("Buy")
# elif tsla_price < 200:
#     print("Hold")
# else:
#     print("Sell")

# new_holdings = {"MSFT": 310, "NFLX":420, "PLTR": 18}


# def show_new_holdings(recommendation):
#     for ticker in recommendation:
#         if recommendation[ticker] < 20:
#             print(ticker, "Strong Buy")
#         elif recommendation[ticker] > 20 and recommendation[ticker] <= 200:
#             print(ticker, "Buy")
#         elif recommendation[ticker] > 200 and recommendation[ticker] <= 400:
#             print(ticker, "Hold")
#         else:
#             print(ticker, "Sell")
# show_new_holdings(new_holdings)


# price = 45
# sector = "Tech"

# if price < 30 or sector != "Tech":
#     print("Watch this one")

# --------------------- End of Practice ----------------------------

import yfinance as yf

tickers = ["MSFT", "NFLX", "AMZN", "META", "NVDA"]

for ticker in tickers:
    stock = yf.Ticker(ticker)
    current_price = stock.info["currentPrice"]
    open_price = stock.info["open"]
    if current_price < open_price:
        print(f"{ticker}: Current- {current_price} vs Open- {open_price} -> Strong Buy")
    elif current_price > open_price:
        print(f"{ticker}: Current- {current_price} vs Open- {open_price} -> Sell")
    elif current_price == open_price:
        print(f"{ticker}: Current- {current_price} vs Open- {open_price} -> Hold")