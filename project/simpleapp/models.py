from django.db import models
from django.core.validators import MinValueValidator


# # Создаём модель товара
# class Product(models.Model):
#     name = models.CharField(
#         max_length=50,
#         unique=True,  # названия товаров не должны повторяться
#     )
#     description = models.TextField()
#     quantity = models.IntegerField(
#         validators=[MinValueValidator(0)],
#     )
#     # поле категории будет ссылаться на модель категории
#     category = models.ForeignKey(
#         to='Category',
#         on_delete=models.CASCADE,
#         related_name='products',  # все продукты в категории будут доступны через поле products
#     )
#     price = models.FloatField(
#         validators=[MinValueValidator(0.0)],
#     )
#
#     def __str__(self):
#         return f'{self.name.title()}: {self.description[:20]}'
#
#
# #  создаём категорию, к которой будет привязываться товар
# class Category(models.Model):
#     name = models.CharField(max_length=100, unique=True)  # названия категорий тоже не должны повторяться
#
#     def __str__(self):
#         return f'{self.name.title()}'



# Создаём модель новости
class News(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
    )
    text = models.TextField()

    dateCreation = models.DateTimeField(auto_now_add=True)

    author = models.CharField(
        max_length=50,
    )

    # category = models.ForeignKey(
    #     to='Category',
    #     on_delete=models.CASCADE,
    #     related_name='news',  # все продукты в категории будут доступны через поле products
    # )

    def __str__(self):
        return f'{self.title.title()}. Дата публикации: {self.dateCreation.strftime("%d %B, %Y")}. {self.text[:50]}...'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'