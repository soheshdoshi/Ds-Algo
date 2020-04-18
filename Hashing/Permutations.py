# #useing sorting timr complexity o(n2log(n))
# def mySolution(x,y):
#     x=sorted(x)
#     x_lenth=len(x)
#     y_lenth=len(y)
#     count=0
#     for i in range(y_lenth-x_lenth+1):
#         if sorted(y[i:i+x_lenth])==x:
#             count+=1
#     return count
from collections import Counter
def mySolution(x,y):
    """
    time Complexity n2 space m+n
    :param x:
    :param y:
    :return:
    """
    x_dict=Counter(x)
    x_lenth=len(x)
    y_lenth=len(y)
    count=0
    for i in range(y_lenth-x_lenth+1):
        if x_dict==Counter(y[i:i+x_lenth]):
            count+=1
    return count





x="abc"
y="abcbacabc"
print(mySolution(x,y))