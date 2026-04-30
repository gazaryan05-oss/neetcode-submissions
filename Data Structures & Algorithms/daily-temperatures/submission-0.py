class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []  # храним ИНДЕКСЫ, а не температуры
        
        for i in range(n):
            # пока стек не пуст и текущая температура выше температуры на вершине стека
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                res[idx] = i - idx  # сколько дней ждал
            stack.append(i)  # добавляем текущий индекс в стек
        
        return res
