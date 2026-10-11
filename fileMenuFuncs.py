import tkinter as tk
from tkinter import filedialog, messagebox

class FileMenuFuncs():
    # コンストラクタ無し
    
    def open(self, textArea):
        filePath = filedialog.askopenfilename(
            filetypes = [("テキストファイル", "*.txt"), ("すべてのファイル", "*.*")]
        )

        if filePath:
            try:
                with open(filePath, "r", encoding="utf-8") as file:
                    content = file.read()
                textArea.delete("1.0", tk.END)
                textArea.insert("1.0", content)
            except Exception as e:
                messagebox.showerror("エラー", f"開けませんでした:\n{e}")

    def save(self, textArea):
        filename = filedialog.asksaveasfilename(
            defaultextension = '.txt', 
            filetypes = [('テキストファイル', '*.txt')])

        if filename:
            try:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.write(textArea.get(1.0, tk.END))
                    messagebox.showinfo("保存", "ファイルを保存しました")
            except Exception as e:
                messagebox.showerror("エラー", f"保存できませんでした:\n{e}")