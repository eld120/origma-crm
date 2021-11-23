from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    r"^(\d{10}$)",
    "Please use numerical format without any spaces or special characters",
)
