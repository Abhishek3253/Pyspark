# using collections.Counter() to get 
# from collections import Counter
# str1 =input(str("enter the String to caluclate Length : \n"))
# # using collections.Counter() to get 
# # count of each element in string 
# res = Counter(str1)

# print(str(res))

#using Dictionary Method 

str1 =input(str("enter the String to caluclate Length : \n"))
count = {}
def char_count(str1):
    for n in str1:
        keys = count.keys()
        if n in keys:
            count[n] += 1
        else:
            count[n] = 1
    return count

res=char_count(str1)
print (str(res))


