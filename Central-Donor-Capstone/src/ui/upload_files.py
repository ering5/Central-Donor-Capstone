
import customtkinter as ctk
from tkinter import filedialog, messagebox
import os


class UploadFilesScreen(ctk.CTkFrame):

    def __init__(self, master, on_back):
        super().__init__(master)

        self.on_back = on_back
        self.selected_file = None

        self.create_widgets()

    def create_widgets(self):

        ctk.CTkLabel(
            self,
            text="Upload Files",
            font=("Arial", 28, "bold")
        ).pack(anchor="w", padx=25, pady=(25, 5))

        ctk.CTkLabel(
            self,
            text="Import donation records from an Excel or CSV file.",
            font=("Arial", 14)
        ).pack(anchor="w", padx=25, pady=(0, 25))

        # Main upload panel
        panel = ctk.CTkFrame(self, corner_radius=12)
        panel.pack(fill="x", padx=25, pady=10)

        ctk.CTkLabel(
            panel,
            text="Select a file to upload",
            font=("Arial", 20, "bold")
        ).pack(pady=(25, 10))

        ctk.CTkLabel(
            panel,
            text="Supported formats: .xlsx, .xls and .csv",
            text_color="gray"
        ).pack(pady=5)

        ctk.CTkButton(
            panel,
            text="Browse Files",
            width=200,
            height=40,
            command=self.browse_file
        ).pack(pady=20)

        self.file_label = ctk.CTkLabel(
            panel,
            text="No file selected",
            wraplength=500
        )
        self.file_label.pack(padx=20, pady=(0, 15))

        self.upload_button = ctk.CTkButton(
            panel,
            text="Continue to Import",
            width=200,
            height=40,
            state="disabled",
            command=self.import_file
        )
        self.upload_button.pack(pady=(0, 25))

        # Instructions
        ctk.CTkLabel(
            self,
            text="Before importing",
            font=("Arial", 18, "bold")
        ).pack(anchor="w", padx=25, pady=(25, 10))

        instructions = (
            "1. Select your Excel or CSV file.\n"
            "2. Review the file before importing.\n"
            "3. Confirm that the columns match the expected format.\n"
            "4. Check for duplicate or incomplete records."
        )

        ctk.CTkLabel(
            self,
            text=instructions,
            justify="left",
            font=("Arial", 14)
        ).pack(anchor="w", padx=30, pady=(0, 20))

        ctk.CTkButton(
            self,
            text="Back to Dashboard",
            fg_color="gray",
            hover_color="dim gray",
            command=self.on_back
        ).pack(anchor="w", padx=25, pady=10)

    def browse_file(self):

        file_path = filedialog.askopenfilename(
            title="Select a donation records file",
            filetypes=[
                ("Supported files", "*.xlsx *.xls *.csv"),
                ("Excel files", "*.xlsx *.xls"),
                ("CSV files", "*.csv"),
                ("All files", "*.*")
            ]
        )

        if not file_path:
            return

        extension = os.path.splitext(file_path)[1].lower()

        if extension not in (".xlsx", ".xls", ".csv"):
            messagebox.showerror(
                "Unsupported File",
                "Please select an Excel or CSV file."
            )
            return

        self.selected_file = file_path

        self.file_label.configure(
            text=f"Selected file: {os.path.basename(file_path)}"
        )

        self.upload_button.configure(state="normal")

    def import_file(self):

        if not self.selected_file:
            return

        messagebox.showinfo(
            "Import Not Yet Available",
            "The file has been selected successfully.\n\n"
            "File validation and importing will be added next. "
            "No records have been imported."
        )
