i = 1
while i <= 9:
    j = 1
    while j <= i:
        val = j * i
        print("%d * %d = %d\t" %(j,i,val), end="")
        j+=1
        pass
    print("")
    i+=1
    pass

