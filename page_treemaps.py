import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from plots import plot_treemap_letters, plot_treemap_words

# fonte padrão do texto nas imagens
DEFAULT_FONT = ("Verdana", 12)


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

