lines = []
while True:
    line = input()
    if line != 'STOP':
        lines.append( line)
    else:
        break
s = '\n'.join(lines)
s = s.split('>')[1:]
s = [ i.split('\n',1)[1].replace('\n','') for i in s]
seq1 = s[0]
seq2 = s[1]
a = [[0 for i in range(len(seq2)+1)] for j in range(len(seq1)+1)]
b = [[0 for i in range(len(seq2)+1)] for j in range(len(seq1)+1)]
for r in range (len(a)):
    for c in range (len(a[r])):
        a[0][0] = 0
        b[0][0] = "n"
        if r == 0 :
            a[r][c] = a[r ][c-1] + 1
            b[r][c] = 'l'
        elif c == 0:
            a[r][c] = a[r-1][c] + 1
            b[r][c] = 'u'
        else:
            if seq1[r-1] == seq2[c-1]:
                a[r][c] = a[r - 1][c - 1]
                b[r][c] = 'o'
            else:
                a[r][c] = min(a[r - 1][c], a[r][c - 1], a[r - 1][c - 1])+1
                if a[r][c] == a[r][c - 1] + 1:
                    b[r][c] = "l"
                elif a[r][c] == a[r - 1][c] + 1:
                    b[r][c] = "u"
                elif a[r][c] == a[r - 1][c - 1] + 1:
                    b[r][c] = "o"
h = len(seq1)
v = len(seq2)
alignseq1 = ""
alignseq2 = ""
while(v >= 0 and h >= 0):
        if b[h][v] == "l":
            alignseq1 += "-"
            alignseq2 += seq2[v - 1]
            v = v-1
        elif b[h][v] == "o":
            alignseq1 += seq1[h-1]
            alignseq2 += seq2[v-1]
            h = h-1
            v = v-1
        elif b[h][v] == "u":
            alignseq1 += seq1[h-1]
            alignseq2 += "-"
            h = h-1
        elif b[h][v] == "n":
            break
print(a[len(seq1)][len(seq2)])
print(alignseq1[::-1])
print(alignseq2[::-1])
