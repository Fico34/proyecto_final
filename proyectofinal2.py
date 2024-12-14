
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


TASA_USD_A_PESOS = 1045
TASA_USD_A_REALES = 6.4
TASA_PESOS_A_REALES = TASA_USD_A_REALES / TASA_USD_A_PESOS

def convertir():
    try:
        monto = float(ingrese_monto.get())
        moneda_de_origen = combo_moneda.get()
        
        if moneda_de_origen == "USD a PESOS":
            resultado = monto * TASA_USD_A_PESOS
            label_resultado.config(text=f"{monto} USD equivale a {resultado:.2f} PESOS.")
        elif moneda_de_origen == "PESOS a USD":
            resultado = monto / TASA_USD_A_PESOS
            label_resultado.config(text=f"{monto} PESOS equivale a {resultado:.2f} USD.")
        elif moneda_de_origen == "USD a REALES":
            resultado = monto * TASA_USD_A_REALES
            label_resultado.config(text=f"{monto} USD equivale a {resultado:.2f} REALES.")
        elif moneda_de_origen == "REALES a USD":
            resultado = monto / TASA_USD_A_REALES
            label_resultado.config(text=f"{monto} REALES equivale a {resultado:.2f} USD.")
        elif moneda_de_origen == "PESOS a REALES":
            resultado = monto * TASA_PESOS_A_REALES
            label_resultado.config(text=f"{monto} PESOS equivale a {resultado:.2f} REALES.")
        elif moneda_de_origen == "REALES a PESOS":
            resultado = monto / TASA_PESOS_A_REALES
            label_resultado.config(text=f"{monto} REALES equivale a {resultado:.2f} PESOS.")
        else:
            messagebox.showerror("Error", "Seleccione una opción válida.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un monto válido.")

ventana = tk.Tk()
ventana.title("Conversor de Monedas")
ventana.config(bg="green")
ventana.geometry("400x400")

label_monto = tk.Label(ventana, text="Monto a convertir:",bg=("gray"))
label_monto.grid(row=0, column=0, padx=10, pady=10)

ingrese_monto = tk.Entry(ventana,bg=("gray"))
ingrese_monto.grid(row=0, column=1, padx=10, pady=10)


label_moneda = tk.Label(ventana, text="Conversión:",bg=("gray"))
label_moneda.grid(row=1, column=0, padx=10, pady=10)

combo_moneda = ttk.Combobox(ventana,
 values=["USD a PESOS", "PESOS a USD", "USD a REALES", "REALES a USD", "PESOS a REALES", "REALES a PESOS "],
state="readonly")
combo_moneda.grid(row=1, column=1, padx=10, pady=10)
combo_moneda.set("Seleccione")


boton_convertir = tk.Button(ventana, text="Convertir", command=convertir,bg=("gray"))
boton_convertir.grid(row=2, column=0, columnspan=2, pady=10)


label_resultado = tk.Label(ventana, text="", fg="blue")
label_resultado.grid(row=3, column=0, columnspan=2, pady=10)


ventana.mainloop()