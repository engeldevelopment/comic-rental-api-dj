# Kata: Alquiler de Comics. :books:


Willian tiene una tienda donde alquila historietss usadas,
donde su costo depende de su precio de compra menos un descuento
por el estado del ejemplar: excelente (10%), bueno (20%), aceptable (25%),
deteriorado (30%), dañado (50%).  


## End Points disponibles :link:

- Listado de comics: **GET** ***/api/v1/comics***
- Alquilar una comic: **POST** ***/api/v1/comics/:id/rent***  
  EL cuerpo de la petición tiene que ser:  
  ```
   {
        "days": integer,
        "client": character 
   }
  ```

## Tecnologías utilizadas :construction:

- Python 3.8
- Django
- Django Rest Framework
