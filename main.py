import openai
import customtkinter as ctk

api_key = "PUT-YOUR-CHATGPT-API-HERE"
openai.api_key = api_key

def textAppend(textbox, text):
    textbox.configure(state="normal")
    textbox.insert('end', text)
    textbox.configure(state="disabled")

def sendMessage(char):
    textAppend(textbox, 'Tú: ' + entry.get() + '\n\nGPT: ')
    response = openai.Completion.create(model="text-davinci-003",
                                        prompt=textbox.get('0.0', 'end'),
                                        temperature=0.7,
                                        frequency_penalty=0,
                                        presence_penalty=0,
                                        max_tokens=256,
                                        stop=["Tú:", "GPT:"])
    answer = response["choices"][0].text.strip()
    textAppend(textbox, answer + '\n\n')
    entry.delete(0, 'end')

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

# Inicializar ventana principal
root = ctk.CTk()
root.geometry('640x480')

# Crear el frame
frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill='both', expand=True)

# Área de conversación
textbox = ctk.CTkTextbox(master=frame, width=600, height=360)
textbox.pack(pady=12, padx=10)
textbox.configure(state="disabled", wrap='word')

# Campo de mensaje
entry = ctk.CTkEntry(master=frame, width=600)
entry.pack(pady=12, padx=10)
entry.bind(sequence='<Return>', command=sendMessage)

# Iniciar bucle de la aplicación
root.mainloop()
