# 🧪 Test Adversarial 02: Información que Exige Múltiples Perspectivas

## 🎯 Objetivo de la Prueba
Evaluar si Sketion tiene el criterio para **reconocer cuándo NO meter todo en un único diagrama** y decidir inteligentemente qué información debe estar junta y qué información debe separarse en múltiples frames coordinados.

---

## 📥 Prompt de Entrada (Raw Input)

```text
Una universidad quiere implementar un sistema de reserva de espacios.

Los estudiantes pueden reservar salas de estudio.
Los profesores pueden reservar aulas.
Los coordinadores pueden bloquear espacios.
Mantenimiento puede marcar espacios como no disponibles.
Seguridad puede restringir determinados espacios.

Una reserva puede ser:
- solicitada
- aprobada
- confirmada
- modificada
- cancelada
- rechazada
- expirada

Algunos espacios requieren aprobación.
Otros pueden reservarse inmediatamente.

Una sala puede estar disponible para estudiantes durante determinados horarios pero reservada para profesores durante otros.

Las reservas no pueden solaparse.

Los coordinadores pueden crear bloqueos que tienen prioridad sobre reservas normales.

Si mantenimiento marca un espacio como no disponible, las reservas existentes deben revisarse.

El sistema debe enviar notificaciones cuando:
- una reserva es aprobada
- una reserva es rechazada
- una reserva cambia
- un espacio queda bloqueado
- una reserva existente resulta afectada por un bloqueo

Además, la universidad quiere analizar:
- utilización por espacio
- utilización por facultad
- horas reservadas
- cancelaciones
- no-shows
- demanda por horario
- espacios subutilizados

Diseña una representación visual que permita comprender el funcionamiento completo del sistema.
No indiques previamente qué tipo de diagrama utilizar.
Decide qué información debe estar junta y qué información debe separarse en frames.
```

---

## 🔍 Criterios de Evaluación y Juicio de Sketion

| Criterio | Decisión Correcta (PASS) | Decisión Incorrecta (FAIL) |
| :--- | :--- | :--- |
| **Separación en Marcos** | **Mínimo 3 a 4 Frames coordinados:** (1. Arquitectura/RBAC, 2. Máquina de Estados/Preemption, 3. Matriz de Políticas Horarias, 4. Dashboard de Utilización). | Intentar comprimir roles, 7 estados, matriz horaria, preemption y métricas en un solo canvas gigante inmanejable. |
| **Preemption Jerárquico** | Modelar explícitamente que Mantenimiento y Seguridad desplazan reservas docentes/estudiantiles. | Tratar todas las reservas con la misma prioridad sin jerarquía de desalojo. |
| **Cero Solapamiento** | Explicitar el mecanismo de consistencia (Exclusion Constraint `tsrange` en PostgreSQL o Distributed Lock en Redis). | Omitir cómo se garantiza que dos personas no reserven la misma sala al mismo tiempo. |
| **Detección de Subutilización** | Incluir en el dashboard el análisis de espacios con $<35\%$ de uso para reasignación. | Mostrar solo métricas globales de éxito sin alertar sobre capacidad ociosa. |
