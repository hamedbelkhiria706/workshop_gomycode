a=input('saisir test:')
cr,cl=[0,0]
for x in a:
    y=format(ord(x),'08b')
    for m in y:
        if(m=="0"):
            cr+=1
        else:
            cl+=1
print(cr,cl)