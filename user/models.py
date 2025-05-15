import re

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class AppUser(User):

    class Meta:
        proxy = True

    def welcome_message(self):
        return f"Welcome, {self.username}! Your account was created successfully."

    def clean(self):
        super().clean()

        # --- Username validation ---
        if not re.search(r'[a-zA-Z]', self.username):
            raise ValidationError("Username must contain at least one letter.")

        if not re.search(r'\d|[^a-zA-Z0-9]', self.username):  # Allows digits or special characters
            raise ValidationError("Username must contain at least one number or special character.")

        # If the username has letters, they must all be lowercase
        # islower() will fail when there are no letters, or if symbols are present.
        if any(char.isupper() for char in self.username if char.isalpha()):
            raise ValidationError("Username must contain only lowercase letters.")

        # --- Email validation ---
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.fullmatch(email_pattern, self.email):
            raise ValidationError("Invalid email format.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Triggers clean() for validation
        return super().save(*args, **kwargs)