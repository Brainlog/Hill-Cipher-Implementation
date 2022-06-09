import math as mh

from rx import for_in
print("Enter the length of key : ")
n = int(input())
L = [[0 for j in range(0, n)] for i in range(0, n)]  # key
print(L)
print(type([2, "gg"]))
for i in range(0, n):
    for j in range(0, n):
        L[i][j] = int(input())
print("This is the key", L)
print("Enter the text for encrypting : ")
text = input()
maincipher = [0 for i in range(0, len(text))]
print(text)
print("maincipher",maincipher)
itr = 0
print(len(text))
while(itr < len(text)):
    
    play = [0 for i in range(0, n)]
    chk = 0
    for p in range(itr,itr+n):
        if (p < len(text)):
            # print(text[p])
            # print(p,chk)
            play[chk] = ord(list(text)[p])-96
            # print(play[chk])
            chk += 1
           
        else:
            play[chk] = 0
            # print(play[chk])
            chk += 1    
    cipher = [0 for i in range(0, n)]
    for j in range(0, n):
        for z in range(0, n):
            cipher[j] = play[z]*L[z][j]
            cipher[j] = cipher[j]%26
    chk = 0        
    for j in range(itr,itr+n):
        if (j < len(text)):
            # print(cipher[chk])
            maincipher[j] = chr(cipher[chk]+96)  
            chk += 1  
        else:
            maincipher.append(chr(cipher[chk] + 96))      
    itr += n  
print(maincipher)  
s = ""
print(s.join(maincipher))       


