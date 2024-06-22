s = "abcabcc"
count=0

for i in range(len(s)):
    if i < len(s) - 1 and s[i] != s[i+1]:
        count=count+1
        i=i+1
        
    
print(count)