with open("snooker.txt", 'r', encoding='latin2') as f:
    lista = list()
    fejlec = f.readline()
    for sor in f:
        lista.append(sor.strip().split(";"))




#3. feladat
print( f'3. feladat: A világranglistán {len(lista)} versenyző szerepel')




#4. feladat
öb = sum ( [ int(sor[3]) for sor in lista ] )
öv = len(lista)

átlag = öb / öv

print( f'4. feladat: a versenyzők átlagosan {átlag:.2f} fontot kerestek')

#5. feladat

számláló = 0
for orszag, in lista:
    if orszag == "Kína":
        számláló += 1
        
#print( f'5. feladat: A legjobban kereső {} versenyző:')