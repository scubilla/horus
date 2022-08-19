from django.forms import *
from app.core.erp.models import Category

# Create the form class.
class CategoryForm(ModelForm):
      def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for form in self.visible_fields():
              form.field.widget.attrs['class'] = 'form-control'
              form.field.widget.attrs['autocomplete'] = 'off'
          self.fields['name'].widget.attrs['autofocus'] = True


      class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name':'Nombre'
        }
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder':'Ingrese un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Ingrese descripción',
                    'row': 3,
                    'cols': 5
                }
            ),
        }

