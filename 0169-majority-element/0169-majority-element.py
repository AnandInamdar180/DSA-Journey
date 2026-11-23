class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count={}
        highest_num= None
        max_count=0
        for num in nums:
            count[num]=count.get(num,0)+1
            if count[num]>max_count:
                max_count=count[num]
                highest_num=num
        return highest_num