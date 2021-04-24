def maxProfit(self, prices):
        cur = 0
        answer = 0
        minimum = 10000000
        maximum = 0
        min_index = -1
        max_index = -1
        while cur < len(prices):
            while cur + 1 < len(prices) and prices[cur] >= prices[cur+1]:
                cur += 1
            if prices[cur] < minimum:
              minimum = prices[cur]
              min_index = cur
            
            while cur + 1 < len(prices) and prices[cur] <= prices[cur+1]:
                cur += 1
            # if prices[cur] >= maximum:
            maximum = prices[cur]
            max_index = cur

            if max_index > min_index:            
              answer = max(answer, maximum - minimum)

            print(minimum, maximum, cur, answer, min_index, max_index)
            cur += 1
            
        return answer


print(maxProfit(0, [3,3,5,0,0,3,1,4]))