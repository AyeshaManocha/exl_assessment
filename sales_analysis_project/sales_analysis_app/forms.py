# sales_analysis_app/forms.py
from django import forms

class SalesDataUploadForm(forms.Form):
    sales_data = forms.FileField(label='Upload Sales Data (CSV)')
