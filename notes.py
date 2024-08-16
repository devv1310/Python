# list 
# it is one of the most important primitive
# data-type
# ordered data-type
# multiple elements.
# indexing (zero based)(negative as well)
# duplication allowed
# mutable data-type
# faster then tuple.(tuple countainer)
# slower then tuple
# []

# numerals sequence set map None

#    0   1    2       3
#lis=[23,4.5,"apple",[2,3,4]]
#    -4  -3    -2     -1
#print(type(lis))
#print(lis)

#print(lis[2])
#print(lis[-2])
#                               0   1  2  3  4                                
#lis=[101,"apple","bhopal",98.3,[45,47,47,49,90]]

#print(lis)
#lis[2]="indore"
#print(lis)

#print(lis[4])

#print(lis[4][3],lis[-1][-2])
#print(lis)
#print(lis)

#slicing =

#lis=[11,22,34,"hello",4,-9,66,"hi",55,900,344]

#print(lis)

#print(lis[3:8])

#a=lis[3:8] #a list type

#b=lis[3:11] #[3:] end of the list 
#print(b)

#c=lis[7:2:-2] #jump value negative only
#print(c)

#rev=lis[::-1]
#print(rev)

#print(lis[:4]+lis[7:])# list concatenate

#--------------------------------------------------------------------#

# append(value) #last m add hoga

# lis=[2,3,4]
# print(lis)
# lis.append(98)
# print(lis)
# lis.append(["apple","banana"])
# print(lis)

#extend (iterable)---->return none list hi pass krni h
#extend(list/tupler)

#lis=[2,3,4]

#print(lis)
#lis.extend([22,33,44]) #[2, 3, 4, 22, 33, 44]
#lis.append([22,33,44]) #[2, 3, 4, [22, 33, 44]]
# lis=[2,3,4]+[22,33,44]
#print(lis)


#WAP to creat a list of n element
#also create a seperate list for even and odd numbers.

# lis=[]
# n=int(input("enter any range"))
# for i in range(n):
#     num=int(input("enter no."))
#     lis.append(num)
#     print(lis)

# index() return index number
#index(value,start,end)

# lis=[2,3,4,66,77,88,20000,77,68]

# a=lis.index(77)
# print(a) #4

# b=lis.index(77,a+1)
# print(b)

#count(value)----->freaquency return
#WAP to find out the index number of element 77
#coming in a list lis.(using loop)

# lis=[2,3,4,66,77,77,88,20000,77,68]

# a=lis.count(77)
# print(a)

# lis=[2,3,4,66,77,77,88,20000,77,68]

# c=lis.count(77)
# b=0
# for i in range(c):
#     a=lis.index(77,b)#lis.index(77,0) , lis.index(77,5)
#     b=a+1 #4+1
#     print(a)

#max() , min() , sum() , len()

#lis=[2,3,4,66,77,77,88,20000,77,68]

# length=len(lis)
# print(length)

# print(max(lis))
# print(min(lis))
#print(sum(lis))


#----------------------------------------------------------------------------------------------------------#

#WAP to create a list of list 
#[["1","ajay","bhopal"],["2","sourabh","ujjain"],["sumit","bhopal"]]


# n=int(input("how many records do u want to insert:"))   #4

# lis=[]

# for i in range(n):
#     name=input("enter name:")
#     address=input("enter address:")
#     roll=input("enter roll number:")
#     lis2=[roll,name,address]
#     lis.append(lis2)
# print(lis)

#----------------------------------------------------------------------------------
#


# n=int(input("how many records do u want to insert:"))

# #lis=[[],[],[]]
# lisn=[]
# lisa=[]
# lisr=[]
# for i in range(n):
#     name=input("enter name:")
#     lisn.append(name) #lis[0].append(name)
#     address=input("enter address:")
#     lisa.append(address) #lis[1].append(address)
#     roll=input("enter roll number:")
#     lisr.append(roll) #lis[2].append(roll)

# print(lisn+lisa+lisr) #print(lis)

#---------------------------------------------------------------------


#result list contain name and adress

# names=["ajay","sourabh","sumit"]
# address=["bhopal","ratlam","ujjain"]
# a=[] #zip function se bhi krna h 
# for i in range(3):
#     a.append([names[i],address[i]])
# print(a)
