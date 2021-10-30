import math

def sub(rot):
    print("Enter Plain Text:", end=' ')
    s=input()
    
    shift=13
    if not rot:
        print("Enter Shift:", end=' ')
        shift=int(input())
    encrypted=""
    for i in s:
        if i!=' ':
            encrypted+=chr(((ord(i)-65+shift)%26)+65)
        else:
            encrypted+=' '
    print("Encrypted String:",encrypted)
    decrypted=""
    for i in encrypted:
        if i!=' ':
            decrypted+=chr(((ord(i)-shift-65)%26)+65)
        else:
            decrypted+=' '
    print("Decrypted String:",decrypted)
    print()

def vernam():
    print("Enter Plain Text:", end=' ')
    s=input()
    print("Enter Key:", end=' ')
    key=input()
    if len(s)==len(key):
        encrypted=""
        for i in range(len(s)):
            if s[i]!=' ':
                encrypted+=chr((ord(s[i])+ord(key[i])-130)%26 +65)
            else:
                encrypted+=' '
        print("Encrypted String:",encrypted)
        decrypted=""
        for i in range(len(s)):
            if encrypted[i]!=' ':
                decrypted+=chr((ord(encrypted[i])-ord(key[i])-130)%26 +65)
            else:
                decrypted+=' '
        print("Decrypted String:",decrypted)
        print()

    else:
        print("Plain Text Length and Key Length do not match")
        print()




def double_transposition():
    print("Enter Plain Text:", end=' ')
    s=input()
    print("Enter 1st Key:", end=' ')
    key=input()
    print("Enter 2nd Key:", end=' ')
    key2=input()
    # print(len(key),len(key2),len(s))
    if len(key2)!=math.ceil(len(s)/len(key)):
        print("Dimensions of the keys and the plain text do not match. Please try again")
        print()
        return None

    table=[]
    for i in range(len(key)):
        temp=list(s[i:len(s):len(key)])
        # print(temp)
        table.append(temp)
    for i in range(len(key)):
        if len(table[i])!=len(key):
            t1=len(table[i])
            for _ in range(len(key2)-t1):
                table[i].append('x')
    order=[]
    for i in range(len(key)):
        order.append([key[i],i])
    order=sorted(order, key = lambda x: x[0])
    for i in range(len(order)):
        order[i].append(i)

    
    
    # print(table)
    

    order2=[]
    for i in range(len(key2)):
        order2.append([key2[i],i])
    order2=sorted(order2, key = lambda x: x[0])
    for i in range(len(order2)):
        order2[i].append(i)
    # print(order2)
    #Shuffle Rows
    order2=sorted(order2, key = lambda x: x[1])
    for i in range(len(key)):
        temp=[]
        for j in range(len(key2)):
            temp.append([ table[i][j],order2[j][2] ])
        temp=sorted(temp, key = lambda x: x[1])
        table[i]=[]
        for j in temp:
            table[i].append(j[0])
    order2=sorted(order2, key = lambda x: x[0])

    # print(table)

    #Shuffle Columns
    final=[]
    for i in order:
        final.append(table[i[1]])

    # print(order)
    # print(final)

    
    encrypted=""
    for i in range(len(key2)):
        for j in final:
            encrypted+=j[i]
    print("Encrypted String:",encrypted)

    
    decrypt_table=[]
    for i in range(len(key)):
        decrypt_table.append([])
        for j in range(i,len(encrypted),len(key)):
            decrypt_table[-1].append(encrypted[j])
    # print(decrypt_table)

    #Unshuffle column
    decrypt_final=[]
    order=sorted(order, key = lambda x: x[1])
    for i in order:
        decrypt_final.append(decrypt_table[i[2]])

    #Unshuffle Rows
    for i in range(len(key)):
        temp=[]
        for j in range(len(key2)):
            temp.append([ decrypt_final[i][j],order2[j][1] ])
        temp=sorted(temp, key = lambda x: x[1])
        decrypt_final[i]=[]
        for j in temp:
            decrypt_final[i].append(j[0])
    
    # print(decrypt_final)

    decrypted=""
    for i in range(len(key2)):
        for j in decrypt_final:
            decrypted+=j[i]
    print("Decrypted String:",decrypted)
    print()



def transposition():
    print("Enter Plain Text:", end=' ')
    s=input()
    print("Enter Key:", end=' ')
    key=input()

    if len(key)>len(s):
        print("Dimensions of the key and the plain text do not match. Please try again")
        print()
        return None

    table=[]
    for i in range(len(key)):
        temp=list(s[i:len(s):len(key)])
        # print(temp)
        table.append(temp)
    order=[]
    for i in range(len(key)):
        order.append([key[i],i])
    order=sorted(order, key = lambda x: x[0])
    # print(table)
    encrypted=""
    for i in order:
        for j in range(math.ceil(len(s)/len(key))):
            if j<len(table[i[1]]):    
                encrypted+=table[i[1]][j]
            else:
                encrypted+='x'
    print("Encrypted String:",encrypted)
    
    decrypt_table=[]
    k=0
    for i in range(len(encrypted)//len(key)):
        decrypt_table.append([])
        for j in range(i,len(encrypted),len(encrypted)//len(key)):
            decrypt_table[-1].append(encrypted[j])
    # print(decrypt_table)
    for i in range(len(order)):
        order[i].append(i)
    order=sorted(order, key = lambda x: x[1])
    # print(order)
    decrypted=""
    for i in decrypt_table:
        for j in order:
            decrypted+=i[j[2]]
    print("Decrypted String:",decrypted)
    print()


choice=1
while choice!=0:
    print("Please Enter your choice for an Encryption algorithm\n1: Substitution Cipher\n2: ROT 13\n3: Vernam Cipher\n4: Transposition\n5: Double Transposition\n0: To Exit")
    choice=int(input())
    if choice==1:
        sub(False)
    if choice==2:
        sub(True)
    if choice==3:
        vernam()
    if choice==4:
        transposition()
    if choice==5:
        double_transposition()