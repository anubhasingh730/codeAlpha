import requests
import json

class StockPortfolio:
    def _init_(self, api_key):
        self.api_key = api_key
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            print("Stock already exists in portfolio. Updating quantity.")
            self.portfolio[symbol] += quantity
        else:
            self.portfolio[symbol] = quantity
        print(f"Added {quantity} shares of {symbol} to portfolio.")

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if self.portfolio[symbol] >= quantity:
                self.portfolio[symbol] -= quantity
                print(f"Removed {quantity} shares of {symbol} from portfolio.")
            else:
                print("Not enough shares to remove.")
        else:
            print("Stock not found in portfolio.")

    def track_performance(self):
        for symbol, quantity in self.portfolio.items():
            url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}"
            response = requests.get(url)
            data = json.loads(response.text)
            price = float(data["Global Quote"]["05. price"])
            value = price * quantity
            print(f"{symbol}: {quantity} shares @ ${price:.2f} = ${value:.2f}")

def main():
    api_key = "YOUR_API_KEY"
    portfolio = StockPortfolio(api_key)

    while True:
        print("\n1. Add stock")
        print("2. Remove stock")
        print("3. Track performance")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == "2":
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == "3":
            portfolio.track_performance()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if _name_ == "_main_":
    main()