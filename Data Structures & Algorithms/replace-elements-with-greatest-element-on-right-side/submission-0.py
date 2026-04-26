class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
       
        max_elemnt = -1
        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_elemnt
            max_elemnt = max(current, max_elemnt)
        return arr