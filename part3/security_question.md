## Caso de Uso - Sistema de seguridad

Suponga que es el jefe de ingeniería de una nueva y emocionante startup tecnológica que instala paneles solares a través de una aplicación.
¡Es Uber para paneles solares! Estás realizando una auditoría de seguridad de la infraestructura de tu aplicación. Estás utilizando el Top 10 de OWASP
para 2021 como guía sobre qué problemas de seguridad podrían ser un problema para usted.

Su infraestructura se implementa en contenedores de Kubernetes en Amazon Web Services. Tiene estos componentes:
- Una aplicación móvil para Android e iOS.
- Una interfaz web que el cliente puede utilizar en lugar de la aplicación móvil. Esto está escrito en Javascript con Next.js.
- Una base de datos MySQL que almacena información del cliente, incluidas contraseñas, direcciones particulares, números de teléfono, etc.
   También contiene información del pedido del cliente.
- Un backend de Python implementado en FastAPI. Esto se comunica con la base de datos y proporciona datos tanto a la interfaz web como al \
   aplicaciones móviles.

Tiene 12 empleados de ingeniería de software que tienen acceso completo al sistema, 3 empleados de atención al cliente que pueden ver
información del cliente y realizar cambios en pedidos y cuentas, y un empleado de ventas.

Utilizando OWASP Top 10, ¿qué buscaría para que su sistema sea seguro?

---
**Solución**

Lo primero a considerar es que todo mi 
proyecto está orquestado por
una tecnología llamada **Kubernetes** que se ejecuta en un servidor del proveedor
**Amazon Web Services**, así que 
debo considerar varios puntos de seguridad para cada tecnología implementada en el proyecto comenzando por ésta misma.

---

### 1. Seguridad en AWS - Kubernetes
Amazon Web Services (AWS) ofrece varias ventajas en términos de seguridad al utilizar Kubernetes en su plataforma.




| Aspecto de Seguridad          | Ventajas en AWS para Kubernetes                                        |
|------------------------------|-----------------------------------------------------------------------|
| Administración de Identidad y Acceso | AWS IAM permite la gestión granular de permisos y accesos a recursos.    |
| Virtual Private Cloud (VPC)   | AWS VPC crea una red privada virtual para aislar clústeres de Kubernetes. |
| Security Groups y Network ACLs | Controla el tráfico de red con reglas de seguridad a nivel de red.     |
| AWS EKS (Elastic Kubernetes Service) | AWS ofrece un servicio gestionado de Kubernetes con actualizaciones de seguridad regulares. |
| AWS CloudTrail y CloudWatch    | Audita acciones en tu cuenta y monitorea eventos de seguridad.          |
| AWS Key Management Service (KMS) | Gestiona y protege claves de cifrado para datos en repositorios y en tránsito. |
| Auto Scaling y Load Balancing | Escala automáticamente los nodos de Kubernetes y proporciona balanceo de carga. |
| Federación de Identidad con AWS | Permite la integración con sistemas de identidad externos o propios.    |
| Integración con AWS WAF       | Protege aplicaciones contra ataques web comunes cuando se utiliza un balanceador de carga de AWS. |
| Actualizaciones y Parches     | AWS se encarga de mantener actualizada la infraestructura subyacente y aplicar parches de seguridad. |

**Conclusión:**
Aunque AWS nos proporciona herramientas y servicios como **Kubernetes** hay que tener en cuenta que la seguridad en la nube sigue siendo una responsabilidad compartida entre AWS y el cliente. 

La configuración incorrecta o la mala gestión de la seguridad pueden resultar en vulnerabilidades.

Por lo tanto debemos ser cuidadosos y planificar cada etapa de nuestro proyecto.

---
### 2. Seguridad en el Frontend - NextJS

Hay que tener en cuenta que **NextJS** nos permite hacer aplicaciones híbridas tanto como front y back, en este caso lo usaremos del lado front (cliente) y **FastApi** será el framework para nuestro Backend. 

#### Puntos a considerar

**1. Validar la entrada de datos**

* Formularios
* Consultas URL
* Cookies

Se debe validar y sanitizar adecuadamente por medio
de funciones y escape de datos para prevenir ataques **XSS**

**2. Configuración de HTTPS**

Usar un certificado SSL HTTPS en lugar de HTTP. Esto cifra la comunicación entre el cliente y el servidor, lo que protege los datos en tránsito y garantiza la autenticidad del servidor.

**3. Actualizaciones regulares**

Es necesario mantener actualizadas las dependencias y bibliotecas que se usen en la aplicación, debido a que estas actualizaciones suelen incluir parches de seguridad importantes.

**4. Uso de cookies y almacenamiento local**

* Utilizar cookies de manera segura
* Evitar el almacenamiento de información sensible en el navegador del usuario. 
* Asegurarse de que las cookies no sean accesibles desde scripts no confiables.

**5. Validación en el servidor**

A pesar de no estar utilizando SSR (Server Side Rendering), es buena práctica validar y procesar nuevamente todos los datos en el servidor antes de realizar acciones importantes. 

No se debe confiar 100% en la validación del lado del cliente.

**6. Escaneo de seguridad**
Realizar análisis de seguridad y pruebas de penetración en la aplicación para identificar posibles vulnerabilidades en el código del lado del cliente.

**7. Educación del equipo**
Capacitar al equipo de desarrollo en seguridad web y metodologías como **OWASP** para conocer las mejores prácticas y escribir código seguro.

---
### 3. Seguridad en la base de datos - MySQL

**Actualizar y aplicar parches de seguridad regularmente**
Hay que asegurarse de mantener el sistema operativo, MySQL y cualquier otro software relacionado actualizado con los últimos parches de seguridad. Los exploits conocidos se corrigen en las actualizaciones.

**Limitar el acceso físico y de red**
Asegurarse que el servidor MySQL esté en un lugar seguro, en nuestro caso en los servidores de **AWS** y restringir el acceso físico a personas no autorizadas. Además, configura un firewall para limitar el acceso a las direcciones IP necesarias y utiliza conexiones seguras (SSL/TLS).

**Usar autenticación segura**
Utilizar autenticación sólida para los usuarios de MySQL. Evitar el uso de contraseñas débiles y asegurarse de que cada usuario tenga solo los permisos necesarios para realizar su trabajo.

**Encriptar los datos**
Utiliza encriptación para proteger los datos almacenados en la base de datos. MySQL ofrece soporte para cifrado de datos en reposo y en tránsito. Asegúrate de habilitar estas funciones.

**Realizar copias de seguridad y almacenarlas de forma segura**
Realizar copias de seguridad regulares de los datos y almacenar en un lugar seguro y fuera del servidor MySQL. Las copias de seguridad son esenciales en caso de pérdida de datos o ataques.

**Aplicar principios de seguridad en el código**
Asegurarse de que las aplicaciones que acceden a la base de datos estén programadas con seguridad en mente. Utilizar sentencias preparadas para evitar inyecciones SQL y valida y filtra los datos de entrada. En este caso debemos tener muy en cuenta el **ORM** que usamos en conjunto con **FastApi**.

**Auditar y monitorear**
Configurar la auditoría de MySQL para registrar eventos importantes y establece alertas para eventos sospechosos. Monitorea los registros y actividades en la base de datos de forma constante.

**Restringir el acceso físico y lógico**
Limitar el acceso a los servidores y a la base de datos solo a las personas autorizadas. Utilizar contraseñas seguras para acceder a los sistemas y cambia las contraseñas periódicamente.

**Implementar políticas de seguridad**
Crear políticas de seguridad de datos que incluyan restricciones de acceso, manejo de contraseñas, retención de registros y otras directrices para el manejo seguro de datos sensibles.

**Capacitación al personal**
Asegurarse de que el personal que trabaja con el servidor MySQL esté capacitado en seguridad de bases de datos y siga buenas prácticas de seguridad.

---
### 4. Seguridad en el Backend - FastApi

La seguridad es de suma importancia más en nuestro
backend, debemos tener en cuenta las siguientes recomendaciones.

**Autenticación y autorización**
Utiliza sistemas de autenticación sólidos para verificar la identidad de los usuarios antes de permitirles acceder a datos sensibles. FastAPI admite diversos métodos de autenticación, como JWT (JSON Web Tokens) o Basic Auth. Hay que asegurarse de que solo los usuarios autenticados y autorizados tengan acceso a los recursos adecuados.

**Validación de datos de entrada**
Utilizar la validación de datos de entrada proporcionada por FastAPI. Esto ayuda a prevenir ataques de inyección SQL y otros ataques de seguridad. FastAPI utiliza la validación de datos Pydantic para asegurarse de que los datos de entrada cumplan con las especificaciones esperadas.

También existe un Patrón de diseño muy usado llamado **DTO** (Data Transfer Object) el cuál nos permite
validar los datos de entrada y salida.

**Conexión segura a MySQL**
Cuando nos conectemos a la base de datos MySQL desde FastAPI, hay que asegurarse de utilizar conexiones seguras. Hay bibliotecas como `mysql-connector-python` con SSL o TLS para encriptar la conexión entre FastAPI y MySQL.

**Utilizar sentencias SQL seguras**
Evitar la construcción manual de sentencias SQL concatenando datos de entrada directamente en las consultas. En su lugar, utilizar consultas parametrizadas o un **ORM (Object-Relational Mapping)** para proteger contra inyecciones SQL.

**Configurar la seguridad de FastAPI**
FastAPI proporciona capacidades de seguridad incorporadas, como la protección CSRF (Cross-Site Request Forgery) y la protección contra ataques DDoS (Denial of Service). Asegúrate de habilitar estas opciones según sea necesario.

**Almacenamiento seguro de contraseñas**
En este caso debemos almacenar contraseñas de usuario en la base de datos, utilizar una función de hash segura como bcrypt para almacenar las contraseñas de forma segura. Nunca se debe almacenar contraseñas en texto plano.

**Auditoría y registro de actividad**
Configurar el registro de actividad para rastrear y auditar eventos importantes, como el acceso a datos sensibles o intentos de autenticación fallidos.

**Actualizaciones y parches**
Mantener actualizado FastAPI y todas las dependencias del proyecto para asegurarse de estar protegido contra las últimas vulnerabilidades.

**Capacitación del equipo**
Asegurarse de que el equipo de desarrollo esté capacitado en seguridad web y conozca las mejores prácticas de seguridad.

**Pruebas de seguridad**
Realizar pruebas de seguridad, como pruebas de penetración y pruebas de seguridad automatizadas, para identificar y solucionar posibles vulnerabilidades en tu aplicación.

---
**Conclusión del caso**
Después de haber visto de manera general prácticas de seguridad para cada tecnología involucrada en nuestro proyecto podemos concluir que OWASP está presente en cada una de las tecnologías mencionadas anteriormente y es muy importante implementar ésta metodología de buenas prácticas para que la nueva startup tecnológica que instala paneles solares brinde a sus usuarios una aplicación confiable.

> **Tiene 12 empleados de ingeniería de software que tienen acceso completo al sistema, 3 empleados de atención al cliente que pueden ver información del cliente y realizar cambios en pedidos y cuentas, y un empleado de ventas.**

Esta parte me parece importante analizar y es que al tener un número pequeño de empleados es mas fácil crear conciencia y buenos hábitos para implementar buenas prácticas de seguridad como nos menciona **OWASP**.

> Consulta realizada por: César Camilo Ruano Martínez, con la ayuda de mi Dios ♥.