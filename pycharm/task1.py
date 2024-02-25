with open('asd.txt','r') as f:
    spis=f.readlines()



res=''.join(spis)
res=res.split(' ')
for i in range(0,len(res)-1,2):
    c=res[i]
    res[i]=res[i+1]
    res[i+1]=c
print(" ".join(res))



