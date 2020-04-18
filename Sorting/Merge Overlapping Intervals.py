def mySolution(arr_list):
    arr_list=sorted(arr_list)
    temp=[]
    l=[]
    for i in range(len(arr_list)):
        if len(temp)==0:
            temp=[arr_list[i][0],arr_list[i][1]]
        else:
            if arr_list[i][0]>=temp[0] and arr_list[i][0]<=temp[1]:
                temp[0]=min(temp[0],arr_list[i][0])
                temp[1]=max(temp[1],arr_list[i][1])
            else:
                l.append(temp)
                temp=[arr_list[i][0],arr_list[i][1]]
    l.append(temp)
    return l



arr=[[1,3],[2,6],[8,10],[15,18]]
mySolution(arr)
