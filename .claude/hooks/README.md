# Hooks - Claude Code

Los **hooks** en Claude Code permiten ejecutar comandos shell automáticamente en respuesta a eventos específicos durante el desarrollo.

---

## 📚 **Tipos de Hooks Disponibles**

### **1. Pre-Tool-Use Hook**
Se ejecuta **antes** de que Claude use una herramienta.

**Ejemplo de uso:**
- Validar permisos antes de operaciones críticas
- Verificar estado del sistema
- Hacer backups automáticos

**Configuración en `settings.local.json`:**
```json
{
  "hooks": {
    "preToolUse": {
      "enabled": true,
      "command": "bash /path/to/pre-tool-use.sh"
    }
  }
}
```

---

### **2. User-Prompt-Submit Hook**
Se ejecuta cuando el usuario envía un mensaje.

**Ejemplo de uso:**
- Logging de interacciones
- Validaciones antes de procesar
- Actualizar contexto automáticamente

**Configuración:**
```json
{
  "hooks": {
    "userPromptSubmit": {
      "enabled": true,
      "command": "bash /path/to/prompt-submit.sh"
    }
  }
}
```

---

### **3. Post-Tool-Use Hook**
Se ejecuta **después** de que Claude usa una herramienta.

**Ejemplo de uso:**
- Ejecutar tests automáticamente después de cambios
- Actualizar documentación
- Commit automático de cambios

**Configuración:**
```json
{
  "hooks": {
    "postToolUse": {
      "enabled": true,
      "command": "bash /path/to/post-tool-use.sh"
    }
  }
}
```

---

## 🔧 **Configuración de Hooks**

### **Archivo de Configuración**
Los hooks se configuran en `.claude/settings.local.json`:

```json
{
  "hooks": {
    "preToolUse": {
      "enabled": true,
      "command": "bash .claude/hooks/pre-tool-use.sh",
      "blocking": true
    },
    "userPromptSubmit": {
      "enabled": true,
      "command": "bash .claude/hooks/prompt-submit.sh",
      "blocking": false
    },
    "postToolUse": {
      "enabled": true,
      "command": "bash .claude/hooks/post-tool-use.sh",
      "blocking": false
    }
  }
}
```

### **Parámetros:**
- `enabled`: Activa/desactiva el hook
- `command`: Comando shell a ejecutar
- `blocking`: Si `true`, bloquea la operación hasta completar

---

## 📝 **Ejemplos de Scripts**

### **Ejemplo: Pre-Tool-Use Validation**
```bash
#!/bin/bash
# .claude/hooks/pre-tool-use.sh

# Verificar que no hay cambios sin commit
if [[ -n $(git status -s) ]]; then
  echo "⚠️ Hay cambios sin commit"
  echo "Considera hacer commit antes de continuar"
fi

# Verificar tests
if ! npm test --silent; then
  echo "❌ Los tests están fallando"
  exit 1  # Bloquear operación
fi

exit 0  # Permitir operación
```

### **Ejemplo: Post-Tool-Use Auto-Format**
```bash
#!/bin/bash
# .claude/hooks/post-tool-use.sh

# Auto-format código modificado
if [[ "$TOOL_NAME" == "Edit" ]] || [[ "$TOOL_NAME" == "Write" ]]; then
  echo "🔧 Formateando código..."
  npm run format
fi

exit 0
```

### **Ejemplo: User-Prompt Logging**
```bash
#!/bin/bash
# .claude/hooks/prompt-submit.sh

# Log de interacciones
echo "[$(date)] User prompt submitted" >> .claude/interaction.log

exit 0
```

---

## ⚠️ **Best Practices**

### **1. Mantén los Hooks Rápidos**
- Evita operaciones lentas que bloqueen el flujo
- Usa `blocking: false` para hooks no críticos

### **2. Manejo de Errores**
```bash
#!/bin/bash
set -e  # Salir en error

# Tu lógica aquí

exit 0
```

### **3. Logging**
```bash
# Crear log file
LOG_FILE=".claude/hooks.log"
echo "[$(date)] Hook executed" >> $LOG_FILE
```

### **4. Testing**
Prueba tus hooks manualmente antes de activarlos:
```bash
bash .claude/hooks/pre-tool-use.sh
echo $?  # Verificar exit code
```

---

## 🎯 **Casos de Uso Comunes**

### **1. Auto-Test Before Critical Operations**
```json
{
  "preToolUse": {
    "enabled": true,
    "command": "npm test",
    "blocking": true
  }
}
```

### **2. Auto-Commit After Changes**
```json
{
  "postToolUse": {
    "enabled": true,
    "command": "git add -A && git commit -m 'Auto-commit by Claude'",
    "blocking": false
  }
}
```

### **3. Backup Before Destructive Operations**
```json
{
  "preToolUse": {
    "enabled": true,
    "command": ".claude/hooks/backup.sh",
    "blocking": true
  }
}
```

---

## 🚫 **Desactivar Hooks Temporalmente**

Para desactivar todos los hooks temporalmente:

```json
{
  "hooks": {
    "preToolUse": {
      "enabled": false
    },
    "postToolUse": {
      "enabled": false
    },
    "userPromptSubmit": {
      "enabled": false
    }
  }
}
```

O elimina el archivo `settings.local.json`.

---

## 📚 **Recursos Adicionales**

- [Documentación Oficial de Claude Code](https://docs.claude.com)
- [Ejemplos de Hooks](./examples/)

---

*Última actualización: [FECHA]*
