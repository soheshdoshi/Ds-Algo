def postOrderRecusive(inorde,preorder,n):
    index=inorde.index(preorder[0])
    if index!=0:
        postOrderRecusive(inorde[:index],preorder[1:index+1],len(inorde[:index]))
    if index!=n-1:
            postOrderRecusive(inorde[index+1:],preorder[index+1:],len(inorde[index+1:]))
    print(preorder[0])





a=[4,2,5,1,3,6]
b=[1,2,4,5,3,6]
postOrderRecusive(a,b,len(a))
