
class UnionFind:
    def __init__(self, size):
        self.parent = [index for index in range(size)]

    def find(self, child):
        if self.parent[child] != child:
            self.parent[child] = self.find(self.parent[child])
        return self.parent[child]

    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa != pb:
            self.parent[pa] = self.parent[pb]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        account_table = defaultdict(list)
        for account in accounts:
            name = account[0]
            emails = set(account[1:])
            account_table[name].append(emails)

        # merge accounts with the same name and shared emails
        merged_accounts = {}
        for name, value in account_table.items():
            merged_sets = self.merge_emails(value)
            merged_accounts[name] = merged_sets

        # sort the emails for each acount
        output = []
        for name, value in merged_accounts.items():
            for emails in value:
                new_entry = [name]
                for email in sorted(emails):
                    new_entry.append(email)
                output.append(new_entry)

        return output


    def merge_emails(self, value):
        # index each email address with the account_index/account_id
        email_index = defaultdict(list)
        for account_index, emails in enumerate(value):
            for email in emails:
                email_index[email].append(account_index)

        uf = UnionFind(len(value))
        # merge the accounts that share at least one emails
        for email, indices in email_index.items():
            for index_index, index in enumerate(indices[1:]):
                uf.union(index, indices[index_index])

        # build groups of accounts with their group ids
        groups = defaultdict(list)
        for account_index in range(len(value)):
            group_id = uf.find(account_index)
            groups[group_id].append(account_index)

        # reconstruct the emails for each account group
        output = []
        for group_id, account_indices in groups.items():
            new_entry = set()
            for account_index in account_indices:
                new_entry.update(value[account_index])
            output.append(new_entry)

        return output


