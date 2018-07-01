litery = ["a","ą","b","c","ć","d","e","ę","f","g","h","i","j","k","l","ł","m","n","ń","o","ó","p","r","s","ś","t","u","w","y","z","ż","ź","A","Ą","B","C","Ć","D","E","Ę","F","G","H","I","J","K","L","Ł","M","N","Ń","O","Ó","P","R","S","Ś","T","U","W","Y","Z","Ż","Ź"," ",".","!","?"]

while(True):
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

    if(input("Czy zakończyć? Napisz 'tak', aby zakończyć lub cokolwiek innego, aby kontynuować. ")=="tak"):
        break
    
