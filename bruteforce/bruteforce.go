package bruteforce

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func BruteForceMaxPathSum(triangle [][]int) int {
	var maxSum int

	var dfs func(row, col, sum int)
	dfs = func(row, col, sum int) {
		if row == len(triangle) {
			maxSum = max(maxSum, sum)
			return
		}

		dfs(row+1, col, sum+triangle[row][col])
		dfs(row+1, col+1, sum+triangle[row][col])
	}

	dfs(0, 0, 0)

	return maxSum
}
