class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        def largestRectangleArea(A):
            stack = []
            n = len(A)
            ret = 0
            tp = -1
            area_with_top = -1
            i = 0
            while i < n:
                if len(stack) == 0 or A[i] >= A[stack[-1]]:
                    stack.append(i)
                    i += 1
                else:
                    tp = stack.pop()
                    area_with_top = A[tp] * (i if len(stack) == 0 else i - stack[-1] - 1)
                    if ret < area_with_top:
                        ret = area_with_top
            while len(stack) != 0:
                tp = stack.pop()
                area_with_top = A[tp] * (i if len(stack) == 0 else i - stack[-1] - 1)
                if ret < area_with_top:
                    ret = area_with_top

            return ret

        n = len(A)
        m = len(A[0])
        # print(m)
        stack = A[0]
        # print(stack)
        res = []
        temp1 = largestRectangleArea(stack)
        res.append(temp1)
        tot = []
        tot.append(A[0])
        for i in range(1, n):
            tot.append([0] * m)
        # print(tot)
        for i in range(1, n):
            temp = []
            for j in range(0, m):
                # print(A[i][j])
                # if A[i][j]==1:
                #     temp.append((stack[j]+A[i][j]))
                # else:
                #     temp.append(0)
                if A[i][j] == 1:
                    tot[i][j] = int(tot[i - 1][j]) + int(A[i][j])

            # stack=temp
            # #temp1=largestRectangleArea(stack)
            # #res.append(temp1)
            # tot.append(temp)

        for i in tot:
            res.append(largestRectangleArea(i))
        # print(res)
        return max(res)