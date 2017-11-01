#!/usr/bin/python

### LASCON 2016
### 
### Basic python tutorial
### Ludmila Brochini
### 
### 
### Try these lines on python interpreter (or ipython) 
### and take a look at references in presentation
###

#numbers and strings
x=2  # no need to declare type
x>5 #comparison opperators like >,<, <=,>= ... 
x==5 #equal to ...
x!=5 #not equal to ...
x>1 and x<3 # can be combined with logical opperators and,or, not
3+4  # basic arithmetic opperators  + , -,*,/
2**5 # **(power)
x+5
10/2 #integer division ...
y=x/10     # yields an integer
type(y)    #Verify type. Python has many nice built-in functions see ref 
2/10.0 	   #if numerator or denominator is a float, the result is also float
y='LASCON' #can reuse names with different obj 
y='LAS'+'CON '# string concatenation 
#y+2016	      # cannot concatenate diferent types
mystr=y+str(2016) #You can however change to suitable type


#print (python 3 uses parenthesis, python 2 does not)
print 'any string'  # using print with quotes will print a string 
print mystr
print 'x=', x  

#lists  
a=[] #empty list
a=[2,4,6,10,4,13,11]
a[0] # first element indexed by 0
a[2:4] # third to fifth elements
a[2:]  # third to last
a[-2:] # last 2

b=['pyramidal','granule','basket']

a+a # concatenates lists
a*2
a+b

#you can create a list of lists
c=[a,a,a]
c[1]
c[1][2]#third element of the second list  

dir(a) #built-in that returns all atributes of an object
a.append(1) # use methods using dot notation
a.append(4) 
a.append('anything') # python allows you to mix data types
del x,y #delete variable
del a[-1] #delete just the last element
a.pop(2) #pops third element of your list
a.count(4) #counts how many times 4 appears in a
a.sort() #sorts your list
max(a) # maximum value
min(a) # minimum
len(a) # list length 
cmp(a,c) #comparison: returns 0 if lists are equal

#tuple: defined  with () immutable type ("read only")
tup=(1,2,'neuron')
tup[2] 
#tup[1]=3 # not allowed to do this because tuples cannot be updated
#enumerate yields tuples

#dictionary:type where a value (python object) is associated to a key (python type, like a string or number). There is no element position or order like in a list

d={'Cell':'Pyramidal','Layer':'V','Number':500,3:100}
d['Cell'] #look what value corresponds to a key
d['Number']+=500 # update a value corresponding to a key

#some useful dictionary methods
d.keys()
d.values()
d.items()
d.has_key('Number')

#Flow control Statement if
# if statement:
#	do something
x=input('Type a number ') #input from keyboard
if x<0:			 
	print 'negative' 
elif x==0:
	print 'zero'
else:
	print 'positive'

#iterations
#for element in list:
#   do something

for celltype in b:
	print 'Hippocampal ',celltype,' cells' # attention to block indentation

#range function creates a list of ordered integer elements, 
#starting from 0 as default
a=range(-2,2)
for i in range(4):
    print a[i]
    if a[i]==0:
         print 'break point reached when i=', i
         break	 #terminates current loop and goes to next statement

for key, value in d.items():  #alternatively iteritems	
	if d[key]=='V' : 
		print 'There are', key, value,' cells' 
				

#functions

def myprint(mystring):
	print mystring
	return

#this function returns nothing so you can simply call it by:
myprint('Printing something')

def printpow(base,exponent):
	"""Prints arguments and returns base^exponent""" # this is a docstring
	print "This function returns", base, "to the power of", exponent 
	return base**exponent

#help(printpow) #displays docstring
p=printpow(exponent=2,base=3)

# Classes
class Rectangle:
	def __init__(self, height, width):
		self.h = height
		self.w = width
	def area(self):		#function inside a class is called method
		return self.h*self.w

rec=Rectangle(2,1)
square=Rectangle(2,2)
square.h  # access attributes and methods of an object through the dot notation
square.w
square.area() 

#modules
#are python codes that contain variables, objects, methods, and functions that you can import and use

import numpy
v=numpy.arange(0,1,0.1)	# like range for non integers

import numpy as np #short
# element-wise sum:
a=[1,2,3]
b=[4,5,6]
x=np.array(a)
y=np.array(b)
print x+y
print np.add(x,y) #may use lists directly
#other element-wise opperations
print x - y
print np.subtract(x, y)
print x * y
print np.multiply(x, y)
print x / y
print np.divide(x, y)
print np.sqrt(x)
#compute inner product
print np.dot(x,y)

x = np.array([[1,2,3],[4,5,6]], dtype=np.float64) 
#would be int if it wasn't forced to be float using dtype
print np.sum(x) #sum of all elements
print np.sum(x,axis=0) #sum of each row

#pseudo-random number generator: numpy.random

np.random.rand(10) #uniform
a=np.random.randint(0,10,20)

b=a[2:6] # splitting an array and 
b=a[a>5] #  contains only elements from a greater than 5, in the same order as a
b=np.diff(a) 
# computes the difference between one element and the previous one

#simple plot example
from matplotlib import pyplot as plt #for 2D plots
x=range(10)
y=np.multiply(x,x)
h=np.random.randn(1000)#lets make a histogram with h

plt.plot(x,y)
plt.show()

myfig=plt.figure(figsize=(6,10)) #creates figure that wont appear yet 
plt.subplot(2,1,1) #2 plots in one figure
plt.plot(x,x,'bo-',linewidth=2.0) 
# choose color (b- blue, r-red), 'o' to plot dots and '-' to plot a line
plt.plot(x,y,'ro-',linewidth=2.0) # and line width
plt.xlabel('x',fontsize=11) # you may use tex notation between $$
plt.ylabel('y',fontsize=11) # choose font size
plt.title('Another Figure')
plt.subplot(2,1,2) #2 plots in one figure
n, bins, patches = plt.hist(h, 20) # number of bins in histogram
plt.xlabel('h',fontsize=11)
plt.ylabel('counts',fontsize=11)#tex notation between $$
plt.title('some histogram')
plt.axis([-3, 3, 0, 150]) # set axis intervals
plt.show() # you can either display it or 
myfig.savefig('figexample.pdf') # save it to file  (pdf, png, eps, jpeg)


#more topics: io, pickling etc, another time maybe...


