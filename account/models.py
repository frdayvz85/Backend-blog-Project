from django.db import models
from django.conf import settings
from django.forms import ModelForm, Textarea, TextInput





class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
         return 'Profile for user {}'.format(self.user.username)






class Contact(models.Model):
    STATUS = (
        (1, 'New'),
        (2, 'Read'),
    )
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=300)
    status = models.IntegerField(choices=STATUS,default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    

    class Meta:
        verbose_name = "Contact Form Message"
        verbose_name_plural = "Contact Form Messages"

    



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'email', 'message']
        widgets = {
            'name': TextInput(attrs={'class':'input', 'placeholder':'Name & Surname'}),
            'subject': TextInput(attrs={'class':'input', 'placeholder':'Subject'}),
            'message': TextInput(attrs={'class':'input', 'placeholder':'Your Message'}),
            'email': TextInput(attrs={'class':'input', 'placeholder':'Your Email'}),

        }





