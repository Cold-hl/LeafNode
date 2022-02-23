from django.db import models


# Create your models here.

# 节点信息
class Nodes(models.Model):
    Nodes_name = models.CharField(verbose_name="节点名称", max_length=200)
    Nodes_data = models.TextField(verbose_name="节点数据")
    Nodes_id = models.ManyToManyField('Edges')


# 边信息
class Edges(models.Model):
    Edges_name = models.CharField(verbose_name="节点名称", max_length=200)
    Edges_data = models.TextField(verbose_name="节点数据")
