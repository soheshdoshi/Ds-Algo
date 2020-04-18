def mySolution(arr):
    arr_list=arr.split(" ")
    return " ".join(arr_list[::-1])



arr="This is a chance"
print(mySolution(arr))