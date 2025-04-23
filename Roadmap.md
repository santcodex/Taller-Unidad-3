# Roadmap de funciones del programa
### 1. Inicialización y Preparación de Archivos.
##### Verificar y crear archivo CSV:

- Se verifica si el archivo contactos.csv existe.

- Si no existe, se crea el archivo y se escribe una cabecera con los campos ["Nombre", "Telefono"].

- Se maneja cualquier excepción que pueda ocurrir durante la creación del archivo.

##### Verificar y crear archivo JSON:

- Se comprueba si el archivo contactos.json existe.

- Si no existe, se crea el archivo con una lista vacía ([]), lo que prepara el contenedor de contactos.

- Se manejan errores en la creación del archivo de forma similar al CSV.
# 2. Interacción con el Usuario.
##### Saludo y solicitud de datos:
- Se muestra un mensaje de bienvenida (por ejemplo, "Bienvenido a tu Agenda de Contactos").

- Se solicitan al usuario el ingreso del nombre y teléfono del contacto mediante la función input().
##### Creación del objeto contacto:
- Los datos ingresados se encapsulan en un diccionario llamado contacto_nuevo con las claves "Nombre" y "Telefono".
# 3. Registro del Contacto en los Archivos.
##### Guardar el contacto en el archivo CSV:
- Se abre el archivo contactos.csv en modo "append" (añadir al final) para conservar los contactos existentes.

- Se escribe una nueva línea con los datos del contacto.

- Se asegura el manejo de errores durante el procedimiento de escritura.
##### Guardar el contacto en el archivo JSON:
- Lectura: Se abre el archivo contactos.json en modo lectura para cargar la lista actual de contactos.

- Actualización: Se añade el nuevo contacto al array ya existente.

- Escritura: La lista actualizada se escribe de nuevo en el archivo contactos.json con formato indentado para facilitar la lectura.

- Se implementa manejo de excepciones para capturar y reportar errores durante la lectura o escritura.
# 4. Visualización de Datos.
##### Mostrar contenido del archivo CSV:
- Se abre el archivo contactos.csv en modo lectura.

- Se recorre cada línea (fila) y se imprime en consola, mostrando así todos los contactos almacenados.
##### Mostrar contenido del archivo JSON:
- Se abre el archivo contactos.json y se carga la lista de contactos.

- Se imprime cada objeto (contacto) presente en la lista para que el usuario pueda ver la información consolidada.
