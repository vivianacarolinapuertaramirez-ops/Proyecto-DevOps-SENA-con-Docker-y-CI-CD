# Proyecto DevOps SENA - Docker y CI/CD

## Descripción
Proyecto formativo desarrollado para el programa **DevOps y Contenedores** del SENA. Se implementa una arquitectura de dos capas, empaquetada en contenedores, siguiendo buenas prácticas de automatización y despliegue continuo.

## Objetivos
- Aplicar principios de la cultura DevOps
- Crear y gestionar contenedores con Docker
- Implementar arquitectura multicontenedor con Docker Compose
- Automatizar pruebas y validaciones con GitHub Actions
- Gestionar versiones del código con Git y GitHub

## Tecnologías usadas
- Docker / Docker Compose
- Python 3 + Flask
- HTML5, CSS3 y JavaScript
- Servidor web Nginx
- Git / GitHub
- GitHub Actions

## Comandos para ejecutar el proyecto
```bash
# Construir y levantar todos los servicios
docker compose up --build

# Ver los contenedores activos
docker ps

# Detener y eliminar los contenedores
docker compose down