def computeLPSArray(string):
    M = len(string)
    lps = [None] * M

    length = 0
    lps[0] = 0  # lps[0] is always 0

    # the loop calculates lps[i]
    # for i = 1 to M-1
    i = 1
    while i < M:

        if string[i] == string[length]:

            length += 1
            lps[i] = length
            i += 1

        else:  # (str[i] != str[len])

            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is
            # similar to search step.
            if length != 0:

                length = lps[length - 1]

                # Also, note that we do not
                # increment i here

            else:  # if (len == 0)

                lps[i] = 0
                i += 1

    return lps


# Method returns minimum character
# to be added at front to make
# string palindrome
def getMinCharToAddedToMakeStringPalin(string):
    revStr = string[::-1]
    concat = string + "$" + revStr
    lps = computeLPSArray(concat)
    return len(string) - lps[-1]

A="babb"
print(getMinCharToAddedToMakeStringPalin((A)))
