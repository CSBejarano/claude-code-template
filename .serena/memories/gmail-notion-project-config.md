# Configuración del Proyecto Gmail→Notion (Producción)

## Usuario

- **Google Cloud Console**: Interfaz en español
- **Proyecto**: Gemini API (según screenshot)
- **Objetivo**: Automatización completa de Gmail con clasificación y sincronización a Notion

## Estado Actual

- **Fase**: 1.1 - Conectando Gmail con OAuth2
- **Paso**: Configurando OAuth Consent Screen
- **Screenshot**: Usuario en "Descripción general de OAuth"

## Scopes Necesarios para Gmail

1. `https://www.googleapis.com/auth/gmail.readonly` - Leer correos
2. `https://www.googleapis.com/auth/gmail.modify` - Modificar etiquetas
3. `https://www.googleapis.com/auth/gmail.labels` - Gestionar etiquetas

## Importante

- NO usar scopes de envío de correos (gmail.compose, gmail.send)
- Solo permisos de lectura y modificación de etiquetas
- Configuración para uso personal (External o Internal si es Google Workspace)

## Archon Task ID

- **Task ID**: 97f81b99-cc58-456a-a277-04365b27ea8e
- **Título**: Sistema Real de Gestión Gmail → Notion (Producción)

## Próximos Pasos

1. Completar configuración de OAuth consent screen
2. Crear credenciales OAuth 2.0
3. Descargar archivo JSON de credenciales
4. Configurar .env en el proyecto
