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
        self.storage_heading.grid(row=0)

        instructions = "Please enter a value below and " \
                       "then press one of the buttons to convert " \
                       "it from one storage unit to another."
        self.storage_instructions = Label(self.storage_frame,
                                          text=instructions,
                                          wrap=250, width=40,
                                          justify="left")
        self.storage_instructions.grid(row=1)

        self.storage_entry = Entry(self.storage_frame,
                                   font=("Arial", "14")
                                   )
        self.storage_entry.grid(row=2, padx=10, pady=10)

        error = "Please enter a number"
        self.output_label = Label(self.storage_frame, text="",
                                  fg="#9C0000")
        self.output_label.grid(row=3)

        # Conversion, help and history / export buttons
        self.button_frame = Frame(self.storage_frame)
        self.button_frame.grid(row=4)

        self.to_bytes_button = Button(self.button_frame,
                                      text="To Bytes",
                                      bg="#990099",
                                      fg=button_fg,
                                      font=button_font, width=12,
                                      command=lambda: self.storage_convert("bytes"))
        self.to_bytes_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_kilobytes_button = Button(self.button_frame,
                                           text="To Kilobytes",
                                           bg="#009900",
                                           fg=button_fg,
                                           font=button_font, width=12,
                                           command=lambda: self.storage_convert("kilobytes"))
        self.to_kilobytes_button.grid(row=0, column=1, padx=5, pady=5)

        self.to_megabytes_button = Button(self.button_frame,
                                          text="To Megabytes",
                                          bg="#CC6600",
                                          fg=button_fg,
                                          font=button_font, width=12,
                                          command=lambda: self.storage_convert("megabytes"))
        self.to_megabytes_button.grid(row=1, column=0, padx=5, pady=5)

        self.to_gigabytes_button = Button(self.button_frame,
                                          text="To Gigabytes",
                                          bg="#004C99",
                                          fg=button_fg,
                                          font=button_font, width=12,
                                          command=lambda: self.storage_convert("gigabytes"))
        self.to_gigabytes_button.grid(row=1, column=1, padx=5, pady=5)

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
    def storage_convert(self, target_unit):
        to_convert = self.check_value()
        set_feedback = "yes"
        answer = ""
        from_to = ""

        if to_convert == "invalid":
            set_feedback = "no"

        # Convert to bytes
        elif target_unit == "bytes":
            answer = to_convert * 1024 ** 0
            from_to = "{} {} is {} Bytes"

        # convert to Kilobytes
        elif target_unit == "kilobytes":
            answer = to_convert * 1024 ** 1
            from_to = "{} {} is {} Kilobytes"

        # Convert to Megabytes
        elif target_unit == "megabytes":
            answer = to_convert * 1024 ** 2
            from_to = "{} {} is {} Megabytes"

        # Convert to Gigabytes
        elif target_unit == "gigabytes":
            answer = to_convert * 1024 ** 3
            from_to = "{} {} is {} Gigabytes"

        if set_feedback == "yes":
            answer = self.round_ans(answer)

            # create user output and add to calculation history
            feedback = from_to.format(to_convert, target_unit, answer)
            self.var_feedback.set(feedback)

            self.all_calculations.append(feedback)

            # Delete code below when history component is working!
            print(self.all_calculations)

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
