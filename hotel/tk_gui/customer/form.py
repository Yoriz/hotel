import tkinter as tk
from tkinter import ttk

from data.classes import Customer
from tk_gui.tk_helper.tk_entry import change_entry

EVENT_CUSTOMER_SAVE = "<<CustomerSave>>"
EVENT_CUSTOMER_CANCEL = "<<CustomerCancel>>"


class CustomerForm(tk.Toplevel):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.title("Customer Form")
        self.resizable(width=False, height=False)
        self.create_controls()
        self.layout_controls()
        self.bind_events()

    def create_controls(self) -> None:
        self.control_grid = ControlGrid(master=self)
        self.button_frame = ButtonFrame(master=self)

    def layout_controls(self) -> None:
        self.control_grid.pack()
        self.button_frame.pack(side="right")

    def bind_events(self) -> None:
        self.button_frame.save_button.bind("<Button-1>", self.on_button_save)
        self.button_frame.cancel_button.bind("<Button-1>", self.on_button_cancel)

    def on_button_save(self, event) -> None:
        self.event_generate(EVENT_CUSTOMER_SAVE)

    def on_button_cancel(self, event) -> None:
        self.event_generate(EVENT_CUSTOMER_CANCEL)

    def update_customer_display(self, customer: Customer) -> None:
        self.control_grid.update_customer_display(customer)

    def get_customer(self) -> Customer:
        return self.control_grid.get_customer()


class ControlGrid(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.create_controls()
        self.layout_controls()

    def create_controls(self) -> None:
        self.id_label = ttk.Label(master=self, text="ID:")
        self.id_display = ttk.Label(master=self)
        self.first_name_label = ttk.Label(master=self, text="First Name:")
        self.first_name_entry = ttk.Entry(master=self, width=30)
        self.last_name_label = ttk.Label(master=self, text="Last Name:")
        self.last_name_entry = ttk.Entry(master=self, width=30)
        self.email_address_label = ttk.Label(master=self, text="Email:")
        self.email_address_entry = ttk.Entry(master=self, width=30)

    def layout_controls(self) -> None:
        self.id_label.grid(row=0, column=0, pady=2, padx=2)
        self.id_display.grid(row=0, column=1, pady=2, padx=2, sticky="w")
        self.first_name_label.grid(row=1, column=0, pady=2, padx=2)
        self.first_name_entry.grid(row=1, column=1, pady=2, padx=2)
        self.last_name_label.grid(row=2, column=0, pady=2, padx=2)
        self.last_name_entry.grid(row=2, column=1, pady=2, padx=2)
        self.email_address_label.grid(row=3, column=0, pady=2, padx=2, sticky="E")
        self.email_address_entry.grid(row=3, column=1, pady=2, padx=2)

    def update_customer_display(self, customer: Customer) -> None:
        self.id_display.config(text=str(customer.id))
        change_entry(entry=self.first_name_entry, string=customer.first_name)
        change_entry(entry=self.last_name_entry, string=customer.last_name)
        change_entry(entry=self.email_address_entry, string=customer.email_address)

    def get_customer(self) -> Customer:
        id_ = int(self.id_display.cget("text"))
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email_address = self.email_address_entry.get()
        return Customer(
            id=id_,
            first_name=first_name,
            last_name=last_name,
            email_address=email_address,
        )


class ButtonFrame(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.create_controls()
        self.layout_controls()

    def create_controls(self) -> None:
        self.save_button = ttk.Button(master=self, text="Save")
        self.cancel_button = ttk.Button(master=self, text="Cancel")

    def layout_controls(self) -> None:
        self.save_button.pack(side="right", padx=2, pady=2)
        self.cancel_button.pack(side="right", padx=2, pady=2)


def main():
    customer = Customer(
        id=1,
        first_name="First name",
        last_name="Last name",
        email_address="Email address",
    )
    main_window = tk.Tk()
    customer_form = CustomerForm(main_window)
    customer_form.update_customer_display(customer=customer)

    def test_customer_save_event(event):
        customer = customer_form.get_customer()
        print(customer)

    customer_form.bind(EVENT_CUSTOMER_SAVE, test_customer_save_event)
    main_window.mainloop()


if __name__ == "__main__":
    main()
