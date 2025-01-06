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

### Relaciones

- Un Usuario puede tener múltiples Listas de Contactos y Campañas
- Una Lista de Contactos puede contener múltiples Emails
- Una Campaña puede dirigirse a múltiples Listas de Contactos

## Requisitos Técnicos

- Python 3.8+
- Django 4.0+
- Bootstrap 5
- PostgreSQL (recomendado para producción)

## Instalación y Configuración

[Instrucciones pendientes de desarrollo]

## Uso

[Instrucciones pendientes de desarrollo]

## Consideraciones de Seguridad

- Validación de emails con expresiones regulares
- Autenticación requerida para todas las operaciones
- Aislamiento de datos entre usuarios
- Manejo seguro de errores

## Licencia

[Pendiente de definir]
