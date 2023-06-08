def checksum(s):
    c=0
    for i in range(len(s)):
        c += ord(s[i])
    return c
def cmp(s1, s2):
    if len(s1) != len(s2):
        return False
    elif checksum(s1) != checksum(s2):
        return False
    else:
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True
f1=open("life.txt","r")
life=f1.read().split()
f2=open("wiki.txt","r")
wiki=f2.read().split()
pl=0
pc=0
c=0
check=[False ]* len(life)
for i in range(len(life)):
    c+=len(life[i])
for i in range(len(life)-2):
    for j in range(len(wiki)-2):
        if cmp(life[i], wiki[j]):
            if cmp(life[i+1], wiki[j+1]):
                if cmp(life[i+2], wiki[j+2]):
                    print("Найдено сходство: ", life[i], life[i+1], life[i+2])
                    pl+=1
                    for k in range(3):
                        if check[i+k] == False:
                            pc += len(life[i+k])
                            check[i+k]=True
                    break
print("Найдено сходств: ", pl)
print("Процент плагиата: ", pc /c*100 )