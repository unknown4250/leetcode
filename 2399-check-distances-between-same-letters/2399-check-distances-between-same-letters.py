class Solution(object):
    def checkDistances(self, s, distance):
        # 같은 문자 간의 거리를 저장할 배열
        check = [-1] * 26

        for idx, ch in enumerate(s):
            # 문자가 처음 나타난 경우, 해당 위치 저장 
            if check[ord(ch)-97] == -1:
                check[ord(ch)-97] = idx
            # 문자가 두 번째 나타난 경우, 처음 위치와의 거리 저장
            else:
                check[ord(ch)-97] = idx - check[ord(ch)-97] - 1
        
        for i in range(26):
            # 없는 문자이면 확인 안함
            if check[i] == -1:
                continue
            # distance와 실제 문자 간 거리가 다르면 false 리턴
            if distance[i] != check[i]:
                return False
        return True
        