print('''
\t   Pra*************************
\t   *****Deep*******************
\t   ****************************
\t   *********Construction*******
\t   ****************************
\t   *********************Company
                              
''')
a={'1':'Login','2':'Exit'}
for i in a:
    print(i,':',a[i])
a3=int(input('Enter Your Command:'))
if a3==1:
    a1=input('Enter The UserName:')
    a2=input('Enter Your Password')
elif a3==2:
    exit
else:
    print('Please enter Right One:')
        
      