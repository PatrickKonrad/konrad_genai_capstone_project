import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog

def save_to_file(some_key):
    save_file = open("key.txt", 'w')
    save_file.write(some_key)
    save_file.close

def enter_openai_key():
    key = simpledialog.askstring("Input", "Enter your OpenAI Key:", parent=root)
    save_to_file(key)
    messagebox.showinfo("OpenAI key", "OpenAI key has been saved. To logout re-enter key, but leave the input blank.")
        
root = tk.Tk()

root.title("Virtual Assistant for the Digital Humanities")
root.geometry("500x500")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Authorize/Deauthorize OpenAI", command=enter_openai_key)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

label = tk.Label(root, text="Virtual Assistant for the DH", font=('Arial', 18 ))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

output_btn_label = tk.Label(root, text= "Output format", font=('Arial', 14))
output_btn_label.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)
buttonframe.columnconfigure(3, weight=1)

btn1 = tk.Button(buttonframe, text ="csv", font=("Arial", 16))
btn1.grid(row=0, column=0,sticky=tk.W+tk.E)
btn2 = tk.Button(buttonframe, text ="json", font=("Arial", 16))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe, text ="pd df", font=("Arial", 16))
btn3.grid(row=0, column=2,sticky=tk.W+tk.E)
btn4 = tk.Button(buttonframe, text ="csv", font=("Arial", 16))
btn4.grid(row=0, column=3,sticky=tk.W+tk.E)
buttonframe.pack(fill='x')

task_label = tk.Label(root, text= "DH Tasks", font=('Arial', 14))
task_label.pack()

buttonframe2 = tk.Frame(root)
buttonframe2.columnconfigure(0, weight=1)
buttonframe2.columnconfigure(1, weight=1)
buttonframe2.columnconfigure(2, weight=1)
buttonframe2.columnconfigure(3, weight=1)

btn5 = tk.Button(buttonframe2, text ="NER", font=("Arial", 16))
btn5.grid(row=0, column=0,sticky=tk.W+tk.E)
btn6 = tk.Button(buttonframe2, text ="Summarize", font=("Arial", 16))
btn6.grid(row=0, column=1, sticky=tk.W+tk.E)
btn7 = tk.Button(buttonframe2, text ="Keywords", font=("Arial", 16))
btn7.grid(row=0, column=2,sticky=tk.W+tk.E)
btn8 = tk.Button(buttonframe2, text ="Sentiment A.", font=("Arial", 16))
btn8.grid(row=0, column=3,sticky=tk.W+tk.E)
buttonframe2.pack(fill='x')

#myenty = tk.Entry(root)
#myenty.pack()

root.mainloop()

