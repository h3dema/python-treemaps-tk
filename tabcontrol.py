import tkinter as tk
from tkinter import ttk


class TabControl(ttk.Notebook):

    """
      Classe simples que implementa um controle com guias.
      Você pode inserir o seu conteúdo dentro das guias que são Frames.
    """

    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.tabs = []

    def add_tab(self, text: str) -> ttk.Frame:
        tab = ttk.Frame(self)
        self.add(tab, text=text)
        self.tabs.append(tab)
        return tab

    def get_tab(self, num: int) -> ttk.Frame:
        if num < 0 or num >= len(self.tabs):
            return None
        return self.tabs[num]

    def delete_tab(self, num: int):
        if num < 0 or num >= len(self.tabs):
            return
        self.tabs[num].destroy()

    @property
    def num_tabs(self) -> int:
        return len(self.tabs)


if __name__ == "__main__":
    app = tk.Tk()
    app.title("Tab Widget")

    tabControl = TabControl(app)
    tabControl.add_tab("Tab1")
    tabControl.add_tab("Tab2")

    tabControl.pack(expand=1, fill="both")

    #
    # conteudo do tab 1
    #
    ttk.Label(
        tabControl.get_tab(0),
        text="Este controle utiliza notebooks"
    ).grid(
        column=0,
        row=0,
        padx=30,
        pady=30)

    ttk.Label(
        tabControl.get_tab(0),
        text="Ao clicar em uma dessas guias, o widget Notebook exibirá um painel filho associado à guia selecionada. Em nosso caso, este painel filho é um Frame."
    ).grid(
        column=0,
        row=1,
        padx=30,
        pady=30)

    #
    # conteudo do tab 2
    #
    ttk.Label(
        tabControl.get_tab(1),
        text="Este é o conteudo na segunda guia"
    ).grid(
        column=0,
        row=3,
        padx=30,
        pady=30)

    from threading import Timer

    def remove():
        tabControl.delete_tab(1)
        print("Deleted #1")
    Timer(30, remove).start()

    app.mainloop()

