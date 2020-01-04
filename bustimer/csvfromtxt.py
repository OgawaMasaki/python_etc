with open('data/output/pdf.txt', "r",encoding = "utf-8") as f:
    data = [v.rstrip() for v in f.readlines()]
#print(data)
print(type(data))


#for i in range(len(data)):
#    print(str(i) + ":" + str(data[i]))

del data[0:54]



for k in range(len(data)):
    print(str(k) + ":" + str(data[k]))

