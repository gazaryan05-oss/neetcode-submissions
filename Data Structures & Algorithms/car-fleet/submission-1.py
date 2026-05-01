class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        count = 0
        slow = 0

        for start, spd in cars:
            current = (target - start) / spd
            if slow < current:
                count += 1
                slow = current 
        return count
        