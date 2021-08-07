import sys
import unicodedata
#creating dictionairies globals
enAlphabet = "abcdefghijklmnopqrstuvwxyz"

letToNumber= dict(zip(enAlphabet, range(len(enAlphabet))))

numberToLetter = {v:k for k, v in letToNumber.items()}

def chooseLanguage():
    print("Portugues(1) English(2)")
    lang = input()
    return lang

def escolhaModo():
    print("Escolha: Encriptar(1) Decriptar(2)")
    choice = input()
    return choice

def chooseMode():
    print("Please Choose: Encrypt(1) Decrypt(2)")
    choice = input()
    return choice

def closethis():
    print("option doesn't exist / opçao nao encontrada")
    sys.exit(0)

def changeLetter(fraglist, key):
    result=''
    for element in fraglist:
        keyPos= 0
        for letter in element:
            #find the number of actual letter
            myLetterNumber = letToNumber[letter]
            #find number of keyword letter
            keyNumber = letToNumber[key[keyPos]]
            newletterByNumber = (myLetterNumber + keyNumber) %(26)
     
            letterEncrypted = numberToLetter[newletterByNumber]
            result+= letterEncrypted
            keyPos+=1
    
    return result
pass

def changeback(fraglist, key):
    result=''
    for element in fraglist:
        keyPos= 0
        for letter in element:
            #find the number of actual letter
            myLetterNumber = letToNumber[letter]
            #find number of keyword letter
            keyNumber = letToNumber[key[keyPos]]
            newletterByNumber = (myLetterNumber - keyNumber) %(26)
     
            letterEncrypted = numberToLetter[newletterByNumber]
            result+= letterEncrypted
            keyPos+=1
    return result

def removeSpecialChar(message):
    m2= unicodedata.normalize("NFD", message)
    m2 = m2.encode("ascii","ignore")
    m2= m2.decode("utf-8")
    return m2

def encrypt(message, key):
    print("encript")
    endMessage= len(message)
    sizeKey = len(key)
    fragList=[]
    #quebra a minha mensagem no tamanho da key
    for f in range(0, endMessage, sizeKey):
        fragList.append(message[f:f + sizeKey])
    result= changeLetter(fragList, key)
    return result

def decrypt(text, key):
    print("decript")
    endMessage= len(text)
    sizeKey = len(key)
    fragList=[]
    #quebra a minha mensagem no tamanho da key
    for f in range(0, endMessage, sizeKey):
        fragList.append(text[f:f + sizeKey])
    message = changeback(fragList, key)
    print("Sua mensagem decripada é:")
    print("\n"+ message)

def enContinue(choice):
    if(choice=="1"):
        print("Escreva a mensagem a ser cifrada no arquivo messageEnglish\n Agora, escreva no terminal sua chave:")
        key= input()

        f = open("messageEnglish.txt",'r', encoding='utf-8')
        text= f.read()
        f.close()
        lowertext = removeSpecialChar(text).lower()

        message=''
        #remove graphic signs and spaces
        for char in lowertext:
            if char in enAlphabet:
                message+=char
            
        finalMessage = encrypt(message, key)
        print("sua mensagem encriptada é: ")
        print(finalMessage)
    elif(choice=="2"):
        print("Escreva a mensagem a ser decifrada no arquivo cypher.txt \n Escreva no terminal a chave para decifrar:")
        key= input()

        f = open("cypher.txt",'r', encoding='utf-8')
        text= f.read()
        f.close()
        decrypt(text, key)
    else:
        closethis()


#Main:    
print("Ola, esse é o programa cifrador/decifrador\n")
choice = escolhaModo()
print(choice)
enContinue(choice)

#language = chooseLanguage()
#print(language)



# if(language == 1):
#     escolhaModo()

# elif(language==2):

#     choice= chooseMode()
#     enContinue(choice)

# else:
#     closethis()



#for english

#for port
    #for port it is important to clear the message from graphic signals
