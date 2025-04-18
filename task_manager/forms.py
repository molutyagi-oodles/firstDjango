from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed']
        widgets = {
            'due_date': forms.DateTimeInput(
                attrs={
                    'type': 'datetime-local',
                    'class': 'w-full p-2 border-2 border-gray-300 rounded-md',
                },
                format='%Y-%m-%dT%H:%M'  # format required by datetime-local input
            )
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full px-4 py-2 border-2 border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-800',
                'placeholder': f'Enter {field.label.lower()}'
            })
        if self.instance and self.instance.pk and self.instance.due_date:
            self.fields['due_date'].initial = self.instance.due_date.strftime('%Y-%m-%dT%H:%M')


# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title', 'description', 'due_date', 'completed']
#         widgets = {
#             'due_date': forms.DateInput(attrs={'type': 'datetime-local'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super(TaskForm, self).__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs.update({
#                 'class': 'w-full px-4 py-2 border-2 border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-800',
#                 'placeholder': f'Enter {field.label.lower()}'
#             })
