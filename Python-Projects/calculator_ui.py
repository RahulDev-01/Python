import tkinter as tk


# Main Calculator Class
class Calculator:
    def __init__(self, root):
        # Initialize main window
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # Stores the current mathematical expression
        self.expression = ""

        # Entry widget to display input and results
        self.entry = tk.Entry(
            root,
            font=("Arial", 20),
            borderwidth=2,
            relief="solid",
            justify="right"
        )
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # Create calculator buttons
        self.create_buttons()

    def create_buttons(self):
        """
        Creates calculator buttons and arranges them
        in rows using Frames.
        """
        buttons = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "=", "+"),
            ("C",)
        ]

        for row in buttons:
            frame = tk.Frame(self.root)
            frame.pack(expand=True, fill="both")

            for btn in row:
                tk.Button(
                    frame,
                    text=btn,
                    font=("Arial", 14),
                    command=lambda b=btn: self.on_click(b)
                ).pack(side="left", expand=True, fill="both")

    def on_click(self, value):
        """
        Handles button click events.
        """
        # Clear the calculator
        if value == "C":
            self.expression = ""
            self.entry.delete(0, tk.END)

        # Evaluate the expression
        elif value == "=":
            try:
                result = eval(self.expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
                self.expression = str(result)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.expression = ""

        # Append numbers/operators to expression
        else:
            self.expression += value
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)


# Program entry point
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
