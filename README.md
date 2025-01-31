# 🚘 TFG_ocr_matriculas 

¡Buenas a todos los desarrolladores y usuarios que visiten este repositorio! 😄 Aquí estaré trabajando sobre mi proyecto de fin del grado en desarrollo de aplicaciones web, en el que usaré **ocr** para el **reconocimiento de matriculas en una barrera de un garaje** 🎥. También implementaré una **base de datos para almacenar las matriculas** de clientes ficticios 💿, los cuales pueden o no contar con los derechos necesarios para que la puerta se abra, el proyecto estará destinado a una barrera de parking publico de pago que al mismo tiempo es compartido por propietarios de plazas de garaje, mi intención también es hacer una pequeña **interfaz grafica** 💻, donde se pueda visualizar más comodamente las matriculas y en tiempo real y sus permisos.

## 📱 Tecnologías 

Para este proyecto se usarán las siguientes tecnologías y librerias: 

- Python 🐍: Se usará como lenguaje de programación para todo el proyecto, por su versatilidad y gran cantidad de librerias y documentación, aparte de por su sencilles de uso
- EasyOCR 🔍: Diría que es la biblioteca de reconocimiento óptico de caracteres (OCR) por exelencia de Python por su sencillez, permite extraer texto de imágenes con modelos de deep learning, y para eso eso la usaremos.
- OpenCV 📷: Es una biblioteca de visión por computadora que es usada para procesar imágenes y videos, la usaremos precisamente para proesar la imagen de las matriculas a travez de filtros y contrastes para facilitar el trabajo y mejorar la precision del sistema de OCR.
- NumPy 🔢: una biblioteca para cálculos numéricos y manipulación de matrices, ampliamente conocida entre desarrolladores python, en nuestro caso la usaremos brevemente para detectar el alto y ancho de la matricula del vehículo.
- Imutils 📏: `Es un conjunto de funciones útiles para facilitar el manejo de las imágenes con OpenCV, como redimensionamiento y rotación, solo la usamos en una ocación a si que es posible que busquemos una solucion futura.`
- Matplotlib 📊: `Es una biblioteca usada para visualización de datos, nosotros la usaremos para visualizar la imagen de la matricula ya procesada, tal vez más adelante nos sea precindible.`
- Tkinter 🖥️: Esta es la ultima biblioteca que usaremos, la implementaremos para la interfaz gráfica de usuario (GUI), a la hora de crear la aplicación de escritorio.
- MySQL 🗄️: MySQL es un sistema de gestión de bases de datos relacionales, es usado para almacenar y gestionar datos de manera eficiente y conocido mundialmente, nosotros lo usaremos para rear y gestionar facilmente la base de dtos de matriculas y clientes, así como la hora de entrada y/o salida de los vehiculos.

>Estas tecnologias y librerias han sido elegidas principalamente para el proyecto, pero pueden variar a lo largo del desarrollo ya que pueden surgir necesidades o dificultades especificas en algun punto del proceso

Quisiera incluir en las tecnologías el uso de los modelos de inteligencía artificial de lenguaje natural como pueden ser **Chat-GPT** y **Deepseek**, con la intención de contrastar la información encontrada en páginas web revisadas para este proyecto, pero sobre todo para la explicación de como usar determinadas funciones especificas encontradas en la documentación oficial de las librerias. Ya que la información dada por estos modelos de IA contrastada adecuadamente con documentaciones y proyectos de codigo abierto ajenos a mi, está resultando de muy gran ayuda, con explicaciones y ejemplos.

## 📂 Estructura del proyecto

Para este proyecto la intención principal será llevar el siguiente esquema de archivos y ficheros:

```bash
📂 TFG_ocr_matriculas
│── 📂 src               # Código fuente
│   ├── capture_cam.py   # Captura de la imagen
│   ├── ocr.py           # Lógica de OCR con EasyOCR
│   ├── app.py           # Interfaz gráfica con Tkinter
│   ├── main.py          # Archivo principal de inicialización
│── 📂 data              # Imágenes de prueba
│── 📂 docs              # Documentación del proyecto (se subirá el archivo de TFG)
│── README.md            # Documentación principal
│── requirements.txt     # Librerías necesarias
│── config.ini           # Configuración del sistema
```

## 🚀 Instalación y Configuración

Aquí detallaremos que deberemos hacer si queremos replicar este proyecto en un entorno local, para ello comento que se estoy trabajando en mi entorno de desarrollo principal que es un ordenador portatil con Windows 11 con un procesador ryzen 5 serie 7520U con gráfica integrada, con 16 GB de memoria RAM, a esto me gustaría hacer el inciso que para las tareas de ocr e inteligencia artificial normalmente primero desarrollo el codigo y las pruebas en mi ordenador de escritorio con Windows 10, ryzen 5 5600X, una tarjeta gráfica 4060 super y 32 GB de RAM, ya sea en local o con conección remota para el uso de recursos.

### 1️⃣ Clonar repositorio

Para clonar el repositorio se debe usar la siguiente url:

```bash
https://github.com/VictorGutierrez610/TFG_ocr_matriculas.git
```

### 2️⃣ Instalar dependencias 

para instalar las dependencias necesarias para ejecutar este proyecto en cada entorno local, usaremos el archivo `requiremenst.txt` en el cual proximamente se detallarán todas las librerías utilizadas en él.

### 3️⃣ Configurar la base de datos

Esta será la explicación inicial de la base de datos planteada hasta ahora, aun qué en el futuro del proyecto puede variar según las necesaidades. A la BBDD la llamaremos `parking_system`, y constará principalmente de una única tabla llamada `vehiculos` que tendrá 4 campos (columnas), en los que incluiremos un `id` como clave primaria autoincremental, la `matricula` del vehículo que será un cadena de caractares que en un principio ajustaremos su tamaño a un *VARCHAR(10)* y además no podrá ser nulo ya que no tendría sentido crear un registro (fila) sin una matricula asociada, el nombre del `propietario` que será un *VARCHAR(100)* inicialmente y este si podrá ser nulo, ya que el proyecto está pensado para que funcione en un garaje compartido entre "parking público" y propietarios de plazas de garaje, y por último crearemos un campo llamado `permiso` para indicar si el vehiculo tiene o no permiso para la salida del parking, esté permiso estará asociado al pago realizado o no del ticket del cliente.

```bash
CREATE DATABASE parking_system;
USE parking_system;

CREATE TABLE `parking_system`.`vehiculos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `matricula` VARCHAR(10) NOT NULL,
  `propietario` VARCHAR(100) NULL,
  `permiso` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `matricula_UNIQUE` (`matricula` ASC) VISIBLE);

);
```

