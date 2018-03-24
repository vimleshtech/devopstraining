f = open(r'C:\Users\hp\Desktop\GitRepo.txt','r')

d = f.readlines() # [row1,row2]
c = 0

for r in d:
    if r.replace('\n','') == "Git":
        c = c+1

print(c)

f.close()






