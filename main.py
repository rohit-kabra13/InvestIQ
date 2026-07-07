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

# import yfinance as yf

# tickers = ["FKAE1", "MSFT", "NFLX", "AMZN", "TSLA", "RDW", "PLTR", "QBTS", "NVDA", "AMD", "GOOG", "FAKE2", "VOO", "VTI", "SCHD", "SPCX", "NOLIST"]

# for ticker in tickers:
#     try:
#         stock = yf.Ticker(ticker)
#         if "currentPrice" in stock.info:
#             current_price = stock.info["currentPrice"]
#         else:
#             print(f"{ticker} no price data available")
#             continue
#         if "open" in stock.info:
#             open_price = stock.info["open"]
#         else:
#             print(f"{ticker} no price data available")
#             continue
#         if current_price < open_price:
#             print(f"{ticker}- Current: {current_price} vs Open: {open_price} --> Strong Buy")
#         elif current_price > open_price:
#             print(f"{ticker}- Current: {current_price} vs Open: {open_price} --> Buy")
#         elif current_price == open_price:
#             print(f"{ticker}- Current: {current_price} vs Open: {open_price} --> Buy")
#     except KeyError:
#         print(f"{ticker} exists but is missing price data")
#     except:
#         print(f"{ticker} doesn't exist")



import yfinance as yf

tickers = ["AAPL", "COIN", "GME", "KO", "SMCI"]

def get_recommendation(percent_change):
    if percent_change < -0.05:
        return "High Risk - Dropping Fast"
    elif percent_change >= -0.05 and percent_change < 0:
        return "Mild Dip"
    else:
        return "Stable or Rising"
for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)
        if "currentPrice" in stock.info:
            current_price = stock.info["currentPrice"]
        else:
            print(f"No price data available")
            continue
        if "open" in stock.info:
            open_price = stock.info["open"]
        else:
            print(f"No price data available")
            continue
        percent_change = (current_price - open_price) / open_price
        # if percent_change < -0.05:
        #     print(f"{ticker} Current- {current_price} Open- {open_price} Percent Change: {percent_change} --> High Risk - Dropping Fast")
        # elif percent_change >= -0.05 and percent_change < 0:
        #     print(f"{ticker} Current- {current_price} Open- {open_price} Percent Change: {percent_change}  --> Mild Dip")
        # else:
        #     print(f"{ticker} Current- {current_price} Open- {open_price} Percent Change: {percent_change}  --> Stable or Rising")
        result = get_recommendation(percent_change)
        print(f"{ticker}- Current: {current_price} Open: {open_price} Percent Change: {percent_change} --> {result}")
    except:
        print(f"{ticker} doesn't exist")
