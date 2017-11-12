
# coding: utf-8

# In[ ]:


import sys
sys.stdin.readline()

x1 = {'x1': 'x11', 'x2': 'x12', 'x3': 'x13'}
x2 = {'x1': 'x21', 'x2': 'x22', 'x3': 'x23'}
x3 = {'x1': 'x31', 'x2': 'x32', 'x3': 'x33'}
a=[x1['x1'],x1['x2'],x1['x3']]
b=[x2['x1'],x2['x2'],x2['x3']]
c=[x3['x1'],x3['x2'],x3['x3']]

l1=len(set(a))
l2=len(set(b))
l3=len(set(c))
c1=len(set([a[0],b[0],c[0]]))
c2=len(set([a[1],b[1],c[1]]))
c3=len(set([a[2],b[2],c[2]]))
d1=len(set([a[0],b[1],c[2]]))
d2=len(set([a[2],b[1],c[0]]))
counter=1
print '***Welcome to Tic Tac Toe*** \nPlayer 1 your turn, o is your key '
while l1*l2*l3*c1*c2*c3*d1*d2 !=1:
    
    print '\n \n Current Position'
    print a
    print b
    print c
    
    row = eval(raw_input("Input row :")) 
    column  = raw_input("Input column :") 
    
      
    if row[column]!='o' and  row[column]!='x' : 
        if counter%2==1:
            row[column]='o'
        else:
            row[column]='x'
        counter =counter+1
                    
        a=[x1['x1'],x1['x2'],x1['x3']]
        b=[x2['x1'],x2['x2'],x2['x3']]
        c=[x3['x1'],x3['x2'],x3['x3']]

        print 'Current Position after input'
        print a
        print b
        print c
        print 'Checking for results ...'
        l1=len(set(a))
        l2=len(set(b))
        l3=len(set(c))
        c1=len(set([a[0],b[0],c[0]]))
        c2=len(set([a[1],b[1],c[1]]))
        c3=len(set([a[2],b[2],c[2]]))
        d1=len(set([a[0],b[1],c[2]]))
        d2=len(set([a[2],b[1],c[0]]))
        if l1==1 or l2==1 or l3==1 or c1==1 or c2==1 or c3==1 or d1==1 or d2==1:
            print '\n Contratulation you are the Winner'
            if counter%2==1:
                print 'Player 1 '
            else:
                print 'Player 2 '
            break
       
        elif counter<=9:
            print 'No result'
            if counter%2==1:
                print 'Player 1 your turn, o is your key'
            else:
                print 'Player 2 your turn, x is your key'
            continue
        else :
            print 'Game Drawn, No winner'
            break
    else:
        print 'Please already filled, \n\nTry Again'
        



# In[5]:


5%2

