---
name: "Story PRP Template - Enfoque en Implementación de Tareas"
description: "Template para convertir historias de usuario en tareas ejecutables de implementación"
---

## Historia Original

Pega a continuación la historia original compartida por el usuario:

```
[Descripción de historia de usuario/tarea desde Jira/Linear/etc]
```

## Metadata de la Historia

**Tipo de Historia**: [Feature/Bug/Enhancement/Refactor]
**Complejidad Estimada**: [Baja/Media/Alta]
**Sistemas Principales Afectados**: [Lista de componentes/servicios principales]

---

## REFERENCIAS DE CONTEXTO

[Documentación y patrones auto-descubiertos]

- {file_path} - {Por qué este patrón/archivo es relevante}
- {doc_path} - {Secciones específicas necesarias para implementación}
- {external_url} - {Documentación de librerías o ejemplos}

---

## TAREAS DE IMPLEMENTACIÓN

[Bloques de tareas en orden de dependencia - cada bloque es atómico y testeable]

### Guías para las Tareas

- Usamos palabras clave densas en información para ser específicos y concisos sobre los pasos y detalles de implementación.
- Las tareas deben ser detalladas y específicas para asegurar claridad y precisión.
- El desarrollador que ejecute las tareas debe poder completarlas usando solo el contexto de este archivo, con referencias a rutas relevantes del codebase y puntos de integración.

### {ACTION} {archivo_destino}:

- {VERB/KEYWORD}: {Detalle específico de implementación}
- {PATTERN}: {Patrón existente a seguir del codebase}
- {IMPORTS}: {Imports requeridos o dependencias}
- {GOTCHA}: {Problemas conocidos o restricciones a evitar}
- **VALIDATE**: `{comando de validación ejecutable}`

### Formato de Ejemplo:

### CREATE services/user_service.py:

- IMPLEMENT: Clase UserService con operaciones CRUD asíncronas
- PATTERN: Seguir estructura de services/product_service.py
- IMPORTS: from models.user import User; from db import get_session
- GOTCHA: Siempre usar context manager de sesión async
- **VALIDATE**: `python -c "from services.user_service import UserService; print('✓ Import exitoso')"`

### UPDATE api/routes.py:

- ADD: user_router al router principal
- FIND: `app.include_router(product_router)`
- INSERT: `app.include_router(user_router, prefix="/users", tags=["users"])`
- **VALIDATE**: `grep -q "user_router" api/routes.py && echo "✓ Router agregado"`

### ADD tests/user_service_test.py:

- CREATE: Casos de prueba para clase UserService
- PATTERN: Seguir estructura de tests/product_service_test.py
- IMPORTS: from services.user_service import UserService; from models.user import User
- GOTCHA: Usar fixtures de test async
- **VALIDATE**: `pytest tests/user_service_test.py && echo "✓ Tests pasados"`

---

## Loop de Validación

### Nivel 1: Sintaxis y Estilo (Feedback Inmediato)

```bash
# Linting y formateo de todo el proyecto
# Adapta estos comandos a las herramientas de tu proyecto

# Ejemplo Python:
ruff check src/ --fix
mypy src/
ruff format src/

# Ejemplo JavaScript/TypeScript:
npm run lint
npm run typecheck
npm run format

# Esperado: Cero errores. Si existen errores, LEE el output y corrige antes de continuar.
```

### Nivel 2: Tests Unitarios (Validación de Componentes)

```bash
# Ejecutar tests para componentes afectados
# Adapta a tu framework de testing

# Ejemplo Python:
pytest tests/test_user_service.py -v
pytest tests/ -v --cov=src

# Ejemplo JavaScript:
npm test -- user.service.test.ts
npm run test:coverage

# Esperado: Todos los tests pasan. Si fallan, debuggea la causa raíz y corrige implementación.
```

### Nivel 3: Testing de Integración (Validación del Sistema)

```bash
# Startup del servicio y validación de integración
# Adapta a la arquitectura de tu proyecto

# Iniciar servicio
npm start &  # o: python main.py &
sleep 3

# Health check
curl -f http://localhost:3000/health || echo "Health check falló"

# Testing de endpoint específico del feature
curl -X POST http://localhost:3000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "test"}' \
  | jq .

# Validación de base de datos (si aplica)
psql $DATABASE_URL -c "SELECT 1;" || echo "Conexión a base de datos falló"

# Esperado: Todas las integraciones funcionando, respuestas correctas, sin errores de conexión
```

### Nivel 4: Validación Creativa y Específica del Dominio

Usa herramientas CLI disponibles o servidores MCP para extender la validación.

```bash
# Ejemplos de validaciones basadas en herramientas disponibles:

# Testing de interfaz web (Playwright)
npm run test:e2e

# Testing de contenedores (Docker)
docker-compose up --build
docker-compose exec app npm test

# Testing de API (curl/httpie)
http POST localhost:3000/api/users name=test

# Migraciones de base de datos (si aplica)
npm run migrate:up
npm run migrate:down
```

---

## CHECKLIST DE COMPLETITUD

- [ ] Todas las tareas completadas
- [ ] Validación de cada tarea pasó
- [ ] Suite completa de tests pasa
- [ ] Sin errores de linting
- [ ] Todas las gates de validación disponibles pasaron
- [ ] Criterios de aceptación de la historia cumplidos

---

## Notas

[Cualquier contexto adicional, decisiones tomadas, o items de seguimiento]

<!-- EOF -->
