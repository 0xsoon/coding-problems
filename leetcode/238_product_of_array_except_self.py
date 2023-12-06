from typing import List

class Solution:
    def productExceptSelf(self, nums:List[int]) -> List[int]:
        x = 1
        ans = []
        for num in nums:
            prod = num * x
            ans.append(prod)
            x = prod
        
        R = 1
        for i in reversed(range(1 , len(nums))):
            prod =  ans[i - 1] * R
            print(prod)
            ans[i] = prod
            R = nums[i] * R  
        ans[0] = R
        return ans


if __name__ == "__main__":
    input_str = input()
    input_list = input_str.split()
    input_list = [int(el) for el in input_list] 

    sol = Solution()
    sol.productExceptSelf(input_list)
