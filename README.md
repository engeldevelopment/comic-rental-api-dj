# Kata: Alquiler de Comics. :books:


Willian tiene una tienda donde alquila historietas usadas,
donde su costo depende de su precio de compra menos un descuento
por el estado del ejemplar: excelente (10%), bueno (20%), aceptable (25%),
deteriorado (30%), dañado (50%).  


## End Points disponibles :link:

- Listado de comics: **GET** ***/api/v1/comics/***
- Listado de comics por status: **GET** ***/api/v1/comics?status=xxx***
  - valores permitidos para el status:  
    - excellent
    - good
    - acceptable
    - impaired
    - damaged
- Listado de rentals: **GET** ***/api/v1/rentals/***  
- Alquilar una comic: **POST** ***/api/v1/comics/:id/rentals/***  
  EL cuerpo de la petición tiene que ser:  
  ```
   {
        "days": integer,
        "client": character 
   }
  ```
  
 La estructura del listado de Rentals será la siguiente:  
 ```
[ 
    {
        "id": "61d07f22-6644-4562-a353-b24ed859042c",
        "days": 5,
        "client": "Engel Pinto",
        "amount": 2.5,
        "price": 5.0,
        "comic": {
            "id": 3,
            "name": "X-Man",
            "price": 5.0,
            "status": "damaged"
        },
        "rented_at": "2020-03-19T19:00:00",
        "finished_at": "2020-03-24T19:00:00"
    }
]
```

## Tecnologías utilizadas :construction:

- Python 3.8
- Django
- Django Rest Framework
- Django filter
- Django Injector
