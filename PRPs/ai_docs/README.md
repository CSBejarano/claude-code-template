# AI Docs - Documentación Curada de Librerías

Esta carpeta almacena documentación curada de librerías externas para que Claude Code pueda acceder rápidamente sin necesidad de buscar en internet.

---

## 📚 **¿Qué va aquí?**

Guarda aquí documentación relevante de:
- Librerías y frameworks que uses frecuentemente
- APIs externas que integres
- Patrones de código específicos
- Best practices de tecnologías clave

---

## 📝 **Formato Recomendado**

Crea archivos `.md` con el siguiente formato:

```markdown
# [Nombre de la Librería]

## Instalación
[comandos de instalación]

## Uso Básico
[ejemplos de código]

## Patrones Comunes
[patrones que uses en tu proyecto]

## Gotchas y Problemas Comunes
[problemas conocidos y soluciones]

## Referencias
- [Link a documentación oficial]
- [Link a tutoriales útiles]
```

---

## 🔍 **Cómo lo usa Claude Code**

Cuando uses el agente `@library-researcher`, puede guardar automáticamente documentación aquí para futura referencia:

```bash
"@library-researcher busca documentación de FastAPI y guárdala"
```

Claude buscará, analizará y guardará la información más relevante en un archivo como:
- `fastapi_guide.md`
- `redis_patterns.md`
- `openai_api_reference.md`

---

## 📋 **Estructura Sugerida**

```
ai_docs/
├── README.md                    # Este archivo
├── [framework]_guide.md         # Guía del framework principal
├── [api]_integration.md         # Integración de API externa
├── [pattern]_examples.md        # Ejemplos de patrones
└── troubleshooting/             # Solución de problemas
    ├── [tech]_common_errors.md
    └── performance_tips.md
```

---

## ✨ **Ejemplos de Documentación Útil**

### **Para un proyecto web:**
- `fastapi_async_patterns.md`
- `pydantic_validation.md`
- `sqlalchemy_relationships.md`
- `redis_caching_strategies.md`

### **Para un proyecto de IA:**
- `openai_api_reference.md`
- `langchain_chains.md`
- `vector_db_best_practices.md`

### **Para cualquier proyecto:**
- `git_workflows.md`
- `docker_compose_patterns.md`
- `testing_strategies.md`

---

## 🎯 **Best Practices**

1. **Mantén la documentación actualizada**
   - Revisa periódicamente si hay versiones nuevas
   - Actualiza ejemplos cuando cambien APIs

2. **Incluye ejemplos de código real**
   - No solo teoría, sino ejemplos que funcionen
   - Usa snippets de tu proyecto cuando sea posible

3. **Documenta gotchas específicos**
   - Problemas que te encontraste y cómo los resolviste
   - Warnings y limitaciones conocidas

4. **Organiza por frecuencia de uso**
   - Las librerías que uses más deben estar más detalladas
   - Librerías ocasionales pueden tener menos detalle

---

## 🔄 **Workflow Recomendado**

1. **Necesitas usar una nueva librería:**
   ```bash
   "@library-researcher busca mejores prácticas de [librería]"
   ```

2. **Claude investiga y resume la documentación**

3. **Guarda el resumen aquí:**
   ```bash
   "Guarda esta información en PRPs/ai_docs/[libreria]_guide.md"
   ```

4. **Actualiza según aprendes:**
   - Añade notas de tu experiencia
   - Documenta problemas que encontraste
   - Agrega ejemplos del proyecto

---

## 📊 **Beneficios**

- ⚡ **Más rápido**: Claude no necesita buscar en internet cada vez
- 🎯 **Más preciso**: Documentación específica para tu proyecto
- 📚 **Acumulativo**: El conocimiento se queda en el proyecto
- 🔄 **Reutilizable**: Otros desarrolladores se benefician

---

*Empieza guardando documentación de tus 3 librerías más usadas*
