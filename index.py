from tkinter import *

class reproductor:
    def __init__(self, ventana):
        ventana.title("Reproductor de audio")
        ventana.geometry("600x900")
        ventana.config(bg="gray", bd=0)
        ventana.configure(bg="black")
        

        self.ReproduciendoLabel = Label(ventana, text="Reproduciendo x cancion o audio")
        self.ReproduciendoLabel.config(bg="black", fg="white", font=("Arial", 12))
        self.ReproduciendoLabel.config(width=50, height=10, border=0)
        self.ReproduciendoLabel.place(x=77, y=500)

        self.boton2 = Button(ventana, text="⏸", bg="white", fg="black", font=("Arial", 20))
        self.boton2.place(x=16, y=780)
        self.boton2.config(width=8, height=2)

        self.boton1 = Button(ventana, text="▶️", bg="white", fg="black", font=("Arial", 20))
        self.boton1.place(x=150, y=780)
        self.boton1.config(width=10, height=2)

        self.boton3 = Button(ventana, text="↻", bg="white", fg="black", font=("Arial", 20))
        self.boton3.place(x=300, y=780)
        self.boton3.config(width=10, height=2)

        self.boton4 = Button(ventana, text="📁", bg="white", fg="black", font=("Arial", 20), command=ventana.destroy)
        self.boton4.place(x=450, y=780)
        self.boton4.config(width=8, height=2)

ventana = Tk()
ventana.iconbitmap('C:\\Users\\thedr\\OneDrive\\Desktop\\Trabajo Practico Final Tkinter\\assets\\img\\icono.ico')
ventana.resizable(0,0)
imagen = PhotoImage(file="C:\\Users\\thedr\\OneDrive\\Desktop\\Trabajo Practico Final Tkinter\\assets\\img\\portada.png")
imagenLogo = PhotoImage(file="C:\\Users\\thedr\\OneDrive\\Desktop\\Trabajo Practico Final Tkinter\\assets\\img\\headset.png")
fondo = Label(ventana, image=imagen).place(x=0, y=0)
logoHeadset = Label(ventana, image=imagenLogo).place(x=180, y=120)

barra_menu = Menu(ventana)
menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Guida de uso")
barra_menu.add_cascade(label="Como se usa", menu=menu_archivo)
ventana.config(menu=barra_menu)

reproductor(ventana)
ventana.mainloop()