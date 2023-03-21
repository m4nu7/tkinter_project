from functionPkg.functions import *
root = tk.Tk()
root.title("Search and Merge PDF ")
root.configure(bg = "#F9E9A0")              # we can also use root["bg"] = "#F9E9A0"......bg or background can be used

# get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# window size
window_width = 1000
window_height = 600

# find centers
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

# window geometry
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# path label
label1 = tk.Label(root, text="Search Path : ", bd=5, bg="#F9E9A0", fg="#010E0B", padx=10, pady=10)
label1.grid(row=0, column=0)

# path entry
e1 = tk.Entry(root, width=100, bd=5, bg="#ECF2F1", fg="black")
e1.grid(row=0, column=1)

# search button
button1 = tk.Button(root, text="Search", bg="#98E4F7", fg="#130D64", width=20, command=lambda: searchdir(e1, e2))
button1.grid(row=0, column=2)

# Text widget label
label1 = tk.Label(root, text=" List of folders/files in the path specified : ", bd=5, bg="#F9E9A0", fg="#010E0B",
                  padx=10, pady=10)
label1.grid(row=1, column=0)

# Text widget scrollbar
sb = tk.Scrollbar(root, orient="vertical")
sb.grid(row=2, column=2, ipady=80)

e2 = tk.Text(root, height=20, width=80, bg="#ECF2F1", fg="black", wrap="word")
e2.grid(row=2, column=1)

e2.config(yscrollcommand=sb.set)
sb.config(command=e2.yview)

# Merge button
button2 = tk.Button(root, text="Merge PDF", bg="#98E4F7", fg="#130D64", width=20,
                    command=lambda: appendPdf(pdflistgen, e1, e3))
button2.grid(row=3, column=1)

# Message display Text box
e3 = tk.Text(root, height=5, width=80, bg="#ECF2F1", fg="black", wrap="word")
e3.grid(row=4, column=1)


root.mainloop()