from subcontrol import SubControl
from tkinter import messagebox


class HeatControl(SubControl):
    def capture(self):
        try:
            temp = float(self.entry.get())
            if not (25 <= temp and temp <= 35):
                raise ValueError
            self.target_var.set("Target Temperature: " + str(temp) + "C")
            self.ser.write("TTEM" + str(temp))
        except ValueError:
            messagebox.showerror("Error", "Target temperature can only be a number between 25 and 35")
