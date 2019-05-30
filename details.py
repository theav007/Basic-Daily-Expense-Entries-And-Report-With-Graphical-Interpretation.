print('''
      ***Bhahikhata***
      ''')
e={1:'Day',2:'Name',3:'Remarks',4:'Mode',5:'Exit'}
for i in e:
    print('\t',i,':',e[i])
e1=int(input('Enter The Options:'))
if e1==1:
    import day
elif e1==2:
    import name
elif e1==3:
    import remark
elif e1==4:
    import mode
elif e1==5:
    exit
else:
    print('Please Enter Right Option:')
    