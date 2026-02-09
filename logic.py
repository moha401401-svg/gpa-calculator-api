
def func(Grades):
    r=['CS','Math1','Discrete','Elctronics','Creative_thinking','Technical_writing']
    sub=list(getattr(Grades,l)for l in r )
    t=[]
    p=[4,3.7,3.4,3.2,3,2.8,2.6,2.4,2.2,2,1.5,1]
    for i in sub:
        c=0
        f=100
        while f>=50:
            if f<=60:
                if f>i>=(f-5):
                    break
                else:
                    f-=5
                    c+=1
            else:
                if f>i>=(f-4) or i==100:
                    break
                else:
                    f-=4
                    c+=1
        if f<50:
            t.append(0)
        else:
            t.append(p[c])
    for i in range(len(r)):
       if i<=3:
           t[i]*=3
       else:
            t[i]*=2
    total=sum(t)
    GPA=total/16
    return GPA



    


