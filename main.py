import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import threading
import pyttsx3
import os

from brain import responder

# ================= VOZ =================
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

# ================= JANELA =================
root = tk.Tk()
root.title("SCP-079")
root.configure(bg="black")

root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

# ================= CAMINHO =================
base_dir = os.path.dirname(__file__)
img_path = os.path.join(base_dir, "assets", "scp079.png")

# ================= TELA DE LOADING =================
frame_loading = tk.Frame(root, bg="black")
frame_loading.pack(fill=tk.BOTH, expand=True)

try:
    img = Image.open(img_path).resize((300, 300))
    img_tk = ImageTk.PhotoImage(img)

    label_img = tk.Label(frame_loading, image=img_tk, bg="black")
    label_img.image = img_tk
    label_img.pack(pady=20)
except Exception as e:
    print("Erro imagem:", e)

label_loading = tk.Label(
    frame_loading,
    text="STARTING SYSTEM...",
    fg="#00ff00",
    bg="black",
    font=("Consolas", 14)
)
label_loading.pack(pady=10)

progress = ttk.Progressbar(frame_loading, length=300, mode="determinate")
progress.pack(pady=20)

# ================= SISTEMA PRINCIPAL =================
def iniciar_sistema():
    frame_loading.destroy()

    # CHAT
    chat = tk.Text(root, bg="black", fg="#00ff00", font=("Consolas", 12))
    chat.pack(fill=tk.BOTH, expand=True)
    chat.config(state=tk.DISABLED)

    def log(msg):
        chat.config(state=tk.NORMAL)
        chat.insert(tk.END, msg + "\n")
        chat.config(state=tk.DISABLED)
        chat.yview(tk.END)

    # RESPOSTA
    def respost_thread(text):
        respost = respost(text)
        root.after(0, lambda: log(f"> SCP-079: {respost}"))
        threading.Thread(target=talk, args=(respost,), daemon=True).start()

    # ENVIO
    def send():
        text = enter.get()

        if text.strip() == "":
            return

        enter.delete(0, tk.END)
        log(f"> You: {text}")

        threading.Thread(target=respost_thread, args=(text,), daemon=True).start()

    # INPUT
    enter = tk.Entry(root, bg="black", fg="green", insertbackground="green", font=("Consolas", 12))
    enter.pack(fill=tk.X, padx=10, pady=10)

    enter.bind("<Return>", lambda e: send())

    # BOTÃO
    tk.Button(root, text="send", bg="black", fg="green", command=send).pack()

    log(">> SCP-079 ONLINE")
    log(">> E to write")

# ================= ANIMAÇÃO LOADING =================
def carregar():
    for i in range(101):
        progress["value"] = i
        root.update_idletasks()
        root.after(15)
    iniciar_sistema()

threading.Thread(target=carregar, daemon=True).start()

root.mainloop()