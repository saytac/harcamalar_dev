from django.db import models

# Harcama Modeli
class Harcama(models.Model):
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
        ('Kedi' , 'Kedi'),
        ('Diğer', 'Diğer'),
    ]

    ODEME_TUR_CHOICES = [
        ('kredikartı', 'Kredi Kartı'),
        ('nakit', 'Nakit'),
    ]

    kalem = models.CharField(max_length=50, choices=KALEM_CHOICES)
    odeme_turu = models.CharField(max_length=20, choices=ODEME_TUR_CHOICES)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.kalem} - {self.fiyat} TL"
