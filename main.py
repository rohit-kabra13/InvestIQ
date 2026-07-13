# # # # # # --------------------- Beginning of Practice ----------------------------
# # # # # # print("Hello InvestIQ")

# # # # # # portfolio_value = 65000
# # # # # # print(portfolio_value)

# # # # # # stock_prices = [150, 200, 75]
# # # # # # print(stock_prices[1])

# # # # # # portfolio = {"AAPL": 150, "GOOG": 200, "TSLA": 75}
# # # # # # print(portfolio["TSLA"])

# # # # # # for ticker in portfolio:
# # # # # #     print(ticker, portfolio[ticker])

# # # # # # def show_portfolio():
# # # # # #     for ticker in portfolio:
# # # # # #         print(ticker, portfolio[ticker])

# # # # # # show_portfolio()

# # # # # # watchlist = {"NFLX": 400, "AMZN": 130}

# # # # # # def show_holdings(holdings):
# # # # # #     for ticker in holdings:
# # # # # #         print(ticker, holdings[ticker])

# # # # # # show_holdings(portfolio)
# # # # # # show_holdings(watchlist)

# # # # # # tsla_price = portfolio["TSLA"]

# # # # # # if tsla_price < 50:
# # # # # #     print("Strong Buy")
# # # # # # elif tsla_price < 100:
# # # # # #     print("Buy")
# # # # # # elif tsla_price < 200:
# # # # # #     print("Hold")
# # # # # # else:
# # # # # #     print("Sell")

# # # # # # new_holdings = {"MSFT": 310, "NFLX":420, "PLTR": 18}


# # # # # # def show_new_holdings(recommendation):
# # # # # #     for ticker in recommendation:
# # # # # #         if recommendation[ticker] < 20:
# # # # # #             print(ticker, "Strong Buy")
# # # # # #         elif recommendation[ticker] > 20 and recommendation[ticker] <= 200:
# # # # # #             print(ticker, "Buy")
# # # # # #         elif recommendation[ticker] > 200 and recommendation[ticker] <= 400:
# # # # # #             print(ticker, "Hold")
# # # # # #         else:
# # # # # #             print(ticker, "Sell")
# # # # # # show_new_holdings(new_holdings)


# # # # # # price = 45
# # # # # # sector = "Tech"

# # # # # # if price < 30 or sector != "Tech":
# # # # # #     print("Watch this one")

# # # # # # --------------------- End of Practice ----------------------------



# # import yfinance as yf
# # # idenitfying the Fake Ticker in the list

# # tickers = ["FKAE1", "MSFT", "NFLX", "AMZN", "TSLA", "RDW", "PLTR", "QBTS", "NVDA", "AMD", "GOOG", "FAKE2", "VOO", "VTI", "SCHD", "SPCX", "NOLIST"]

# # for ticker in tickers:
# #     try:
# #         stock = yf.Ticker(ticker)
# #         if "currentPrice" in stock.info:
# #             current_price = stock.info["currentPrice"]
# #         else:
# #             print(f"{ticker} no price data available")
# #             continue
# #         if "open" in stock.info:
# #             open_price = stock.info["open"]
# #         else:
# #             print(f"{ticker} no price data available")
# #             continue
# #         if current_price < open_price:
# #             print(f"{ticker}- Current: {current_price} vs Open: {open_price} --> Strong Buy")
# #         elif current_price > open_price:
# #             print(f"{ticker}- Current: {current_price} vs Open: {open_price} --> Buy")
# #         elif current_price == open_price:
# #             print(f"{ticker}- Current: {current_price} vs Open: {open_price} --> Buy")
# #     except KeyError:
# #         print(f"{ticker} exists but is missing price data")
# #     except:
# #         print(f"{ticker} doesn't exist")



# # # Build a Single Function - Percent Change

# # tickers = ["AAPL", "COIN", "GME", "KO", "SMCI"]

# # def get_recommendation(percent_change):
# #     if percent_change < -0.05:
# #         return "High Risk - Dropping Fast"
# #     elif percent_change >= -0.05 and percent_change < 0:
# #         return "Mild Dip"
# #     else:
# #         return "Stable or Rising"
# # for ticker in tickers:
# #     try:
# #         stock = yf.Ticker(ticker)
# #         if "currentPrice" in stock.info:
# #             current_price = stock.info["currentPrice"]
# #         else:
# #             print(f"No price data available")
# #             continue
# #         if "open" in stock.info:
# #             open_price = stock.info["open"]
# #         else:
# #             print(f"No price data available")
# #             continue
# #         percent_change = (current_price - open_price) / open_price
# #         result = get_recommendation(percent_change)
# #         print(f"{ticker}- Current: {current_price} Open: {open_price} Percent Change: {percent_change} --> {result}")
# #     except:
# #         print(f"{ticker} doesn't exist")



# # # Build a Double Function

# # tickers = ["MSFT", "DIS", "BA"]

# # def get_health_score(percent_change, distance_from_high):
# #     if percent_change < 0 and distance_from_high > 0.03:
# #         return "Weak"
# #     if percent_change < 0 and distance_from_high <= 0.03:
# #         return "Recovering"
# #     if percent_change >= 0:
# #         return "Strong"
# # for ticker in tickers:
# #     try:
# #         stock = yf.Ticker(ticker)
# #         if "currentPrice" in stock.info:
# #             current_price = stock.info["currentPrice"]
# #         else:
# #             print(f"No price data available")
# #             continue
# #         if "open" in stock.info:
# #             open_price = stock.info["open"]
# #         else:
# #             print(f"No price data available")
# #             continue
# #         if "dayHigh" in stock.info:
# #             days_high = stock.info["dayHigh"]
# #         else:
# #             print(f"No Price Data Available")
# #             continue
# #         percent_change = (current_price - open_price) / open_price
# #         distance_from_high = (days_high - current_price) / days_high
# #         result =  get_health_score(percent_change, distance_from_high)
# #         print(f"{ticker}- Current: {current_price} Day's High: {days_high} Percent Change: {percent_change} Distance from High: {distance_from_high} --> {result}")
# #     except:
# #         print("f{ticker} doesn't exist")


# # # # Using Append to identify the List

# # tickers = ["MSFT", "DIS", "BA"]

# # def get_health_score(percent_change, distance_from_high):
# #     if percent_change < 0 and distance_from_high > 0.03:
# #         return "Weak"
# #     if percent_change < 0 and distance_from_high <= 0.03:
# #         return "Recovering"
# #     if percent_change >= 0:
# #         return "Strong"
# # weak_stocks =[]
# # for ticker in tickers:
# #     try:
# #         stock = yf.Ticker(ticker)
# #         if "currentPrice" in stock.info:
# #             current_price = stock.info["currentPrice"]
# #         else:
# #             print(f"No price data available")
# #             continue
# #         if "open" in stock.info:
# #             open_price = stock.info["open"]
# #         else:
# #             print(f"No price data available")
# #             continue
# #         if "dayHigh" in stock.info:
# #             days_high = stock.info["dayHigh"]
# #         else:
# #             print(f"No Price Data Available")
# #             continue
# #         percent_change = (current_price - open_price) / open_price
# #         distance_from_high = (days_high - current_price) / days_high
# #         result =  get_health_score(percent_change, distance_from_high)
# #         if result == "Recovering":
# #             weak_stocks.append(ticker)
# #         # print(f"{ticker}- Current: {current_price} Day's High: {days_high} Percent Change: {percent_change} Distance from High: {distance_from_high} --> {result}")
# #     except:
# #         print("f{ticker} doesn't exist")
# # print(weak_stocks)


# # Self Practice

# import yfinance as yf
# tickers = ["AMZN", "GOOG", "AMD", "NFLX", "BA"]

# def classify_move(percent_change):
#     if percent_change > 0.01:
#         return "Gainer"
#     if percent_change < -0.01:
#         return "Loser"
#     else:
#         return "Flat"
# gainer = {}
# loser = {}
# for ticker in tickers:
#     try:
#         stock = yf.Ticker(ticker)
#         if "currentPrice" in stock.info:
#             current_price = stock.info["currentPrice"]
#         else:
#             print(f"No Price Data Available")
#             continue
#         if "open" in stock.info:
#             open_price = stock.info["open"]
#         else:
#             print(f"No Price Data Available")
#             continue
#         percent_change = (current_price - open_price) / open_price
#         result = classify_move(percent_change)
#         if result == "Gainer":
#             gainer[ticker] = round(percent_change, 4)
#         elif result == "Loser":
#             loser[ticker] = round(percent_change, 4)
#     except:
#         print(f"Ticker not available")
# for ticker, percent_change in gainer.items():
#     print(f"{ticker} is up {percent_change}")
# for ticker, percent_change in loser.items():
#     print(f"{ticker} is down {percent_change}")


# import yfinance as yf
# tickers = ["AAPL", "TSLA", "AMD", "META", "KO"]

# def get_rating(percent_change):
#     if percent_change > 0.02:
#         return "Strong"
#     if percent_change < -0.02:
#         return "Weak"
#     else:
#         return "Neutral"
# report = {}
# strong_stocks = []
# weak_stocks = []
# for ticker in tickers:
#     try:
#         stock = yf.Ticker(ticker)
#         if "currentPrice" in stock.info:
#             current_price = stock.info["currentPrice"]
#         else:
#             print(f"No Price Data Available")
#             continue
#         if "open" in stock.info:
#             open_price = stock.info["open"]
#         else:
#             print(f"No Price Data Available")
#             continue
#         percent_change = (current_price - open_price) / open_price
#         rating =  get_rating(percent_change)
#         report[ticker] = {"current": current_price, "open": open_price, "change": round(percent_change, 4), "rating": rating}
#         if rating == "Strong":
#             strong_stocks.append(ticker)
#         elif rating == "Weak":
#             weak_stocks.append(ticker)
#     except:
#         print(f"{ticker} Not listed")
# for ticker, data in report.items():
#     print(f"{ticker}: Current - {data['current']} Open - {data['open']} Change - {data['change']} Rating - {data['rating']}")





import yfinance as yf
tickers = ["NVDA", "AAPL", "AMD", "NFLX", "COIN", "BA"]

def get_rating(percent_change):
    if percent_change > 0.02:
        return "Strong"
    if percent_change < -0.02:
        return "Weak"
    else:
        return "Neutral"
report = {}
strong_stocks = []
weak_stocks = []
best_ticker = None
best_change = -999

for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)
        if "currentPrice" in stock.info:
            current_price = stock.info["currentPrice"]
        else:
            print(f"No price data avaialble")
            continue
        if "open" in stock.info:
            open_price = stock.info["open"]
        else:
            print(f"No price data available")
            continue
        percent_change = round((current_price - open_price) / (open_price), 4)
        rating = get_rating(percent_change)
        report[ticker] = {"current": current_price, "open": open_price, "change": round(percent_change, 4), "rating": rating}
        if percent_change > best_change:
            best_ticker = ticker
            best_change = percent_change
    except:
        print(f"Not available")

print(f"🏆 Best performer: {best_ticker} at {best_change}")
