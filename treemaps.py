import os
import platform
import matplotlib

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import tkinter as tk
from tkinter import ttk

from texto import MachadoAssis
from plots import plot_treemap_letters, plot_treemap_words

import warnings
# para ocultar algumas mensagens do Tkinter
warnings.filterwarnings('ignore', category=UserWarning)

# precisamos informar ao matplotlib para ele utilizar Tk
matplotlib.use("TkAgg")

# fonte padrão do texto nas imagens
DEFAULT_FONT = ("Verdana", 12)

# o icon da janela precisa do caminho completo (Linux)
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


class Controller(tk.Tk):

    def __init__(self, pages: list = [], *args, **kwargs):
        texto = MachadoAssis()
        N = 20

        tk.Tk.__init__(self, *args, **kwargs)

        if 'windows' in platform.platform().lower():
            tk.Tk.iconbitmap(self, default="matplotlib.ico")  # Windows
        elif 'linux' in platform.platform().lower():
            tk.Tk.iconbitmap(self, f"@{CURRENT_PATH}/matplotlib.xbm")
        else:
            raise Exception('Platform not supported')
        tk.Tk.wm_title(self, "Treemaps examples")

        # criar o frame (janela) para apresentacao
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        #
        # criar as frames de desenho
        #
        self.frames = [[] for _ in range(len(pages) + 1)]
        refs = {}
        for i, F in enumerate(pages):
            # cria um frame para cada página que desejamos apresentar
            frame = F(self.container, self, texto, N=N)
            frame.grid(row=0, column=0, sticky="nsew")
            frame.forget()  # para garantir que esteja escondida
            self.frames[i + 1] = frame
            refs[i + 1] = F.__description__
        #
        # configura a página inicial
        #
        self.frames[0] = StartPage(self.container, self, refs)
        self.frames[0].grid(row=0, column=0, sticky="nsew")

        self.currPage = 0
        self.show_frame(0)  # primeira página da lista é "página inicial"

    def show_frame(self, newPage: int):
        assert 0 <= newPage < len(self.frames)

        self.frames[self.currPage].forget()
        frame = self.frames[newPage]
        frame.tkraise()
        self.currPage = newPage  # atualiza qual é a página corrente
        self.container.pack()
        print("->", newPage, frame)


class StartPage(tk.Frame):
    """ cria um frame com um link (botao) para acesso a cada uma das páginas que foram criadas
    """

    __description__ = "Start page"

    def __init__(self, parent, controller, refs):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Selecione o gráfico desejado", font=DEFAULT_FONT)
        label.pack(pady=10, padx=10)

        buttons = {}
        for i, frame_description in refs.items():
            buttons[i] = ttk.Button(
                self,
                text=f"Go to `{frame_description}`",
                command=lambda: controller.show_frame(i),
                width=100,
            )
            buttons[i].pack()
            print(f"Button #{i}: {frame_description}")


class PageTreemapLetters(tk.Frame):

    __description__ = "Treemap com letras"

    def __init__(self, parent, controller, texto, *args, **kwargs):
        self.texto = texto
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Treemap com letras", font=DEFAULT_FONT)
        label.pack(pady=10, padx=10)

        f = plot_treemap_letters(texto)

        canvas = FigureCanvasTkAgg(f, self)
        toolbar = NavigationToolbar2Tk(canvas, self)

        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        if controller is not None:
            button1 = ttk.Button(self,
                                 text="Back to menu",
                                 command=lambda: controller.show_frame(0))
            button1.pack()


class PageTreemapWords(tk.Frame):

    __description__ = "Treemap com palavras"

    def __init__(self, parent, controller, texto, N, *args, **kwargs):
        self.texto = texto
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Treemap com palavras", font=DEFAULT_FONT)
        label.pack(pady=10, padx=10)

        f = plot_treemap_words(texto, N)

        canvas = FigureCanvasTkAgg(f, self)
        toolbar = NavigationToolbar2Tk(canvas, self)

        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        if controller is not None:
            button1 = ttk.Button(self,
                                 text="Back to menu",
                                 command=lambda: controller.show_frame(0))
            button1.pack()


if __name__ == "__main__":
    app = Controller(pages=[PageTreemapLetters, PageTreemapWords])
    app.mainloop()
