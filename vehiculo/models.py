from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    marcas_opciones=[
        ('FIAT','Fiat'),
        ('CHEVROLET','Chevrolet'),
        ('FORD','Ford'),
        ('TOYOTA','Toyota'),
         ]
    categoria_opciones=[
        ('PARTICULAR','Particular'),
        ('TRANSPORTE','Transporte'),
        ('CARGA','Carga'),
    ]
    
    id=models.AutoField(primary_key=True)
    marca = models.CharField(max_length=20,choices=marcas_opciones,default='FORD',verbose_name='Marca')
    modelo=models.CharField(max_length=100,verbose_name='Modelo')
    serial_carroceria=models.CharField(max_length=50,verbose_name='Serial Carroceria')
    serial_motor=models.CharField(max_length=50,verbose_name='Serial Motor')
    categoria=models.CharField(max_length=20,choices=categoria_opciones,verbose_name='Categoria',default='PARTICULAR')
    precio=models.IntegerField(verbose_name='Precio')
    fecha_creacion=models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Creacion')
    fecha_modificacion=models.DateTimeField(auto_now=True,verbose_name='Fecha de modificacion')

   
        