
def dis(c1,c2):
    r=1
    r=(((c1[0]-c2[0])**2)+((c1[1]-c2[1])**2))**0.5
    return r

lim=int(input())

l=list(input().split(','))
man=[]
count=1;
for i in l:
    man.append(list(map(int,i.split(':'))))
j=1

mi=0
ma=0
mav=0
miv=lim
while j<len(man):
    
    if dis(man[0],man[j]) > mav:
        ma=j
        mav=dis(man[0],man[j])
    if dis(man[0],man[j]) <mi:
        mi=j
        miv=dis(man[0],man[j])
        
    j+=1

print(int((mav-miv)//lim)+1)
            
            
    
