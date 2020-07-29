class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        revision_list_1 = [int(i) for i in version1.split(".")]
        revision_list_2 = [int(i) for i in version2.split(".")]
        
        def padding(revisions, to_length):
            for i in range(len(revisions), to_length):
                revisions.append(0)
            return revisions
        
        max_length = max(len(revision_list_1), len(revision_list_2))
        padded_revision_1 = padding(revision_list_1, max_length)
        padded_revision_2 = padding(revision_list_2, max_length)
        for p in range(0, max_length):
            if padded_revision_1[p] > padded_revision_2[p]:
                return 1
            elif padded_revision_1[p] < padded_revision_2[p]:
                return -1
        
        return 0
