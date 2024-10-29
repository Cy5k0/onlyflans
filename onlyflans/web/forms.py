from django import forms
from .models import ContactForm


# class ContactFormForm(forms.Form):
#     customer_email = forms.EmailField(
#         label="Email del cliente",
#         widget=forms.EmailInput(attrs={"class": "form-control"}),
#     )
#     customer_name = forms.CharField(
#         label="Nombre del cliente",
#         max_length=64,
#         widget=forms.TextInput(attrs={"class": "form-control"}),
#     )
#     message = forms.CharField(
#         label="Mensaje", widget=forms.Textarea(attrs={"class": "form-control"})
#     )


class ContactFormModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ["customer_email", "customer_name", "message"]
        labels = {
            "customer_email": "Email del cliente",
            "customer_name": "Nombre del cliente",
            "message": "Mensaje",
        }
        widgets = {
            "customer_email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "nombre@ejemplo.com"}
            ),
            "customer_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Escribe tu nombre"}
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Escribe tu mensaje aquí",
                }
            ),
        }
