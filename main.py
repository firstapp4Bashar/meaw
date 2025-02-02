pip install playsound
import tkinter as tk
from playsound import playsound

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("زر القطة")
root.geometry("400x300")  # حجم النافذة
root.configure(bg="blue")  # خلفية زرقاء

# دالة لتشغيل الصوت عند الضغط على الزر
def play_meow():
    playsound("meow.mp3")

# إنشاء الزر
button = tk.Button(
    root,
    text="Meow",
    bg="red",  # لون الزر أحمر
    fg="white",  # لون النص أبيض
    font=("Arial", 20),
    command=play_meow
)

# وضع الزر في وسط النافذة
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# تشغيل النافذة
root.mainloop()
python cat_button.py
