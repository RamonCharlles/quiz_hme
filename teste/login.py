import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Login")
        self.root.geometry("480x300+290+100")
        self.root.resizable(False, False)

        try:
            self.bg = ImageTk.PhotoImage(file="images/bg1.png")
            lbl_bg = tk.Label(self.root, image=self.bg)
            lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            print("Erro: Arquivo de imagem 'images/bg1.png' não encontrado.")
            # Se a imagem não for encontrada, podemos continuar sem ela
            pass

        Frame_login = tk.Frame(self.root, bg="white")
        Frame_login.place(x=150, y=50, height=200, width=300)

        lbl_title = tk.Label(Frame_login, text="Login System", font=("Elephant", 25, "bold"), fg="midnight blue", bg="white").place(x=20, y=20)

        lbl_user = tk.Label(Frame_login, text="Username", font=("Goudy Old Style", 15, "bold"), fg="gray", bg="white").place(x=20, y=70)
        self.txt_uname = ttk.Entry(Frame_login, font=("times new roman", 15))
        self.txt_uname.place(x=20, y=90, width=250)

        lbl_pass = tk.Label(Frame_login, text="Password", font=("Goudy Old Style", 15, "bold"), fg="gray", bg="white").place(x=20, y=120)
        self.txt_pass = ttk.Entry(Frame_login, show="*", font=("times new roman", 15))
        self.txt_pass.place(x=20, y=140, width=250)

        forget_btn = tk.Button(Frame_login, text="Forget Password?", cursor="hand2", bg="white", fg="red", bd=0, font=("times new roman", 12)).place(x=10, y=170)
        login_btn = tk.Button(Frame_login, text="Login", font=("Arial Rounded MT Bold", 15, "bold"), bg="midnight blue", fg="white", cursor="hand2").place(x=170, y=170, width=100, height=30)

def main():
    root = tk.Tk()
    obj = Login_System(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    