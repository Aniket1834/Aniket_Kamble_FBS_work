import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import joblib

# Load trained model
model = joblib.load("food_model.pkl")

# Match order with notebook
class_names = ['Burger', 'Pizza']

THRESHOLD = 0.80

# Main Window
root = tk.Tk()
root.title("Food Image Classifier")
root.geometry("700x750")
root.configure(bg="#121212")
root.resizable(False, False)

# ---------- Title ----------
title_label = tk.Label(
    root,
    text="🍕 Food Image Classification System 🍔",
    font=("Segoe UI", 22, "bold"),
    fg="#ffffff",
    bg="#121212"
)
title_label.pack(pady=20)

subtitle_label = tk.Label(
    root,
    text="Upload an image to detect whether it is Pizza, Burger or Something Else",
    font=("Segoe UI", 12),
    fg="#bbbbbb",
    bg="#121212"
)
subtitle_label.pack(pady=5)

# ---------- Image Frame ----------
image_frame = tk.Frame(root, bg="#1e1e1e", bd=2, relief="ridge")
image_frame.pack(pady=20)

image_label = tk.Label(image_frame, bg="#1e1e1e")
image_label.pack(padx=20, pady=20)

# ---------- Result Section ----------
result_frame = tk.Frame(root, bg="#121212")
result_frame.pack(pady=20)

result_label = tk.Label(
    result_frame,
    text="No image selected",
    font=("Segoe UI", 16, "bold"),
    fg="#00adb5",
    bg="#121212"
)
result_label.pack(pady=10)

confidence_label = tk.Label(
    result_frame,
    text="Confidence: 0%",
    font=("Segoe UI", 12),
    fg="#cccccc",
    bg="#121212"
)
confidence_label.pack(pady=5)

# ---------- Prediction Function ----------
def select_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )

    if file_path:
        img = Image.open(file_path).convert("RGB")

        # Resize for model
        img_resized = img.resize((224, 224))

        # Resize for display
        display_img = img.resize((350, 350))
        display_img = ImageTk.PhotoImage(display_img)

        image_label.config(image=display_img)
        image_label.image = display_img

        img_array = np.array(img_resized) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)

        confidence = float(np.max(prediction))
        predicted_class = class_names[np.argmax(prediction)]

        confidence_percent = round(confidence * 100, 2)

        if confidence >= THRESHOLD:
            result_label.config(
                text=f"Prediction: {predicted_class}",
                fg="#4CAF50"
            )
        else:
            result_label.config(
                text="Prediction: Not Pizza and Not Burger",
                fg="#f44336"
            )

        confidence_label.config(
            text=f"Confidence: {confidence_percent}%"
        )

# ---------- Button ----------
select_button = tk.Button(
    root,
    text="Select Image",
    command=select_image,
    font=("Segoe UI", 14, "bold"),
    bg="#00adb5",
    fg="white",
    activebackground="#00cfc8",
    width=18,
    height=2,
    bd=0,
    cursor="hand2"
)
select_button.pack(pady=20)

# ---------- Footer ----------
footer = tk.Label(
    root,
    text="Developed using TensorFlow + Joblib + Tkinter",
    font=("Segoe UI", 9),
    fg="#777777",
    bg="#121212"
)
footer.pack(side="bottom", pady=15)

root.mainloop()