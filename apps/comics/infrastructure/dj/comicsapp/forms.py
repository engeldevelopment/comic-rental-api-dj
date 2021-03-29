from django import forms

from .models import Comic


class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = ('name', 'price', 'status',)

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError(f"This is not a valid price '{price}.'")
        return price
