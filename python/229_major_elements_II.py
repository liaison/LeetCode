class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        major_elements = defaultdict(int)
        
        # voting for the major elements
        for num in nums:
            major_elements[num] += 1
            if len(major_elements) == 3:
                to_delete = []
                for k, v in major_elements.items():
                    major_elements[k] -= 1
                    if v == 1:
                        to_delete.append(k)
                for k in to_delete:
                    del major_elements[k]
        
        ret = []
        # a second round to verify if the major elements takes 1/3 votes
        for elem in major_elements:
            if nums.count(elem) > len(nums) / 3:
                ret.append(elem)
        
        return ret