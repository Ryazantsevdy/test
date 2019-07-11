s1 = '{{}}'
print('Hello')
print(s1)
index=0;
print(int(len(s1)/2))
for index in range(0,int(len(s1)/2)):
	print(s1[index],"|", s1[-1-index])
	print(s1[index]=='{' and s1[-1-index]=='}')
	print(s1[index]=='(' and s1[-1-index]==')')
	print((s1[index]=='{' and s1[-1-index]=='}') or (s1[index]=='(' and s1[-1-index]==')'))
	print (index)




'''
if len(s1) % 2 !=0:
        print(len(s1))

else:
    while(index<=len(s1)/2) :
        if (s1[index]=='{' and s1[-1-index]=='}') or (s1[index]=='(' and s1[-1-index]==')'):
            index+=1
        else:
'''        	
s2='({()})'
def myMetod (string):
    index=0;

    if len(string) % 2 !=0:
        print(len(string))
        return False
    else:
        while(index<=len(s1)/2):
            if (string[index]=='{' and string[-1-index]=='}') or (string[index]=='(' and string[-1-index]==')'):
                index+=1
            else:
                return False
    return True
            


print(myMetod(str(s2)))