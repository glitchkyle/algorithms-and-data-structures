def edit_distance(word_one, word_two):
    n = len(word_one)
    m = len(word_two)
    out = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1,n+1):
            x = out[i-1][j-1]
            y = out[i-1][j]
            z = out[i][j-1]
            minimum = min(x, y, z)

            if word_two[i - 1] == word_one[j - 1]:
                out[i][j] = minimum
            else:
                out[i][j] = minimum + 1

    return out[n-1][m-1]