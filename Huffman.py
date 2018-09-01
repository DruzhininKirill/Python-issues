def make_tree(text):
    se = set(text)
    ls = [(text.count(ch), ch) for ch in se]
    ls.sort()
    print("fvr= ",ls)
    while len(ls) >= 2:
        d = (ls[0][0] + ls [1][0], (ls[0][1], ls[1][1]))
        print(d)
        if ls[-1][0]<d[0]:
            ls.append(d)
        else:
            for num in range(2,len(ls)):
                if ls[num][0]>=d[0]:
                    break
            ls.insert(num,d)
        ls.pop(0)
        ls.pop(0)
    return ls[0][1]
def fn_cod (st,el):
    global ls_haf
    if type(el) == str:
        ls_haf.append( (el,st) )
        return
    fn_cod(st+"0", el[0])
    fn_cod(st + "1", el[1])
    return
def make_dict(text):
    global ls_haf
    ls = make_tree(text)
    ls_haf=[]
    fn_cod("",ls)
    dc_haf = dict(ls_haf)
    return dc_haf
def compress(text,dc_haf):
    st_res=""
    for ch in text:
        st_res=st_res+dc_haf[ch]
    return st_res
def decompress(text,dc_haf):
    dc_decod = {dc_haf[key]:key for key in dc_haf}
    st_res=""
    while len(text)>0:
        num=1
        while text[:num] not in dc_decod:
            num= num+1
        st_res+= dc_decod[text[:num]]
        text = text[num:]
    return st_res


# text = input("text")
# dc_haf = make_dict(text)
# print(dc_haf)
# compressed_text = compress(text,dc_haf)
# dc = decompress(compressed_text,dc_haf)
# print(compressed_text)
# print(dc)


def huffman_encode(fileIn):
    global a
    global koef
    fileIn = open(fileIn)
    text = fileIn.read()
    dc_haf = make_dict (text)
    a = dc_haf
    koef = len(str(a))
    compressed_text = compress (text, dc_haf)
    fileHuf = open ("fileHuf.txt", "w")
    for s in compressed_text:
        fileHuf.write (s)
    return fileHuf

def huffman_decode(fileIn):
    fileIn = open (fileIn)
    text = fileIn.read()
    dc = decompress (text, a)
    fileHufDEC = open ("fileHufDEC.txt", "w")
    for s in dc:
        fileHufDEC.write (s)
    return fileHufDEC



huffman_encode("Textforcomp.txt")
huffman_decode("fileHuf.txt")