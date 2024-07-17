Briefing proyecto

1.  Ideas primarias, secundarias y planteamiento de objetivos:

Ideas Primarias:
●   Mar necesita digitalizar la gestión de los alumnos y las cuentas de la Escuela de Música Armonía.
●   La información se debe almacenar en una base de datos SQL.
●   Gestión de datos a través de una API tipo REST.

Ideas Secundarias:
●   Alumnos y profesores deben tener sus datos almacenados de manera estructurada.
●   Las clases tienen diferentes precios, descuentos y niveles.
●   Los alumnos pueden estar inscritos en varias clases, incluso del mismo tipo de instrumento.
●   Los familiares de primer grado reciben un 10% de descuento sobre el total de las clases.
●   Los precios de las clases deben ser modificables.

    Objetivos:

●   Digitalizar la gestión de alumnos y cuentas de la Escuela de Música Armonía.
●   Crear una base de datos SQL para almacenar información sobre alumnos, profesores y clases.
●   Implementar una API REST para la gestión de datos.
●   Diseñar un esquema de base de datos que contemple los distintos precios, niveles y descuentos de las clases.
●   Permitir la inscripción de alumnos en múltiples clases y niveles.
●   Incluir la opción de descuentos para familiares de primer grado.
●   Hacer los precios de las clases modificables.

2.  Tareas necesarias para lograr los objetivos planteados en las ideas.
2.1 Análisis y diseño de la base de datos:
●   Identificar entidades y relaciones.
●   Crear diagramas entidad-relación (ER).
●   Diseñar el esquema de la base de datos en SQL.
2.2 Desarrollo de la base de datos:
●   Implementar la base de datos según el diseño.
●   Crear tablas y definir relaciones entre ellas.
2.3 Diseño de la API REST:
●   Definir los endpoints necesarios para gestionar alumnos, profesores y clases.
●   Diseñar las operaciones CRUD (Create, Read, Update, Delete).
2.4 Implementación de la API REST:
●   Desarrollar los endpoints definidos.
●   Conectar la API con la base de datos.
2.5 Gestión de precios y descuentos:
●   Implementar lógica para calcular precios con descuentos.
●   Diseñar la funcionalidad para modificar precios.
2.6 Gestión de usuarios y seguridad:
●   Implementar autenticación y autorización en la API.
●   Diseñar roles y permisos.
2.7 Pruebas y validación:
●   Probar la API y la base de datos.
●   Validar que se cumplen los requisitos funcionales.
2.9 Documentación y capacitación:
●   Documentar la API y la base de datos.
●   Proporcionar capacitación a Mar y su equipo.

Entidades y Relaciones:

●   Entidades: Alumnos, Profesores, Clases, Instrumentos, Inscripciones, Niveles, Precios.
●   Relación: Un alumno puede estar inscrito en varias clases, y una clase puede tener varios alumnos inscritos. Un instrumento puede estar asociado con varias clases y profesores.
Definir las relaciones:
●   Un Alumno puede inscribirse en muchas Clases.
●   Una Clase puede ser impartida por uno o varios Profesores.
●   Un Instrumento puede tener varias Clases.
●   Un Nivel se asocia a una Clase.

Organización en jira: https://escuelamusica.atlassian.net/jira/software/projects/SCRUM/boards/1/backlog

Documentación en Notion: https://www.notion.so/inuvi/Escuela-M-sica-956d213eaf2f4c0680aae8783f4a9022?pvs=4

Presentación de negocio en Canva: https://www.canva.com/design/DAGKuv758fQ/Q8-2_DbY2vwWDHi-y2c0vw/view?utm_content=DAGKuv758fQ&utm_campaign=designshare&utm_medium=link&utm_source=editor

