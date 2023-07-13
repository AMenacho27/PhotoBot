# Importar la libreria os
import os

# Funcion encargada de agrupar las fotos por TX
def agruparFotos():
    #tx = input("Ingrese el TX: ")
    try:
        # Listado de los tx, usualmente hay que copiar y pegar el resultado al llamar la funcion obtenerNombre() ya que se genera un espacio.
        tx = ['40966005', '40965017', '40965000', '40969020', '40965088', '40965025', '40965033', '40965015']
        # Ruta donde se encuentra las fotos descargadas
        path = "Z:/Ing. Kevin/Prueba"
        # Variable para contar cuantas fotos tiene cada TX (Por el momento se puede omitir)
        contador = 0
        # Variable temporal para almacenar las fotos de cada tx, esta variable vacia su contenido al terminar con todas las fotos de un TX
        tx_temp = []
        
        # Variable que almacena los archivos que hay en la ruta almacenada en la variable path
        dirs = os.listdir( path )
        
        # Ciclo repetitivo para iterar la lista tx 
        for x in range(len(tx)):
            # Funcion para crear una carpeta de cada tx 
            os.mkdir(f'Z:/Ing. Kevin/Prueba/{tx[x]}')
            for y in range(len(dirs)):
                if(dirs[y].__contains__(f"{tx[x]}")):
                    tx_temp.append(dirs[y])
                    contador +=1
                                        
            for z in range(len(tx_temp)):
                old_file = f'Z:/Ing. Kevin/Prueba/{tx_temp[z]}'
                new_file = f'Z:/Ing. Kevin/Prueba/{tx[x]}/{tx_temp[z]}'
                os.rename(old_file, new_file)
                    #for z in range(len(tx_temp)):
                        #old_file = f'Z:/Ing. Kevin/Prueba/{tx_temp[z]}'
                        #new_file = f'Z:/Ing. Kevin/Prueba/{tx[x]}/{tx_temp[z]}'
                        #os.rename(old_file, new_file)
            print(f"fotos del tx {tx[x]}, cantidad: {len(tx_temp)}")
            print(tx_temp)
            print("-"*90)
            tx_temp.clear()
    except:
        pass
        #print("Las carpetas ya se encuentran creadas \nEliminelas manualmente")
                
    #for x in range (len(photos)):
        #if (photos[x].__contains__(f'{tx}')):
            #photo2.append(photos[x])
            #contador +=1
                    
    #else:
        #print("Fin del proceso 2")

    #for x in photo2:
        #print(x)
        
        #new_file = f'"Z:/Ing. Kevin/Prueba"/{tx}/{x}'
        #old_file = f'"Z:/Ing. Kevin/Prueba"/{x}'
        
        #print(new_file)
        #os.rename(old_file, new_file)
        
    #print(f"\nLa cantidad de foto del aviso es: {contador}")
    print(dirs)

def obtenerNombre():
    tx = []
    file = open("TX.txt", 'w')
    path = "Z:/Ing. Kevin/Prueba"
    dirs = os.listdir( path )
    #print(dirs)
    for x in dirs:
        temp3 = x.replace("_","-")
        temp = temp3.split('-')
        for x in temp:
            if x.startswith("TX"):
                temp2 = x.replace("TX","")      
                tx.append(temp2)
                #file.write(f"{temp2}\n")
    tx2 = set(tx)
    lista_tx = list(tx2)
    for x in tx2:
        file.write(f"{x}\n")
    print(lista_tx)    
    #agruparFotos(lista_tx)

def obtenerGis():
    gis = []
    file = open("GIS.txt", 'w')
    path = "Z:/Ing. Kevin/Prueba/"
    dirs = os.listdir(path)
    gis_temp = []
    #print(dirs)

    for x in dirs:
        path = f"Z:/Ing. Kevin/Prueba/{x}"
        temp = os.listdir(path)
        for y in temp:
            temp4 = y.replace("_","-")
            temp = temp4.split('-')
            for z in temp:
                if z.startswith("GIS"):
                    temp5 = z.replace("GIS","")
                    gis.append(temp5)
        print(f"La cantidad de Gis en el tx{x} es: {len(set(gis))}")
        print(f"Listado de Gis del tx {x}: {list(set(gis))}")
        
        file.write(f"Gis del tx{x}:\n {list(set(gis))}\n")
        #agruparFotosGis(list(set(gis)))
        gis.clear()
        
    gis2 = set(gis)
    lista_gis = list(gis2)
    for x in gis2:
        file.write(f"{x}\n")
    print(lista_gis)
    print(f"La cantidad total de GIS es {len(lista_gis)}")
    #print(f"El TX {x} tiene {len(temp)} fotos")
    #print(os.listdir(path))
    print("-"*150)
        
def agruparFotosGis():
    gis_temp = []
    gis_temp3 = []
    gis_temp2 = []
    path = "Z:/Ing. Kevin/Prueba"
    dirs = os.listdir(path)
    dirs.remove('Thumbs.db')
    for x in dirs:
        path = f"Z:/Ing. Kevin/Prueba/{x}"
        dirs2 = os.listdir(path)
        # Para imprimir conteo de archivos en carpeta
        #print("-"*150)
        #print(f"Fotos del TX {x}: cantidad {len(dirs2)} fotos")

        #print(dirs2)
        for y in dirs2:
            temp3 = y.replace("GIS-","GIS")
            temp = temp3.split('-')
            #print(temp)
            #gis_temp2.clear()
            for z in temp:
                if z.startswith("GIS"):
                    temp2 = z.replace("GIS","") 
                    gis_temp.append(temp2)
           
        gis_temp2 = list(set(gis_temp))
        #print(gis_temp2)
        gis_temp.clear()

        #print(f"Cantidad de GIS: {len(set(gis_temp))}")
        #print(list(set(gis_temp)))
        #print("-"*150)
        for j in range(len(gis_temp2)):
            os.mkdir(f"Z:/Ing. Kevin/Prueba/{x}/{gis_temp2[j]}")
            for k in range(len(dirs2)):
                if(dirs2[k].__contains__(f"{gis_temp2[j]}")):
                    gis_temp3.append(dirs2[k])
            for h in range(len(gis_temp3)):
                old_file = f'Z:/Ing. Kevin/Prueba/{x}/{gis_temp3[h]}'
                #print(old_file)
                new_file = f'Z:/Ing. Kevin/Prueba/{x}/{gis_temp2[j]}/{gis_temp3[h]}'
                #print(new_file)
                os.rename(old_file, new_file)
            gis_temp3.clear()
        

#obtenerNombre()
#agruparFotos()
#obtenerGis()
agruparFotosGis()
