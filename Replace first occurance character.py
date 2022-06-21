str1 =input(str("enter the input String  : \n"))

def Replace(str1):
    char=str1[0]
    
  
    str1=str1.replace(char,'@')
    return str1
res=(Replace(str1))
print(res)
