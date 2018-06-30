litery = ["a","ą","b","c","ć","d","e","ę","f","g","h","i","j","k","l","ł","m","n","o","ó","p","r","s","ś","t","u","w","y","z","ż","ź"," ",".","!","?"]

wej=input("Podaj wiadomosc: ")
klucz=int(input("Podaj klucz (Wartość dodatnia jeśli szyfrujemy lub ujemna jeśli odszyfrowywujemy): "))
wyj=""

for l in range(len(wej)):
    if(wej[l] in litery):
        lkl=klucz
        while(lkl>len(litery)):
            lkl=lkl-len(litery)

        war=litery.index(wej[l])+lkl

        while war>len(litery):
            war=war-len(litery)
        wyj=wyj+litery[war]
    else:
        wyj=wyj+wej[l]

print(wyj)
input("")
