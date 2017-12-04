from tkinter import *
from tkinter import ttk
import subcontrol
import serial

# need to add serial support


target_rpm = 1500
target_ph = 7
target_temp = 30

class Menu:
    def __init__(self, root):
        self.master = root
        self.master.title("Bioreactor Controller Team 9")
        self.master.geometry("200x300")

        self.heat_control, self.mix_control, self.ph_control = None, None, None

        Label(text="Bioreactor Controller").grid(row=0, column=1, sticky=N)
        Label(text="-- by ENGS101P 2nd Project Team 9").grid(row=1, column=1, sticky=N)

        self.mix_button = ttk.Button(self.master, text="Mixing Control", command=self.open_mix)
        self.mix_button.grid(row=2, column=1, sticky=N, padx=2, pady=6)
        self.heat_button = ttk.Button(self.master, text="Heating Control", command=self.open_heat)
        self.heat_button.grid(row=3, column=1, sticky=N, padx=2, pady=6)
        self.ph_button = ttk.Button(self.master, text="pH Control", command=self.open_ph)
        self.ph_button.grid(row=4, column=1, sticky=N, padx=2, pady=6)

        self.exit_button = ttk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.grid(row=5, column=1, sticky=N, padx=2, pady=20)
        # set_spacing(self.master, 6, 40)

        self.heat_control = subcontrol.SubControl(self.master, "Heating Control", "Target Temperature: " + str(target_temp),
                                                  "Current Temperature: Unknown")
        self.mix_control = subcontrol.SubControl(self.master, "Mixing Control", "Target RPM: " + str(target_rpm),
                                                  "Current RPM: Unknown")
        self.ph_control = subcontrol.SubControl(self.master, "Ph Control", "Target Ph: " + str(target_ph),
                                                  "Current Ph: Unknown")

        self.heat_control.hide()
        self.ph_control.hide()
        self.mix_control.hide()

    def open_mix(self):
        self.mix_control.show()

    def open_heat(self):
        self.heat_control.show()

    def open_ph(self):
        self.ph_control.show()


def main():
    root = Tk()
    menu = Menu(root)
    root.mainloop()


if __name__ == '__main__':
    main()
