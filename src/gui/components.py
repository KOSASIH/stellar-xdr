import tkinter as tk
from tkinter import scrolledtext
from src.encoder import encode_batch
from src.decoder import decode_batch
from src.xdr_types import Transaction, AccountID

class XDRFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        # Input for transactions
        self.input_label = tk.Label(self, text="Enter Transactions (source,destination,amount):")
        self.input_label.pack()

        self.input_text = scrolledtext.ScrolledText(self, height=5)
        self.input_text.pack(pady=5)

        # Encode button
        self.encode_button = tk.Button(self, text="Encode to XDR", command=self.encode_to_xdr)
        self.encode_button.pack(pady=5)

        # Output for XDR
        self.output_label = tk.Label(self, text="Encoded XDR:")
        self.output_label.pack()

        self.output_text = tk.Text(self, height=5, state='disabled')
        self.output_text.pack(pady=5)

        # Decode button
        self.decode_button = tk.Button(self, text="Decode from XDR", command=self.decode_from_xdr)
        self.decode_button.pack(pady=5)

        # Input for XDR
        self.xdr_input_label = tk.Label(self, text="Enter XDR (hex):")
        self.xdr_input_label.pack()

        self.xdr_input_text = tk.Entry(self)
        self.xdr_input_text.pack(pady=5)

    def encode_to_xdr(self):
        try:
            transactions_data = self.input_text.get("1.0", tk.END).strip().splitlines()
            transactions = []
            for tx_data in transactions_data:
                source_id, destination_id, amount = tx_data.split(',')
                transaction = Transaction(AccountID(source_id.strip()), AccountID(destination_id.strip()), float(amount.strip()))
                transactions.append(transaction)
            xdr_data = encode_batch(transactions)
            self.output_text.config(state='normal')
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, xdr_data.hex())
            self.output_text.config(state='disabled')
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decode_from_xdr(self):
        try:
            xdr_hex = self.xdr_input_text.get().strip()
            xdr_bytes = bytes.fromhex(xdr_hex)
            transactions = decode_batch(xdr_bytes)
            decoded_transactions = "\n".join(f"{tx.source.account_id} -> {tx.destination.account_id}, Amount: {tx.amount}" for tx in transactions)
            messagebox.showinfo("Decoded Transactions", decoded_transactions)
        except Exception as e:
            messagebox.showerror("Error", str(e))
