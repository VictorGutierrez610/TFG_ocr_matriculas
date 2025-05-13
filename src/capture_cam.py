import cv2

class Camera:
    def __init__(self, image_cap):  # Constructor de la clase
        self.image_cap = image_cap

    def get_frame(self):
        if not self.image_cap.isOpened():  # Verificar si la cámara está abierta
            raise Exception("No se puede abrir la cámara")
        ret, frame = self.image_cap.read()
        if not ret:
            raise Exception("No se pudo capturar el fotograma")
        return frame

    def release(self):
        self.image_cap.release()

# Crear la instancia de la cámara
image_cap = cv2.VideoCapture(0)  # 0: cámara portátil, 1: cámara USB
camera_instance = Camera(image_cap)
