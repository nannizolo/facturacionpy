import os
import PyPDF2
import timeit

start = timeit.default_timer()

# Establecer la carpeta para buscar archivos PDF
carpeta = 'C:/Users/usuario/Desktop/facturas11/re'

# Obtener la lista de archivos PDF en la carpeta
archivos_pdf = os.listdir(carpeta)

# Iterar sobre los archivos PDF
archivos_incorrectos = []
for archivo in archivos_pdf:

    # Abrir el archivo PDF
    pdf_file = open(carpeta + '/' + archivo, 'rb')

    # Crear un lector de PDF
    try:
        reader = PyPDF2.PdfReader(pdf_file)
    except Exception:
        archivos_incorrectos.append(archivo)
        print(f'El archivo {archivo} no está bien formado.')
        continue

    # Obtener el texto del archivo
    texto_pdf = ''
    for page in reader.pages:
        texto_pdf += page.extract_text()

    # Buscar la cadena que es igual al nombre del archivo sin su extensión en el texto del archivo
    cadena_buscada = archivo.split('.')[0]
    if cadena_buscada not in texto_pdf:
        archivos_incorrectos.append(archivo)

# Escribir los resultados en un archivo .txt
with open('Facturas incorrectas.txt', 'a') as f:
    if len(archivos_incorrectos) > 0:
        for archivo in archivos_incorrectos:
            f.write(archivo + '\n')
    else:
        f.write('No se encontraron facturas incorrectas.')

end = timeit.default_timer()

print(f'El código tardó {end - start} segundos en ejecutarse.')

