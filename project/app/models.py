from django.db import models
    
class Icecream(models.Model):
    name_icecream = models.CharField(max_length=50)
    price = models.FloatField()
        
    def __str__(self):
        return self.name_icecream

class Icecream_Taste(models.Model):
    taste = models.CharField(max_length=50)
        
    def __str__(self):
        return self.taste

class Clients(models.Model):
    name = models.CharField(max_length=50)    
        
    def __str__(self):
        return self.name    

class Icecream_shop(models.Model):
    quantity = models.IntegerField()
    sales = models.FloatField()
    address = models.CharField(max_length=50)    
    icecream = models.ForeignKey(Icecream, on_delete=models.CASCADE)
    icecream_taste = models.ForeignKey(Icecream_Taste, on_delete=models.CASCADE)
    clients = models.ForeignKey(Clients, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sales)
