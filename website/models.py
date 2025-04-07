import uuid
from django.db import models
from django.contrib.auth.models import User


class CarouselImages(models.Model):
    image = models.ImageField(upload_to='carousel-images/', blank=True, null=True, verbose_name="Imagem do carrossel")

    class Meta:
        verbose_name = "Imagem do Carrossel"
        verbose_name_plural = "Imagens do Carrossel"


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Nome")
    description = models.TextField(blank=True, null=True, verbose_name="Descrição", default="Categoria sem uma descrição")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Nome do produto")
    description = models.TextField(verbose_name="Descrição do produto")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço do produto", default=0.00)
    stock = models.PositiveIntegerField(verbose_name="Em estoque")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name="Categoria do produto")
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name="Desconto (%)")
    image = models.ImageField(upload_to='uploads/', blank=True, null=True, verbose_name="Imagem do produto")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.category.name}"

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name="Cliente")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pendente'),
            ('processing', 'Processando'),
            ('shipped', 'Enviado'),
            ('delivered', 'Entregue'),
            ('cancelled', 'Cancelado')
        ],
        default='pending', verbose_name="Estado do pedido"
    )

    def __str__(self):
        return f'Pedido {self.id} - {self.user.username}'

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"


class OrderItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name="Pedido")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Produto")
    quantity = models.PositiveIntegerField(verbose_name="Quantidade")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

    class Meta:
        verbose_name = "Item do Pedido"
        verbose_name_plural = "Itens do Pedido"


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment', verbose_name="Pedido")
    transaction_id = models.CharField(max_length=255, verbose_name="ID da Transação")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pendente'),
            ('completed', 'Concluído'),
            ('failed', 'Falhou')
        ],
        default='pending', verbose_name="Estado do Pagamento"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return f'Pagamento {self.transaction_id} - {self.status}'

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"


class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Cliente")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', verbose_name="Produto")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="Estrelas")
    comment = models.TextField(blank=True, null=True, verbose_name="Comentário")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return f'Avaliação de {self.user.username} para {self.product.name}'

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
