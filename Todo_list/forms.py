from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from .models import TodoModel

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ('task', 'date', 'done','status')

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)

        self.fields['date'] = JalaliDateField(label=('date'),widget=AdminJalaliDateWidget)
        self.fields['task'].widget.attrs.update({'class': 'form-control' ,'dir':'rtl' , 'id':'task' , 'aria-label':'First name' ,'placeholder':'Task' })

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

        # self.fields['date_time'] = SplitJalaliDateTimeField(label=_('date time'), 
        #     widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        # )