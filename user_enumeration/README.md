# Ejemplos de User Enumeration

Esta carpeta contiene ejemplos de cómo puede ocurrir la enumeración de usuarios en aplicaciones web, específicamente en los endpoints de login y restablecimiento de contraseña.


## Archivos
- `insecure_endpoints.py`: Todos los endpoints vulnerables a user enumeration en un solo archivo.
- `secure_endpoints.py`: Todos los endpoints implementados de forma segura, evitando user enumeration.


## ¿Qué es User Enumeration?
La enumeración de usuarios ocurre cuando una aplicación revela si un usuario existe o no a través de mensajes de error diferentes, permitiendo a un atacante descubrir usuarios válidos.

## Ejemplo inseguro
En `insecure_endpoints.py` cada endpoint responde de forma diferente según si el usuario existe o no, lo que permite a un atacante enumerar usuarios válidos.

## Ejemplo seguro
En `secure_endpoints.py` todos los endpoints responden con mensajes y tiempos genéricos, sin revelar si el usuario existe o no, mitigando el riesgo de user enumeration.

## Uso
Puedes ejecutar cualquiera de los archivos con:


```
python insecure_endpoints.py
# o
python secure_endpoints.py
```

Luego prueba los endpoints con herramientas como curl o Postman.
