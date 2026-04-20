class Solution:
    def hasDuplicate(self, my_list: List[int]) -> Bool:
        my_sorted_list = self.sort(my_list) 
        
        for i in range(len(my_sorted_list) - 1):
            if my_sorted_list[i] == my_sorted_list[i + 1]:
                return True
        
        return False
        


    def sort(self, li: List[int]) -> List[int]:
        n = len(li)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if li[j] > li[j + 1]:
                    li[j], li[j + 1] = li[j + 1], li[j]
                    swapped = True
            if not swapped:
                break
        return li
