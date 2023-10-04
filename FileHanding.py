r=open("File","r")
#print(r.read())  #return file content
#print(r.readline()) #return one line

w=open("Fileright","w")
#w.write("Something")

for i in r:
    w.write(i)
