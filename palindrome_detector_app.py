import tkinter as tk
from palindrome_module import is_palindrome

def check_palindrome():
    word = entry.get()
    if is_palindrome(word):
        result_label.config(text="It's a palindrome!", fg="green")
    else:
        result_label.config(text="Not a palindrome.", fg="red")

root = tk.Tk()
root.title("Palindrome Detector")

entry_label = tk.Label(root, text="Enter a word or phrase:")
entry_label.pack()

entry = tk.Entry(root, width=40)
entry.pack()

check_button = tk.Button(root, text="Check", command=check_palindrome)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()