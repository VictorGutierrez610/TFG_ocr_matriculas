import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import capture_cam
import ocr
import cv2
import threading

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Camera Interface")
        self.root.geometry("800x800")  # Ajustar el tamaño de la ventana

        self.camera = None  # Inicializar la cámara como None
        self.camera_running = False
        self.ocr_running = False

        # Crear botones
        self.start_button = tk.Button(root, text="Start Camera", command=self.start_camera, width=20)
        self.start_button.pack(pady=10)

        self.close_button = tk.Button(root, text="Close Camera", command=self.close_camera, width=20)
        self.close_button.pack(pady=10)

        # Crear un widget para mostrar la cámara
        self.video_label = tk.Label(root)
        self.video_label.pack(expand=True, fill="both")

        # Crear un widget para mostrar el texto detectado
        self.text_label = tk.Label(root, text="", font=("Arial", 16), fg="blue")
        self.text_label.pack(pady=10)

    def start_camera(self):
        if not self.camera_running:
            # Reiniciar la instancia de la cámara
            self.camera = capture_cam.Camera(cv2.VideoCapture(0))
            if not self.camera.image_cap.isOpened():
                messagebox.showerror("Error", "No se puede abrir la cámara.")
                return
            self.camera_running = True
            self.ocr_running = True
            self.update_frame()
            self.run_ocr_with_delay()

    def update_frame(self):
        if self.camera_running:
            try:
                frame = self.camera.get_frame()
                # Convertir el fotograma a un formato compatible con tkinter
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img)
                self.video_label.imgtk = imgtk
                self.video_label.configure(image=imgtk)
                # Llamar a esta función de nuevo después de 10 ms
                self.root.after(10, self.update_frame)
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.camera_running = False

    def run_ocr_with_delay(self):
        if self.ocr_running:
            # Lanzar el OCR en un hilo aparte
            threading.Thread(target=self.run_ocr_on_frame, daemon=True).start()
            # Programar la siguiente llamada
            self.root.after(1000, self.run_ocr_with_delay)  # 1 segundo entre OCRs

    def run_ocr_on_frame(self):
        try:
            frame = self.camera.get_frame() # Capturar un fotograma de la cámara
            recognizer = ocr.ocr(frame) # Procesar el frame directamente
            recognizer.load_image() # Cargar la imagen
            edged = recognizer.preprocess_image() # Preprocesar la imagen
            recognizer.detect_plate(edged) # Detectar la matrícula
            recognizer.recognize_text()  # Leer el texto de la imagen recortada

            detected_text = recognizer.text if recognizer.text else "No se detectó texto"
        except Exception as e:
            print(f"Error en OCR: {e}")
            detected_text = "Error en OCR"
        # Actualizar la etiqueta en el hilo principal
        self.root.after(0, lambda: self.text_label.config(text=f"Matrícula detectada: {detected_text}"))

    def close_camera(self):
        if self.camera_running:
            self.camera_running = False
            self.ocr_running = False
            self.camera.release()
            self.video_label.configure(image="")
        else:
            messagebox.showinfo("Info", "The camera is not running.")

# Crear la ventana principal
root = tk.Tk()
app = CameraApp(root)
root.mainloop()