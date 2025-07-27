# Best time to buy and sell stocks for maximum profit   #leetcode=121
prices = [7, 1, 5, 3, 6, 4]
n = len(prices)
mini = prices[0]  # Initialize the minimum price
profit = 0  # Initialize the maximum profit
buy_day = 0  # Day to buy the stock
sell_day = 0  # Day to sell the stock

for i in range(n):
    cost = prices[i] - mini  # Calculate the profit if sold today
    if cost > profit:
        profit = cost
        sell_day = i  # Update the selling day
    if prices[i] < mini:
        mini = prices[i]
        buy_day = i  # Update the buying day

print("Maximum profit:", profit)
print("You have to buy stock on day", buy_day + 1)
print("You have to sell stock on day", sell_day + 1)
