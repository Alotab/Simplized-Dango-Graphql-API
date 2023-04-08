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

    all_products = graphene.List(ProductType, id=graphene.Int())
    all_product = graphene.Field(ProductType, id=graphene.Int())
    all_owner = graphene.Field(OwnerType, id=graphene.Int())
    

    def resolve_all_products(root, info):
        return Product.objects.all()
    
    def resolve_all_product(root, info, id):
        return Product.objects.get(pk=id)
    
    def resolve_all_owner(root, info, id):
        return Owner.objects.get(id=1)
    


class CreateOwnerMutation(graphene.Mutation):

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        location = graphene.String(required=True)

    owner = graphene.Field(OwnerType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, location):
        owner = Owner(first_name=first_name, last_name=last_name, location=location)
        owner.save()

        return CreateOwnerMutation(owner=owner)


class Mutation(graphene.ObjectType):
    create_owner = CreateOwnerMutation.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)