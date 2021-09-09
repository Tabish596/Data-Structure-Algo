all([True,False,True,True])     #checks if all values are true
any([True,False,True,True])     #checks if any value is True
range(20,5,-1)
lambda x : x = a+b
b = set()    #similar ti list but do not accepts duplicate values
b = set([1,2,2,5,1,6,7,8])
def numberofargs(*argv):        #used fr passing number of arguments with only one number
    for arg in argv:
        print(arg)
numberofargs('hi','hellu','yo')   

z = ['tabish','gogo','shah']
y = [1,2,3]

r = zip(z,y)
print(list(r))