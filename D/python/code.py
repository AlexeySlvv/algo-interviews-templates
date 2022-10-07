from typing import List
from collections import defaultdict


def get_longest_increasing_path(matrix: List[List[int]]) -> int:
	if not matrix or not matrix[0]:
		return 0
        
	mx, dp = matrix, defaultdict(int)
	n, m = len(mx), len(mx[0])
        
	def dfs(i, j):
		if dp[i,j] == 0:
			mij = mx[i][j]
			if i and mij > mx[i-1][j]:
				dp[i,j] = max(dp[i,j], dfs(i-1,j))
			if i < n-1 and mij > mx[i+1][j]:
				dp[i,j] = max(dp[i,j], dfs(i+1,j))
			if j and mij > mx[i][j-1]:
				dp[i,j] = max(dp[i,j], dfs(i,j-1))
			if j < m-1 and mij > mx[i][j+1]:
				dp[i,j] = max(dp[i,j], dfs(i,j+1))
			dp[i,j] += 1
		return dp[i,j]

	p_max = 0
	for i in range(n):
		for j in range(m):
			p_max = max(p_max, dfs(i,j))
	return p_max

def read_matrix() -> List[List[int]]:
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    return matrix

matrix = read_matrix()
print(get_longest_increasing_path(matrix))