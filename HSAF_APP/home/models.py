from django.db import models

# Create your models here.


# model for user authn tabel using pre made django table. 

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'




class posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    userid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'posts'

