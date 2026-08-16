# 🏛️ Especificación Técnica y Funcional: Sistema de Reserva de Espacios Universitarios

**Gestión Concurrente de Aulas, Salas de Estudio y Auditorios con Jerarquía de Bloqueos, Notificaciones y Analítica de Ocupación.**

---

## 🎯 1. Arquitectura y Estrategia de Separación de Información

Para representar el sistema de forma integral sin sobrecargar al observador, Sketion ha estructurado la solución en **4 marcos (*Frames*) funcionales independientes y complementarios**:

```text
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│                      SISTEMA DE RESERVA DE ESPACIOS UNIVERSITARIOS (PRUEBAS V4)                    │
├──────────────────────────┬──────────────────────────┬───────────────────────┬─────────────────────┤
│ FRAME 1: ARQUITECTURA    │ FRAME 2: CICLO DE VIDA   │ FRAME 3: POLÍTICAS    │ FRAME 4: DASHBOARD  │
│ • 5 Roles de Usuario     │ • 6 Estados Principales  │ • Matriz de Horarios  │ • Analítica Campus  │
│ • Time-Slot Policy Engine│ • 5 Ramas de Excepción   │ • Reglas por Rol      │ • Utilización 88.4% │
│ • Eventos & Kafka        │ • Preemption Jerárquico  │ • Protocolo Averías   │ • Subutilización    │
└──────────────────────────┴──────────────────────────┴───────────────────────┴─────────────────────┘
```

---

## 🔍 2. Detalle de los 4 Frames en `sistema_reserva_espacios_universidad.excalidraw`

### [Frame 1] Arquitectura Distribuida y Control RBAC por Roles
Estructurado en 6 columnas de infraestructura con separación de 65px:
1. **Actores & Roles (RBAC):**
   - 🎓 *Estudiantes:* Salas de estudio grupal e individual.
   - 👨‍🏫 *Profesores:* Aulas magistrales y laboratorios.
   - 🏛️ *Coordinadores:* Bloqueos institucionales y exámenes.
   - 🔧 *Mantenimiento:* Bloqueos técnicos por avería.
   - 🛡️ *Seguridad:* Restricciones de aforo y emergencias.
2. **Gateway & Auth:** API Gateway con SSO universitario (OAuth2/SAML) y *Time-Slot Policy Engine* que valida las franjas horarias autorizadas para cada rol.
3. **Servicios Core:** *Booking Lifecycle Service*, *Priority & Lock Engine* (gestión de preemption) y *Approval Workflow Service*.
4. **Event Streaming:** Kafka Event Broker con despacho asíncrono de alertas (`BookingRequested`, `SpaceBlocked`, `ReservationPreempted`).
5. **Persistencia & Locks:** PostgreSQL con restricción de exclusión `tsrange` (imposibilidad matemática de solapamiento) + Redis Cluster para locks temporales de 5 minutos.
6. **Canales de Notificación:** App Móvil con push y QR check-in + Email institucional.

---

### [Frame 2] Máquina de Estados & Protocolo de Desplazamiento (*Preemption*)
* **Flujo Principal (6 Estados):**
  $$\text{1. Solicitada} \longrightarrow \text{2. En Evaluación} \longrightarrow \text{3. Aprobada} \longrightarrow \text{4. Confirmada} \longrightarrow \text{5. En Curso} \longrightarrow \text{6. Finalizada}$$
* **Ramas de Excepción:**
  - `Rechazada`: Cuando el coordinador deniega la solicitud con motivo.
  - `Expirada`: Si el usuario no realiza check-in QR en puerta en los primeros 15 min.
  - `Modificada`: Cambio de fecha, hora o aforo con revalidación.
  - `Cancelada`: Anulación voluntaria con más de 2 horas de antelación.
  - `Desplazada (Preempted)`: Cuando un actor de mayor rango bloquea el espacio, activando la reubicación automática inteligente.
* **Tabla Jerárquica de Prioridad de Bloqueo:**
  - 🚨 **Nivel 1 (Máxima):** Seguridad (Emergencia / Aforo crítico).
  - 🔧 **Nivel 2:** Mantenimiento (Averías y obras $\rightarrow$ Desplaza reservas existentes).
  - 🏛️ **Nivel 3:** Coordinación (Exámenes oficiales y actos de rectorado).
  - 👨‍🏫 **Nivel 4:** Profesores (Clases magistrales y prácticas regladas).
  - 🎓 **Nivel 5:** Estudiantes (Salas de estudio en franjas abiertas).

---

### [Frame 3] Matriz de Disponibilidad Horaria y Gestión de Conflictos
Tabla de gobernanza con anchos proporcionales y 5 niveles de control:

| Tipo de Espacio | Usuarios Autorizados | Horarios y Reglas de Franja | Modo de Reserva | Protocolo ante Bloqueo / Mantenimiento |
| :--- | :--- | :--- | :--- | :--- |
| **Salas de Estudio Grupal** | Estudiantes (pregrado/posgrado) | Lunes a Viernes (8:00 a 22:00) | 100% Instantáneo | Notificación Push en $< 60\text{s}$ y sugerencia de sala libre en el mismo edificio. |
| **Aulas Magistrales y Seminarios** | Profesores y Departamentos | Mañanas: Clases \| Tardes: Talleres | Aprobación Coordinador ($< 4\text{h}$) | Reubicación automática a aula con igual capacidad y proyector. |
| **Laboratorios Especializados** | Profesores e Investigadores | Sujeto a calendario de investigación | Aprobación Doble (Dpto + Lab) | Inspección previa de seguridad; aviso urgente de suspensión con 48h. |
| **Auditorios y Paraninfos** | Coordinación y Rectorado | Eventos solemnes y congresos | Aprobación Coordinación Central | Prioridad Nivel 3: Desplaza cualquier reserva docente previa. |
| **Espacios Bloqueados por Avería** | Personal de Mantenimiento | Bloqueo 24/7 hasta fin de obra | Trigger Inmediato Mantenimiento | Cancelación/reubicación de todas las reservas de la franja y alerta. |

---

### [Frame 4] Dashboard Analítico de Ocupación y Subutilización
Panel ejecutivo con métricas de alto contraste y detección de capacidad ociosa:

1. **`88.4%`** — *Utilización Promedio de Espacios* (Meta: $> 80\%$).
2. **`14,250 h`** — *Horas Reservadas en el Semestre* ($+18\%$ vs año anterior).
3. **`Ingeniería (94%)`** — *Facultad con Mayor Demanda* (Medicina 89%, Derecho 76%).
4. **`1.8%`** — *Tasa de No-Shows* (Reducida mediante check-in QR y penalización por reincidencia).
5. **`3.4%`** — *Tasa de Cancelaciones a Tiempo* ($> 2\text{h}$ de antelación).
6. **`10:00 - 13:00`** — *Franja de Demanda Pico*.
7. **`6 Salas`** — *Espacios Subutilizados Detectados ($< 35\%$ de uso)* en Edificio B y Pabellón Norte, con recomendación de reasignación a salas de estudio libre.

---

## 📁 3. Archivos Entregados en `PRUEBAS_V4/`

* 🎨 [**`PRUEBAS_V4/sistema_reserva_espacios_universidad.excalidraw`**](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V4/sistema_reserva_espacios_universidad.excalidraw)
* 📜 [**`PRUEBAS_V4/generate_university_space_reservation.py`**](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V4/generate_university_space_reservation.py)
* 📋 [**`PRUEBAS_V4/especificacion_reserva_espacios_universidad.md`**](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V4/especificacion_reserva_espacios_universidad.md)
* 📊 [**`PRUEBAS_V4/evaluacion_critica_universidad.md`**](file:///Users/leonfeliperodriguez/Desktop/Trabajos/Sketion%20SKILL/PRUEBAS_V4/evaluacion_critica_universidad.md)
