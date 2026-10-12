import os
import shutil

# Ruta de la carpeta que se va a organizar
folder_path = "C:/Users/jerem/Documents"

# Diccionario con las extensiones y sus respectivas carpetas
file_types = {
    '.txt': 'Documentos',
    '.pdf': 'Documentos',
    '.jpg': 'Imagenes',
    '.png': 'Imagenes',
    '.py': 'Scripts',
    '.mp3': 'Musica',
    '.mp4': 'Videos'
}

# Recorrer todos los archivos en la carpeta especificada
for file_name in os.listdir(folder_path):
    # Omitir si es una carpeta
    if os.path.isdir(os.path.join(folder_path, file_name)):
        continue
    
    # Obtener la extensión del archivo
    file_extension = os.path.splitext(file_name)[1].lower()
    
    # Mover el archivo si su extensión está definida en el diccionario
    if file_extension in file_types:
        target_folder = os.path.join(folder_path, file_types[file_extension])
        
        # Crear la carpeta de destino si no existe
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            
        # Rutas de origen y destino
        source_path = os.path.join(folder_path, file_name)
        target_path = os.path.join(target_folder, file_name)
        
        # Mover el archivo
        shutil.move(source_path, target_path)

print("¡Archivos organizados con éxito!")
