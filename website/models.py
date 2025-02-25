import uuid
from django.db import models
from django.contrib.auth.models import User


class CarouselImages(models.Model):
    image = models.ImageField(upload_to='carousel-images/', blank=True, null=True,verbose_name="Imagem do carosel")


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,verbose_name="Nome")
    description = models.TextField(blank=True, null=True,verbose_name="Descrição", default="Categoria sem uma descrição")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,verbose_name="Nome do produto")
    description = models.TextField(verbose_name="Descrição do produto")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Preço do produto")
    stock = models.PositiveIntegerField(verbose_name="Em Stock")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',verbose_name="Categoria do produto")
    image = models.ImageField(upload_to='products/', blank=True, null=True,verbose_name="Imagem do produto")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders',verbose_name="Cliente")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('processing', 'Processing'),
            ('shipped', 'Shipped'),
            ('delivered', 'Delivered'),
            ('cancelled', 'Cancelled')
        ],
        default='pending',verbose_name="Estado do pedido"
    )

    def __str__(self):
        return f'Order {self.id} - {self.user.username}'

class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items',verbose_name="Pedido")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produto")
    quantity = models.PositiveIntegerField(verbose_name="Quantidade")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Preço")

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    transaction_id = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('failed', 'Failed')
        ],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Payment {self.transaction_id} - {self.status}'

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE ,verbose_name="Cliente")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews',verbose_name="Produto")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)],verbose_name="Estrelas")
    comment = models.TextField(blank=True, null=True,verbose_name="Comentário")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} for {self.product.name}'
