import random

i=5
while i:
   
    print('1:SANG\n2:KAQZ\n3:QEICHI')


    user=int(input())
    comp=random.randint(1,3)
    if user==1 :
        if comp==1 :
           
            print('No One!!\n')

        elif comp==2 :   

            print('Computer is Win!\n')

        else :

            print('User Win!\n') 

    elif user==2:

        if comp==1:           
            print('User Win!\n')

        elif comp==2 :    

            print('No One!!\n')

        else :

            print('Computer Win!\n')

    elif user==3 :

        if comp==1 :  

            print('Computer Win!\n')

        elif comp==2 :

            print('User Win!\n')

        else :    

            print('No One!!\n')

    else :

        print('Invalid!\n')  
         
    i-=1         