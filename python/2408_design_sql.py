class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        self.db = {}
        self.row_counter = {}
        self.col_counter = {}
        for index, table_name in enumerate(names):
            col_num = columns[index]
            self.db[table_name] = {}
            self.row_counter[table_name] = 1
            self.col_counter[table_name] = col_num


    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.db:
            return False

        col_num = len(row)
        if self.col_counter[name] != col_num:
            return False

        table = self.db[name]
        rowId = self.row_counter[name]
        table[rowId] = row
        # increase the counter
        self.row_counter[name] = rowId + 1
        return True


    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.db:
            return

        table = self.db[name]
        if rowId not in table:
            return
        del table[rowId]


    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.db:
            return "<null>"
        table = self.db[name]
        if rowId not in table:
            return "<null>"

        if columnId < 1 or columnId > self.col_counter[name]:
            return "<null>"

        return table[rowId][columnId-1]


    def exp(self, name: str) -> List[str]:
        if name not in self.db:
            return []
        table = self.db[name]
        ret = []
        for rowId, columns in table.items():
            entry = "{},{}".format(rowId, ",".join(columns))
            ret.append(entry)
        return ret


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)