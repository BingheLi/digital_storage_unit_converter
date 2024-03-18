from tkinter import *


class Converter:

    def __init__(self):

        # Initialise variables (such as the feedback variable)
        self.var_feedback = StringVar()
        self.var_feedback.set("")

        self.var_has_error = StringVar()
        self.var_has_error.set("no")

        self.all_calculations = []

        # common format for all buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # Set up GUI Frame
        self.storage_frame = Frame(padx=10, pady=10)
        self.storage_frame.grid()

        self.storage_heading = Label(self.storage_frame,
                                     text="Digital Storage Unit Converter",
                                     font=("Arial", "16", "bold")
                                     )
        self.storage_heading.grid(row=0, columnspan=4)

        instructions = "Please enter a value below and " \
                       "select the units to convert from and to."
        self.storage_instructions = Label(self.storage_frame,
                                          text=instructions,
                                          wrap=250, width=40,
                                          justify="left")
        self.storage_instructions.grid(row=1, columnspan=4)

        self.storage_entry = Entry(self.storage_frame,
                                   font=("Arial", "14"))
        self.storage_entry.grid(row=2, column=0, padx=5, pady=5)

        self.from_unit_label = Label(self.storage_frame, text="From:")
        self.from_unit_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        self.from_unit_var = StringVar()
        self.from_unit_var.set("bytes")
        self.from_unit_dropdown = OptionMenu(self.storage_frame, self.from_unit_var,
                                              "bytes", "kilobytes", "megabytes", "gigabytes")
        self.from_unit_dropdown.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        self.to_unit_label = Label(self.storage_frame, text="To:")
        self.to_unit_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        self.to_unit_var = StringVar()
        self.to_unit_var.set("kilobytes")
        self.to_unit_dropdown = OptionMenu(self.storage_frame, self.to_unit_var,
                                            "bytes", "kilobytes", "megabytes", "gigabytes")
        self.to_unit_dropdown.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        error = "Please enter a number"
        self.output_label = Label(self.storage_frame, text="",
                                  fg="#9C0000")
        self.output_label.grid(row=5, columnspan=4)

        # Buttons
        self.clear_button = Button(self.storage_frame,
                                   text="Clear",
                                   bg="#CC6600",
                                   fg=button_fg,
                                   font=button_font, width=12,
                                   command=self.clear_entry)
        self.clear_button.grid(row=2, column=1, padx=5, pady=5)

        self.convert_button = Button(self.storage_frame,
                                     text="Convert",
                                     bg="#004C99",
                                     fg=button_fg,
                                     font=button_font, width=12,
                                     command=self.storage_convert)
        self.convert_button.grid(row=6, columnspan=2, padx=5, pady=5)

        self.solution_button = Button(self.storage_frame,
                                      text="Show Solution",
                                      bg="#009900",
                                      fg=button_fg,
                                      font=button_font, width=12,
                                      command=self.show_solution)
        self.solution_button.grid(row=7, columnspan=2, padx=5, pady=5)

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

    # Shows how the units are converted
    def show_solution(self):
        from_unit = self.from_unit_var.get()
        to_unit = self.to_unit_var.get()
        conversion_factors = {
            "bytes": 1,
            "kilobytes": 1024,
            "megabytes": 1024 ** 2,
            "gigabytes": 1024 ** 3
        }
        solution = f"1 {from_unit} = {conversion_factors[from_unit] / conversion_factors[to_unit]} {to_unit}"
        self.var_feedback.set(solution)
        self.output_answer()

    # Shows user output and clears entry widget
    # ready for next calculation
    def output_answer(self):
        output = self.var_feedback.get()
        has_errors = self.var_has_error.get()

        if has_errors == "yes":
            # red text, pink entry box
            self.output_label.config(fg="#9C0000")
            self.storage_entry.config(bg="#F8CECC")

        else:
            self.output_label.config(fg="#004C00")
            self.storage_entry.config(bg="#FFFFFF")

        self.output_label.config(text=output)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Digital Storage Unit Converter")
    Converter()
    root.mainloop()
