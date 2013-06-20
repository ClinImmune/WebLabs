from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager
)

class LabUserManager(BaseUserManager):
    """
    A new user manager for both standard and administrative users
    """

    def normalize_email(self, email):
    	email = email or ''
    	try:
            email_name, domain_part = email.strip().rsplit('@', 1)
        except ValueError:
            pass
        else:
            email = '@'.join([email_name, domain_part.lower()])
        print email
        return email
    
    def create_user(
            self, 
            email,
            first_name,
            last_name,
            university=None,
            job_title=None,
            bio=None,
            password=None
    ):
        """
        Creates a standard user with no administrative privledges
        """
        if not email:
            raise ValueError('Users must provide an email')
            
        if not first_name:
            raise ValueError('Users must provide a first name')
        
        if not last_name:
            raise ValueError('Users must provide a last name')
            
        if not university:
            raise ValueError('Users must provide an email address')
            
        # Note: a biography and job_title are not required
        user = self.model(
            email=BaseUserManager.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            university=university,
            job_title=job_title,
            bio=bio
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(
            self, 
            email,
            first_name,
            last_name,
            university,
            job_title=None,
            bio=None,
            password=None
    ):
        """
        Creates an administrative user
        """    
                        
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            university=university,
            job_title=job_title,
            bio=bio,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user                

class LabUser(AbstractBaseUser):
    """
    Model for every user on the site
    The only required fields are:
        email,
        first_name,
        last_name,
        university,
    although, this will be discussed later
    
    """
    email = models.EmailField(
        verbose_name = 'email address',
        max_length   = 255,
        unique       = True,
        db_index     = True,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    name_is_public = models.BooleanField(default=True)
    university = models.CharField(max_length=150)
    job_title = models.CharField(max_length=50, null=True)
    bio = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    objects = LabUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'university',
    ]
    
    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
    
    @property 
    def is_staff(self):
        return self.is_admin
    
    @property
    def is_public(self):
    	return self.name_is_public
    
    def get_full_name(self):
        return self.full_name
        
    def get_short_name(self):
        return self.first_name
        
    def __unicode__(self):
        return self.full_name

