def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    n, m = len(seq1), len(seq2)

    score = [[i * gap if j == 0 else j * gap if i == 0 else 0 
              for j in range(m+1)] for i in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            diag = score[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            score[i][j] = max(diag, score[i-1][j] + gap, score[i][j-1] + gap)

    align1, align2 = "", ""
    i, j = n, m

    while i > 0 and j > 0:
        diag = score[i-1][j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)

        if score[i][j] == diag:
            align1, align2 = seq1[i-1] + align1, seq2[j-1] + align2
            i, j = i-1, j-1
        elif score[i][j] == score[i-1][j] + gap:
            align1, align2 = seq1[i-1] + align1, "-" + align2
            i -= 1
        else:
            align1, align2 = "-" + align1, seq2[j-1] + align2
            j -= 1

    while i > 0:
        align1, align2 = seq1[i-1] + align1, "-" + align2
        i -= 1
    while j > 0:
        align1, align2 = "-" + align1, seq2[j-1] + align2
        j -= 1

    return align1, align2, score[n][m]


# Example
a1, a2, score = needleman_wunsch("GATTACA", "GCATGCU")
print(a1, "\n", a2, "\nScore:", score)