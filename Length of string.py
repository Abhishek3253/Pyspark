#Using iterating String 
# str1 =input(str("enter the String to caluclate Length :"))
# c=0
# for i in str1:
#     c+=1
# print("Length of Sring is = " ,c)

#Using function 
# str1 =input(str("enter the String to caluclate Length :"))


# def Len(x):
#     c=0
#     for i in str1:
#         c+=1
#     return c
# res=Len(str1)
# print("Lenth of Given String" ,res)


#using inbulit Function len()
# str1 =input(str("enter the String to caluclate Length :"))
# res=len(str1)
# print(res)

#using Lambada function :
import functools
str1 =input(str("enter the String to caluclate Length : \n"))

def Len(str1):
    return functools.reduce(lambda x,y: x+1, str1, 0)

#Driver code 
res=Len(str1)
print(res)






