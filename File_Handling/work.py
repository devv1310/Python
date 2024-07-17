# 1. Create
# 2. Open
# 3. Read/Write
# 4. Close
# Syntx:-
#   open(file name,'mode)
#                    |......x -> Create
#                    |......r -> Read
#                    |......w -> Write //if your have data already in your file so never run 'w' mode becz its delete all data
#                    |......a -> Append 
# Type of File :- 1. Text File 2. Bnary File 3. .csv file 
# f=open("new.txt",'x') 
# f=open('new1.txt','w')
# f=open('new2.txt','r')
# f=open('new3.txt','r')
# print(f.read())

# Method :- open()
#           readable()   
#           writeable()
#           closeable()
# f=open('n1.txt','x')
# f=open('n2.txt','x')
# print(f.readable())
# print(f.writable())
# print(f.closed)
# f.close()
# print(f.closed)
# print(f.writable())
