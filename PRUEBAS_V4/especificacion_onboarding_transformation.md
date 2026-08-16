# 📋 Especificación Técnica y Funcional: Transformación del Onboarding de Empleados (Pruebas V4)

**De Proceso Manual Fragmentado (3-7 Días) a Orquestación Automatizada con Gobernanza (< 4 Horas)**

---

## 🎯 1. Objetivos del Negocio & Problemática Actual

### Estado Actual (Legacy Manual):
* **Duración:** 3 a 7 días hábiles hasta que el empleado puede trabajar.
* **Fricciones Principales:**
  1. *Duplicación de información:* Empleado llena 5 formularios con datos repetidos.
  2. *Recepción fragmentada:* Envío de documentos escaneados por correo suelto.
  3. *Bloqueos de revisión:* Si un dato es ilegible, RRHH devuelve el correo y el proceso se congela.
  4. *Digitación manual en 5 sistemas:* RRHH carga manualmente el perfil en HRIS, Active Directory, Slack, ERP y Jira.
  5. *Falta de visibilidad:* Nadie sabe en qué estado está la incorporación.
  6. *Riesgos de Seguridad:* Accesos privilegiados otorgados por inercia o demorados 4 días por falta de canales dedicados.

### Estado Futuro Propuesto (Target < 4 Horas):
* **Duración:** Menos de 4 horas para incorporación total (y < 15 min para primer acceso a Email/Slack).
* **Gobernanza:** Automatización para cuentas estándar + Puertas de aprobación humana obligatorias (*Human-in-the-loop*) para accesos departamentales y privilegiados.

---

## 🏛️ 2. Arquitectura de la Solución y Descomposición en 4 Frames

Para representar con claridad todas las dimensiones del problema, Sketion ha generado una **composición multi-frame de 4 lienzos coordinados**:

```text
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        COMPOSICIÓN MULTI-FRAME DE ONBOARDING (PRUEBAS V4)                         │
├──────────────────────────┬──────────────────────────┬───────────────────────┬─────────────────────┤
│ FRAME 1: EL DUELO (VS)   │ FRAME 2: CADENA ACTORES  │ FRAME 3: GOBERNANZA   │ FRAME 4: DASHBOARD  │
│ • Antes (Gris/Dolor)     │ • 5 Swimlanes por actor  │ • Matriz de permisos  │ • 6 KPIs de éxito   │
│ • Espina de Stickies     │ • Handoffs de seguridad  │ • SLA y Fallback      │ • Target < 4 horas  │
│ • Después (Orquestado)   │ • Slots de evidencia     │ • Reglas CISO / JIT   │ • Checklist despl.  │
└──────────────────────────┴──────────────────────────┴───────────────────────┴─────────────────────┘
```

---

## 🔍 3. Detalle de los 4 Frames en `incorporacion_empleados_onboarding.excalidraw`

### Frame 1: Arquetipo D · El Duelo (Before vs After)
* **Lado Izquierdo (Legacy Manual):**
  - Envío de PDFs por correo suelto.
  - Revisión manual con idas y vueltas de email.
  - Digitación repetitiva en 5 sistemas aislados.
  - Cadenas de llamadas buscando la firma del gerente.
  - Empleados esperando 3 días con la pantalla bloqueada.
* **Espina Central (Post-its Amarillos `#FFE95C` a $1.5^\circ$):**
  - `[DOCUMENTACIÓN]`
  - `[VALIDACIÓN RRHH]`
  - `[PROVISIONING 5 SISTEMAS]`
  - `[APROBACIONES]`
  - `[SEGURIDAD & PRIVILEGIOS]`
  - `[PRIMER DÍA]`
* **Lado Derecho (Sistema Orquestado):**
  - Portal self-service con OCR y validación atómica en 60s.
  - Sincronización en paralelo vía Event Broker.
  - Aprobaciones 1-clic interactivas en Slack con SLA < 2h.
  - Primer día operativo al 100% desde las 9:00 AM.
* **Métricas Comparativas al Pie:**
  - *Tiempo Onboarding:* `3-7 días` $\rightarrow$ `3.8 h`
  - *Handoffs Manuales:* `8+` $\rightarrow$ `2`
  - *Tasa de Errores:* `18%` $\rightarrow$ `0.2%`

---

### Frame 2: Arquetipo E · La Cadena de Actores y Gobernanza (Swimlanes)
* **Carril 1: Empleado (Portal Self-Service):** Sube documentación digitalizada una sola vez.
* **Carril 2: Orquestador (Workflow Core Engine):** Ejecuta OCR, valida datos y provisiona cuentas base inmediatamente.
* **Carril 3: Gerente de Área (Aprobador 1-Clic):** Valida herramientas funcionales del equipo (Figma, GitHub, Jira).
* **Carril 4: CISO / Seguridad (Guardián de Privilegios):** Revisa accesos críticos (AWS Root, Base de Datos Producción) con MFA FIDO2 y acceso Just-in-Time (JIT 8h).
* **Carril 5: Sistemas Destino (5 Plataformas Core):** Sincronización SCIM/API síncrona en HRIS, IdP/SSO, Slack, ERP y Cloud.

---

### Frame 3: Matriz de Gobernanza y Políticas de Acceso
Tabla dinámica proporcional con 5 niveles de control:

| Categoría de Acceso | Sistemas Involucrados | Tipo de Aprobación | SLA Objetivo | Política de Seguridad y Auditoría |
| :--- | :--- | :--- | :--- | :--- |
| **Identidad Base** | Google Workspace, Slack, HRIS | 100% Automatizado | < 5 min | Asignación estándar por rol sin intervención humana. |
| **Productividad** | Figma, Notion, Jira, GitHub | Aprobación Gerente (1-Clic) | < 2 horas | Validación funcional; si no responde en 4h, escala a Director. |
| **Finanzas / ERP** | SAP, Stripe Dashboard, Facturación | Gerente + Finanzas (Doble) | < 3 horas | Requiere doble visto bueno; nunca se auto-aprueba. |
| **Privilegiados / Prod** | AWS Root, Bastion, BD Clientes | CISO / Seguridad (OBLIGATORIO) | < 4 horas | Estrictamente manual con Just-in-Time (TTL 8h) y registro SIEM. |
| **Offboarding Inmediato** | 5 Sistemas Conectados | Automático por Trigger | < 60 seg | Revocación global síncrona para evitar accesos huérfanos. |

---

### Frame 4: Dashboard de KPIs y Observabilidad del Onboarding
Panel de 6 métricas de alto impacto con chips editoriales:

1. **`3.8 h`** — *Tiempo Total de Onboarding* (Meta: < 4 h | Antes: 3-7 días).
2. **`45 min`** — *Tiempo Esperando Aprobación Gerencial* (Antes: 48 horas).
3. **`2`** — *Intervenciones Humanas Máximas* (Solo Gerente y CISO | Antes: 8+).
4. **`0.2%`** — *Tasa de Errores de Digitación* (Antes: 18%).
5. **`82%`** — *Porcentaje Total Automatizado*.
6. **`15 min`** — *Tiempo hasta Primer Acceso Básico* (Email y Slack activos).

Incluye además la caja de **Checklist de Despliegue del Sistema** con los 5 pasos de integración técnica.
