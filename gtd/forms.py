from django import forms
from gtd.models import TodoItem, User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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
class LoginForm(AuthenticationForm):
    """
    用户登录表单
    """
    remember_me = forms.BooleanField(label='下次自动登录', initial=False, required=False)


class RegistrationForm(UserCreationForm):
    """
    新用户注册表单
    """

    email = forms.EmailField(help_text='用户账号认证和密码重置')

    def clean_email(self):
        """
        确保注册邮箱的唯一性
        """
        value = self.cleaned_data['email']
        qs = User.objects.filter(email__iexact=value)
        if not qs.exists():
            return value
        raise forms.ValidationError('邮箱已被注册,请更换邮箱')
