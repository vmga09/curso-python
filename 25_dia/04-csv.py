import csv
import os

# # ESCRIBIR
# with open("archivo.csv", "w", newline='') as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["twit_id", "user_id", "text"])
#     writer.writerow([1000, 1, "Este es un twit"])
#     writer.writerow([1001, 2, "otro twit!"])


# # LEER
# with open("archivo.csv") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)


# # ACTUALIZAR CSV
with open("archivo.csv") as r, open("archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        try:
            print(linea)
            if linea[0] == "1000":
                writer.writerow([1001, 1, "Texto Modificado"])
            else:
                writer.writerow(linea)
        except:
            print('linea vacia')
os.remove("archivo.csv")
os.rename("archivo_temp.csv", "archivo.csv")
