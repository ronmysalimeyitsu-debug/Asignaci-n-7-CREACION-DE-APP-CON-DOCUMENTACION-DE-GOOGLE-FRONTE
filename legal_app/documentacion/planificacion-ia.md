# Planificación y Uso de IA Generativa

Durante la concepción y desarrollo de la aplicación de consulta legal, se implementó un flujo de trabajo asistido por IA Generativa. El desarrollador actuó como arquitecto y líder técnico, delegando la estructuración de scripts y la lógica de procesamiento de documentos a la IA, mientras mantenía el control absoluto sobre la arquitectura y la precisión de los datos jurídicos.

## 1. Casos de Uso Específicos (Delegados)

* **Procesamiento de Archivos PDF:** Soporte técnico para la integración y configuración inicial de bibliotecas (`pypdf`) requeridas para la extracción de texto local.
* **Estructuración de Endpoints:** Generación del esqueleto base para las consultas de texto y la gestión de bases de datos.
* **Maquetación Rápida:** Generación de clases y componentes visuales estándar para la interfaz de usuario de consulta.
* **Población de Datos de Prueba:** Redacción de extractos y resúmenes normativos para validar el correcto funcionamiento del sistema local.

## 2. Decisiones Humanas (No delegadas)

* **Definición de la Estructura de Directorios:** Exigencia estricta de una arquitectura modular separando lógica, rutas y almacenamiento para asegurar escalabilidad.
* **Validación de Contenido Legal:** Verificación rigurosa de que la extracción de artículos e información jurídica coincida exactamente con las normativas originales.
* **Control de Ejecución:** Auditoría del código para garantizar que la carga de archivos locales funcione de manera fluida y sin interrupciones.
