from django.db import models
from datetime import datetime  

from django.contrib.auth.models import User as djUser

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50, default="user")
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_img = models.CharField(max_length=255, default="default.png") 
    verified = models.CharField(max_length=50, default="f")

    def convert_user(self) -> djUser:
        if self is not None:
            return djUser.objects.create_user(username = self.username, password = self.password, 
            email = self.email,first_name = self.first_name, last_name = self.last_name)
        else:
            return None

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['username', 'email'], name='unique_name_email')
        ]

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=50, default="")
    start_time = models.DateField()
    end_time = models.DateField()
    registration_deadline = models.DateField()
    location = models.CharField(max_length=50)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.CharField(max_length=20, default="open")
    participators = models.IntegerField(default=0)
    images = models.CharField(max_length=1000, default="")

class Discussion(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default=None, blank=True, null=True)
    title = models.CharField(max_length=50, default="", blank=True, null=True)
    content = models.TextField()
    images = models.CharField(max_length=1000, default="", blank=True, null=True)
    item_type = models.CharField(max_length=50) #Announcement(Starter + Organizer), Starter, Reply 
    timestamp = models.TimeField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=None, blank=True, null=True)

class Like(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Discussion, on_delete=models.CASCADE)

class Views(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Discussion, on_delete=models.CASCADE)

class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    attendee = models.ForeignKey(User, on_delete=models.PROTECT)
    price = models.FloatField()
    #status = models.CharField(max_length=50, default=None)

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateField()

class Follower(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)

class Node:
     
    def __init__(self, key):
         
        self.key = key
        self.child = []
   
    def newNode(key):   
        temp = Node(key)
        return temp
    
    def has_childs(self):
        if len(self.child) > 0:
            return True
        return False
     
    def LevelOrderTraversal(root):
        if (root == None):
            return
        q = []  
        q.append(root); 
        while (len(q) != 0):
            n = len(q)
            while (n > 0):
                p = q[0]
                q.pop(0)
                for i in range(len(p.child)):        
                    q.append(p.child[i])
                n -= 1
   