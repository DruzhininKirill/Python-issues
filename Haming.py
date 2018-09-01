class Hamming_Encoder:
    def __init__(self, dataBits):
        self.dataBits = dataBits
        ure = dataBits+1
        i = 0
        while pow(2,i) < i + ure:
            i +=1
        self.controlBits = i
    def display(self):
        print(self.dataBits, self.controlBits)
    def encode(self,line1):
        sb = Hamming_Encoder(len(line1))
        n=0
        line2 = list(line1)
        for i in range (1, sb.controlBits+1):
            line2.insert(pow(n,2),"0")
            n+=1
        line = "".join(line2)
        print("Input: ", line)


        lines = []
        for i in range(1, sb.controlBits+1, 1):
            liner = ""
            # while len(liner)< (sb.controlBits+sb.dataBits):
            for j in range(1, len(line)+1, 1):
                if j != pow(2,i-1):
                    liner = liner+"0"
                else:
                    flag = 0
                    while len(liner)< (sb.controlBits+sb.dataBits):
                        if flag % 2 == 0:
                            for num in range (0,pow(2,i-1),1):
                                liner = liner + "1"
                            flag = 3
                        else:
                            for num in range (0,pow(2,i-1),1):
                                liner = liner + "0"
                            flag = 0
                    break
            liner = liner[0:sb.controlBits+sb.dataBits]
            lines.append(liner)
        # print("lines = ", lines)
        r_list = []
        for i in range(0,sb.controlBits):
            sum = 0
            for j in range (0,len(line)):
                sum = sum +int(line[j])*int(lines[i][j])
            r = sum % 2
            r_list.append(r)
        # print(r_list)
        # print(line1)
        n=0
        result = list(line1)
        for i in range (0, sb.controlBits):
            result.insert(pow(2,n),str(r_list[i]))
            n+=1
        result = "".join(result)
        print("Haming code ", result)

    def decoder(self, line1):
        sb = Hamming_Encoder (len (line1))
        line = line1
        print ("Input for dec: ", line)
        lines = []
        for i in range (1, sb.controlBits + 1, 1):
            liner = ""
            for j in range (1, len (line) + 1, 1):
                if j != pow (2, i - 1):
                    liner = liner + "0"
                else:
                    flag = 0
                    while len (liner) < (sb.controlBits + sb.dataBits):
                        if flag % 2 == 0:
                            for num in range (0, pow (2, i - 1), 1):
                                liner = liner + "1"
                            flag = 3
                        else:
                            for num in range (0, pow (2, i - 1), 1):
                                liner = liner + "0"
                            flag = 0
                    break
            liner = liner[0:sb.controlBits + sb.dataBits]
            lines.append (liner)
        # print ("lines = ", lines)
        r_list = []
        for i in range (0, sb.controlBits):
            sum = 0
            for j in range (0, len (line)):
                sum = sum + int (line[j]) * int (lines[i][j])
            r = sum % 2
            r_list.append (r)

        # print (r_list)
        n=0
        mistake = 0
        for i in r_list:
            mistake = mistake + int(i)* pow(2,n)
            n+=1
        print("mistake position: ", mistake)


h1 = Hamming_Encoder(9)
# h1.display()
h1. encode("100100101110001")
h1. decoder("11110110001011110001")
