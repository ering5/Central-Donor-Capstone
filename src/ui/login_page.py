"""Login screen layout for the Central Donor application."""

import tkinter as tk
from tkinter import ttk


class LoginPage(ttk.Frame):
    """A reusable login form frame."""

    def __init__(self, master=None, login=None):
        super().__init__(master, padding=24)
        self.login = login
        self.pack(expand=True, fill="both")

        self.columnconfigure(1, weight=1)

        title = ttk.Label(self, text="Central Donor", font=("Segoe UI", 20, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=(0, 24))

        ttk.Label(self, text="Username").grid(row=1, column=0, sticky="w", padx=(0, 12))
        self.username = ttk.Entry(self)
        self.username.grid(row=1, column=1, sticky="ew")

        ttk.Label(self, text="Password").grid(row=2, column=0, sticky="w", padx=(0, 12), pady=(12, 0))
        self.password = ttk.Entry(self, show="*")
        self.password.grid(row=2, column=1, sticky="ew", pady=(12, 0))

        self.login_button = ttk.Button(self, text="Log in", command=self._submit)
        self.login_button.grid(row=3, column=0, columnspan=2, pady=(24, 0), sticky="ew")

        self.username.bind("<Return>", lambda _event: self._submit())
        self.password.bind("<Return>", lambda _event: self._submit())

    def _submit(self):
        if callable(self.login):
            self.login(self.username.get(), self.password.get())

    def get_credentials(self):
        return self.username.get(), self.password.get()


def create_login_page(root, login=None):
    """Create and return the login page."""
    return LoginPage(root, login=login)


# Compatibility name for callers that build the layout directly.
def login_page(parent, login=None):
    return create_login_page(parent, login=login)
