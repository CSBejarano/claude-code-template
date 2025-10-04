# Ejemplo: Proyecto Node.js con Claude Code

Esta guía muestra cómo configurar un proyecto Node.js/TypeScript para trabajar con Claude Code de manera óptima.

## 📁 Estructura Recomendada

```
mi-proyecto-nodejs/
├── src/
│   ├── index.ts
│   ├── app.ts
│   ├── api/
│   │   ├── routes/
│   │   │   ├── users.ts
│   │   │   └── index.ts
│   │   └── middleware/
│   │       ├── auth.ts
│   │       └── errorHandler.ts
│   ├── services/
│   │   ├── userService.ts
│   │   └── emailService.ts
│   ├── models/
│   │   ├── User.ts
│   │   └── types.ts
│   ├── utils/
│   │   ├── logger.ts
│   │   └── validators.ts
│   └── config/
│       ├── database.ts
│       └── env.ts
│
├── tests/
│   ├── unit/
│   │   ├── services/
│   │   └── utils/
│   ├── integration/
│   │   └── api/
│   └── setup.ts
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
├── package.json
├── tsconfig.json
├── .env.example
├── .gitignore
├── README.md
├── CLAUDE.md
└── QUICK_START.md
```

## 🔧 Gestores de Paquetes

### Opción 1: pnpm (Recomendado - Más rápido, eficiente)

**Instalación**:
```bash
npm install -g pnpm
```

**package.json**:
```json
{
  "name": "mi-proyecto-nodejs",
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "build": "tsc",
    "start": "node dist/index.js",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:cov": "jest --coverage",
    "lint": "eslint src/**/*.ts",
    "lint:fix": "eslint src/**/*.ts --fix",
    "typecheck": "tsc --noEmit",
    "format": "prettier --write \"src/**/*.ts\"",
    "check-all": "pnpm lint:fix && pnpm typecheck && pnpm test"
  },
  "dependencies": {
    "express": "^4.18.2",
    "zod": "^3.22.4",
    "dotenv": "^16.3.1"
  },
  "devDependencies": {
    "@types/express": "^4.17.21",
    "@types/node": "^20.10.0",
    "@types/jest": "^29.5.10",
    "typescript": "^5.3.2",
    "tsx": "^4.6.2",
    "jest": "^29.7.0",
    "ts-jest": "^29.1.1",
    "eslint": "^8.55.0",
    "@typescript-eslint/parser": "^6.13.2",
    "@typescript-eslint/eslint-plugin": "^6.13.2",
    "prettier": "^3.1.0"
  }
}
```

**Comandos pnpm**:
```bash
# Instalar dependencias
pnpm install

# Agregar dependencia
pnpm add express

# Agregar dependencia de desarrollo
pnpm add -D typescript

# Ejecutar scripts
pnpm dev
pnpm test
pnpm build
```

### Opción 2: npm

**Comandos npm**:
```bash
npm install
npm install express
npm install -D typescript
npm run dev
```

### Opción 3: yarn

**Comandos yarn**:
```bash
yarn install
yarn add express
yarn add -D typescript
yarn dev
```

## 📘 TypeScript Configuration

**tsconfig.json**:
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "lib": ["ES2022"],
    "moduleResolution": "node",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "allowSyntheticDefaultImports": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "tests"]
}
```

**tsconfig.test.json** (para tests):
```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "types": ["jest", "node"]
  },
  "include": ["src/**/*", "tests/**/*"]
}
```

## ✅ Testing con Jest

**jest.config.js**:
```javascript
export default {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/tests'],
  testMatch: ['**/*.test.ts'],
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
    '!src/index.ts'
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  },
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1'
  }
};
```

**tests/setup.ts**:
```typescript
// Setup global para tests
beforeAll(() => {
  // Configuración global
});

afterAll(() => {
  // Limpieza global
});
```

**tests/unit/services/userService.test.ts**:
```typescript
import { UserService } from '@/services/userService';

describe('UserService', () => {
  let userService: UserService;

  beforeEach(() => {
    userService = new UserService();
  });

  describe('getUser', () => {
    it('should return user by id', async () => {
      const user = await userService.getUser(1);
      expect(user).toBeDefined();
      expect(user.id).toBe(1);
    });

    it('should throw error for invalid id', async () => {
      await expect(userService.getUser(-1))
        .rejects
        .toThrow('Invalid user ID');
    });
  });
});
```

**Comandos**:
```bash
# Ejecutar tests
pnpm test

# Con watch mode
pnpm test:watch

# Con cobertura
pnpm test:cov

# Test específico
pnpm test userService.test.ts
```

## 🎨 Linting con ESLint

**.eslintrc.json**:
```json
{
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": 2022,
    "sourceType": "module",
    "project": "./tsconfig.json"
  },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:@typescript-eslint/recommended-requiring-type-checking"
  ],
  "plugins": ["@typescript-eslint"],
  "rules": {
    "@typescript-eslint/no-unused-vars": ["error", {
      "argsIgnorePattern": "^_"
    }],
    "@typescript-eslint/explicit-function-return-type": "warn",
    "@typescript-eslint/no-explicit-any": "error",
    "no-console": ["warn", { "allow": ["warn", "error"] }]
  },
  "ignorePatterns": ["dist/", "node_modules/", "*.js"]
}
```

**Comandos**:
```bash
# Lint
pnpm lint

# Auto-fix
pnpm lint:fix
```

## 💅 Formatting con Prettier

**.prettierrc.json**:
```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 100,
  "tabWidth": 2,
  "arrowParens": "always"
}
```

**.prettierignore**:
```
node_modules
dist
coverage
*.md
```

**Comandos**:
```bash
pnpm format
```

## 🔍 Validación con Zod

```typescript
import { z } from 'zod';

// Schema de validación
export const UserSchema = z.object({
  id: z.number().int().positive(),
  email: z.string().email(),
  name: z.string().min(2).max(100),
  age: z.number().int().min(0).optional(),
});

export type User = z.infer<typeof UserSchema>;

// Uso en API
import { Request, Response } from 'express';

export const createUser = async (req: Request, res: Response): Promise<void> => {
  try {
    const userData = UserSchema.parse(req.body);
    // userData es tipo-safe ahora
    const user = await userService.create(userData);
    res.status(201).json(user);
  } catch (error) {
    if (error instanceof z.ZodError) {
      res.status(400).json({ errors: error.errors });
      return;
    }
    res.status(500).json({ error: 'Internal server error' });
  }
};
```

## 📝 Ejemplo CLAUDE.md para Node.js

```markdown
# Mi Proyecto Node.js

## 🎯 Misión del Proyecto

[Descripción del objetivo del proyecto]

## 🏗️ Arquitectura

**Stack Tecnológico**:
- **Runtime**: Node.js 20+
- **Lenguaje**: TypeScript 5.3
- **Framework**: Express.js
- **Base de Datos**: PostgreSQL + Prisma
- **Validación**: Zod
- **Testing**: Jest + ts-jest
- **Linting**: ESLint + Prettier
- **Package Manager**: pnpm

**Estructura**:
- `src/api/`: Endpoints y middleware
- `src/services/`: Lógica de negocio
- `src/models/`: Tipos y schemas
- `src/utils/`: Utilidades

## 🔧 Comandos de Desarrollo

```bash
# Setup inicial
pnpm install

# Desarrollo (con hot-reload)
pnpm dev

# Testing
pnpm test
pnpm test:watch
pnpm test:cov

# Linting
pnpm lint:fix

# Type checking
pnpm typecheck

# Build
pnpm build

# Producción
pnpm start

# Check completo
pnpm check-all
```

## 📚 Convenciones de Código

### Naming
- **Variables/Funciones**: `camelCase`
- **Clases/Interfaces/Types**: `PascalCase`
- **Constantes**: `UPPER_SNAKE_CASE`
- **Archivos**: `camelCase.ts`
- **Componentes**: `PascalCase.ts`

### Imports
```typescript
// Node built-ins
import fs from 'fs';
import path from 'path';

// Third-party
import express from 'express';
import { z } from 'zod';

// Local - usar alias @/
import { UserService } from '@/services/userService';
import type { User } from '@/models/types';
```

### Types vs Interfaces
```typescript
// ✅ Usar type para unions, intersections, primitives
type Status = 'active' | 'inactive';
type UserWithRole = User & { role: Role };

// ✅ Usar interface para objetos que pueden extenderse
interface User {
  id: number;
  name: string;
}

interface AdminUser extends User {
  permissions: string[];
}
```

### Async/Await
```typescript
// ✅ Correcto
async function fetchUser(id: number): Promise<User> {
  try {
    const user = await db.user.findUnique({ where: { id } });
    if (!user) throw new Error('User not found');
    return user;
  } catch (error) {
    logger.error('Failed to fetch user', { id, error });
    throw error;
  }
}

// ❌ Incorrecto - no manejar errores
async function fetchUser(id: number): Promise<User> {
  return await db.user.findUnique({ where: { id } });
}
```

## 🧪 Testing

- **Cobertura mínima**: 80%
- **Tests unitarios**: `tests/unit/`
- **Tests de integración**: `tests/integration/`
- **Setup**: `tests/setup.ts`

## 🚀 Deployment

[Instrucciones de deployment específicas]

## 📖 Referencias

- [Node.js Docs](https://nodejs.org/docs/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Express.js Guide](https://expressjs.com/en/guide/routing.html)
```

## 🚀 Comandos Comunes Claude Code

```bash
# Inicializar proyecto Node.js
/init-project

# Crear PRP para nueva feature
/prp-create nombre-feature

# Ejecutar PRP
/prp-execute PRPs/nombre-feature.md
```

## 🔒 .gitignore para Node.js

```gitignore
# Node
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*
pnpm-debug.log*
lerna-debug.log*

# Build output
dist/
build/
*.tsbuildinfo

# Testing
coverage/
.nyc_output/

# Environment
.env
.env.local
.env.*.local

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
logs/
*.log
```

## 📦 Express.js Setup Ejemplo

**src/app.ts**:
```typescript
import express, { Express } from 'express';
import { errorHandler } from './api/middleware/errorHandler';
import routes from './api/routes';

export const createApp = (): Express => {
  const app = express();

  // Middleware
  app.use(express.json());
  app.use(express.urlencoded({ extended: true }));

  // Routes
  app.use('/api', routes);

  // Error handling
  app.use(errorHandler);

  return app;
};
```

**src/index.ts**:
```typescript
import { createApp } from './app';
import { config } from './config/env';

const app = createApp();

app.listen(config.port, () => {
  console.log(`Server running on port ${config.port}`);
});
```

## 🎓 Mejores Prácticas

### 1. Siempre tipar todo
```typescript
// ✅ Correcto
function getUser(id: number): Promise<User> {
  return db.user.findUnique({ where: { id } });
}

// ❌ Incorrecto
function getUser(id) {
  return db.user.findUnique({ where: { id } });
}
```

### 2. Usar validación con Zod
```typescript
import { z } from 'zod';

const UserCreateSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
  age: z.number().int().min(18),
});

type UserCreate = z.infer<typeof UserCreateSchema>;
```

### 3. Error handling consistente
```typescript
class AppError extends Error {
  constructor(
    public statusCode: number,
    message: string,
    public isOperational = true
  ) {
    super(message);
    Object.setPrototypeOf(this, AppError.prototype);
  }
}

// Uso
throw new AppError(404, 'User not found');
```

### 4. Dependency injection
```typescript
export class UserService {
  constructor(
    private db: DatabaseClient,
    private logger: Logger
  ) {}

  async getUser(id: number): Promise<User> {
    this.logger.info('Fetching user', { id });
    return this.db.user.findUnique({ where: { id } });
  }
}
```

### 5. Environment variables con validación
```typescript
import { z } from 'zod';

const envSchema = z.object({
  NODE_ENV: z.enum(['development', 'production', 'test']),
  PORT: z.string().transform(Number),
  DATABASE_URL: z.string().url(),
});

export const config = envSchema.parse(process.env);
```

---

**Este template Node.js/TypeScript está optimizado para trabajar con Claude Code y seguir las mejores prácticas de la comunidad JavaScript/TypeScript.**
