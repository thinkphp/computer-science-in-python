def fn():
    str2 = input()
    #ABCBA
    freq = [ 0 ] * 26
    for c in str2:
        freq[(ord(c)-ord('A'))]+=1
    check = 0
    ans = []
    for i in range(26):
        check+=(freq[i]%2)
    if check > 1:
        print("NO SOLUTION")
    else:
        for i in range(26):
            if freq[i] == 0:
                continue
            else:
                if freq[i]%2 == 0:
                    for j in range(freq[i]//2):
                        ans.append(chr(i+ord('A')))

        for i in range(26):
            if freq[i] == 0:
               continue
            else:
               if freq[i]&1:
                  for j in range(freq[i]):
                      ans.append(chr(i+ord('A')))

        for i in range(25,-1,-1):
            if freq[i] == 0:
                continue
            else:
                if freq[i]%2 == 0:
                    for j in range(freq[i]//2):
                        ans.append(chr(i+ord('A')))
        for c in ans:
            print(c,end="")
fn()
