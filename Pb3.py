import math
f = open('intrare.txt', 'r')
f_string = f.read()
f_words = {}
g_words = {}
for word in f_string.split():
     if word !="," and word !=" " and word !=".":
        if word in f_words:
            f_words[word]+=1
        else:
            f_words[word]=1
        if word not in g_words:
            g_words[word]=0
g = open('fisier2.txt', 'r')
g_string = g.read()
for word in g_string.split():
     if word !="," and word !=" " and word !=".":
        if word in g_words:
            g_words[word]+=1
        else:
            g_words[word]=1
        if word not in f_words:
            f_words[word]=0
print(f_words)
print(g_words)
suma2 = sumaF = sumaG = 0
for word in f_words:
    suma2 += f_words[word]*g_words[word]
    sumaF += f_words[word]*f_words[word]
    sumaG += g_words[word]*g_words[word]
dcos = suma2/(math.sqrt(sumaF)*math.sqrt(sumaG))
print(format(dcos, ".4f"))
f.close()
g.close()
