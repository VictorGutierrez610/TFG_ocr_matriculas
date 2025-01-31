import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as plt

class ocr:
    def __init__(self, image_capture):
        self.image_capture = image_capture  # Ruta de la imagen
        self.image = None  # Aquí cargaremos la imagen
        self.gray_image = None  # Imagen en escala de grises
        self.cropped_image = None  # Imagen recortada de la matrícula
        self.text = None  # Texto detectado en la matrícula

    def load_image(self):
        '''Carga la imagen desde la ruta proporcionada.'''
        self.image = cv2.imread(self.image_capture)
        if self.image is None:
            raise FileNotFoundError('Error al cargar la imagen. Verifica la ruta.')
        print('Imagen cargada correctamente.')

    def preprocess_image(self):
        '''Convierte la imagen a escala de grises y aplica filtro bilateral.'''
        if self.image is None:
            raise ValueError('Primero debes cargar la imagen.')
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        bfilter = cv2.bilateralFilter(self.gray_image, 11, 17, 17)
        edged = cv2.Canny(bfilter, 30, 200)
        print('Imagen preprocesada (escala de grises y bordes detectados).')
        return edged

    def detect_plate(self, edged):
        '''Encuentra el contorno que corresponde a la matrícula.'''
        keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(keypoints)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

        location = None
        for contour in contours:
            approx = cv2.approxPolyDP(contour, 10, True)
            if len(approx) == 4:
                location = approx
                break

        if location is None:
            raise ValueError('No se encontró un contorno válido con 4 vértices.')
        print('Matrícula detectada.')
        
        # Crear máscara y recortar la imagen
        mask = np.zeros(self.gray_image.shape[:2], np.uint8)  # type: ignore
        self.cropped_image = cv2.drawContours(mask, [location], 0, (255,), -1)
        self.cropped_image = cv2.bitwise_and(self.image, self.image, mask=mask) # type: ignore

        # Coordenadas para recortar
        (x, y) = np.where(mask == 255)
        (x1, y1) = (np.min(x), np.min(y))
        (x2, y2) = (np.max(x), np.max(y))
        self.cropped_image = self.gray_image[x1:x2+1, y1:y2+1] # type: ignore

    def recognize_text(self):
        '''Usa EasyOCR para leer texto de la imagen recortada.'''
        if self.cropped_image is None:
            raise ValueError('Primero debe detectar la matrícula.')
        reader = easyocr.Reader(['en'])
        result = reader.readtext(self.cropped_image)
        if not result:
            raise ValueError('No se detectó texto en la matrícula.')
        self.text = result[0][1].strip()
        print(f'Matrícula detectada: {self.text}')

    def show_cropped_image(self):
        '''Muestra la imagen recortada.'''
        if self.cropped_image is None:
            raise ValueError('Primero debes detectar la matrícula.')
        plt.imshow(self.cropped_image, cmap='gray')
        plt.axis('off')
        plt.show()

# Uso de la clase
if __name__ == '__main__':
    image_cap = 'data\image2.jpg'

    recognizer = ocr(image_cap)  # Crear el objeto
    recognizer.load_image()                  # Cargar imagen
    edged = recognizer.preprocess_image()    # Preprocesar imagen
    recognizer.detect_plate(edged)           # Detectar matrícula
    recognizer.recognize_text()              # Reconocer texto
    recognizer.show_cropped_image()          # Mostrar resultado


