def createIntialString(n):
    whiteBall=["W"]*(n)
    BlackBall=["B"]*(n)
    return whiteBall+["H"]+BlackBall

def intitalMove(string_list,hole_index):
    string_list[hole_index],string_list[hole_index-1]=string_list[hole_index-1],string_list[hole_index]
    return hole_index-1
    # return string_list

def checkInList(string,final_list):
    if string in final_list:
        return 1
    final_list.append(string)
    return 0
def checkIndex(a,b,last_index):
    if a<0 or b<0 or a>=last_index or b>=last_index:
        return 0
    return 1
def left_one_move(string_list,hole_index,last_index,final_list):
    if checkIndex(hole_index,hole_index-1,last_index):
        string_list[hole_index],string_list[hole_index-1]=string_list[hole_index-1],string_list[hole_index]
        if checkInList("".join(string_list),final_list):
            string_list[hole_index],string_list[hole_index+1]=string_list[hole_index+1],string_list[hole_index]
            return hole_index
        else:
            return hole_index-1
    return hole_index
def right_one_move(string_list,hole_index,last_index,final_list):
    if checkIndex(hole_index,hole_index+1,last_index):
        string_list[hole_index],string_list[hole_index+1]=string_list[hole_index+1],string_list[hole_index]
        if checkInList("".join(string_list),final_list):
            string_list[hole_index],string_list[hole_index-1]=string_list[hole_index-1],string_list[hole_index]
            return hole_index
        else:
            return hole_index+1
    return hole_index



def backtrack(string_list,final_list,hole_index,last_index):
    if string_list==string_list[::-1]:
        print(final_list)
        return
    hole_index=intitalMove(string_list,hole_index)
    final_list.append("".join(string_list))
    #print(string_list, final_list,hole_index)
    left_hole_index=left_one_move(string_list,hole_index,last_index,final_list)
    if left_hole_index==hole_index:
        final_list.pop()
    print(string_list,final_list)

def mySolution(n):
    l=createIntialString(n)
    new_list = []
    new_list.append("".join(l))
    #print(l,new_list)
    backtrack(l,new_list,n,(2*n)+1)



mySolution(1)