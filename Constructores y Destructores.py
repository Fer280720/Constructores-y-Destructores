class Archivo:
    def __init__(self, nombre_archivo):
        """Constructor: Inicializa el objeto y abre el archivo para escritura."""
        self.nombre_archivo = nombre_archivo
        try:
            # Intentamos abrir el archivo en modo de escritura
            self.archivo = open(nombre_archivo, 'w')
            print(f"Archivo '{self.nombre_archivo}' abierto correctamente.")
        except Exception as e:
            print(f"Error al abrir el archivo: {e}")
            self.archivo = None
    
    def escribir(self, contenido):
        """Método para escribir contenido en el archivo."""
        if self.archivo:
            self.archivo.write(contenido + '\n')
            print(f"Contenido escrito en el archivo '{self.nombre_archivo}'.")
    
    def __del__(self):
        """Destructor: Se llama automáticamente cuando el objeto es destruido."""
        try:
            # Si el archivo está abierto, lo cerramos
            if self.archivo:
                self.archivo.close()
                print(f"Archivo '{self.nombre_archivo}' cerrado correctamente.")
        except Exception as e:
            print(f"Error al cerrar el archivo: {e}")


# Crear una instancia de la clase Archivo
archivo_obj = Archivo("mi_archivo.txt")

# Escribir en el archivo
archivo_obj.escribir("Hola, este es un mensaje de prueba.")

# El destructor será llamado automáticamente cuando 'archivo_obj' sea destruido
del archivo_obj  # Se llama a __del__ para cerrar el archivo

