class Solution:
    def simplifyPath(self, path: str) -> str:
        
        folders = path.split('/')
        
        canonical = deque([])
        for i, folder in enumerate(folders):
            if folder == "" and i > 0:
                # skip
                continue
            elif folder == "..":
                # we might go beyond the root folder
                if canonical:
                    canonical.pop()
            elif folder == ".":
                continue
            else:
                canonical.append(folder)       
        
        if len(canonical) == 0 or canonical[0] != "":
            canonical.appendleft("")
        
        if len(canonical) == 1:
            return "/"
        else:
            return "/".join(canonical)

