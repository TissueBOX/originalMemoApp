import tkinter as tk
from tkinter import filedialog, messagebox
from menubar import MenuBar

def main():
    root = tk.Tk()
    root.title('tissueMemo')
    
    # ----------------------------
    # 追加処理はこの間に入れる
    textArea = tk.Text(root, wrap="word")
    textArea.pack()

    menuBar = MenuBar()

    menuBar.makeMenuBar(root, textArea)
    
    # ここまで
    # ----------------------------
    
    root.mainloop()

main()
