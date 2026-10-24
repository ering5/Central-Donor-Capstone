
import customtkinter as ctk
from tkinter import messagebox


class AdminScreen(ctk.CTkFrame):

    def __init__(self, master, on_back):
        super().__init__(master)

        self.on_back = on_back

        # Temporary sample users
        self.users = [
            {"username": "admin", "role": "Administrator"},
            {"username": "staff1", "role": "Standard User"},
            {"username": "staff2", "role": "Standard User"}
        ]

        self.create_widgets()
        self.display_users()

    def create_widgets(self):

        self.scrollable_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        self.scrollable_frame.pack(fill="both", expand=True)

        ctk.CTkLabel(
            self.scrollable_frame,
            text="Administrative Tools",
            font=("Arial", 28, "bold")
        ).pack(anchor="w", padx=25, pady=(25, 5))

        ctk.CTkLabel(
            self.scrollable_frame,
            text="Manage users and system settings.",
            font=("Arial", 14)
        ).pack(anchor="w", padx=25, pady=(0, 20))

        # User management section
        user_frame = ctk.CTkFrame(
            self.scrollable_frame,
            corner_radius=12
        )
        user_frame.pack(fill="x", padx=25, pady=10)

        ctk.CTkLabel(
            user_frame,
            text="User Accounts",
            font=("Arial", 20, "bold")
        ).pack(anchor="w", padx=20, pady=(20, 5))

        ctk.CTkLabel(
            user_frame,
            text="Sample accounts for interface development only.",
            text_color="gray"
        ).pack(anchor="w", padx=20, pady=(0, 10))

        # List of users
        self.user_list = ctk.CTkScrollableFrame(
            user_frame,
            height=150
        )
        self.user_list.pack(
            fill="x", padx=15, pady=(0, 10)
        )

        # User action buttons
        button_frame = ctk.CTkFrame(
            user_frame, fg_color="transparent"
        )
        button_frame.pack(
            fill="x", padx=20, pady=(0, 20)
        )

        ctk.CTkButton(
            button_frame,
            text="Create User",
            command=self.create_user
        ).pack(side="left", padx=(0, 10))

        ctk.CTkButton(
            button_frame,
            text="Manage Selected User",
            fg_color="gray",
            hover_color="dim gray",
            command=self.manage_user
        ).pack(side="left")

        # Additional administrative actions
        ctk.CTkLabel(
            self.scrollable_frame,
            text="Other Tools",
            font=("Arial", 20, "bold")
        ).pack(anchor="w", padx=25, pady=(25, 10))

        ctk.CTkButton(
            self.scrollable_frame,
            text="System Activity",
            width=250,
            height=40,
            command=lambda: self.not_available(
                "System Activity"
            )
        ).pack(anchor="w", padx=25, pady=5)

        ctk.CTkButton(
            self.scrollable_frame,
            text="System Settings",
            width=250,
            height=40,
            command=lambda: self.not_available(
                "System Settings"
            )
        ).pack(anchor="w", padx=25, pady=5)

        ctk.CTkButton(
            self.scrollable_frame,
            text="Back to Dashboard",
            width=200,
            height=40,
            fg_color="gray",
            hover_color="dim gray",
            command=self.on_back
        ).pack(anchor="w", padx=25, pady=25)

    def display_users(self):

        for widget in self.user_list.winfo_children():
            widget.destroy()

        for user in self.users:

            row = ctk.CTkFrame(
                self.user_list,
                fg_color="transparent"
            )
            row.pack(fill="x", padx=5, pady=5)

            ctk.CTkLabel(
                row,
                text=user["username"],
                font=("Arial", 14, "bold")
            ).pack(side="left", padx=10)

            ctk.CTkLabel(
                row,
                text=user["role"],
                text_color="gray"
            ).pack(side="right", padx=10)

    def create_user(self):

        messagebox.showinfo(
            "Create User",
            "The user creation form will be added later."
        )

    def manage_user(self):

        messagebox.showinfo(
            "Manage User",
            "Select a user to view or change their account settings. "
            "This functionality will be added later."
        )

    def not_available(self, feature):

        messagebox.showinfo(
            feature,
            f"{feature} will be implemented in a later step."
        )
