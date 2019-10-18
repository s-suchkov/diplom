from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
#
class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class Article(models.Model):
    title = models.TextField()
    text = models.TextField()
    date = models.DateTimeField()

class Section(models.Model):
    text = models.TextField()


class Products(models.Model):
    name = models.TextField()
    image = models.ImageField()
    text = models.TextField()
    section = models.ForeignKey('Section', on_delete=models.CASCADE, null=True, blank=True)
    article = models.ManyToManyField('Article', blank=True)


    def __str__(self):
        return self.name

class Review(models.Model):
    products = models.ForeignKey('Products', on_delete=models.CASCADE, null=True, blank=True)
    rating = models.TextField()
    name = models.TextField()
    text = models.TextField()

class Order(models.Model):
    date = models.DateTimeField()
    username = models.TextField()
    count = models.IntegerField()

class Basket(models.Model):
    author = models.EmailField(unique=False)
    buy = models.BooleanField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, blank=True, related_name='ord')
    product = models.ManyToManyField('Products', blank=True, related_name='bas')

