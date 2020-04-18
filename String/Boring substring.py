def check(s):
    for i in range(len(s) - 1):
        if (abs(ord(s[i]) -
                ord(s[i + 1])) == 1):
            return False
    return True

def Rearrange(Str):
    # To store the odd and the
    # even positioned characters
    odd, even = "", ""

    # Traverse through the array
    for i in range(len(Str)):
        if (ord(Str[i]) % 2 == 0):
            even += Str[i]
        else:
            odd += Str[i]

            # Sort both the Strings
    odd = sorted(odd)
    even = sorted(even)

    # Check possibilities
    if (check(odd + even)):
        return 1
    elif (check(even + odd)):
        return 1
    else:
        return 0

print(Rearrange("iagaabf"))