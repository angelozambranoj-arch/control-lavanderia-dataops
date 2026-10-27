# Control de lavandería con DataOps

Proyecto académico del curso DataOps de Angelo Zambrano. Caso aplicado a la programación de lavandería de una empresa textil, tomando Topitop como contexto organizacional.

**Los datos son ficticios y no representan información interna de la empresa.**

## Problema
El intercambio de archivos de programación con varias versiones dificulta identificar la información vigente, rastrear cambios y recuperar una versión anterior.

## Solución
Versionar código, reglas de validación, datos demostrativos y documentación con Git y GitHub. Validar las órdenes antes de generar un tablero estático.

## Flujo de ramas
- `main`: versión estable.
- `develop`: integración de cambios.
- `feature/control-lavanderia`: desarrollo de la funcionalidad.

Los cambios se proponen mediante pull requests. El historial registra cada integración. Es un ejercicio individual de flujo de trabajo; no acredita revisión por otros integrantes.

## Ejecutar (Python 3.11 o superior)
```bash
python src/control_lavanderia.py --input datos/ordenes.csv --output docs/index.html
python -m http.server 8000 --directory docs
```
Abrir http://localhost:8000. No requiere instalar paquetes externos.

## Validación y publicación
GitHub Actions valida los datos y genera el tablero. La publicación en GitHub Pages requiere activar Pages en Settings > Pages > Source: GitHub Actions. Consultar `documentacion/guia.md`.

## Entregable
Problemática, beneficios, creación del repositorio y ramas, control de versiones, despliegue y conclusiones. El estado real de cada ejecución se consulta en Actions.
