import tkinter as tk
from cryptography.fernet import Fernet, InvalidToken
from sleutelbeheer import sleutel_laden

key = sleutel_laden()
f = Fernet(key)

def tekst_versleutelen():
    message = invoer.get('1.0', tk.END).strip()
    versleuteld = f.decrypt(message.encode())
    resultaat.delete('1.0', tk.END)
    resultaat.insert(tk.END, versleuteld.decode())

def tekst_ontsleutelen():
    message = invoer.get('1.0', tk.END).strip()

    try:
        ontsleuteld = f.decrypt(message.encode())
        resultaat.delete('1.0', tk.END)
        resultaat.insert(tk.END, ontsleuteld.decode())

    except (InvalidToken, ValueError):
        resultaat.delete('1.0', tk.END)
        resultaat.insert(tk.END, 'Ontsleutelen mislukt!')

window = tk.Tk()
window.geometry('800x600')
window.title('Encryptie')

label_tekst = tk.Label(window, text='Voer je tekst in')
label_tekst.pack(pady= 10)

invoer = tk.Text(window, height=3, width=50)
invoer.pack()

knop_versleutelen = tk.Button(window, text='Versleutelen', command=tekst_versleutelen)
knop_versleutelen.pack(pady= 5)

knop_ontsleutelen = tk.Button(window, text='Ontsleutelen', command=tekst_ontsleutelen)
knop_ontsleutelen.pack(pady= 5)

label_resultaat = tk.Label(window, text='Resultaat')
label_resultaat.pack(pady= 10)

resultaat = tk.Text(window, height=3, width=50)
resultaat.pack()

window.mainloop()