for i in range(1,672):
    fd = open('user.csv','a')
    myCsvRow = str(i)+","+str((chr)(i%26 + 64))+"\n"
    fd.write(myCsvRow)
    fd.close()
