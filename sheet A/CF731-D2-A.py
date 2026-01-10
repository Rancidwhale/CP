import string
a = list(string.ascii_lowercase)
b = list(string.ascii_lowercase)[::-1]

s = input()
p='a'
rot=0
for i in s:
    rot += min( ( abs( ord(p) - ord(i) ) ) ,( abs( ord('z') - ord(p) ) +1+ abs( ord('a') - ord(i) ) ) , (abs( ord('a') - ord(p))+1+abs( ord('z') - ord(i) )))
    p = i
    
print(rot)
    