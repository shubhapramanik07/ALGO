#  Leetcode 121: Best Time to Buy and Sell Stock 

price = [7,1,5,3,6,4]
n = len(price)
max_profit = 0
for i in range(n):
    for j in range(i+1,n):
        # if price[j] - price[i] > max_profit:
        #     max_profit = price[j] - price[i]
        if price[j] > price[i]:
            profit = price[j] - price[i]
            max_profit = max(max_profit, profit)

print(max_profit)
print("Brute Force Approach")

# time complexity: O(n^2) where n is the number of days
# space complexity: O(1) as we are using only constant space


#* /****************************************/

#? optimal solution using one pass  

# price = [12,11,4,3,10,5]
# min_price = float('inf')
# max_profit = 0
# for i in price:
#     min_price = min(min_price,i)
#     max_profit = max(max_profit,i-min_price)

# print(max_profit)

# time complexity: O(n) where n is the number of days
# space complexity: O(1) as we are using only constant space