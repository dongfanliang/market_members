#coding=utf-8
from django import forms

TEXTINPUTATTR = {"style": "width:142px;font-size:10pt;"}
EXTRAINPUTATTR = {"style": "height:40PX;width:250px;font-size:10pt;"} 
class UserForm(forms.Form):


    user_name = forms.RegexField(required=True, min_length = 2, max_length=19, label='姓　　名：',regex = r'(^[A-Za-z0-9]+$)',
                             widget = forms.TextInput(attrs = TEXTINPUTATTR))
    
    #sex = forms.ChoiceField(widget=forms.Select, choices = (('0','性别'),('1','男'),('2','女')))
    user_password1 = forms.RegexField(required=True, min_length = 5, label='密　　码:', regex = r'(^[A-Za-z0-9]+$)',widget = forms.PasswordInput(attrs = TEXTINPUTATTR)) 
    user_password2 = forms.RegexField(required=True, min_length = 5, label='确认密码:', regex = r'(^[A-Za-z0-9]+$)',widget = forms.PasswordInput(attrs = TEXTINPUTATTR),help_text='输入大于5位数字或字母')
    user_email = forms.EmailField(max_length = 200 ,widget=forms.TextInput(attrs = TEXTINPUTATTR),label='邮　　箱：')
    user_branch = forms.RegexField(required=True, min_length = 1, max_length=255, label='分　　店：',regex = r'(^[A-Za-z0-9]+$)',
                             widget = forms.TextInput(attrs = TEXTINPUTATTR))
    user_branch_address = forms.RegexField(required=True, min_length = 2, max_length=255, label='分店地址：',regex = r'(^[A-Za-z0-9]+$)',
                             widget = forms.TextInput(attrs = TEXTINPUTATTR))
    user_extra = forms.RegexField(required=False, min_length = 2, max_length=255, label='额外信息：',regex = r'(^[A-Za-z0-9]+$)',
                             widget = forms.TextInput(attrs = EXTRAINPUTATTR),help_text='输入少于255个字')
    

    def clean_user_password2(self):
        psw1 = self.cleaned_data.get("user_password1", "")
        psw2 = self.cleaned_data.get("user_password2", "")
        if psw1 != psw2:
            raise forms.ValidationError("两次密码输入不同.")
            return psw2

class PasswordForm(forms.Form):
    username = forms.RegexField(required=True, min_length = 1, max_length=19, label='用户名：　',regex = r'(^[A-Za-z0-9]+$)',
                                 widget = forms.TextInput(attrs = TEXTINPUTATTR))
    email = forms.EmailField(max_length = 200 ,widget=forms.TextInput(attrs = TEXTINPUTATTR),label='邮　箱:　')
