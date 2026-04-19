class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures) # default result is 0 for all days
        stack = [] # store the indices of temperatures list

        for i, temp in enumerate(temperatures):
            # If current temp > stack top's temp → found a warmer day
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # pop indices from the stack while current temp is warmer
                prev_day_index = stack.pop()
                result[prev_day_index] = i - prev_day_index

            stack.append(i) # push current day index on to the stack
        return result