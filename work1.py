a_list=[1,2,3,4]
sum=0
for i in range(len(a_list)):
    b_list=a_list.copy()
    x=str(b_list.pop(i))
    for j in range(len(b_list)):
        c_list=b_list.copy()
        y=str(c_list.pop(j))
        for k in range(len(c_list)):
            z=str(c_list[k])
            print(x+y+z)
            sum +=1
print("总数是%d"%sum)
     
