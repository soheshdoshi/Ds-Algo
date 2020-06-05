def check_all_1(arr):
    for i in arr:
        if i=='0':
            return False
    return True
def mySolution(A,B):
    lenth=len(A)
    arr_list=list(A)
    min_step=0
    index=0
    while index<lenth:
        if index+B<=lenth and arr_list[index]=='0':
            min_step+=1
            for i in range(0,B):
                if arr_list[index+i]=='0':
                    arr_list[index+i]='1'
                else:
                    arr_list[index+i]='0'
        else:
            index+=1
    if check_all_1(arr_list):
        return min_step
    return -1
A = "0000000000"
B = 10
print(mySolution(A,B))

