Par=[(10,2,31),(7,50,60),(60,50,9)]

maxim=0
Par=sorted(Par)
for i in range (0,len(Par)):
    Par[i]=sorted(Par[i])
print(Par)
for dimensiuni in Par:
    if(min(dimensiuni[0],dimensiuni[1],dimensiuni[2])>maxim):
        maxim=min(dimensiuni[0],dimensiuni[1],dimensiuni[2])

dict ={}

for dimensiuni in Par:
    a=(dimensiuni[0],dimensiuni[1])
    if(a in dict):
        if(min(a[1],a[0],dict[a]+dimensiuni[2])>maxim):
            maxim=min(a[1],a[2],dict[a]+dimensiuni[2])
        if(dict[a]<dimensiuni[2]):
            dict[a]=dimensiuni[2]
    else:
        dict[a]=dimensiuni[2]
    b=(dimensiuni[1],dimensiuni[2])
    if (b in dict):
        if (min(b[1], b[0], dict[b] + dimensiuni[0]) > maxim):
            maxim = min(b[1], b[0], dict[b] + dimensiuni[0])
        if (dict[b] < dimensiuni[0]):
            dict[b] = dimensiuni[0]
    else:
        dict[b] = dimensiuni[0]
    c=(dimensiuni[0],dimensiuni[2])
    if (c in dict):
        if (min(c[1], c[0], dict[c] + dimensiuni[1]) > maxim):
            maxim = min(c[1], c[0], dict[c] + dimensiuni[1])
        if (dict[c] < dimensiuni[1]):
            dict[c] = dimensiuni[1]
    else:
        dict[c] = dimensiuni[1]
print(dict)
print(maxim)