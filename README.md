# Simplized-Dango-Graphql-API



## Query the Product data  from the DB


`List Product with specific ID`

```
query{
  allProduct(id:3){
    id
    title
    description
    category{
      title
    }
    owner{
      firstName
    }
  }
}
```


`Query all Products from the database`

```
query {
  allProducts{
    id
    title
    quantity
    owner{
      id
      firstName
      lastName
      location
    }
    category{
      title
    }
  }
}
```


## Query owner / user data from the DB


`Query specific owner using the ID`

```
query{
  allOwner(id:1){
    id
    lastName
  }
}
```




## GraphQL CRUD Operations

`Create Owner / User`

```
mutation{
  createOwner(firstName: "Joe", lastName: "Jesus", location: "Benghazi"){
    owner{
      id
    }
  }
}
```



`Update Owner / User using their ID, first_name, last_name and location`

```mutation{
	updateOwner(id: 4, firstName: "Bismark", lastName: "Jaylon",location: "Benghazilization"){
    owner{
      id
      firstName
      lastName
      location
    }
  }
}```



`Delete Owner / User using only their ID`

```mutation{
  deleteOwner(id:4){
    owner{
      firstName
    }
  }
}```