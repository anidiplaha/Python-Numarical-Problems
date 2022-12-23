s =input("Enter Name Here : ")
l = s.split() 
new = ""  
for i in range(len(l)-1): 
        s = l[i]
        new += (s[0].upper()+'.')  
new += l[-1].title()  
print(new) 
