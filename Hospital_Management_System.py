import tkinter as tk
# Create the main window
root = tk.Tk()
root.title("Hospital Management System")
# Set the size of the main window
root.geometry("500x400")
# Add labels and buttons to the main window
tk.Label(root, text="Patient Name:").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)
tk.Label(root, text="Age:").grid(row=1, column=0)
tk.Entry(root).grid(row=1, column=1)
tk.Label(root, text="Gender:").grid(row=2, column=0)
tk.Radiobutton(root, text="Male", value=1).grid(row=2, column=1)
tk.Radiobutton(root, text="Female", value=2).grid(row=2, column=2)
tk.Label(root, text="Address:").grid(row=3, column=0)
tk.Text(root, height=3, width=20).grid(row=3, column=1)
tk.Label(root, text="Contact No.:").grid(row=4, column=0)
tk.Entry(root).grid(row=4, column=1)
tk.Label(root, text="Appointment Date:").grid(row=5, column=0)
tk.Entry(root).grid(row=5, column=1)
tk.Button(root, text="Submit").grid(row=6, column=0, columnspan=2)
# Run the main event loop
root.mainloop()