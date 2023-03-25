from django.db import models

class User:
    id = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __init__(u, p, e, fn, ln):
        self.username = u
        self.password = p
        self.email = e 
        self.first_name = fn
        self.last_name = ln

    def get_id():
        return self.id
    
    def get_username() -> str:
        return self.username
    
    def set_username(user : str):
        self.username = user
    
    def get_password() -> str:
        return self.password
    
    def set_password(pw : str):
        self.password = pw
    
    def get_email() -> str:
        return self.email
    
    def set_email(email : str):
        self.email = email
    
    def get_firstname() -> str:
        return self.first_name
    
    def set_firstname(first : str):
        self.first_name = first
    
    def get_lastname() -> str:
        return self.last_name
    
    def set_lastname(last : str):
        self.last_name = last