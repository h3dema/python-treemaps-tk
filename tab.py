from tkinter import *

from texto import MachadoAssis
from stack import PageTreemapWords, PageTreemapLetters
from tabcontrol import TabControl


if __name__ == "__main__":
    from plots import set_figsize
    set_figsize(size=(10, 9))

    texto = MachadoAssis()
    N = 20

    # Create a GUI app
    app = Tk()

    # Give a title to your app
    app.title("Treemaps")

    tabControl = TabControl(app)
    frame1 = tabControl.add_tab("Treemap com letras")
    frame2 = tabControl.add_tab(f"Treemap com #{N} palavras")

    # treemap no primeiro tab
    t1 = PageTreemapLetters(frame1, controller=None, texto=texto)
    t1.pack()

    # treemap no segundo tab
    t2 = PageTreemapWords(frame2, controller=None, texto=texto, N=N)
    t2.pack()

    tabControl.pack(expand=1, fill="both")

    # posiciona a janela principal
    # ref. https://github.com/tcltk/tk/blob/master/library/tk.tcl#L72
    app.eval('tk::PlaceWindow . center')
    # Make the loop for displaying app
    app.mainloop()
