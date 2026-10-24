
import customtkinter as ctk
from tkinter import ttk, messagebox


class TaxReceiptsScreen(ctk.CTkFrame):

    def __init__(self, master, on_back):
        super().__init__(master)

        self.on_back = on_back

        # Temporary sample donations
        self.donations = [
            {
                "id": "1",
                "date": "2026-10-10",
                "name": "Jane Smith",
                "amount": 100.00,
                "method": "Cheque"
            },
            {
                "id": "2",
                "date": "2026-10-12",
                "name": "John Brown",
                "amount": 50.00,
                "method": "Cash"
            },
            {
                "id": "3",
                "date": "2026-10-15",
                "name": "Mary Wilson",
                "amount": 250.00,
                "method": "Online"
            }
        ]

        self.create_widgets()
        self.display_donations()

    def create_widgets(self):

        ctk.CTkLabel(
            self,
            text="Generate Tax Receipts",
            font=("Arial", 28, "bold")
        ).pack(anchor="w", padx=25, pady=(25, 5))

        ctk.CTkLabel(
            self,
            text="Select a donation to prepare its tax receipt.",
            font=("Arial", 14)
        ).pack(anchor="w", padx=25, pady=(0, 20))

        # Search area
        search_frame = ctk.CTkFrame(self, fg_color="transparent")
        search_frame.pack(fill="x", padx=25, pady=5)

        self.search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Search by donor name or donation ID...",
            height=38
        )
        self.search_entry.pack(fill="x", expand=True)

        self.search_entry.bind(
            "<KeyRelease>", self.search_donations
        )

        # Donation table
        table_frame = ctk.CTkFrame(self)
        table_frame.pack(
            fill="both", expand=True, padx=25, pady=15
        )

        columns = ("id", "date", "name", "amount", "method")

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        headings = {
            "id": "Donation #",
            "date": "Date",
            "name": "Donor Name",
            "amount": "Amount",
            "method": "Method"
        }

        for column, heading in headings.items():
            self.table.heading(column, text=heading)

        self.table.column("id", width=100, anchor="center")
        self.table.column("date", width=120, anchor="center")
        self.table.column("name", width=200)
        self.table.column("amount", width=120, anchor="e")
        self.table.column("method", width=120)

        self.table.pack(
            fill="both", expand=True, padx=10, pady=10
        )

        # Action buttons
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(fill="x", padx=25, pady=(0, 25))

        ctk.CTkButton(
            button_frame,
            text="Generate Receipt",
            width=180,
            height=40,
            command=self.generate_receipt
        ).pack(side="left", padx=(0, 10))

        ctk.CTkButton(
            button_frame,
            text="Back to Dashboard",
            width=170,
            height=40,
            fg_color="gray",
            hover_color="dim gray",
            command=self.on_back
        ).pack(side="left")

    def display_donations(self, donations=None):

        for item in self.table.get_children():
            self.table.delete(item)

        if donations is None:
            donations = self.donations

        for donation in donations:
            self.table.insert(
                "",
                "end",
                values=(
                    donation["id"],
                    donation["date"],
                    donation["name"],
                    f'${donation["amount"]:,.2f}',
                    donation["method"]
                )
            )

    def search_donations(self, event=None):

        search_text = self.search_entry.get().strip().lower()

        filtered = [
            donation
            for donation in self.donations
            if search_text in (
                donation["id"] + " " +
                donation["name"] + " " +
                donation["date"]
            ).lower()
        ]

        self.display_donations(filtered)

    def generate_receipt(self):

        selected = self.table.selection()

        if not selected:
            messagebox.showwarning(
                "No Donation Selected",
                "Please select a donation first."
            )
            return

        messagebox.showinfo(
            "Receipt Generation",
            "The selected donation has been identified.\n\n"
            "Receipt preview, eligibility checks, and PDF "
            "generation will be implemented in a later step. "
            "No receipt has been issued."
        )
