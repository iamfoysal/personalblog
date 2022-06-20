# from django.db import models
# from PIL import Image
# from django.contrib.auth.models import User

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=255, null = True, blank= False)
#     about = models.CharField(max_length=1000, null = True, blank= False)
#     location = models.CharField(max_length=255, null = True, blank= False)
#     image = models.ImageField(upload_to = 'avater/', null = True, blank= False)


#     def __str__(self):
#         return str(self.user)

#     def save(self):
#         super().save()

#         img = Image.open(self.image.path)

#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size)
#             img.save(self.image.path)