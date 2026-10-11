import tkinter as tk
from fileMenuFuncs import FileMenuFuncs

class MenuBar():
    # コンストラクタ無し
    
    def makeMenuBar(self, root, textArea):
        menuBar = tk.Menu(root)
        root.config(menu = menuBar)

        # ------------------------------------------
        # ファイル
        fileMenuFuncs = FileMenuFuncs()
        
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="開く", command=lambda: fileMenuFuncs.open(textArea))
        fileMenu.add_command(label="名前を付けて保存...", command=lambda: fileMenuFuncs.save(textArea))
        fileMenu.add_separator()
        fileMenu.add_command(label="終了", command=root.quit)
        menuBar.add_cascade(label="ファイル", menu=fileMenu)  
