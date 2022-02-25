from django.forms import ModelForm
from gadgets.models import Brand


# Create the form class.
class MakeForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
