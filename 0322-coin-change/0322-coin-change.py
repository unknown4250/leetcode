class Solution(object):
    def coinChange(self, coins, amount):

        if amount == 0: return 0

        queue = deque([(0,0)])

        visited = [False] * (amount + 1)
        visited[0] = True

        while queue:
            total, cur_val = queue.popleft()

            total += 1

            for coin in coins:
                next_val = cur_val + coin

                if next_val == amount:
                    return total
                
                elif next_val < amount:
                    if not visited[next_val]:
                        visited[next_val] = True
                        queue.append((total, next_val))
        
        return -1