
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:

        parents = dict()

        for region in regions:
            parent_region = region[0]
            for subregion in region[1:]:
                parents[subregion] = parent_region

        p1 = region1
        p2 = region2
        while p1 != p2:
            p1 = region2 if p1 not in parents else parents[p1]
            p2 = region1 if p2 not in parents else parents[p2]

        return p1
