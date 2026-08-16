# 🧪 Test Adversarial 01: Información Sin Estructura Visual Explícita

## 🎯 Objetivo de la Prueba
Evaluar si Sketion es capaz de inferir autónomamente un patrón **AS-IS (Estado Actual) $\rightarrow$ Pain Points (Fricción) $\rightarrow$ TO-BE (Propuesta) $\rightarrow$ KPIs (Métricas)** ante un texto narrativo no estructurado, sin recibir ninguna indicación de qué diagrama o plantilla utilizar.

---

## 📥 Prompt de Entrada (Raw Input)

```text
Una empresa quiere reducir el tiempo de incorporación de nuevos empleados.

Actualmente:
RRHH recibe los documentos por correo.
El empleado llena varios formularios.
RRHH revisa manualmente la información.
Si falta algo, devuelve el correo.
Cuando todo está completo, crea manualmente al empleado en cinco sistemas diferentes.

IT crea las cuentas de correo y aplicaciones.
El gerente debe aprobar determinados accesos.
Seguridad revisa los accesos privilegiados.

El proceso normalmente tarda entre 3 y 7 días.

Los principales problemas son:
- duplicación de información
- múltiples transferencias entre equipos
- aprobaciones manuales
- falta de visibilidad
- errores de digitación
- empleados esperando acceso

La empresa quiere reducir el proceso a menos de 4 horas.

Se está considerando automatizar:
- recopilación de documentos
- validación de información
- creación de cuentas
- asignación de permisos
- notificaciones
- seguimiento del estado

Algunas tareas seguirán requiriendo intervención humana.
Los accesos privilegiados nunca pueden aprobarse automáticamente.
El gerente debe aprobar determinados accesos.
Seguridad debe aprobar accesos críticos.

La empresa quiere medir:
- tiempo total de onboarding
- tiempo esperando aprobación
- número de intervenciones humanas
- errores
- porcentaje automatizado
- tiempo hasta primer acceso

Representa visualmente el problema, el proceso actual, los puntos de fricción y la dirección propuesta.
No se especifica qué tipo de diagrama utilizar. Determina tú la representación más adecuada.
```

---

## 🔍 Criterios de Evaluación y Juicio de Sketion

| Criterio | Decisión Correcta (PASS) | Decisión Incorrecta (FAIL) |
| :--- | :--- | :--- |
| **Elección de Arquetipo** | Descomposición en **El Duelo (Before vs After)** o **Swimlanes Multi-Actor**. | Hacer un solo flowchart plano lineal donde se mezclan el dolor y la solución. |
| **Diferenciación de Fricción** | Resaltar los 6 cuellos de botella con paleta de dolor (`#FDEFEF` / `#E03A2F`) o post-its centrales. | Dibujar cajas neutras sin contraste visual de problemas. |
| **Gobernanza de Seguridad** | Puerta de enlace humana obligatoria (*Human-in-the-loop*) para accesos privilegiados. | Automatizar todo al 100% ignorando la regla de seguridad del CISO. |
| **Métricas Comparativas** | Dashboard de 6 KPIs con contraste antes ($3\text{--}7\text{ días}$) vs después ($< 4\text{ h}$). | Omitir las métricas o esconderlas en párrafos largos de texto. |
