import cv2 

class camera:

    def __init__(self, image_cap): # constructor de la clase
        self.image_cap = image_cap 

    def capture(self):
        if not self.image_cap.isOpened(): # controlar si podemos abrir la camara en el indice establecido
            print('No se puede abrir la camara')
            exit()
        else:
            print('capurando cam')

        while True: # capturamos los fotogramas de  la camara
            ret, frame = image_cap.read()
            if not ret:
                print('Saliendo ...')
                break
            cv2.imshow('Camara USB', frame) # Mostrar imagen del fotograma en ventana
            if cv2.waitKey(1) == ord('q'): # esperar a pulsar 'q' para cerrar
                break

        self.image_cap.release()
        cv2.destroyAllWindows()

image_cap = cv2.VideoCapture(1) # variable que apunta a la posicion de la camara a abrir (0: cam portatil, 1: cam USB)

capture_image = camera(image_cap) # creamos el objeto
capture_image.capture() # cargamos la imagen de la captura de la camara