#from tinymce.models import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from ckeditor.fields import RichTextField


User = get_user_model()

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username




class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

#by me 
#About Model
class About(models.Model):
    #short_description = models.TextField()
    #contact = models.TextField()
    site_name = models.CharField(max_length=30, verbose_name="Site Name or Logo")
    back_image = models.ImageField(upload_to='images/')
    
    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"

#introduction Model
class Introduction(models.Model):
    title = models.CharField(max_length=100, verbose_name="Write Title")
    description = RichTextField(max_length=1800, verbose_name="Description")
    
    def __str__(self):
        return self.title

#About Model
class Footer(models.Model):
    #short_description = models.TextField()
    #contact = models.TextField()
    adres = models.CharField(max_length=50, verbose_name="Adress")
    email = models.CharField(max_length=30, verbose_name="Email")
    phone = models.CharField(max_length=30, verbose_name="Phone")
    linkedin = models.CharField(max_length=30, verbose_name="Linkedin",null=True)
    github = models.CharField(max_length=30, verbose_name="Github",null=True)
    twitter = models.CharField(max_length=70, verbose_name="Twitter",null=True)
    facebook = models.CharField(max_length=70, verbose_name="Facebook",null=True)
    insta = models.CharField(max_length=70, verbose_name="İnstagram",null=True)

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footer"

    def __str__(self):
        return "Footer"


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    #content = HTMLField()
   # comment_count = models.IntegerField(default = 0)
    #view_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })

    
    def get_update_url(self):
        return reverse('post-update', kwargs={
            'id': self.id
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'id': self.id
        })

    def get_contact_url(self):
        return reverse('contact')

   

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    
    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()





    


