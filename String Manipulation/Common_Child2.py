def commonChild(s1,s2):
    n,m = len(s1),len(s2)
    dp = [[0]* (m+1) for _ in range(n+1)]

    for i,c1 in enumerate(s1):
        for j,c2 in enumerate(s2):
            if c1 == c2:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    return dp[n-1][m-1]

if __name__ == '__main__':
    a = input()
    b = input()

    print(commonChild(a,b))
