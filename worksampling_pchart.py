import math
from random import  uniform
from random import randrange
#from scipy.stats import truncnorm
import matplotlib.pyplot as plt
import numpy as np


#def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    #return truncnorm(
        #(low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

#X = get_truncated_normal(mean=8, sd=2, low=1, upp=10)
#print(X.rvs(10))



#expected value of p
p=0.20
print('Initial mean:',p)
#level of accuracy
l=0.05*p
print('Initial error limit:',l)
#confidence level
c=0.95
#no of observation
n=(3.84*p*(1-p))/(l*l)
#no of readings per day = 400
m=400
#no of days
d = int(n/400)
#print(d)
d=d+1
#print(d)
print('Initial no of days :',d)

#calculation of siqma
sigma = (p*(1-p))/m
#print(sigma)
sigma=math.sqrt(sigma)
print('The value of initial standard deviation:',sigma)


#ucl
ucl = p + 3*sigma
print('Upper bound:',ucl)
#lcl
lcl= p - 3*sigma
print('Lower bound:',lcl)

l1=[]

#randomly generate 50 observation
for f in range(50):
    l1.append(uniform(ucl+.05, lcl-.05))

 
#print(l1)

l2=[]
#randomly assign 0,1 to each element in l1
for g in l1:
    l2.append((randrange(0,2)))
# 0 means no cause found

#print(l2)

#list l5 used to get initial no of observation depending upon initial no. of days
l5=list(l1[:d])
#plotting initial plot
b=range(0,d)
plt.scatter(b,l5,color="blue",s=0.5)
plt.ylabel("Defective %")
plt.xlabel("Observed Days")
y=p*np.ones(d)
yu=(p+3*sigma)*np.ones(d)
yl=(p-3*sigma)*np.ones(d)
plt.plot(b,y,color="Red",label="Initial values")
plt.plot(b,yu,color="Red")
plt.plot(b,yl,color="Red")
plt.text(10,.06,r"$p_i = {}$".format(p))

#l3 to get element no equal to that of no of days from l1
l3=[]
#to get a copy of l3 after removing 0 assigned elements
l4=[]
y=0

def function(p,l,c,d,m,sigma,ucl,lcl,l3,pold,y):
    #print(d)
    i=0
    l3=list(l1)
    h1=[]
    #print(l1)
    #print(l3)
    #print(len(l1))
    l3=l3[:d]
    l4=list(l3)
    #print(l3)
    #print(len(l3))
    #print(l1)

    #getting indices of days whose value are greater then ucl and lcl
    for h in range(d):
        if l1[h]>ucl or l1[h]<lcl:
            h1.append(h)

    #printing those indices
    #print(h1)

    #removing those elements which have no cause from l3
    for k in h1:
        if l2[k]==0:
            #print(k)
            l3.pop(-(len(l3)-(k-i)))
            i=i+1

    #printing new l3    
    #print(l3)
    #print(len(l3))

    p1=0
    j1=0
    z=0
    
    #checking in new l3 which element are out of bounds and have 1 assigned 
    for i in range(len(l3)):
        if (l3[i] > ucl or l3[i] < lcl):
            #print(i)
            if l2[i]==1:
                #print(i)
                for j in range(i+1):
                    p1=p1+l3[j]
                    j1=j
                j1=j1+1    
                p1=(p1)/(j1)
                #print(p1)
                break
            else:
                z=z+1
            

              
        else:
            #print('this is within limit ucl and lcl')
            z=z+1

    #z is taken to check no of elemnets are out of bounds or not
    #if value of z equals to no. of elemts in new l3 means no elemnt are out of bounds so this is optimal
    #print(z)
    
    p=p1
    #print(p)
  
    l=0.05*p
    #print(l)
    c=0.95
    if l!=0:
        if y < 5:
            print('\nThe new mean is:',p)
            print('The new error limits is:',l)
            n=(3.84*p*(1-p))/(l*l)
            d = int(n/400)
            #print(d)
            d=d+1
            print('No of days :',d)
            m=400
            sigma = (p*(1-p))/m
            #print(sigma)
            sigma=math.sqrt(sigma)
            print('New standard deviation:',sigma)
            #ucl
            ucl = p + 3*sigma
            print('New Upper Bound:',ucl)
            #lcl
            lcl= p - 3*sigma
            print('New Lower bound:',lcl)
            #print(len(l3))
            y=y+1
            #print(y)
    elif y==0:
        print('\n\n \nIt itself is the correct p - chart')
        print('Final mean:',.2)
        print('Final upper bound:',ucl)
        print('Final lower bound:',lcl)        
        c=range(d)
        z=.2*np.ones(d)
        zu=(.2+3*sigma)*np.ones(d)
        zl=(.2-3*sigma)*np.ones(d)
        plt.plot(c,z,color="Green",label="Final value")
        plt.plot(c,zu,color="Green")
        plt.plot(c,zl,color="Green")
        plt.text(10,.04,r"$p_f = {}$".format(round(.2,3)))  #New parameters
        plt.legend(loc='best')
        plt.axvline(x=d,color="Brown")
        plt.show()        
        
    else:
        #print(l4)
        #print(len(l4))
        #print(d)
        #print(pold)
        print('\n\n\nFinal mean:',pold)
        print('Final upper bound:',ucl)
        print('Final lower bound:',lcl)
        c=range(d)
        z=pold*np.ones(d)
        zu=(pold+3*sigma)*np.ones(d)
        zl=(pold-3*sigma)*np.ones(d)
        plt.plot(c,z,color="Green",label="Final value")
        plt.plot(c,zu,color="Green")
        plt.plot(c,zl,color="Green")
        plt.text(10,.04,r"$p_f = {}$".format(round(pold,3)))  #New parameters
        plt.legend(loc='best')
        plt.axvline(x=d,color="Brown")
        plt.show()        
        
    if((len(l3)!=z)):
        if y < 5:
            #print(len(l3))
            pold=p
            function(p,l,c,d,m,sigma,ucl,lcl,l3,pold,y)
        else:
            print('\n \n \nThe problem is entering in an infinte loop.Please run again to see correct model.')
            print('Final mean:',p)
            print('Final upper bound:',ucl)
            print('Final lower bound:',lcl)
            c=range(d)
            z=p*np.ones(d)
            zu=(p+3*sigma)*np.ones(d)
            zl=(p-3*sigma)*np.ones(d)
            plt.plot(c,z,color="Green",label="Final value")
            plt.plot(c,zu,color="Green")
            plt.plot(c,zl,color="Green")
            plt.text(10,.04,r"$p_f = {}$".format(round(p,3)))  #New parameters
            plt.legend(loc='best')
            plt.axvline(x=d,color="Brown")
            plt.show() 
    else:
        return [p,l,c,d,m,sigma,ucl,lcl,l3,pold,y]


#pold is there to store the value of p in the last iteration before termintion bec at last step p becomes 0
pold=0
listhai=function(p,l,c,d,m,sigma,ucl,lcl,l3,pold,y)

                



                

