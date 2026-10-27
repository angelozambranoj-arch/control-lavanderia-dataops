# Guía del proyecto

## Caso y alcance
Se toma Topitop como contexto de una organización actual. La dificultad planteada es un escenario académico: múltiples versiones de la programación de lavandería, cambios sin trazabilidad y recuperación manual de archivos. No se afirma haber auditado los sistemas de la empresa. Todas las OP y cantidades del CSV son ficticias.

## Beneficios de Git y GitHub
Git conserva el historial y permite comparar y restaurar cambios. GitHub centraliza el repositorio, muestra pull requests y ejecuta validaciones. Las ramas separan trabajo en desarrollo de la versión estable. Estas herramientas reducen errores de versiones; no garantizan el cumplimiento de producción ni reemplazan un ERP.

## Estructura
- datos/ordenes.csv: cinco órdenes de ejemplo.
- src/control_lavanderia.py: validación y generación del tablero.
- docs/index.html: tablero generado.
- .github/workflows/validacion.yml: validación automática.
- .github/workflows/publicar.yml: publicación en GitHub Pages.

## Reglas
Columnas exactas: op,planta,cantidad,estado. Una fila por OP, identificador único, planta 1323/1170/Chincha, cantidad entera positiva y estado Pendiente/En proceso/Terminado. El modelo académico no contempla dividir una OP entre plantas.

## Ramas e integración
main conserva la versión estable; develop integra cambios; feature/control-lavanderia contiene la funcionalidad. Se propone feature hacia develop y luego develop hacia main mediante pull requests. Es un ejercicio individual y no implica revisión independiente por compañeros.

## Despliegue local
Con Python 3.11 o superior, ejecutar desde la raíz:
```
python src/control_lavanderia.py
python -m http.server 8000 --directory docs
```
Abrir http://localhost:8000. Detener con Ctrl+C.

## Despliegue público
1. Abrir Settings > Pages en el repositorio.
2. En Build and deployment, seleccionar Source: GitHub Actions.
3. Abrir Actions > Publicar tablero en Pages > Run workflow sobre main.
4. Esperar que finalice correctamente y abrir la URL indicada en el entorno github-pages.

La existencia del workflow no demuestra que la publicación haya ocurrido. Verificar la ejecución y la URL antes de declarar el sitio publicado.

## Control de versiones y recuperación
Antes de integrar, revisar los cambios y la validación en Actions. Para recuperar una versión sin eliminar el historial, usar git revert sobre el commit elegido y proponer el cambio mediante una rama y pull request. No usar force push en main. Conservar datos reales fuera del repositorio público.

## Evidencias para la entrega
Capturar el repositorio con sus archivos, el selector de ramas, los pull requests, el historial de commits, la validación en Actions y el tablero publicado. Usar capturas reales del estado observado. Si Pages no está activado, registrar el despliegue público como pendiente.

## Conclusiones y recomendaciones
El prototipo conecta datos versionados con validación y un tablero reproducible. La estrategia de ramas hace visible qué se desarrolla y qué se integra. Se recomienda revisión por otro integrante, protección de main y validaciones adicionales de fechas, capacidad y prioridad antes de una aplicación real. La protección de ramas y la revisión independiente son recomendaciones, no configuraciones acreditadas por este ejercicio.
