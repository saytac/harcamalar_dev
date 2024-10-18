from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Expense
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['kalem', 'kart', 'fiyat', 'bilgi', 'image']
        labels = {
            'kalem': _('Harcama Kalemi'),
            'kart': _('Ödeme Yöntemi'),
            'fiyat': _('Tutar (TL)'),
            'bilgi': _('Not'),
            'dosya': _('Görsel')
        }
        widgets = {
            'kalem': forms.Select(attrs={'class': 'form-select'}),
            'kart': forms.Select(attrs={'class': 'form-select'}),
            'fiyat': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'bilgi': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
        }

    def clean_fiyat(self):
        fiyat = self.cleaned_data.get('fiyat')
        if fiyat is not None and fiyat <= 0:
            raise ValidationError(_('Tutar sıfırdan büyük olmalıdır.'))
        return fiyat


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Kullanıcı Adı'),
                'autofocus': True
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': _('Şifre')
            }
        )
    )