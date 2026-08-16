# 🧪 Test Adversarial 07: Información Incompleta y Estimación Transparente

## 🎯 Objetivo de la Prueba
Evaluar cómo reacciona Sketion cuando el prompt contiene **lagunas críticas de información** (ej. no especifica SLAs, tipos de bases de datos, protocolos de red o métricas numéricas). Verificar que el motor **NO se frena a hacer preguntas ni deja cajas vacías tipo `[TU CIFRA AQUÍ]`**, sino que infiere estándares de industria realistas y los documenta transparentemente al pie.

---

## 📥 Prompt de Entrada (Raw Input)

```text
Haz un diagrama del sistema de recomendación de videos de una app como TikTok o YouTube Shorts.

Los usuarios ven videos en el feed vertical.
El sistema aprende de lo que ven, de lo que saltan rápido, de los likes y de lo que comparten.
Queremos recomendar el siguiente video en milisegundos.

Hay creadores que suben videos. Los videos se procesan y se indexan.

Muestra cómo funciona la arquitectura y qué métricas deberíamos medir.
```

---

## 🔍 Criterios de Evaluación y Juicio de Sketion

| Criterio | Decisión Correcta (PASS) | Decisión Incorrecta (FAIL) |
| :--- | :--- | :--- |
| **Cero Formularios de Preguntas** | El motor genera el diagrama de inmediato asumiendo un pipeline moderno de ML en streaming (Embeddings, Approximate Nearest Neighbors / HNSW, Candidate Generation $\rightarrow$ Ranking $\rightarrow$ Re-ranking). | Responder con un cuestionario de 6 preguntas ("¿Qué base de datos usas?", "¿Cuál es tu SLA?", "¿Usas Kafka o SQS?"). |
| **Estimación de Métricas Realistas** | Incluye métricas de industria coherentes (`Latencia < 35ms`, `CTR +12%`, `Watch Time 42 min/día`, `Cold Start 3 videos`) con nota al pie. | Dejar chips con `[X ms]` o `[MÉTRICA DE EJEMPLO]`. |
| **Separación de Pipelines** | Distingue claramente el **Pipeline Offline / Batch** (Ingesta de video, extracción de features, entrenamiento de embeddings) del **Pipeline Online / Streaming** (Inferencia en tiempo real sobre el feed del usuario). | Mezclar la subida de videos con la inferencia de milisegundos en una sola caja sin jerarquía. |
