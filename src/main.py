
import customtkinter as ctk
from ui.donation_records import DonorRecordsScreen
from ui.upload_files import UploadFilesScreen
from tax_receipts.tax_receipts import TaxReceiptsScreen
from ui.admin import AdminScreen
# Basic appearance settings
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class DonorApp(ctk.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("Donor Management System")
        self.geometry("800x550")
        self.minsize(650, 450)

        self.show_login()
    
    def show_login(self):
        # Clear the previous screen
        for widget in self.winfo_children():
            widget.destroy()

        # Center the login panel
        self.login_frame = ctk.CTkFrame(
            self,
            width=380,
            corner_radius=15
        )
        self.login_frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # Application title
        ctk.CTkLabel(
            self.login_frame,
            text="Donor Management System",
            font=("Arial", 24, "bold"),
            wraplength=330
        ).pack(pady=(30, 8), padx=20)

        ctk.CTkLabel(
            self.login_frame,
            text="Please log in to continue.",
            font=("Arial", 14)
        ).pack(pady=(0, 25))

        # Username field
        self.username_entry = ctk.CTkEntry(
            self.login_frame,
            width=300,
            height=40,
            placeholder_text="Username"
        )
        self.username_entry.pack(pady=10)

        # Password field
        self.password_entry = ctk.CTkEntry(
            self.login_frame,
            width=300,
            height=40,
            placeholder_text="Password",
            show="*"
        )
        self.password_entry.pack(pady=10)

        # Login button
        ctk.CTkButton(
            self.login_frame,
            text="Log In",
            width=300,
            height=40,
            command=self.show_dashboard
        ).pack(pady=(20, 10))

    
    def show_dashboard(self):
        # Clear the login screen
        for widget in self.winfo_children():
            widget.destroy()

        # Dashboard heading
        ctk.CTkLabel(
            self,
            text="Welcome Admin - Administrator",
            font=("Arial", 26, "bold")
        ).pack(pady=(40, 10))

        ctk.CTkLabel(
            self,
            text="What would you like to do?",
            font=("Arial", 16)
        ).pack(pady=(0, 25))

        # Main dashboard actions
        ctk.CTkButton(
            self,
            text="Update/View Records",
            width=250,
            height=45,
            command=self.show_records
        ).pack(pady=8)

        ctk.CTkButton(
            self,
            text="Upload Files",
            width=250,
            height=45,
            command=self.show_upload
        ).pack(pady=8)

        ctk.CTkButton(
            self,
            text="Generate Tax Receipts",
            width=250,
            height=45,
            command=self.show_tax_receipts
        ).pack(pady=8)

        ctk.CTkButton(
            self,
            text="Administrative Tools",
            width=250,
            height=45,
            command=self.show_admin
        ).pack(pady=8)

        ctk.CTkButton(
            self,
            text="Log Out",
            width=250,
            fg_color="gray",
            hover_color="dim gray",
            command=self.show_login
        ).pack(pady=(25, 10))
    
   
    def show_upload(self):
        for widget in self.winfo_children():
            widget.destroy()

        screen = UploadFilesScreen(
            self,
            on_back=self.show_dashboard
        )
        screen.pack(fill="both", expand=True)

    def show_tax_receipts(self):
        for widget in self.winfo_children():
            widget.destroy()

        screen = TaxReceiptsScreen(
            self,
            on_back=self.show_dashboard
        )
        screen.pack(fill="both", expand=True)

    def show_admin(self):
        for widget in self.winfo_children():
            widget.destroy()

        screen = AdminScreen(
            self,
            on_back=self.show_dashboard
        )
        screen.pack(fill="both", expand=True)

    def show_records(self):
        # Clear the current screen
        for widget in self.winfo_children():
            widget.destroy()

        # Create and display the donor records screen
        records_screen = DonorRecordsScreen(
            self,
            on_back=self.show_dashboard
        )
        records_screen.pack(fill="both", expand=True)


if __name__ == "__main__":
    app = DonorApp()
    app.mainloop()
