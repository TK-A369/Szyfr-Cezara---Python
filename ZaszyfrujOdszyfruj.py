litery = ["a","ą","b","c","ć","d","e","ę","f","g","h","i","j","k","l","ł","m","n","o","ó","p","r","s","ś","t","u","w","y","z","ż","ź"," ",".","!","?"]

wej=input("Podaj wiadomosc: ")
klucz=int(input("Podaj klucz (Wartość dodatnia jeśli szyfrujemy lub ujemna jeśli odszyfrowywujemy): "))
wyj=""

for l in range(len(wej)):
    if(wej[l] in litery):
        lkl=klucz
        while(lkl>len(litery)):
            lkl=lkl-len(litery)
        
        wyj=wyj+litery[litery.index(wej[l])+lkl]
    else:
        wyj=wyj+wej[l]

print(wyj)
