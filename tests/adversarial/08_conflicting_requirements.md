# 🧪 Test Adversarial 08: Requisitos Contradictorios y Resolución de Dilemas

## 🎯 Objetivo de la Prueba
Evaluar cómo resuelve Sketion un escenario donde existen **requisitos en conflicto directo** (ej. "Queremos latencia ultrarrápida $< 5\text{ms}$ global" vs "Queremos consistencia estricta ACID en 3 continentes", o "Privacidad total sin guardar logs" vs "Auditoría forense obligatoria de fraude").

---

## 📥 Prompt de Entrada (Raw Input)

```text
Diseña la arquitectura de un exchange descentralizado de criptomonedas y trading de alta frecuencia (HFT).

Requisitos contradictorios planteados por los stakeholders:
1. El equipo de Trading exige: Latencia de ejecución < 2 milisegundos con order matching en memoria pura.
2. El equipo de Compliance exige: Cada orden debe registrarse de forma inmutable en blockchain y ser auditada contra listas negras de la OFAC antes de ejecutarse.
3. El equipo de Seguridad exige: Las claves privadas de los usuarios nunca pueden estar en servidores conectados a internet (Cold Storage absoluto).
4. El equipo de UX exige: Depósitos instantáneos en 1 clic sin esperar confirmaciones de bloque.

Muestra cómo la arquitectura resuelve estos trade-offs arquitectónicos mediante segregación de capas y sistemas híbridos (Off-chain Matching Engine vs On-chain Settlement con Rollups L2 y MPC Wallets).
```

---

## 🔍 Criterios de Evaluación y Juicio de Sketion

| Criterio | Decisión Correcta (PASS) | Decisión Incorrecta (FAIL) |
| :--- | :--- | :--- |
| **Modelado de Trade-Offs** | Usar una arquitectura en 2 planos: **Plano Rápido Off-Chain (Matching en memoria $<2\text{ms}$ + MPC)** y **Plano Lento On-Chain (Batch Settlement en Rollup L2 + Auditoría Asíncrona)**. | Conectar directamente el Matching Engine a la blockchain creando un cuello de botella de 15 segundos que destruye la latencia. |
| **Matriz de Resolución de Conflictos** | Incluir una tabla que explique formalmente cada dilema, el compromiso adoptado (*trade-off*) y la justificación técnica. | Ignorar las contradicciones y asumir que todo se puede hacer instantáneo y seguro a la vez sin compensaciones. |
