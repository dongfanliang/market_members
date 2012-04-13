#coding=utf-8
from django import forms
import datetime

TEXTINPUTATTR = {"style": "width:142px;font-size:10pt;"}
GENDER_CHOICES = (('F', '男'),('M', '女'))
RANK = (('A','普通会员'), ('B','银卡'),('C','金卡'))
STATUS = (('1','正常'),('2','锁定'),('3','挂失'))

class RegisterForm(forms.Form):
    member_card_id = forms.RegexField(required=True, min_length = 10, max_length=10, label='会员卡号：',regex = r'(^[A-Za-z0-9]+$)',
                             widget = forms.TextInput(attrs = TEXTINPUTATTR))

    member_name = forms.RegexField(required=True, min_length = 2, max_length=10, label='姓　　名：',regex = r'(^[A-Za-z0-9]+$)',
                             widget = forms.TextInput(attrs = TEXTINPUTATTR))
    #sex = forms.ChoiceField(widget=forms.Select, choices = (('0','性别'),('1','男'),('2','女')))
    member_password1 = forms.RegexField(required=True, min_length = 6,max_length=6, label='密　　码:', regex = r'(^[A-Za-z0-9]+$)',widget = forms.PasswordInput(attrs = TEXTINPUTATTR)) 
    member_password2 = forms.RegexField(required=True, min_length = 6,max_length=6, label='确认密码:', regex = r'(^[A-Za-z0-9]+$)',widget = forms.PasswordInput(attrs = TEXTINPUTATTR),help_text='输入6位数字或字母')
    member_sex = forms.ChoiceField(required=True,widget=forms.Select, choices = GENDER_CHOICES, label='性　　别：　　')
    member_id = forms.RegexField(required=True, min_length = 18,max_length=18, label='身份证号:', regex = r'(^[A-Za-z0-9]+$)',widget = forms.TextInput(attrs = TEXTINPUTATTR)) #身份证号
    member_phone = forms.RegexField(required=True, min_length = 8,max_length=20, label=' 电　　话:', regex = r'(^[0-9]+$)',widget = forms.TextInput(attrs = TEXTINPUTATTR))
    member_rank = forms.ChoiceField(widget=forms.Select, choices = RANK, label='等　　级:')
    member_status = forms.ChoiceField(widget=forms.Select, choices = STATUS, label='状　　态:')
    member_createtime = forms.DateField(initial=datetime.date.today, label='创建时间:',widget = forms.TextInput(attrs = TEXTINPUTATTR))
    member_points = forms.RegexField(required=True, initial=0,label='积　　分:', regex = r'(^[0-9]+$)',widget = forms.TextInput(attrs = TEXTINPUTATTR),help_text='初始值为0') 
    member_surplus = forms.RegexField(required=True, initial=0,label='账户余额:', regex = r'(^[0-9]+$)',widget = forms.TextInput(attrs = TEXTINPUTATTR),help_text='初始值为0') 

    def clean_member_password2(self):
        psw1 = self.cleaned_data.get("member_password1", "")
        psw2 = self.cleaned_data.get("member_password2", "")
        if psw1 != psw2:
            raise forms.ValidationError("两次密码输入不同.")
            return psw2


