import tkinter as tk

window = tk.Tk()
window.geometry('800x600')
window.title('Encryptie')

label_tekst = tk.Label(window, text='Voer je tekst in')
label_tekst.pack(pady= 10)

invoer = tk.Text(window, height=3, width=50)
invoer.pack()

knop_versleutelen = tk.Button(window, text='Versleutelen')
knop_versleutelen.pack(pady= 5)

knop_ontsleutelen = tk.Button(window, text='Ontsleutelen')
knop_ontsleutelen.pack(pady= 5)

label_resultaat = tk.Label(window, text='Resultaat')
label_resultaat.pack(pady= 10)

resultaat = tk.Text(window, height=3, width=50)
resultaat.pack()

window.mainloop()