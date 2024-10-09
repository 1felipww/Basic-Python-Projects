import tkinter as tk

def button_click(value):
    if value == "=":
        try:
            expression = entry.get()
            result = eval(expression.replace("x", "*"))  # Change "x" to "*"
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    elif value == "x":
        entry.insert(tk.END, "")
    else:
        entry.insert(tk.END, value)

calculator = tk.Tk()
calculator.title("Calculator")
calculator.geometry("305x465")
calculator.configure(bg="#1e1e1e")

label = tk.Label(calculator, text="Calculator", bg="#1e1e1e", fg="white", font=('Segoe UI', 18))
label.grid(row=0, column=0, columnspan=4, pady=5)

entry = tk.Entry(calculator, width=14, font=('Segoe UI', 28), borderwidth=2, relief="solid", justify='right')
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

buttons = [
    '7', '8', '9', 'C',
    '4', '5', '6', 'x',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
]

bg_color = "#2a2a2a"
text_color = "white"
operator_bg_color = "#3a3a3a"

row = 2
column = 0
for button in buttons:
    bg = operator_bg_color if button in ['C', 'x', '-', '+', '=', 'C'] else bg_color

    tk.Button(
        calculator,
        text=button,
        width=5,
        height=2,
        font=('Segoe UI', 16),
        bg=bg,
        fg=text_color,
        activebackground="#4cc2ff",
        activeforeground="white",
        command=lambda value=button: button_click(value)
    ).grid(row=row, column=column, padx=3, pady=3)

    column += 1
    if column > 3:
        column = 0
        row += 1

calculator.mainloop()
