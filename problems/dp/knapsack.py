def knapsack(B, wt, val):
    n = len(val)
    
    rows = n + 1
    columns = B + 1
    K = [[ 0 for _ in range(columns)] for _ in range(rows)]

    # Build table K[][] in bottom-up manner
    for i in range(1, rows):
        for b in range(1, columns):
            if wt[i-1] <= b:
                K[i][b] = max(val[i-1] + K[i-1][b-wt[i-1]], K[i-1][b])
            else:
                K[i][b] = K[i-1][b]
    
    return K[n][B]