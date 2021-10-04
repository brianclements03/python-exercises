##CONTROL STRUCTURES
 #if thens
 x = 5
 r = x % 2
 if r == 0:
     print('the number x is even')
print('Hello hopperites')

 x = 4
 r = x % 2
 if r == 0:
     print('the number x is even')
 else:
    print('the number x is odd')
 print('Hello hopperites')

 #nested ifs/elses
#keep it shallow
#elif

##Loops
l = [1,2,3,4,5]
for num in range(1,11):
    if num % 2 == 0:
        print(num, 'is even')
    else:
        print(num, 'is odd')