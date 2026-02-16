def romanToInt(s):
    val = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    total = 0
    n = len(s)

    for i in range(n):
        cur = val[s[i]]

        if i+1<n and cur < val[s[i+1]]:
            total -= cur
        else:
            total += cur
    return total

print(romanToInt("LVIII"))