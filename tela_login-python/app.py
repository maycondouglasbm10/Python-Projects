import customtkinter as ctk 

ctk.set_appearance_mode('dark')

def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()

    if usuario == 'maycon' and senha == '123456':
        resultado_login.configure(text='Login feito com sucesso!', 
        text_color='green')
    else:
        resultado_login.configure(text='Login incorreto',
                                  text_color='green')

app = ctk.CTk()
app.title('Sistema  de login')
app.geometry('300x300')

Label_usuario = ctk.CTkLabel(app, text='Usuário:')
Label_usuario.pack(pady=10)

campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)


Label_senha = ctk.CTkLabel(app, text='Senha:')
Label_senha.pack(pady=10)

campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)


button_login = ctk.CTkButton(app,text='Login', command=validar_login)
button_login.pack(pady=10)

resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)
app.mainloop()