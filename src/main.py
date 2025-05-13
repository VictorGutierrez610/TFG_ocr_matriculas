import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import capture_cam
import cv2

class CameraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Camera Interface")
        self.root.geometry("800x600")  # Ajustar el tamaño de la ventana

        self.camera = capture_cam.camera_instance
        self.camera_running = False

        # Crear botones
        self.start_button = tk.Button(root, text="Start Camera", command=self.start_camera, width=20)
        self.start_button.pack(pady=10)

        self.close_button = tk.Button(root, text="Close Camera", command=self.close_camera, width=20)
        self.close_button.pack(pady=10)

        # Crear un widget para mostrar la cámara
        self.video_label = tk.Label(root)
        self.video_label.pack(expand=True, fill="both")

    def start_camera(self):
        if not self.camera_running:
            self.camera_running = True
            self.update_frame()

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

    def close_camera(self):
        if self.camera_running:
            self.camera_running = False
            self.camera.release()
            self.video_label.configure(image="")
        else:
            messagebox.showinfo("Info", "The camera is not running.")

# Crear la ventana principal
root = tk.Tk()
app = CameraApp(root)
root.mainloop()