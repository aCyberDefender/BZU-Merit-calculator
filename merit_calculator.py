import tkinter as tk
from tkinter import messagebox

def calculate_aggregate():
    try:
        # Get input values
        matric_obtained = float(entry_matric_obtained.get())
        matric_total = float(entry_matric_total.get())
        inter_obtained = float(entry_inter_obtained.get())
        inter_total = float(entry_inter_total.get())

        # Calculate A and B
        A = ((matric_obtained / matric_total) * 0.3) * 100
        B = ((inter_obtained / inter_total) * 0.7) * 100

        # Calculate the aggregate percentage
        aggregate_percentage = A + B

        # Display the result in a message box
        messagebox.showinfo("Aggregate Percentage", f"Your Aggregate Percentage is: {aggregate_percentage:.4f}%")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

# Create the main application window
root = tk.Tk()
root.title("BZU Merit Calculator")
root.geometry("400x300")
root.configure(bg="#2c3e50")

# Create and place the labels and entries
tk.Label(root, text="Matric Obtained Marks:", bg="#2c3e50", fg="white", font=("Arial", 12)).place(x=30, y=30)
entry_matric_obtained = tk.Entry(root, font=("Arial", 12), width=20)
entry_matric_obtained.place(x=200, y=30)

tk.Label(root, text="Matric Total Marks:", bg="#2c3e50", fg="white", font=("Arial", 12)).place(x=30, y=70)
entry_matric_total = tk.Entry(root, font=("Arial", 12), width=20)
entry_matric_total.place(x=200, y=70)

tk.Label(root, text="Inter Obtained Marks:", bg="#2c3e50", fg="white", font=("Arial", 12)).place(x=30, y=110)
entry_inter_obtained = tk.Entry(root, font=("Arial", 12), width=20)
entry_inter_obtained.place(x=200, y=110)

tk.Label(root, text="Inter Total Marks:", bg="#2c3e50", fg="white", font=("Arial", 12)).place(x=30, y=150)
entry_inter_total = tk.Entry(root, font=("Arial", 12), width=20)
entry_inter_total.place(x=200, y=150)

# Create and place the Calculate button
calculate_button = tk.Button(root, text="Calculate", font=("Arial", 14, "bold"), bg="#27ae60", fg="white", command=calculate_aggregate)
calculate_button.place(x=150, y=200)

# Run the application
root.mainloop()
