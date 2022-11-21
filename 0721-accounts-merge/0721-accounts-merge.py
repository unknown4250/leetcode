from collections import defaultdict

class UnionFind:
    # 부모 노드 리스트를 자기 자신으로 초기화
    def __init__(self, n):
        self.parents = list(range(n))

    # 두 노드가 속한 집합 합치기
    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)
    
    # 특정 노드가 속한 집합 찾기
    def find(self, x):
        # 루트 노드가 아니면 루트 노드 찾을 때까지 재귀적 호출
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # 유니온 파인드 인스턴스 생성
        uf = UnionFind(len(accounts))

        owner = {}

        # 인덱스, (이름, 이메일 목록)
        for idx, (name, *emails) in enumerate(accounts):
            for email in emails:
                # 이메일이 이미 추가되어 있다면, 한 사람의 계정으로 통합
                if email in owner:
                    # parent: 이메일 주소, child: 인덱스
                    uf.union(idx, owner[email])
                # 해당 이메일의 소유자를 현재 인덱스로 설정
                owner[email] = idx
        
        ans = defaultdict(list)

        # 같은 소유자에 속하는 이메일 목록을 배열의 한 원소에 append
        for email, idx in owner.items():
            ans[uf.find(idx)].append(email)

        # 소유자 + 정렬된 이메일 목록 출력
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]
