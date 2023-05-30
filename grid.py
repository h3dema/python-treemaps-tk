import sys
from tkinter import *

from texto import MachadoAssis
from stack import PageTreemapWords, PageTreemapLetters


if __name__ == "__main__":
    from plots import set_figsize
    set_figsize(size=(10, 9))

    texto = MachadoAssis()
    N = 20

    # Create a GUI app
    app = Tk()

    # Give a title to your app
    app.title("Treemaps")

    # por Letras
    frame1 = LabelFrame(app,
                        text="Treemap com letras",
                        bg="green",
                        fg="white", padx=15, pady=15)

    # coloca o frame1 na posição [0, 0] -> linha coluna
    frame1.grid(row=0, column=0)
    # treemap
    t1 = PageTreemapLetters(frame1, controller=None, texto=texto)
    t1.pack()

    # segundo frame ->
    frame2 = LabelFrame(app,
                        text=f"Treemap com #{N} palavras",
                        bg="yellow",
                        padx=15, pady=15)
    frame2.grid(row=0, column=1)
    # treemap
    t1 = PageTreemapWords(frame2, controller=None, texto=texto, N=N)
    t1.pack()

    # Define a function to close the window
    def close_win():
        app.destroy()
        sys.exit()

    btn = Button(app,
                 text="Close",
                 font=('Poppins bold', 16),
                 command=close_win)
    btn.grid(row=1, column=1, sticky="E")

    # posiciona a janela principal
    # ref. https://github.com/tcltk/tk/blob/master/library/tk.tcl#L72
    app.eval('tk::PlaceWindow . center')
    # Make the loop for displaying app
    app.mainloop()
