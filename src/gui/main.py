import tkinter as tk
from tkinter import messagebox
from .components import XDRFrame

class StellarXDRApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Stellar XDR Encoder/Decoder")
        self.geometry("600x400")
        self.create_widgets()

    def create_widgets(self):
        # Create and pack the XDR frame
        xdr_frame = XDRFrame(self)
        xdr_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = StellarXDRApp()
    app.mainloop()
