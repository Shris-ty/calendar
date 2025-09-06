import tkinter as tk 
from tkinter import ttk
import calendar
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Calendar")
root.geometry("500x500")


img = Image.open(r"C:\\Users\\Lenovo\\OneDrive\\Pictures\\Saved Pictures\\Calender.JPEG").resize((600, 600))
final_img = ImageTk.PhotoImage(img)
labelx = tk.Label(root, image=final_img, bg="black")
labelx.place(x=20, y=20)


def show_calendar():
    try:
        month = int(month_var.get())
        year = int(year_var.get())
        cal_text = calendar.month(year, month)
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, cal_text)
    except:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, "Please select a valid month and year!")


main_frame = tk.Frame(root, bg="white")
main_frame.place(x=150, y=80)  

month_var = tk.StringVar()
year_var = tk.StringVar()

tk.Label(main_frame, text="Month:",bg="black",fg="white",font= "arial 15 bold").pack(pady=5)
month_combo = ttk.Combobox(main_frame, textvariable=month_var, values=list(range(1, 13)), state="readonly")
month_combo.pack(pady=5)


tk.Label(main_frame, text="Year:",bg="black",fg="white",font= "arial 15 bold").pack(pady=5)
year_combo = ttk.Combobox(main_frame, textvariable=year_var, values=list(range(1980, 2101)), state="readonly")
year_combo.pack(pady=5)

tk.Button(main_frame, text="Show Calendar", command=show_calendar,bg="black",fg="white",font= "arial 15 bold").pack(pady=10)


text_area = tk.Text(main_frame, height=10, width=30)
text_area.pack(pady=5)

root.mainloop()
