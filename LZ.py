def encodeLZ(fileIn, fileOut):
    file1 = open(fileIn,"r")
    txt = file1.read()
    file1.close()
    list_of_lz = []
    list_of_lz.append("")
    slist = list(txt)
    lztxt = slist.pop(0)
    list_of_lz.append(lztxt)
    while len(slist) > 0:
        slistcopy = slist.copy()
        while len(slistcopy) > 0:
            flag = 0
            str1 = ""
            for i in slistcopy:
                str1 +=i
            for elem in list_of_lz:
                if str1 == str(elem):
                    element = ""
                    k = len(str1)
                    lztxt = lztxt + str(list_of_lz.index(elem))
                    for i in range(0, k):
                        slist.pop(0)
                    if len(slist)>0:
                        element = slist[0]
                        slist.pop(0)
                    lztxt += element
                    list_of_lz.append((str1 + element))
                    flag = 1
                    break
            if flag == 1:
                break
            if (len(str1) == 1) and (str1 != lztxt[0]):
                list_of_lz.append(str1)
                slist.pop(0)
                lztxt = lztxt + str1
                break
            slistcopy.pop()
    fileend = open(fileOut,"w")
    fileend.write(lztxt)
    fileend.close()
def decodeLZ(fileIn, fileOut):
    f1 = open(fileIn, "r")
    txtlz = f1.read()
    f1.close()
    lzlist = []
    txt = txtlz[0]
    lzlist.append(0)
    lzlist.append(txtlz[0])
    s = 1
    while s+1 < len(txtlz):
        k = ""
        if txtlz[s].isdecimal():
            while txtlz[s].isdecimal():
                k = k + str(txtlz[s])
                s += 1
                if s+1 > len(txtlz):
                    break
            abc = ""
            txt += str(lzlist[int(k)])
            abc = str(lzlist[int(k)])
            if len(txtlz) > s:
                abc +=txtlz[s]
                txt += txtlz[s]
                lzlist.append(abc)
        else:
            txt += txtlz[s]
            flag = 0
            for elem in lzlist:
                if elem == txtlz[s]:
                    flag = 1
                    break
            if flag == 0:
                lzlist.append(txtlz[s])
        s+=1
    f2 = open(fileOut,"w")
    f2.write(txt)
    f2.close()

    encodeLZ("Textforcomp.txt", "fileLz77.txt")
    decodeLZ("fileLz77.txt", "fileLz77DEC.txt")