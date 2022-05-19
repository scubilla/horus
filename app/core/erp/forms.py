from django.forms import ModelForm
from app.core.erp.models import Category

# Create the form class.
class CategoryForm(ModelForm):
      class Meta:
        model = Category
        fields = '__all__'

