import tkinter as tk
from tkinter import messagebox, ttk
from Banco import Banco

class StarWarsGUI:
    def __init__(self):
        self.db = Banco()
        self.root = tk.Tk()
        self.root.title("Star Wars CRUD")

        self.tab_control = ttk.Notebook(self.root)

 
        self.tab_parceiro = ttk.Frame(self.tab_control)
        self.tab_personagem = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_parceiro, text="Parceiros")
        self.tab_control.add(self.tab_personagem, text="Personagens")
        self.tab_control.pack(expand=1, fill="both")

   
        self.setup_parceiros_tab()
  
        self.setup_personagens_tab()

        self.root.mainloop()

    def setup_parceiros_tab(self):
        frame = self.tab_parceiro
        tk.Label(frame, text="Nome").grid(row=0, column=0)
        tk.Label(frame, text="Idade").grid(row=1, column=0)
        tk.Label(frame, text="Planeta").grid(row=2, column=0)

        self.nome_parceiro = tk.Entry(frame)
        self.idade_parceiro = tk.Entry(frame)
        self.planeta_parceiro = tk.Entry(frame)

        self.nome_parceiro.grid(row=0, column=1)
        self.idade_parceiro.grid(row=1, column=1)
        self.planeta_parceiro.grid(row=2, column=1)

        tk.Button(frame, text="Adicionar", command=self.add_parceiro).grid(row=3, column=0)
        tk.Button(frame, text="Listar", command=self.listar_parceiros).grid(row=3, column=1)

        self.listbox_parceiros = tk.Listbox(frame, width=50)
        self.listbox_parceiros.grid(row=4, column=0, columnspan=2)

    def add_parceiro(self):
        nome = self.nome_parceiro.get()
        idade = self.idade_parceiro.get()
        planeta = self.planeta_parceiro.get()
        if not nome or not idade or not planeta:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        if self.db.add_parceiro(nome, int(idade), planeta):
            messagebox.showinfo("Sucesso", "Parceiro adicionado!")
        else:
            messagebox.showerror("Erro", "Nome duplicado!")
        self.listar_parceiros()

    def listar_parceiros(self):
        self.listbox_parceiros.delete(0, tk.END)
        for parceiro in self.db.listar_parceiros():
            self.listbox_parceiros.insert(tk.END, parceiro)

    def setup_personagens_tab(self):
        frame = self.tab_personagem
        labels = ["Nome", "Classe", "Ranque", "Arma", "Filiação", "Moralidade", "ID do Parceiro"]
        self.entries_personagem = {}

        for i, label in enumerate(labels):
            tk.Label(frame, text=label).grid(row=i, column=0)
            entry = tk.Entry(frame)
            entry.grid(row=i, column=1)
            self.entries_personagem[label] = entry

        tk.Button(frame, text="Adicionar", command=self.add_personagem).grid(row=len(labels), column=0)
        tk.Button(frame, text="Listar", command=self.listar_personagens).grid(row=len(labels), column=1)

        self.listbox_personagens = tk.Listbox(frame, width=100)
        self.listbox_personagens.grid(row=len(labels)+1, column=0, columnspan=2)

    def add_personagem(self):
        data = {label: self.entries_personagem[label].get() for label in self.entries_personagem}
        if not all(data.values()):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        if self.db.add_personagem(data["Nome"], data["Classe"], data["Ranque"], data["Arma"],
                                  data["Filiação"], data["Moralidade"], int(data["ID do Parceiro"])):
            messagebox.showinfo("Sucesso", "Personagem adicionado!")
        else:
            messagebox.showerror("Erro", "Erro ao adicionar personagem!")
        self.listar_personagens()

    def listar_personagens(self):
        self.listbox_personagens.delete(0, tk.END)
        for p in self.db.listar_personagens():
            self.listbox_personagens.insert(tk.END, p)
