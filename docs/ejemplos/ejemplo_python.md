# Ejemplo: Proyecto Python con Claude Code

Esta guía muestra cómo configurar un proyecto Python para trabajar con Claude Code de manera óptima.

## 📁 Estructura Recomendada

```
mi-proyecto-python/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── business_logic.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   │   ├── test_services.py
│   │   └── test_utils.py
│   └── integration/
│       └── test_api.py
│
├── .claude/
│   ├── agents/
│   ├── commands/
│   ├── hooks/
│   ├── PLANNING.md
│   ├── TASK.md
│   └── settings.local.json
│
├── docs/
│   └── api/
│
├── pyproject.toml
├── uv.lock                # Si usas UV
├── .env.example
├── .gitignore
├── README.md
├── CLAUDE.md
└── QUICK_START.md
```

## 🔧 Gestores de Dependencias

### Opción 1: UV (Recomendado - Más rápido)

**Instalación**:
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**pyproject.toml**:
```toml
[project]
name = "mi-proyecto"
version = "0.1.0"
description = "Descripción del proyecto"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.104.1",
    "uvicorn[standard]>=0.24.0",
    "pydantic>=2.5.0",
    "pydantic-settings>=2.1.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.3",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.21.1",
    "ruff>=0.1.6",
    "mypy>=1.7.0",
]

[tool.uv]
dev-dependencies = [
    "pytest>=7.4.3",
    "ruff>=0.1.6",
    "mypy>=1.7.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

**Comandos UV**:
```bash
# Crear proyecto nuevo
uv init

# Instalar dependencias
uv sync

# Agregar dependencia
uv add fastapi

# Agregar dependencia de desarrollo
uv add --dev pytest

# Ejecutar script
uv run python src/main.py

# Ejecutar con venv activado
uv run pytest
```

### Opción 2: Poetry

**pyproject.toml**:
```toml
[tool.poetry]
name = "mi-proyecto"
version = "0.1.0"
description = ""
authors = ["Tu Nombre <email@example.com>"]

[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.104.1"
pydantic = "^2.5.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.3"
ruff = "^0.1.6"
mypy = "^1.7.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

**Comandos Poetry**:
```bash
poetry install
poetry add fastapi
poetry add --group dev pytest
poetry run python src/main.py
```

### Opción 3: pip + requirements.txt

**requirements.txt**:
```
fastapi>=0.104.1
uvicorn[standard]>=0.24.0
pydantic>=2.5.0
```

**requirements-dev.txt**:
```
-r requirements.txt
pytest>=7.4.3
ruff>=0.1.6
mypy>=1.7.0
```

**Comandos pip**:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# o
venv\Scripts\activate  # Windows

pip install -r requirements-dev.txt
```

## ✅ Testing con pytest

**pyproject.toml - Configuración pytest**:
```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--verbose",
    "--cov=src",
    "--cov-report=term-missing",
    "--cov-report=html",
]
asyncio_mode = "auto"
```

**tests/conftest.py**:
```python
"""Configuración global de pytest."""
import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    """Cliente de pruebas FastAPI."""
    from src.main import app
    return TestClient(app)

@pytest.fixture
def sample_data():
    """Datos de ejemplo para tests."""
    return {
        "id": 1,
        "name": "Test Item",
        "description": "Test description"
    }
```

**tests/unit/test_services.py**:
```python
"""Tests unitarios de servicios."""
import pytest
from src.services.business_logic import process_data

def test_process_data():
    """Test de procesamiento de datos."""
    result = process_data({"input": "test"})
    assert result["status"] == "success"

@pytest.mark.asyncio
async def test_async_operation():
    """Test de operación asíncrona."""
    result = await some_async_function()
    assert result is not None
```

**Comandos**:
```bash
# Ejecutar todos los tests
uv run pytest
# o
pytest

# Con cobertura
pytest --cov=src --cov-report=html

# Tests específicos
pytest tests/unit/test_services.py

# Con output detallado
pytest -v -s

# Solo tests marcados
pytest -m "not slow"
```

## 🎨 Linting con Ruff

**pyproject.toml - Configuración Ruff**:
```toml
[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
    "UP",  # pyupgrade
]
ignore = [
    "E501",  # line too long (handled by formatter)
]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

**Comandos**:
```bash
# Lint
ruff check src/

# Auto-fix
ruff check --fix src/

# Format
ruff format src/

# Check + format
ruff check --fix src/ && ruff format src/
```

## 🔍 Type Checking con mypy

**pyproject.toml - Configuración mypy**:
```toml
[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
no_implicit_optional = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false
```

**Ejemplo de código con tipos**:
```python
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    """Modelo de usuario."""
    id: int
    name: str
    email: str
    age: Optional[int] = None

def get_user(user_id: int) -> Optional[User]:
    """Obtiene un usuario por ID."""
    # Implementación
    return User(id=user_id, name="John", email="john@example.com")
```

**Comandos**:
```bash
# Type check
mypy src/

# Con más detalles
mypy --show-error-codes src/
```

## 📝 Ejemplo CLAUDE.md para Python

```markdown
# Mi Proyecto Python

## 🎯 Misión del Proyecto

[Descripción del objetivo del proyecto]

## 🏗️ Arquitectura

**Stack Tecnológico**:
- **Lenguaje**: Python 3.12
- **Framework**: FastAPI
- **Base de Datos**: PostgreSQL + SQLAlchemy
- **Testing**: pytest + pytest-cov
- **Linting**: Ruff
- **Type Checking**: mypy
- **Package Manager**: UV

**Estructura**:
- `src/api/`: Endpoints REST
- `src/services/`: Lógica de negocio
- `src/models/`: Modelos Pydantic
- `src/utils/`: Utilidades

## 🔧 Comandos de Desarrollo

```bash
# Setup inicial
uv sync

# Desarrollo
uv run uvicorn src.main:app --reload

# Testing
uv run pytest

# Linting
ruff check --fix src/
ruff format src/

# Type checking
mypy src/

# Build
uv build
```

## 📚 Convenciones de Código

### Naming
- **Funciones**: `snake_case`
- **Clases**: `PascalCase`
- **Constantes**: `UPPER_SNAKE_CASE`
- **Archivos**: `snake_case.py`

### Imports
```python
# Standard library
import os
import sys

# Third-party
from fastapi import FastAPI
from pydantic import BaseModel

# Local
from src.models.user import User
```

### Docstrings
```python
def function_name(param1: str, param2: int) -> bool:
    """
    Resumen en una línea.

    Descripción más detallada si es necesario.

    Args:
        param1: Descripción del parámetro
        param2: Descripción del parámetro

    Returns:
        Descripción del valor de retorno

    Raises:
        ValueError: Cuando param2 es negativo
    """
    pass
```

## 🧪 Testing

- **Cobertura mínima**: 80%
- **Tests unitarios**: `tests/unit/`
- **Tests de integración**: `tests/integration/`
- **Fixtures**: `tests/conftest.py`

## 🚀 Deployment

[Instrucciones de deployment específicas]

## 📖 Referencias

- [Documentación FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [UV Docs](https://docs.astral.sh/uv/)
```

## 🚀 Comandos Comunes Claude Code

```bash
# Inicializar proyecto Python
/init-project

# Crear PRP para nueva feature
/prp-create nombre-feature

# Ejecutar PRP
/prp-execute PRPs/nombre-feature.md

# Crear story PRP
/story-create "Como usuario quiero..."

# Continuar reestructuración
/continue-restructure
```

## 🔒 .gitignore para Python

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/
.venv

# UV
.uv/
uv.lock

# Poetry
poetry.lock

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# Type checking
.mypy_cache/
.pytype/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# Environment
.env
.env.local
.env.*.local

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/
```

## 📦 Scripts Útiles

**pyproject.toml**:
```toml
[tool.uv.scripts]
dev = "uvicorn src.main:app --reload"
test = "pytest"
test-cov = "pytest --cov=src --cov-report=html"
lint = "ruff check src/"
lint-fix = "ruff check --fix src/ && ruff format src/"
typecheck = "mypy src/"
check-all = "ruff check --fix src/ && mypy src/ && pytest"
```

**Uso**:
```bash
uv run dev
uv run test
uv run lint-fix
uv run check-all
```

## 🎓 Mejores Prácticas

### 1. Siempre usar tipos
```python
# ✅ Correcto
def get_user(user_id: int) -> Optional[User]:
    pass

# ❌ Incorrecto
def get_user(user_id):
    pass
```

### 2. Usar Pydantic para validación
```python
from pydantic import BaseModel, validator

class UserCreate(BaseModel):
    email: str
    password: str
    age: int

    @validator('age')
    def age_must_be_positive(cls, v):
        if v < 0:
            raise ValueError('age must be positive')
        return v
```

### 3. Tests asincrónicos
```python
@pytest.mark.asyncio
async def test_async_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/users/1")
    assert response.status_code == 200
```

### 4. Configuración con pydantic-settings
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My App"
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()
```

---

**Este template Python está optimizado para trabajar con Claude Code y seguir las mejores prácticas de la comunidad Python.**
