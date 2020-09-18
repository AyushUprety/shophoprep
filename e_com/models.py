from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=40,blank=False, null=False)
    phoneNo=models.CharField(max_length=50,null=False)
    email=models.EmailField(max_length=100,null=False)
    password=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name

class ProductDetail(models.Model):
    title=models.CharField(max_length=40,blank=False, null=False)
    price=models.IntegerField(null=False)
    summary=models.CharField(max_length=100,null=False)
    sellerlocation=models.CharField(max_length=100,null=False)
    quantity=models.IntegerField(blank=False, null=False)
    imagefile= models.FileField(upload_to='images/', null=True)

    def __str__(self):
        return self.title + ": " + str(self.imagefile)

class CompanyProductDetail(models.Model):
	title=models.CharField(max_length=200,blank=False, null=False)
	price=models.IntegerField()
	summary=models.CharField(max_length=100,null=False)
	sellerlocation=models.CharField(max_length=100,null=False)
	quantity=models.IntegerField()
	imagefile= models.FileField(upload_to='images/', null=True)
	digital = models.BooleanField(default=False,null=True, blank=True)

	def __str__(self):
		 return self.title + ": " + str(self.imagefile)

	@property
	def imageURL(self):
		try:
			url = self.imagefile.url
		except:
			url = ''
		return url          

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name





class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 
	
class OrderItem(models.Model):
	product = models.ForeignKey(CompanyProductDetail, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total



class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

