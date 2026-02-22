# Proyecto Flask para pruebas IDOR

Este proyecto es una aplicación básica en Flask para realizar pruebas de IDOR (Insecure Direct Object Reference) usando diferentes tipos de identificadores: ID incrementable, email, UUID y slug.

## Estructura
- app.py: Aplicación principal de Flask
- requirements.txt: Dependencias del proyecto

## Uso

1. Crea un ambiente virtual (opcional pero recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Define la clave secreta JWT (puedes cambiar el valor):
   ```bash
   export JWT_SECRET="mysecret"
   ```
4. Ejecuta la aplicación:
   ```bash
   python app.py
   ```
5. Genera un token JWT para tu empresa (ejemplo en Python):
   ```python
   import jwt
   token = jwt.encode({"company": "Empresa A"}, "mysecret", algorithm="HS256")
   print(token)
   ```
   Cambia "Empresa A" y "mysecret" según corresponda.
6. Usa el token en tus peticiones HTTP:
   - Agrega el header:
     ```
     Authorization: Bearer <token>
     ```
   - Ejemplo con curl:
     ```bash
     curl -H "Authorization: Bearer <token>" http://localhost:5000/user/1
     ```
7. Accede a los endpoints para probar el comportamiento IDOR:
   - `GET /user/<id>`
   - `GET /user/email/<email>`
   - `GET /user/uuid/<uuid>`
   - `GET /user/slug/<slug>`

## Notas
- Este proyecto es solo para fines educativos y de pruebas de seguridad.
