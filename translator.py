#in a new language all vowels became g
#vowels -> g

#dog -> dgg
#cat -> cgt

def translate(word):
    trans=""
    for i in word:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            trans+='g'
        elif i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
            trans+='G'
        else:
            trans+=i
    return trans

word=input("Enter a word: ")
print("Translated word is: "+translate(word))
