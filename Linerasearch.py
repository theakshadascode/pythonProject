pos=-1
def search(list,n):

    i=0
    while(i < len(list)):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False



list=[2,4,5,6,8,7,9]
n=9

if search(list,n):
    print("Found",pos+1)
else:
    print("Not found")
