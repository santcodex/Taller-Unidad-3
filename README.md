Manejo de Archivos
-------------
### 1. Lenguaje utilizado

- Python (se usan módulos como os, csv y json).

### 2. Herramientas y sus Funciones

- os.path.exists(): Verifica si un archivo existe. Relacionado con la comprobación de la existencia de archivos.

- csv.writer(): Escribe datos en un archivo CSV. Relacionado con la lectura y escritura usando la biblioteca csv.

- csv.reader(): Lee datos de un archivo CSV. Relacionado con los ejemplos prácticos con archivos CSV.

- json.dump(): Guarda datos en formato JSON. Relacionado con la serialización usando la biblioteca json.

-  json.load(): Carga datos desde un archivo JSON. Relacionado con la deserialización usando la biblioteca json.

- with open():  Abre y cierra archivos automáticamente. Relacionado con el cierre automático de archivos usando with.

- try-except: Maneja errores al trabajar con archivos. Relacionado con el uso de bloques try y except para manejo de excepciones.

### 3. Archivos Usados

#####  1contactos.csv:
 - Tipo:  Archivo CSV (valores separados por comas).

- Función: Almacena contactos en formato tabular, con columnas para Nombre y Telefono.

- Tema relacionado: Tipos de archivos: CSV.


##### 2 contactos.json:

- Tipo: Archivo JSON (formato estructurado).

- Función: Almacena contactos como una lista de diccionarios, donde cada contacto tiene las claves Nombre y Telefono.

- Tema relacionado: Tipos de archivos: JSON.

### 4. Temas Cubiertos en el Ejercicio

✅ Tipos de archivos: 
- CSV (contactos.csv) y JSON (contactos.json).

✅ Apertura y cierre de archivos:
- Uso de with open() para manejo seguro de archivos

✅ Escritura de archivos:
- Modos "w" (creación), "a" (añadir datos), "r" (lectura).

✅ **Uso de try-except**:
- Manejo de errores al leer/escribir archivos.Comprobación de existencia de archivos:s:**
- os.path.exists() antes de crear archivos.

✅** Lectura/escritura con csv:**
- csv.writer() y csv.reader() para manejar datos tabul Serialización/deserialización con json: json:**
- json.dump() y json.load() para guardar y cargar datos estructuraCierre automático con with: with:**
- Garantiza que los archivos se cierren correctameOrganización de archivos en proyectos:ectos:**
- Uso de dos formatos (CSV y JSON) para almacenar los mismos daNo se usaron explícitamente:mente:**
- read(), readline(), readlines() (se usan alternativas como csv.reader y json.load).
- Modo r+ (solo se usaron w, a, r).

### 5. Resumen del Funcionamiento del P1.Verifica si existen los archivoschivos** (contactos.csv y contactos.json).
- Si no existen, los crea:
   - CSV: con una cabecera (Nombre, Telefono).
     - JSON: como una lista vacía [].
  
**2.Pide datos al usuario** (nombre y 3.Guarda el contacto en ambos formatos: forCSV:

- **CSV:** Añade una nueva fila con csv.writer().

- **JSON:** Carga la lista existente, añade el nuevo contacto y guarda con json.dump().

**4.Muestra el contenido de ambos archivos** para confirmar los datos.
