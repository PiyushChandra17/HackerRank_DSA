def commonChild(X,Y):
    m = len(X)
    c = [[0]*(m+1) for _ in range(m+1)]

    for i in range(m):
        for j in range(m):
            if X[i]==Y[j]:
                c[i][j]=c[i-1][j-1]+1
            else:
                c[i][j]=max(c[i][j-1],c[i-1][j])
    return c[m-1][m-1]

if __name__ == '__main__':
    X = input()
    Y = input()

    print(commonChild(X,Y))
