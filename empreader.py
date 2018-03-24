f = open(r'C:\Users\hp\Desktop\emp.txt','r')

f.readline()

d = f.readlines() # [row1,row2]

c = 0
for  r in d:
    col = r.split(',')
    c =c + int((col[3]))

print(c)

f.close()






