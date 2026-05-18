# Test-Jenkins
Este es un proyecto de ejemplo para demostrar cómo configurar un pipeline de Jenkins que integra análisis de código con SonarQube para una API REST escrita en Python.

## Agregar el webhook de Jenkins a GitHub
1. Ve a tu repositorio en GitHub.
2. Haz clic en "Settings" (Configuración).
3. En el menú lateral, selecciona "Webhooks".
4. Haz clic en "Add webhook" (Agregar webhook).
5. En el campo "Payload URL", ingresa la URL de tu servidor Jenkins seguida de `/github-webhook/`. Por ejemplo: `http://tu-servidor-jenkins/github-webhook/`.
6. En "Content type" (Tipo de contenido), selecciona `application/json`.
7. En "Which events would you like to trigger this webhook?" (¿Qué eventos te gustaría que desencadenen este webhook?), selecciona "Just the push event" (Solo el evento de push).
8. Haz clic en "Add webhook" (Agregar webhook) para guardar.