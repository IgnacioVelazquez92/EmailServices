# Sistema de Campañas de Email

Sistema de gestión de campañas de email desarrollado con Django que permite a los usuarios crear listas de contactos y enviar campañas de email masivas.

## Características Principales

- Autenticación de usuarios
- Gestión de listas de contactos (CRUD)
- Creación y envío de campañas de email
- Validación de direcciones de email
- Dashboard intuitivo
- Diseño responsive con Bootstrap

## Estructura de la Base de Datos

### Modelos Principales

1. **User**
   - Modelo estándar de Django para autenticación
   - Gestiona credenciales y datos básicos del usuario

2. **ContactList**
   - Almacena las listas de contactos
   - Cada lista pertenece a un usuario específico
   - Contiene nombre y fecha de creación

3. **ContactEmail**
   - Almacena emails individuales
   - Vinculado a una lista de contactos
   - Incluye validación de formato de email

4. **Campaign**
   - Gestiona las campañas de email
   - Contiene asunto, cuerpo y estado del envío
   - Se relaciona con las listas de contactos objetivo

## Diagrama Entidad-Relación
A continuación, se incluye un diagrama de entidad-relación que describe la estructura del sistema:

![Diagrama ER](/DiagramaER.svg)


---

## Instalación y configuración

### Requisitos previos
- Python 3.10 o superior.
- Django 4.x.
- Un servidor de correo electrónico configurado.

### Pasos de instalación
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-repositorio/email-campaign-system.git
   cd email-campaign-system
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configurar las variables de entorno en un archivo `.env`:
   ```env
   SECRET_KEY=tu-clave-secreta
   EMAIL_HOST=smtp.tu-servidor.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=tu-email@dominio.com
   EMAIL_HOST_PASSWORD=tu-contraseña
   EMAIL_USE_TLS=True
   DEFAULT_FROM_EMAIL=tu-email@dominio.com
   ```

5. Realizar las migraciones:
   ```bash
   python manage.py migrate
   ```

6. Ejecutar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

---

## Estructura del proyecto

```plaintext
/
├── Contacts/
├───── templates/
├───── static/          
├── Campaigns/           
├───── templates/                    
├── manage.py             
```    
---

## Video explicativo
En esta sección se incluirá un enlace o video embebido que explique cómo funciona la aplicación, destacando:

1. Navegación por las secciones de la aplicación.
2. Creación de listas de contactos.
3. Creación y envío de una campaña.
4. Edición de perfil de usuario.

**Placeholder para el video:**

[![Video explicativo](https://img.youtube.com/vi/VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=xjqXC0UCPzo)


---

## Contribución

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu función o corrección: `git checkout -b mi-rama`.
3. Envía tus cambios mediante un Pull Request.

---

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

