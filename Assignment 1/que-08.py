def longest_common_consonant_subsequence(str1, str2):
    def is_consonant(char):
        return char.isalpha() and char.lower() not in 'aeiou'

    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if is_consonant(str1[i - 1]) and is_consonant(str2[j - 1]):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if is_consonant(str1[i - 1]) and is_consonant(str2[j - 1]):
            if str1[i - 1] == str2[j - 1]:
                lcs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))


str1 = "abcdegdhajkjdhdjdjdjd"
str2 = "bdfedjdkshsi"
result = longest_common_consonant_subsequence(str1, str2)
print("Longest Common Consonant Subsequence:", result)
