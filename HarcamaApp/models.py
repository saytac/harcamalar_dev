from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    KALEM_CHOICES = [
        ('Market', 'Market'),
        ('Araba', 'Araba'),
        ('Yakıt', 'Yakıt'),
        ('Ulaşım', 'Ulaşım'),
        ('Restoran', 'Restoran'),
        ('Cafe/Pastane', 'Cafe/Pastane'),
        ('Kozmetik/Eczane/Gözlük', 'Kozmetik/Eczane/Gözlük'),
        ('Giyim/Ayakkabı/Çanta', 'Giyim/Ayakkabı/Çanta'),
        ('Sigorta-araba', 'Sigorta-araba'),
        ('Sigorta-sağlık/TSS', 'Sigorta-sağlık/TSS'),
        ('Sigorta-mal', 'Sigorta-mal'),
        ('Online-abonelik', 'Online-abonelik'),
        ('Online-hizmet', 'Online-hizmet'),
        ('Online-alışveriş', 'Online-alışveriş'),
        ('Nalbur/Beyazeşya', 'Nalbur/Beyazeşya'),
        ('Ev-Reji', 'Ev-Reji'),
        ('Ev-Internet', 'Ev-Internet'),
        ('TV-abonelik', 'TV-abonelik'),
        ('Hediye', 'Hediye'),
        ('Kedi', 'Kedi'),
        ('Diğer', 'Diğer'),
    ]

    KART_CHOICES = [
        ('Miles', 'Miles'),
        ('World', 'World'),
        ('Bonus', 'Bonus'),
        ('Maximum', 'Maximum'),
        ('Troy', 'Troy'),
        ('Enpara', 'Enpara'),
        ('Nakit', 'Nakit'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    kalem = models.CharField(max_length=50, choices=KALEM_CHOICES)
    kart = models.CharField(max_length=20, choices=KART_CHOICES)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    bilgi = models.TextField(blank=True, null=True, verbose_name="Notlar")
    image = models.ImageField(upload_to='media/', blank=True, null=True, verbose_name="Resim")

    def __str__(self):
        return f"{self.timestamp} - {self.kalem} - {self.fiyat} TL"

