from django import forms


class BootstrapBaseForm(forms.BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            widget = field.widget

            if isinstance(widget, (forms.TextInput, forms.EmailInput, forms.URLInput,
                                   forms.NumberInput, forms.PasswordInput, forms.Textarea,
                                   forms.DateInput, forms.DateTimeInput, forms.TimeInput)):
                widget.attrs.setdefault('class', 'form-control')

            elif isinstance(widget, (forms.Select, forms.SelectMultiple)):
                widget.attrs.setdefault('class', 'form-select')

            elif isinstance(widget, forms.CheckboxInput):
                widget.attrs.setdefault('class', 'form-check-input')

            elif isinstance(widget, forms.RadioSelect):
                widget.attrs.setdefault('class', 'form-check-input')

            elif isinstance(widget, forms.FileInput):
                widget.attrs.setdefault('class', 'form-control')

            if field.required:
                widget.attrs.setdefault('required', 'required')


class BootstrapForm(BootstrapBaseForm, forms.Form):
    pass


class BootstrapModelForm(BootstrapBaseForm, forms.ModelForm):
    pass
