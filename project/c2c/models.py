from django.db import models

class NewUser (models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30, unique=True)  # Ensure email is unique
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

