def calculateprofit(arr,arr_size):
    profit = 0
    for i in range(1,arr_size):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
    return profit

prices = [847,245,756,394,123]

profit = calculateprofit(prices,len(prices))

print("Max profit:",profit)

