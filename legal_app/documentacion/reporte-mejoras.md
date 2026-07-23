# Reporte de Mejoras y Optimización

Este documento recopila las optimizaciones implementadas en la aplicación de gestión documental y legal para garantizar un rendimiento óptimo en entornos locales.

## 1. Mejoras de Rendimiento
* **Lectura Eficiente por Páginas:** Implementación de bucles optimizados con `pypdf` para evitar el consumo excesivo de memoria RAM al procesar documentos extensos.
* **Manejo de Excepciones:** Incorporación de bloques de control para evitar fallos críticos cuando un archivo PDF no se encuentra disponible en la ruta especificada.

## 2. Experiencia de Usuario (UX)
* **Retroalimentación Visual:** Mensajes claros en consola e interfaz sobre el estado de carga y extracción de los archivos legales.
