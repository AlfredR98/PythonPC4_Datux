'''
Ejercicio 1
'''
ruta_archivo = './scripts/software.txt'
with open(ruta_archivo, mode = 'r+', encoding='utf-8') as file:
    data = file.read().lower()
    repetir = data.count(' la')
    
    try:
        texto_adicional = input('Ingrese el texto adicional:\n')
    except Exception as e:
        print(e)

    dataw = file.write('\n'+texto_adicional)
    file.close()

print(f'\nLa palabra "la" se repite: \t{repetir} veces')

