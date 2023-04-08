import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Product, Owner, Category



class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ['id', 'title', 'owner', 'quantity', 'description', 'category', 'date_created']



class OwnerType(DjangoObjectType):
    class Meta:
        model = Owner
        fields = ['id', 'first_name', 'last_name', 'location']



class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        field = ['id', 'title']




class Query(graphene.ObjectType):

    all_products =  graphene.List(ProductType)
    

    def resolve_all_products(root, info, id):
        return Product.objects.get(pk=id)