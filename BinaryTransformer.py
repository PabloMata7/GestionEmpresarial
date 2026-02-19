import base64

# Cambia 'tu_imagen.png' por el nombre de tu archivo
file_path = 'Mega_Metagross.png'

with open(file_path, "rb") as image_file:
    # Leemos el binario y lo codificamos a Base64
    encoded_string = base64.b64encode(image_file.read())
    
    # Lo convertimos a string para poder copiarlo
    base64_text = encoded_string.decode('utf-8')
    
    print(base64_text)
    
    # Opcional: Guardarlo en un txt para copiarlo fácil al CSV
    with open("imagen_para_csv.txt", "w") as text_file:
        text_file.write(base64_text)
        print("¡Listo! Copia el contenido de 'imagen_para_csv.txt'")