import tkinter as tk
from tkinter import ttk, messagebox
import re

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.contacts = []

        # Country Data
        self.countries = {
            "USA": "+1",
            "UK": "+44",
            "India": "+91"
            # Add more countries as needed
        }

        # Add Contact Frame
        self.add_frame = tk.LabelFrame(root, text="Add Contact")
        self.add_frame.pack(padx=10, pady=10, fill="both")

        self.name_label = tk.Label(self.add_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.add_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(self.add_frame, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(self.add_frame)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.phone_suggestion_label = tk.Label(self.add_frame, text="Phone Suggestion:")
        self.phone_suggestion_label.grid(row=1, column=2, padx=5, pady=5, sticky='w')

        self.email_label = tk.Label(self.add_frame, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(self.add_frame)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.email_suggestion_label = tk.Label(self.add_frame, text="Email Suggestion:")
        self.email_suggestion_label.grid(row=2, column=2, padx=5, pady=5, sticky='w')

        self.address_label = tk.Label(self.add_frame, text="Address:")
        self.address_label.grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(self.add_frame)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.add_frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=3, pady=10)

        # Contact List Frame
        self.list_frame = tk.LabelFrame(root, text="Contacts")
        self.list_frame.pack(padx=10, pady=10, fill="both")

        self.contacts_list = tk.Listbox(self.list_frame, height=10)
        self.contacts_list.pack(side="left", fill="both", expand=True)
        self.contacts_list.bind('<<ListboxSelect>>', self.load_contact)

        self.scrollbar = tk.Scrollbar(self.list_frame, orient="vertical")
        self.scrollbar.config(command=self.contacts_list.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.contacts_list.config(yscrollcommand=self.scrollbar.set)

        # Buttons Frame
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack(padx=10, pady=10, fill="x")

        self.view_button = tk.Button(self.buttons_frame, text="View All Contacts", command=self.view_contacts)
        self.view_button.pack(side="left", padx=5)

        self.search_button = tk.Button(self.buttons_frame, text="Search Contact", command=self.search_contact)
        self.search_button.pack(side="left", padx=5)

        self.update_button = tk.Button(self.buttons_frame, text="Update Contact", command=self.update_contact)
        self.update_button.pack(side="left", padx=5)

        self.delete_button = tk.Button(self.buttons_frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(side="left", padx=5)

        # Bind country selection change to update suggestions
        self.country_combobox = ttk.Combobox(self.add_frame, values=list(self.countries.keys()))
        self.country_combobox.grid(row=0, column=2, padx=5, pady=5)
        self.country_combobox.set("Select Country")
        self.country_combobox.bind("<<ComboboxSelected>>", self.update_suggestions)

    def update_suggestions(self, event):
        selected_country = self.country_combobox.get()
        if selected_country in self.countries:
            country_code = self.countries[selected_country]
            example_phone = f"{country_code}1234567890"  # Example phone number format
            example_email = f"example@{selected_country.lower()}.com"  # Example email format
            self.phone_suggestion_label.config(text=f"Phone Suggestion: {example_phone}")
            self.email_suggestion_label.config(text=f"Email Suggestion: {example_email}")
        else:
            self.phone_suggestion_label.config(text="Phone Suggestion:")
            self.email_suggestion_label.config(text="Email Suggestion:")

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone and email and address:
            if self.validate_email(email) and self.validate_phone(phone):
                self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
                messagebox.showinfo("Success", "Contact added successfully")
                self.clear_entries()
            else:
                messagebox.showwarning("Input Error", "Please enter a valid email and phone number")
        else:
            messagebox.showwarning("Input Error", "Please fill in all fields")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def view_contacts(self):
        self.contacts_list.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def load_contact(self, event):
        selected_contact_index = self.contacts_list.curselection()
        if selected_contact_index:
            index = selected_contact_index[0]
            contact = self.contacts[index]

            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, contact['name'])

            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(tk.END, contact['phone'])

            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, contact['email'])

            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(tk.END, contact['address'])

    def search_contact(self):
        search_term = self.name_entry.get() or self.phone_entry.get()
        self.contacts_list.delete(0, tk.END)
        for contact in self.contacts:
            if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
                self.contacts_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

    def update_contact(self):
        selected_contact_index = self.contacts_list.curselection()
        if selected_contact_index:
            index = selected_contact_index[0]
            if self.validate_email(self.email_entry.get()) and self.validate_phone(self.phone_entry.get()):
                self.contacts[index] = {
                    "name": self.name_entry.get(),
                    "phone": self.phone_entry.get(),
                    "email": self.email_entry.get(),
                    "address": self.address_entry.get()
                }
                messagebox.showinfo("Success", "Contact updated successfully")
                self.view_contacts()
            else:
                messagebox.showwarning("Input Error", "Please enter a valid email and phone number")
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to update")

    def delete_contact(self):
        selected_contact_index = self.contacts_list.curselection()
        if selected_contact_index:
            index = selected_contact_index[0]
            del self.contacts[index]
            messagebox.showinfo("Success", "Contact deleted successfully")
            self.view_contacts()
        else:
            messagebox.showwarning("Selection Error", "Please select a contact to delete")

    def validate_email(self, email):
        email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(email_regex, email)

    def validate_phone(self, phone):
        phone_regex = r'^\+?1?\d{9,15}$'
        return re.match(phone_regex, phone)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
