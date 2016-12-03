from django import forms
from gtd.models import TodoItem
from django.core.exceptions import ValidationError

EMPTY_LIST_ERROR = "You can't have an empty list item"
DUPLICATE_ITEM_ERROR = "You've already got this in your list"

# class ItemForm(forms.models.ModelForm):
#     class Meta:
#         model = TodoItem
#         fields = ('text',)
#         widgets = {
#             'text': forms.fields.TextInput(attrs={
#                 'placeholder': 'Enter a to-do item',
#                 'class': 'form-control input-lg',
#             }),
#         }
#         error_messages = {
#             'text': {'required': EMPTY_LIST_ERROR} # 表示这是个必填项
#         }
#
#     def save(self, for_user):
#         self.instance.list = for_list
#         return super().save()
