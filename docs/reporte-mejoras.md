# Informe de Mejoras e Iteraciones

> **Nota:** Este documento registra la evolución técnica, los componentes de resiliencia implementados en el MVP y el cierre de las iteraciones de procesamiento documental y consultas locales.

## 1. Mejoras de Arquitectura (Implementadas)

* **Delegación de Responsabilidades:** Se refactorizó el script principal (`app.py`), reduciéndolo a un orquestador limpio y delegando la lógica de lectura y procesamiento de documentos a módulos especializados (`utils_pdf.py`).
* **Almacenamiento y Consulta Resiliente:** Se implementó una capa de manejo de rutas locales y control de excepciones, asegurando que la aplicación sobreviva a archivos ausentes o lecturas interrumpidas de normativas jurídicas.
* **Prevención de Errores en Tiempo de Ejecución:** Se incorporó un sistema de validación de entradas de texto y manejo de nulos, garantizando que consultas incompletas no bloqueen el servidor de Flask.

## 2. Iteraciones de Procesamiento y Experiencia de Usuario (Implementadas)

* **Extracción Estructurada por Páginas:** Se incluyó un mecanismo automatizado mediante `pypdf` que detecta y extrae el contenido textual de leyes y decretos respetando la paginación original.
* **Feedback de Procesamiento:** Implementación de mensajes claros en la consola y respuestas estructuradas que comunican el estado de carga de las normativas locales.
* **Contextualización Documental:** Integración de esquemas limpios orientados al análisis jurídico, eliminando dependencias externas de internet para garantizar total privacidad.
* **Robustez de Entorno:** Configuración de dependencias precisas en archivos de requerimientos para facilitar la ejecución y despliegue del software en cualquier equipo.
