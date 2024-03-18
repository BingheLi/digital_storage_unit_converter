import webbrowser
from tkinter import *


class SolutionWindow:

    def __init__(self, parent, solution):
        self.solution_window = Toplevel(parent)
        self.solution_window.title("Conversion Solution")

        Label(self.solution_window, text=solution, font=("Arial", 12)).pack(padx=20, pady=20)


class Converter:

    def __init__(self):

        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        self.all_calculations = []

        # Set up GUI Frame
        self.storage_frame = Frame(padx=10, pady=10, bg="#FFE4E1")
        self.storage_frame.grid()

        self.storage_heading = Label(self.storage_frame,
                                     text="Digital Storage Unit Converter",
                                     font=("Arial", "16", "bold"),
                                     bg="#FFE4E1",
                                     fg="#FF69B4")
        self.storage_heading.grid(row=0, columnspan=4, pady=(0, 10))

        instructions = "Please enter a value below and " \
                       "select the units to convert from and to."
        self.storage_instructions = Label(self.storage_frame,
                                          text=instructions,
                                          wrap=250, width=40,
                                          justify="left",
                                          bg="#FFE4E1",
                                          fg="#FF69B4")
        self.storage_instructions.grid(row=1, columnspan=4, pady=(0, 10))

        self.storage_entry = Entry(self.storage_frame,
                                   font=("Arial", "14"))
        self.storage_entry.grid(row=2, column=0, padx=5, pady=5, sticky="we", columnspan=4)

        self.from_unit_label = Label(self.storage_frame, text="From:", bg="#FFE4E1", fg="#FF69B4")
        self.from_unit_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        self.from_unit_var = StringVar()
        self.from_unit_var.set("bytes")
        self.from_unit_dropdown = OptionMenu(self.storage_frame, self.from_unit_var,
                                              "bytes", "kilobytes", "megabytes", "gigabytes")
        self.from_unit_dropdown.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        self.to_unit_label = Label(self.storage_frame, text="To:", bg="#FFE4E1", fg="#FF69B4")
        self.to_unit_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        self.to_unit_var = StringVar()
        self.to_unit_var.set("kilobytes")
        self.to_unit_dropdown = OptionMenu(self.storage_frame, self.to_unit_var,
                                            "bytes", "kilobytes", "megabytes", "gigabytes")
        self.to_unit_dropdown.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        error = "Please enter a number"
        self.output_label = Label(self.storage_frame, text="",
                                  fg="#FF69B4",
                                  bg="#FFE4E1")
        self.output_label.grid(row=5, columnspan=4)

        # Buttons
        button_bg = "#FF69B4"
        self.clear_button = Button(self.storage_frame,
                                   text="Clear",
                                   bg=button_bg,
                                   fg="#FFFFFF",
                                   font=("Arial", "12", "bold"), width=12,
                                   command=self.clear_entry)
        self.clear_button.grid(row=2, column=2, padx=5, pady=5)

        self.convert_button = Button(self.storage_frame,
                                     text="Convert",
                                     bg=button_bg,
                                     fg="#FFFFFF",
                                     font=("Arial", "12", "bold"), width=12,
                                     command=self.storage_convert)
        self.convert_button.grid(row=6, columnspan=2, padx=5, pady=5)

        self.solution_button = Button(self.storage_frame,
                                      text="Show Solution",
                                      bg=button_bg,
                                      fg="#FFFFFF",
                                      font=("Arial", "12", "bold"), width=12,
                                      command=self.show_solution)
        self.solution_button.grid(row=7, columnspan=2, padx=5, pady=5)

        self.donation_button = Button(self.storage_frame,
                                      text="Donate",
                                      bg="#FFC0CB",
                                      fg="#000000",
                                      font=("Arial", "12", "bold"), width=12,
                                      command=self.open_donation_link)
        self.donation_button.grid(row=8, columnspan=2, padx=5, pady=5)

    # checks user input and if it's valid, converts value
    def check_value(self):

        has_error = "no"
        error = "Please enter a number"

        # check that user has entered a valid number...

        response = self.storage_entry.get()

        try:
            response = float(response)

        except ValueError:
            has_error = "yes"

        # Sets var_has_error so that entry box and
        # labels can be correctly formatted by formatting function
        if has_error == "yes":
            self.var_has_error.set("yes")
            self.var_feedback.set(error)
            return "invalid"

        # If we have no errors...
        else:
            # set to 'no' in case of previous errors
            self.var_has_error.set("no")

            return response

    @staticmethod
    def round_ans(val):
        return round(val, 2)

    # check value is valid and convert it
    def storage_convert(self):
        value_to_convert = self.check_value()
        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()
        set_feedback = "yes"

        if value_to_convert == "invalid":
            set_feedback = "no"

        conversion_factors = {
            "bytes": 1,
            "kilobytes": 1024,
            "megabytes": 1024 ** 2,
            "gigabytes": 1024 ** 3
        }

        if set_feedback == "yes":
            converted_value = value_to_convert * (conversion_factors[from_unit] / conversion_factors[to_unit])

            # create user output and add to calculation history
            feedback = f"{value_to_convert} {from_unit} is {self.round_ans(converted_value)} {to_unit}"
            self.var_feedback.set(feedback)

            self.all_calculations.append(feedback)

            # Delete code below when history component is working!
            print(self.all_calculations)

        self.output_answer()

    # Clears the numerical value entered
    def clear_entry(self):
        self.storage_entry.delete(0, END)

    # Shows the solution of the conversion
    def show_solution(self):
        value_to_convert = self.check_value()
        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()

        conversion_factors = {
            "bytes": 1,
            "kilobytes": 1024,
            "megabytes": 1024 ** 2,
            "gigabytes": 1024 ** 3
        }

        converted_value = value_to_convert * (conversion_factors[from_unit] / conversion_factors[to_unit])

        solution = f"{value_to_convert} {from_unit} is {converted_value} {to_unit}"

        # Display detailed solution in a new window
        SolutionWindow(self.storage_frame, solution)

    # Opens the donation link
    def open_donation_link(self):
        webbrowser.open_new("https://mmc.school.nz")

    # Shows user output and clears entry widget
    # ready for next calculation
    def output_answer(self):
        output = self.var_feedback.get()
        has_errors = self.var_has_error.get()

        if has_errors == "yes":
            # red text, pink entry box
            self.output_label.config(fg="#FF69B4")
            self.storage_entry.config(bg="#FFCCCC")

        else:
            self.output_label.config(fg="#FF69B4")
            self.storage_entry.config(bg="#FFFFFF")

        self.output_label.config(text=output)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Digital Storage Unit Converter")
    Converter()
    root.mainloop()
