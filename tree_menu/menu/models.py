from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)  # Название пункта меню
    url = models.CharField(max_length=200, blank=True, null=True)  # Явный URL
    named_url = models.CharField(max_length=100, blank=True, null=True)  # Именованный URL
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')  # Родительский элемент

    def __str__(self):
        return self.name