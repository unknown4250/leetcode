class Solution(object):
    def largestPalindromic(self, num):

        counter = [0] * 10

        # 숫자를 인덱스로 활용해서 숫자별 개수 카운트
        for n in num:
            counter[int(n)] += 1
        
        result = ''
        # 팰린드롬 만들기
        for i in range(10):
            while counter[i] >= 2:
                # 문자열 왼쪽과 오른쪽에 더해나감
                result += str(i)
                result = str(i) + result
                counter[i] -= 2
        
        # 갯수가 홀수인 숫자 중 값이 가장 큰 숫자를 가운데 값으로 설정
        for i in reversed(range(10)):
            if counter[i] > 0:
                result = result[:len(result)//2] + str(i) + result[len(result)//2:]
                break
        
        # 팰린드롬의 양 옆 '0' 제거
        result = result.strip('0')
        
        # '0' 제거하면 팰린드롬 없는 경우를 위한 예외 처리
        return result if result else "0"
        