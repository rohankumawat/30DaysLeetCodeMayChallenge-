class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_count = [0]*N
        for t in trust:
            trust_count[t[0] - 1] -= 1
            trust_count[t[1] - 1] += 1
        result = -1
        for i in range(N):
            if trust_count[i] == N-1:
                return i + 1
        return result
