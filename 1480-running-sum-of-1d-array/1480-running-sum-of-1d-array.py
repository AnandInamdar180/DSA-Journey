class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total=0
        output=[]

        for i in range(len(nums)):
            total+=nums[i]
            output.append(total)


        return output