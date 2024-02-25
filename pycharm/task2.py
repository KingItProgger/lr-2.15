

with  open('asd.txt','r') as f:
    a=f.read().split()

    a.sort(key=len, reverse=True)
    max_ = len(a[0])
    print(max_)
    for i in range(len(a)):
        if len(a[i])==max_:
            print(a[i])



