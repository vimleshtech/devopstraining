n =1 #int
n ='aaa' #str
n =True # bool
n = [1112,222] #array / list

f = open(r'C:\Users\hp\Desktop\emp.txt','r')


#print(f)
#print(f.read())
#print(f.readline())
#print(f.readline())

#print(f.readlines())

d = f.readlines() # [row1,row2]


print(type(d))

ri  = 0

for r in d:
    if ri>0:
        col = r.split(',')
        print(sum(col[3]))



    ##else:
        ##break

    ri = ri+1
    
print(ri)

#print("hi \t\nhello")

f.close()

###loop
'''
a = [22,333312,222]

for d in a:
    print(d)
'''










