def printUppercaseLetters(str):
    strarr= [x for x in str]
    a = []
    for cap in strarr:
        if(cap.isupper()):
             a.append(cap)
    indCaps=[]
    for i in a:
       indCaps.append(index(i))
    indCaps.sort();
    print(indCaps)

printUppercaseLetters("AbCdEGF")