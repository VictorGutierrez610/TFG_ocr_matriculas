# 🚘 TFG_ocr_matriculas 

¡Buenas a todos los desarrolladores y usuarios que visiten este repositorio! 😄 Aquí estaré trabajando sobre mi proyecto de fin del grado en desarrollo de aplicaciones web, en el que usaré **ocr** para el **reconocimiento de matriculas en una barrera de un garaje** 🎥. También implementaré una **base de datos para almacenar las matriculas** de clientes ficticios 💿, los cuales pueden o no contar con los derechos necesarios para que la puerta se abra, el proyecto estará destinado a una barrera de parking publico de pago que al mismo tiempo es compartido por propietarios de plazas de garaje, mi intención también es hacer una pequeña **interfaz grafica** 💻, donde se pueda visualizar más comodamente las matriculas y en tiempo real y sus permisos.

---

## 🧠 Objetivo del proyecto

El objetivo principal de este proyecto es crear un sistema capaz de:

- 📷 Capturar imágenes de vehículos en tiempo real.
- 🔍 Detectar y leer las matrículas mediante **OCR**.
- 📂 Consultar si la matrícula tiene permiso en una **base de datos MySQL**.
- ✅ Mostrar la información en una interfaz gráfica y permitir el acceso si corresponde.

Todo esto se hace usando herramientas open-source, inteligencia artificial y librerías ampliamente utilizadas en Python. Además, documentaré el proceso para que pueda servir como guía o inspiración para futuros desarrolladores.

---

## 📌 Casos de uso

Este sistema puede ser aplicado en:

- 🅿️ Parkings públicos con barreras automáticas.
- 🏢 Comunidades de vecinos con plazas asignadas.
- 🏭 Empresas o fábricas con accesos restringidos por matrícula.
- 🚧 Proyectos educativos que combinen OCR + gestión de permisos.

---

## 📱 Tecnologías 

Para este proyecto se usarán las siguientes tecnologías y librerias: 

- Python 🐍: Se usará como lenguaje de programación para todo el proyecto, por su versatilidad y gran cantidad de librerias y documentación, aparte de por su sencilles de uso
- EasyOCR 🔍: Diría que es la biblioteca de reconocimiento óptico de caracteres (OCR) por exelencia de Python por su sencillez, permite extraer texto de imágenes con modelos de deep learning, y para eso eso la usaremos.
- OpenCV 📷: Es una biblioteca de visión por computadora que es usada para procesar imágenes y videos, la usaremos precisamente para proesar la imagen de las matriculas a travez de filtros y contrastes para facilitar el trabajo y mejorar la precision del sistema de OCR.
- NumPy 🔢: una biblioteca para cálculos numéricos y manipulación de matrices, ampliamente conocida entre desarrolladores python, en nuestro caso la usaremos brevemente para detectar el alto y ancho de la matricula del vehículo.
- Imutils 📏: `Es un conjunto de funciones útiles para facilitar el manejo de las imágenes con OpenCV, como redimensionamiento y rotación, solo la usamos en una ocación a si que es posible que busquemos una solucion futura.` #posible eliminación
- Matplotlib 📊: `Es una biblioteca usada para visualización de datos, nosotros la usaremos para visualizar la imagen de la matricula ya procesada, tal vez más adelante nos sea precindible.` #posible eliminación
- Tkinter 🖥️: Esta es la ultima biblioteca que usaremos, la implementaremos para la interfaz gráfica de usuario (GUI), a la hora de crear la aplicación de escritorio.
- MySQL 🗄️: MySQL es un sistema de gestión de bases de datos relacionales, es usado para almacenar y gestionar datos de manera eficiente y conocido mundialmente, nosotros lo usaremos para rear y gestionar facilmente la base de dtos de matriculas y clientes, así como la hora de entrada y/o salida de los vehiculos.

>Estas tecnologias y librerias han sido elegidas principalamente para el proyecto, pero pueden variar a lo largo del desarrollo ya que pueden surgir necesidades o dificultades especificas en algun punto del proceso

Quisiera incluir en las tecnologías el uso de los modelos de inteligencía artificial de lenguaje natural como pueden ser **Chat-GPT**, **Deepseek** y la integración de **Github Copilot** en *Visual Studio Code*, con la intención de contrastar la información encontrada en páginas web revisadas para este proyecto, pero sobre todo para la explicación de como usar determinadas funciones especificas encontradas en la documentación oficial de las librerias. Ya que la información dada por estos modelos de IA contrastada adecuadamente con documentaciones y proyectos de codigo abierto ajenos a mi, está resultando de muy gran ayuda, con explicaciones y ejemplos.

---

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

---

## 🚀 Instalación y Configuración

Aquí detallaremos que deberemos hacer si queremos replicar este proyecto en un entorno local, para ello comento que se estoy trabajando en mi entorno de desarrollo principal que es un ordenador portatil con Windows 11 con un procesador ryzen 5 serie 7520U con gráfica integrada, con 16 GB de memoria RAM, a esto me gustaría hacer el inciso que para las tareas de ocr e inteligencia artificial normalmente primero desarrollo el codigo y las pruebas en mi ordenador de escritorio con Windows 10, ryzen 5 5600X, una tarjeta gráfica 4060 super y 32 GB de RAM, ya sea en local o con conexión remota para el uso de recursos.

### 1️⃣ Clonar repositorio

Para clonar el repositorio se debe usar la siguiente url:

```bash
https://github.com/VictorGutierrez610/TFG_ocr_matriculas.git
```

### 2️⃣ Instalar dependencias 

para instalar las dependencias necesarias para ejecutar este proyecto en cada entorno local, usaremos el archivo `requiremenst.txt` en el cual proximamente se detallarán todas las librerías utilizadas en él.

### 3️⃣ Configurar la base de datos

Esta será la explicación inicial de la base de datos planteada hasta ahora, aun qué en el futuro del proyecto puede variar según las necesaidades. A la BBDD la llamaremos `parking_system`, y constará principalmente de una única tabla llamada `vehiculos` que tendrá 4 campos (columnas), en los que incluiremos un `id` como clave primaria autoincremental, la `matricula` del vehículo que será un cadena de caractares que en un principio ajustaremos su tamaño a un *VARCHAR(10)* y además no podrá ser nulo ya que no tendría sentido crear un registro (fila) sin una matricula asociada, el nombre del `propietario` que será un *VARCHAR(100)* inicialmente y este si podrá ser nulo, ya que el proyecto está pensado para que funcione en un garaje compartido entre "parking público" y propietarios de plazas de garaje, y por último crearemos un campo llamado `permiso` para indicar si el vehiculo tiene o no permiso para la salida del parking, esté permiso estará asociado al pago realizado o no del ticket del cliente y será un tipo de dato *tinyint* donde 0 significará negativo y 1 positivo.

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

#### Creación de la BBDD
![Captura de pantalla 2025-01-31 175126](https://github.com/user-attachments/assets/d2cc879d-ec51-42b4-a9bc-61bd9bb90bd6)

#### Creación de la tabla
![Captura de pantalla 2025-01-31 180530](https://github.com/user-attachments/assets/8884a98d-be7d-4aed-aa69-cedbce9c9fae)

### 4️⃣ Estructurar archivos principales

Este sistema se divide en tres archivos clave, cada uno con una responsabilidad bien definida para mantener una arquitectura modular y clara:

#### 1. `main.py` – **Interfaz Gráfica y Control del Flujo**
Este archivo actúa como el núcleo de la aplicación. Crea una interfaz gráfica con Tkinter que permite al usuario iniciar y detener el sistema de cámara y OCR. Controla el flujo del programa, la sincronización de procesos y la comunicación entre los módulos de captura y reconocimiento.

**Funciones principales:**
- Crear la ventana y los botones (`Start Camera`, `Close Camera`).
- Mostrar el vídeo en tiempo real y el texto reconocido.
- Coordinar el flujo de vídeo y OCR de forma paralela y sin bloquear la interfaz.

#### 2. `capture_cam.py` – **Captura de Vídeo desde la Cámara**
Contiene la clase `🔠 Camera`, encargada de gestionar el acceso a la webcam mediante OpenCV. Su función principal es proporcionar fotogramas individuales a `🔰 main.py` de forma eficiente para su visualización y procesamiento.

**Funciones principales:**
- Inicializar la cámara (`🔠 cv2.VideoCapture`).
- Obtener fotogramas en tiempo real (`🔠 get_frame()`).
- Liberar la cámara de forma segura (`🔠 release()`).

#### 3. `ocr.py` – **Procesamiento de Imagen y Reconocimiento de Matrículas**
Incluye la clase `🔠 ocr`, diseñada para recibir un fotograma, procesarlo y extraer el texto de la matrícula utilizando técnicas de visión por computador (OpenCV) y OCR (EasyOCR). El procesamiento se realiza en pasos bien definidos para mejorar la precisión.

**Funciones principales:**
- Cargar y preprocesar la imagen (escalado, grises, bordes).
- Detectar y recortar la región de la matrícula.
- Leer el texto con EasyOCR y devolverlo al interfaz gráfica.

---

## 📋 Resumen Detallado del Flujo y Sincronización del Programa

--> archivo: 🔰
--> clase: 🔠
--> Método: 🔻

### 1. 🏃 Inicio y Configuración de la Interfaz

- El programa comienza ejecutando `🔰 main.py`.
- Se crea una ventana principal con **Tkinter**:
  - Título: `"Camera Interface"`
  - Tamaño: `800x700` píxeles.
- Inicialización de variables:
  - `🔠 self.camera`: instancia de la cámara (inicialmente `None`).
  - `🔠 self.camera_running` y `🔠 self.ocr_running`: flags booleanos que controlan el estado de la cámara y del OCR.
- Creación de botones:
  - **Start Camera**: inicia la cámara y el OCR.
  - **Close Camera**: detiene ambos procesos.
- Widgets:
  - `🔠 video_label`: muestra el vídeo en tiempo real.
  - `🔠 text_label`: muestra el texto de la matrícula detectada.

### 2. 📸 Arranque de la Cámara y Sincronización Inicial

- Al pulsar **Start Camera**:
  - Se comprueba que la cámara no esté ya en uso.
  - Se crea una instancia de `🔠 Camera` (de `🔰 capture_cam.py`) usando `🔠 cv2.VideoCapture(0)`.
  - Se valida la apertura correcta de la cámara. Si falla, se muestra un mensaje de error.
  - Se activan las banderas `🔠 camera_running` y `🔠 ocr_running`.
  - Se ejecutan:
    - `🔠 update_frame()` → para actualizar el vídeo.
    - `🔠 run_ocr_with_delay()` → para lanzar el OCR periódico.

### 3. 🎞️ Captura y Visualización de Vídeo en Tiempo Real

- Método: `🔻 update_frame()`
  - Si la cámara está activa:
    - Se captura un fotograma con `🔠 self.camera.get_frame()`.
    - El fotograma se convierte de **BGR a RGB**.
    - Se adapta la imagen para mostrarse en Tkinter.
    - Se actualiza el widget `🔠 video_label`.
    - Se programa una actualización cada **10 ms** usando:  
      `🔠 self.root.after(10, self.update_frame)`.
  - En caso de error (por ejemplo, desconexión), se muestra un mensaje y se detiene la actualización.

### 4. 🧠 Proceso de OCR en Paralelo

- Método: `🔻 run_ocr_with_delay()`
  - Si `🔠 ocr_running` es `True`:
    - Se lanza un hilo (`🔠 threading.Thread`) que ejecuta `🔠 run_ocr_on_frame()`.
    - Esto permite que el OCR funcione en paralelo sin bloquear la interfaz gráfica.
    - Se reprograma el OCR para ejecutarse cada segundo con:  
      `🔠 self.root.after(1000, self.run_ocr_with_delay)`.

### 5. 🔍 Procesamiento de Imagen y Reconocimiento de Matrícula

- Método: `🔻 run_ocr_on_frame()` (ejecutado en un hilo separado)
  - Captura el fotograma actual de la cámara.
  - Crea una instancia de la clase `🔠 ocr` (de `🔰 ocr.py`) con el fotograma.
  - Llama secuencialmente a los siguientes métodos:
    - `load_image()`: carga la imagen.
    - `preprocess_image()`: convierte a escala de grises, aplica filtro bilateral y bordes con **Canny**.
    - `detect_plate(edged)`: busca contornos con 4 vértices (posible matrícula), crea una máscara y recorta.
    - `recognize_text()`: usa **EasyOCR** para leer el texto.
  - El texto detectado se guarda en `🔠 recognizer.text`.
  - Si no se detecta texto, se muestra un mensaje indicativo.
  - El widget `🔠 text_label` se actualiza de forma segura desde el hilo principal con:  
    `🔠 self.root.after(0, ...)`.

### 6. 🧬 Sincronización y Control de Estados

- El flujo del vídeo y del OCR se sincroniza usando las banderas:
  - `🔠 camera_running`
  - `🔠 ocr_running`
- Mientras `🔠 camera_running` sea `True`, se actualiza continuamente el vídeo.
- Mientras `🔠 ocr_running` sea `True`, el OCR se ejecuta cada segundo en un hilo separado.
- La cámara se accede de forma segura.
- Cualquier error se notifica al usuario mediante mensajes en la interfaz.

### 7. ❌ Cierre y Liberación de Recursos

- Al pulsar **Close Camera**:
  - Se desactivan las banderas `🔠 camera_running` y `🔠ocr_running`.
  - Se libera la cámara con `🔠 self.camera.release()`.
  - Se limpia el contenido mostrado en la interfaz.
  - Si la cámara no estaba activa, se informa al usuario.

### 8. 🧩 Resumen de la Comunicación entre Módulos

- **`🔰 main.py`**
  - Controla la interfaz, lógica principal y sincronización.
  - Importa:
    - `🔠 Camera` de `🔰 capture_cam.py`
    - `🔠 ocr` de `🔰 ocr.py`

- **`🔰 capture_cam.py`**
  - Contiene la clase `🔠 Camera`:
    - Métodos para capturar y liberar la cámara.

- **`🔰 ocr.py`**
  - Contiene la clase `🔠 ocr`:
    - Métodos para:
      - Cargar imágenes.
      - Preprocesarlas.
      - Detectar matrículas.
      - Reconocer texto.

### 9. 🧭 Flujo Lógico de Ejecución

1. El usuario abre la app y pulsa **Start Camera**.
2. Se inicializa la cámara y se empieza a mostrar vídeo en tiempo real.
3. Cada segundo, en paralelo:
   - Se captura un fotograma.
   - Se detecta y reconoce la matrícula.
   - Se actualiza el texto mostrado.
4. El usuario puede detener todo en cualquier momento con **Close Camera**.

✅ **Este diseño garantiza que:**
- La interfaz gráfica permanece fluida y reactiva.
- El proceso de OCR es eficiente, periódico y no bloquea la aplicación.
- Los recursos se gestionan correctamente y de forma segura.


