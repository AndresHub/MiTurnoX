import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import cv2
import os

class VideoPlayerApp:
    def __init__(self, root, video_dir, display_area):
        self.root = root
        self.video_dir = video_dir
        self.display_area = display_area
        self.video_files = [f for f in os.listdir(video_dir) if f.endswith(('.mp4', '.avi', '.mov'))]
        self.video_index = 0
        self.playing = True
        self.setup_ui()
        self.frame_update_interval = 30  # Update every 30 milliseconds
        self.update_frame()

    def setup_ui(self):
        self.frame = ctk.CTkFrame(self.root, width=self.display_area[0], height=self.display_area[1])
        self.frame.pack(pady=20)
        self.label = ctk.CTkLabel(self.frame, width=self.display_area[0], height=self.display_area[1])
        self.label.pack()
        self.imgtk = None  # To keep a reference to the image

    def update_frame(self):
        if self.playing:
            video_path = os.path.join(self.video_dir, self.video_files[self.video_index])
            cap = cv2.VideoCapture(video_path)
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, self.display_area)
                img = Image.fromarray(frame)
                self.imgtk = ImageTk.PhotoImage(image=img)
                
                # Update the label with the new image
                self.label.configure(image=self.imgtk)
                self.label.image = self.imgtk  # Keep a reference to avoid garbage collection

                # Schedule the next frame update
                self.root.after(self.frame_update_interval, self.update_frame)
            else:
                cap.release()
                self.video_index = (self.video_index + 1) % len(self.video_files)
                self.update_frame()
        else:
            self.root.destroy()

    def stop(self):
        self.playing = False

def main():
    root = ctk.CTk()
    video_dir = r'C:\Users\andre\Documents\GitHub\MiTurnoX\ProjectoMiTurnoX\TesteoMódulos\MiTurnoX'  # Corrected path
    display_area = (800, 600)  # Specify the width and height of the video display area
    app = VideoPlayerApp(root, video_dir, display_area)

    root.protocol("WM_DELETE_WINDOW", app.stop)
    root.mainloop()

if __name__ == "__main__":
    main()



