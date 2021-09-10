from django import forms

class jobInput(forms.Form):
    inp = forms.CharField(max_length=50,
        widget = forms.TextInput(attrs = {"type":"text","class":"form-control","placeholder":"Enter todo e.g. Wash my car", "aria-label":"Todo", "aria-describedby":"add-btn"}
        ))
