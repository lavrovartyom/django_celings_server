from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Layout, Submit
from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    """Форма подачи заявки."""

    class Meta:
        model = Client
        fields = ["full_name", "phone_number", "address", "comment"]
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Ваше имя"}),
            "phone_number": forms.TextInput(
                attrs={"placeholder": "+7(XXX)-XXX-XX-XX", "type": "tel"}
            ),
            "address": forms.TextInput(attrs={"placeholder": "Ваш адрес"}),
            "comment": forms.Textarea(attrs={"rows": 3, "placeholder": "Комментарий"}),
        }

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            *[
                Div(Field(name, css_class="input-lg"), css_class="col-md-4")
                for name in self.fields
            ]
            + [
                Div(
                    Submit(
                        "submit",
                        "Записаться на замер",
                        css_class="btn btn-primary mt-2 w-100",
                    ),
                    css_class="col-md-4",
                )
            ]
        )
