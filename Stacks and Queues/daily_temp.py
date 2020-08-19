'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
'''

def dailyTemperatures(T):
        n = len(T)
        stack = []
        result = [0] * n

        for i in range(n):
            current_temperature = T[i]
            print("i="+str(i)+", stack : ")
            print(*stack,end = ' ')
            print()
            while len(stack) and current_temperature > T[stack[-1]]:
                item_index = stack.pop()
                result[item_index] = i - item_index
            print("End of iteration, stack: ")
            print(*stack,end = ' ')
            print()
            print("Result array: ")
            print(*result,end = ' ')
            print()
            stack.append(i)

        return result

print('Enter the temperature for each day: ',end = '\n')
arr = list(map(int, input().strip().split(',')))
print(*dailyTemperatures(arr))