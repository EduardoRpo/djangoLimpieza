from django.db import models

# Create your models here.
class Tipo(models.Model):
    nombre=models.CharField(max_length=30, verbose_name='Tipo')
    
    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        

    def __str__(self):
        return self.nombre

class Documentos(models.Model):
    fecha=models.DateTimeField(auto_now_add=True)
    tipo=models.ForeignKey(Tipo, on_delete=models.PROTECT )
    #codigo=models.ForeignKey(Codigo, on_delete=models.PROTECT)
    #codigo=models.CharField(max_length=30)
    image = models.FileField(upload_to='LySi/Documentos/', verbose_name='Archivo')
    observaciones=models.TextField(max_length=250, blank=True)

    def __str__(self):
         txt="{0}"
         return txt.format(self.fecha)
    
    class Meta:
        verbose_name='Documento'
        verbose_name_plural='Documentos'
        ordering =['fecha']  