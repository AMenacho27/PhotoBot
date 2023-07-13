import os

aviso = ["305554160","305554162","305554163"]
path = "D:\FOTOBOT"

dirs = os.listdir( path )
photos = []

for file in dirs:
   photos.append(file)
else:
    print("Fin del proceso 1")


contador = 0 
photo2 = []



for x in range (len(aviso)):
    os.mkdir(f'D:\FOTOBOT\{aviso[x]}')
    for k in range (len(photos)):
        if (photos[x+k].__contains__(f'{aviso[x]}')):
            photo2.append(photos[x+k])
            contador +=1
            
    for j in photo2:
        print(x)
        old_file = f'D:\FOTOBOT\{j}'
        new_file = f'D:\FOTOBOT\{aviso[x]}\{j}'
        print(new_file)
        os.rename(old_file, new_file)
        
print(f"\nLa cantidad de foto del aviso es: {contador}")