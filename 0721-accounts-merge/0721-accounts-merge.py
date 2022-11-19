class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        uf = UnionFind(len(accounts))

        owner = {}

        for idx, (name, *emails) in enumerate(accounts):
            for email in emails:
                if email in owner:
                    uf.union(idx, owner[email])
                owner[email] = idx
        
        ans = defaultdict(list)

        for email, owner in owner.items():
            ans[uf.find(owner)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]

