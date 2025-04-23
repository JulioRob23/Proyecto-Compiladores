import re 

regexreservadas = r'Charmander|Totodile|Wooper|Pikachu|Corviknight|Ratata|Paras|Clefable|Tentacool|Seel|Dragonite|Necrozma|Mewtwo'
regexID = r'[a-zA-Z][A-Za-z0-9]*'
regexINT = r'[0-9]+'
regexFLOAT = r'[0-9]+\.[0-9]{0,4}'
regexBOOL = r'0|1'
regexSTRING = r'\"[A-Za-z0-9\!\¡\?\¿\@\#\$\s]+\"'
regexCOND = r'\=|(\!\=)|(\<)|(\>)|(\<\=)|(\=\>)'
regexOPENP = r'\('
regexCLOSEP = r'\)'
regexC = r'\,'
regexOP = r'\+|\-|\*|\/'

def GetTokens(line): 
    global tokens, tokensplain 
    TokensWF = line.split(" ")
    for token in TokensWF:
        if token == '':
            continue
        if token[0] == '"':
            i = 1
            temp = ""
            count = 0
            while i == 1:
                count += 1
                if count == 1: 
                    temp = token
                token += f" {TokensWF[TokensWF.index(temp) + count]}"
                if token[-1] == '"': 
                    i = 0
            for indx in range(TokensWF.index(temp),TokensWF.index(temp)+count+1):
                TokensWF[indx] = ""
        if re.match(regexreservadas, token): 
            tokens.append("KEY WORD")
            tokensplain.append(token)
            continue
        if re.match(regexID,token): 
            tokens.append("ID")
            tokensplain.append(token)
            continue
        if re.match(regexINT,token): 
            tokens.append("INT")
            tokensplain.append(token)
            continue
        if re.match(regexFLOAT,token): 
            tokens.append("FLOAT")
            tokensplain.append(token)
            continue
        if re.match(regexBOOL,token): 
            tokens.append("BOOL")
            tokensplain.append(token)
            continue
        if re.match(regexSTRING,token): 
            tokens.append("STRING")
            tokensplain.append(token)
            continue
        if re.match(regexCOND,token): 
            tokens.append("COND")
            tokensplain.append(token)
            continue
        if re.match(regexOPENP,token): 
            tokens.append("OPEN P")
            tokensplain.append(token)
            continue
        if re.match(regexCLOSEP,token): 
            tokens.append("CLOSE P")
            tokensplain.append(token)
            continue
        if re.match(regexC,token): 
            tokens.append("COMMA")
            tokensplain.append(token)
            continue
        if re.match(regexOP,token): 
            tokens.append("OPERATOR")
            tokensplain.append(token)
            continue
  
tokensplain = []
tokens = []
file = open("prueba5.txt","r")
text = file.readlines()
for line in text: 
    if line == "" or line == "\n":
        continue
    GetTokens(line)
for i in range(len(tokens)):
    print(f"{tokens[i]} : {tokensplain[i]}")