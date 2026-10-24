
import customtkinter as ctk
from tkinter import ttk, messagebox


class DonorRecordsScreen(ctk.CTkFrame):

    def __init__(self, master, on_back):
        super().__init__(master)

        self.on_back = on_back

        # Temporary sample data
        # The database will replace this later.
        self.donations = [
            {
                "number": "1",
                "date": "2026-10-10",
                "name": "Jane Smith",
                "address": "123 Main Street",
                "amount": 100.00,
                "method": "Cheque"
            },
            {
                "number": "2",
                "date": "2026-10-12",
                "name": "John Brown",
                "address": "45 Oak Avenue",
                "amount": 50.00,
                "method": "Cash"
            },
            {
                "number": "3",
                "date": "2026-10-15",
                "name": "Mary Wilson",
                "address": "78 Park Road",
                "amount": 250.00,
                "method": "Online"
            }
        ]

        self.create_widgets()
        self.display_donations()

    def create_widgets(self):

        # Screen heading
        heading = ctk.CTkLabel(
            self,
            text="Donor Records",
            font=("Arial", 28, "bold")
        )
        heading.pack(anchor="w", padx=25, pady=(25, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Search and manage donation records.",
            font=("Arial", 14)
        )
        subtitle.pack(anchor="w", padx=25, pady=(0, 20))

        # Search bar
        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.pack(fill="x", padx=25, pady=5)

        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Search by name, address, date or method...",
            height=38
        )
        self.search_entry.pack(
            side="left", fill="x", expand=True, padx=(0, 10)
        )

        self.search_entry.bind(
            "<KeyRelease>", self.search_donations
        )

        add_button = ctk.CTkButton(
            search_frame,
            text="+ Add Donation",
            height=38,
            command=self.add_donation
        )
        add_button.pack(side="right")

        # Action buttons
        action_frame = ctk.CTkFrame(self, fg_color="transparent")
        action_frame.pack(fill="x", padx=25, pady=10)

        ctk.CTkButton(
            action_frame,
            text="Edit Selected",
            width=130,
            command=self.edit_donation
        ).pack(side="left", padx=(0, 10))

        ctk.CTkButton(
            action_frame,
            text="Back to Dashboard",
            width=160,
            fg_color="gray",
            hover_color="dim gray",
            command=self.on_back
        ).pack(side="left")

        # Table container
        table_frame = ctk.CTkFrame(self)
        table_frame.pack(
            fill="both", expand=True, padx=25, pady=(5, 25)
        )

        columns = (
            "number",
            "date",
            "name",
            "address",
            "amount",
            "method"
        )

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        # Column headings and widths
        self.table.heading("number", text="#")
        self.table.heading("date", text="Date")
        self.table.heading("name", text="Name")
        self.table.heading("address", text="Address")
        self.table.heading("amount", text="Amount")
        self.table.heading("method", text="Method")

        self.table.column("number", width=45, anchor="center")
        self.table.column("date", width=105, anchor="center")
        self.table.column("name", width=150)
        self.table.column("address", width=200)
        self.table.column("amount", width=100, anchor="e")
        self.table.column("method", width=100)

        # Scrollbar for larger lists
        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.table.yview
        )
        self.table.configure(yscrollcommand=scrollbar.set)

        self.table.pack(
            side="left", fill="both", expand=True, padx=(10, 0), pady=10
        )
        scrollbar.pack(side="right", fill="y", padx=(0, 10), pady=10)

    def display_donations(self, donations=None):

        # Remove existing rows
        for item in self.table.get_children():
            self.table.delete(item)

        # Display either all records or filtered records
        if donations is None:
            donations = self.donations

        for donation in donations:
            self.table.insert(
                "",
                "end",
                values=(
                    donation["number"],
                    donation["date"],
                    donation["name"],
                    donation["address"],
                    f'${donation["amount"]:,.2f}',
                    donation["method"]
                )
            )

    def search_donations(self, event=None):

        search_text = self.search_entry.get().strip().lower()

        filtered_donations = []

        for donation in self.donations:
            searchable_text = " ".join(
                str(value) for value in donation.values()
            ).lower()

            if search_text in searchable_text:
                filtered_donations.append(donation)

        self.display_donations(filtered_donations)

    def add_donation(self):
        messagebox.showinfo(
            "Add Donation",
            "The donation entry form will be added in a later step."
        )

    def edit_donation(self):
        selected = self.table.selection()

        if not selected:
            messagebox.showwarning(
                "No Record Selected",
                "Please select a donation record to edit."
            )
            return

        messagebox.showinfo(
            "Edit Donation",
            "The editing form will be added in a later step."
        )
