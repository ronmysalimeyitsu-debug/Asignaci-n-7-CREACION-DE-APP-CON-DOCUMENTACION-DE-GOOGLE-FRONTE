import os

# Create the 'documentacion' directory inside 'legal_app'
docs_dir = "legal_app/documentacion"
os.makedirs(docs_dir, exist_ok=True)

# 1. planificacion-ia.md
planificacion_content = """# Planificación y Uso de IA Generativa

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
"""

with open(os.path.join(docs_dir, "planificacion-ia.md"), "w", encoding="utf-8") as f:
    f.write(planificacion_content)

# 2. reporte-mejoras.md
reporte_content = """# Reporte de Mejoras y Optimización

Este documento recopila las optimizaciones implementadas en la aplicación de gestión documental y legal para garantizar un rendimiento óptimo en entornos locales.

## 1. Mejoras de Rendimiento
* **Lectura Eficiente por Páginas:** Implementación de bucles optimizados con `pypdf` para evitar el consumo excesivo de memoria RAM al procesar documentos extensos.
* **Manejo de Excepciones:** Incorporación de bloques de control para evitar fallos críticos cuando un archivo PDF no se encuentra disponible en la ruta especificada.

## 2. Experiencia de Usuario (UX)
* **Retroalimentación Visual:** Mensajes claros en consola e interfaz sobre el estado de carga y extracción de los archivos legales.
"""

with open(os.path.join(docs_dir, "reporte-mejoras.md"), "w", encoding="utf-8") as f:
    f.write(reporte_content)

# 3. resumen-fases.md
resumen_content = """# Resumen de Fases del Proyecto

El desarrollo de la aplicación se estructuró en fases metódicas para asegurar la calidad y robustez del software:

* **Fase 1 - Configuración Inicial y Repositorio:** Creación de la estructura base del proyecto, configuración de Git y subida inicial del entorno a GitHub.
* **Fase 2 - Documentación:** Redacción y estructuración del archivo `README.md` y la carpeta de documentación técnica.
* **Fase 3 - Procesamiento de Documentos:** Implementación de los módulos en Python para la lectura automatizada de normativas locales.
* **Fase 4 - Integración y Pruebas:** Conexión de las utilidades de lectura con la interfaz principal de la aplicación.
"""

with open(os.path.join(docs_dir, "resumen-fases.md"), "w", encoding="utf-8") as f:
    f.write(resumen_content)

# 4. especificacion.md
especificacion_content = """# Especificación Técnica del Sistema

## 1. Alcance del Sistema
La aplicación permite la administración, consulta y extracción de información contenida en normativas y documentos legales almacenados localmente, garantizando privacidad y autonomía frente a servicios en la nube.

## 2. Requerimientos Técnicos
* **Lenguaje:** Python 3.10 o superior.
* **Librerías Principales:** `pypdf` para el manejo de archivos PDF, Flask para la interfaz web.
* **Control de Versiones:** Git / GitHub.
"""

with open(os.path.join(docs_dir, "especificacion.md"), "w", encoding="utf-8") as f:
    f.write(especificacion_content)

print("Carpeta 'documentacion' y archivos creados exitosamente.")