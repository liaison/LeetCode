class FileSystem:

    def __init__(self):
        self.path_map = {}

    def createPath(self, path: str, value: int) -> bool:
        if path == "" or path == "/" or path[0] != "/" or path in self.path_map:
            # invalid path or path exists already
            return False

        folders = path.split("/")
        parent_path = ""
        for folder in folders[1:-1]:
            parent_path = parent_path + "/" + folder
            if parent_path not in self.path_map:
                return False

        self.path_map[path] = value
        return True

    def get(self, path: str) -> int:
        if path in self.path_map:
            return self.path_map[path]
        else:
            return -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)