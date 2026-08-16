# 🧪 Test Adversarial 05: Jerarquía Extrema Multinivel y Sistemas Anidados

## 🎯 Objetivo de la Prueba
Evaluar cómo maneja Sketion una estructura con **más de 4 niveles de profundidad jerárquica** (ej. Organización Global $\rightarrow$ Unidades de Negocio $\rightarrow$ Microservicios $\rightarrow$ Componentes $\rightarrow$ Tablas de BD / Algoritmos). Verificar si el motor sabe cuándo anidar scopes (*Nested Scopes*), cuándo usar cajas concéntricas (*La Cebolla*) o cuándo crear un *Zoom-In Exploded Box*.

---

## 📥 Prompt de Entrada (Raw Input)

```text
Representa la arquitectura corporativa de gobernanza de datos para una multinacional bancaria.

Nivel 1: Grupo Corporativo Global
Nivel 2: 3 Divisiones Continentales (América, Europa, Asia-Pacífico)
Nivel 3: Cada división contiene 4 Dominios de Negocio (Retail Banking, Corporate, Wealth Mgmt, Risk)
Nivel 4: Dentro del Dominio de Risk en Europa, existen 3 subsistemas:
- Credit Risk Engine (Calcula scoring crediticio con modelos de machine learning)
- Fraud Watchdog (Analiza patrones de transacciones en streaming con Kafka)
- Regulatory Compliance Reporter (Genera reportes de Basilea III y GDPR)

Dentro del Credit Risk Engine, se encuentran:
- Data Ingestion Pipeline (Procesa extractos bancarios y bureau de crédito)
- Feature Store (Almacena 250 variables en Redis)
- Inference Server (Expone endpoints gRPC con latencia < 20ms)
- Model Registry (Controla versiones de modelos en MLflow)

El sistema debe mostrar cómo los datos fluyen desde las agencias locales en Europa hasta el reporte consolidado global, respetando la soberanía de datos de cada país.
```

---

## 🔍 Criterios de Evaluación y Juicio de Sketion

| Criterio | Decisión Correcta (PASS) | Decisión Incorrecta (FAIL) |
| :--- | :--- | :--- |
| **Manejo de Jerarquía Profunda** | Usar **Arquetipo T (Caja Explotada / Deep Dive Zoom)** o **Arquetipo J (La Cebolla)**: Frame 1 muestra el mapa global de divisiones y conecta con líneas de proyección hacia el Frame 2 que desglosa el *Credit Risk Engine* con sus 4 componentes internos. | Intentar dibujar 5 niveles de cajas anidadas microscópicas en un solo árbol ilegible. |
| **Soberanía de Datos** | Representar la frontera de soberanía (GDPR en Europa) con un Scope perimetral destacado. | Conectar las bases de datos de Europa directamente a servidores en América sin barreras de gobernanza. |
