from django.db import models

# inheriting from Model
class Wall(models.Model): 
    # mappiing to DB     
    content = models.TextField(blank = True, null = True)
    image = models.FileField(upload_to='images/', blank = True, null = True)
    # blank= not req in django, #null= not req in DB