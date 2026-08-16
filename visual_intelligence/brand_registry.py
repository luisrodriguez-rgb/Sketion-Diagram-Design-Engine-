"""
Sketion Brand & Technology Registry (v8.2 - Pure Vector & Badges)
Reconocimiento y estilización de más de 60 marcas y tecnologías del ecosistema tech/fintech.
100% LIBRE DE EMOJIS: Utiliza exclusivamente códigos cromáticos oficiales de marca,
tags técnicos y badges vectoriales.
"""

from dataclasses import dataclass
from typing import Dict, Any, Optional, List


@dataclass
class BrandSpec:
    brand_id: str
    display_name: str
    category: str
    brand_color: str
    bg_color: str
    vector_icon: str
    tech_tags: List[str]


class BrandRegistry:
    """Registro de marcas, productos y plataformas tecnológicas reconocidas por Sketion."""

    _BRANDS: Dict[str, BrandSpec] = {
        # 1. CLOUD & INFRAESTRUCTURA
        "aws": BrandSpec("aws", "Amazon Web Services", "CLOUD", "#FF9900", "#FFF9EE", "server", ["EC2", "ALB", "S3", "EKS"]),
        "gcp": BrandSpec("gcp", "Google Cloud Platform", "CLOUD", "#4285F4", "#EFF6FF", "server", ["GKE", "BigQuery", "PubSub"]),
        "azure": BrandSpec("azure", "Microsoft Azure", "CLOUD", "#0089D6", "#EFF8FF", "server", ["AKS", "CosmosDB"]),
        "cloudflare": BrandSpec("cloudflare", "Cloudflare", "SECURITY_EDGE", "#F38020", "#FFF7ED", "shield", ["WAF", "DDoS", "CDN", "Workers"]),
        "kubernetes": BrandSpec("kubernetes", "Kubernetes (K8s)", "ORCHESTRATION", "#326CE5", "#EFF6FF", "server", ["Pods", "Ingress", "Cluster"]),
        "docker": BrandSpec("docker", "Docker Containers", "CONTAINER", "#2496ED", "#EFF6FF", "server", ["Images", "Compose"]),
        "terraform": BrandSpec("terraform", "HashiCorp Terraform", "IAC", "#7B42BC", "#F5EEFF", "server", ["HCL", "State"]),

        # 2. BASES DE DATOS & STORAGE
        "postgresql": BrandSpec("postgresql", "PostgreSQL", "DATABASE_ACID", "#336791", "#EFF6FF", "database", ["SQL", "ACID", "Relational"]),
        "aurora": BrandSpec("aurora", "AWS Aurora PostgreSQL", "DATABASE_ACID", "#336791", "#EFF6FF", "database", ["Multi-AZ", "Serverless"]),
        "redis": BrandSpec("redis", "Redis In-Memory", "CACHE_KEYVALUE", "#DC382D", "#FFF5F2", "server", ["In-Memory", "PubSub", "Redlock"]),
        "mongodb": BrandSpec("mongodb", "MongoDB Document DB", "NOSQL", "#47A248", "#F0FDF4", "database", ["BSON", "Atlas"]),
        "clickhouse": BrandSpec("clickhouse", "ClickHouse OLAP", "DATABASE_OLAP", "#FFCC00", "#FFFBEB", "database", ["Columnar", "Realtime SQL"]),
        "dynamodb": BrandSpec("dynamodb", "Amazon DynamoDB", "NOSQL", "#4053D6", "#EEF2FF", "database", ["Key-Value", "Single-Digit MS"]),
        "minio": BrandSpec("minio", "MinIO Object Storage", "STORAGE_S3", "#C72C48", "#FFF5F5", "database", ["S3 Compatible", "WORM"]),
        "snowflake": BrandSpec("snowflake", "Snowflake Data Cloud", "DATA_WAREHOUSE", "#29B5E8", "#F0F9FF", "database", ["SQL", "Analytics"]),
        "supabase": BrandSpec("supabase", "Supabase Backend", "BAAS", "#3ECF8E", "#ECFDF5", "database", ["Postgres", "Realtime Auth"]),
        "firebase": BrandSpec("firebase", "Google Firebase", "BAAS", "#FFCA28", "#FFFBEB", "server", ["Firestore", "Auth"]),

        # 3. STREAMING & QUEUES
        "kafka": BrandSpec("kafka", "Apache Kafka", "STREAMING", "#231F20", "#F8FAFC", "terminal", ["Event Bus", "Partitions", "Topics"]),
        "rabbitmq": BrandSpec("rabbitmq", "RabbitMQ Message Broker", "QUEUE", "#FF6600", "#FFF7ED", "terminal", ["AMQP", "Exchanges"]),
        "flink": BrandSpec("flink", "Apache Flink", "STREAM_PROCESSING", "#E65243", "#FFF5F2", "server", ["Stateful Stream", "Event Time"]),
        "spark": BrandSpec("spark", "Apache Spark", "DATA_PROCESSING", "#E25A1C", "#FFF7ED", "server", ["Batch", "Stream"]),

        # 4. FINTECH & PAGOS
        "stripe": BrandSpec("stripe", "Stripe Payments", "PAYMENTS", "#635BFF", "#EEF2FF", "card", ["Cards", "Checkout", "Billing"]),
        "visa": BrandSpec("visa", "Visa Direct Switch", "PAYMENT_NETWORK", "#1A1F71", "#EFF6FF", "card", ["ISO 8583", "Interchange"]),
        "mastercard": BrandSpec("mastercard", "Mastercard Switch", "PAYMENT_NETWORK", "#EB001B", "#FFF5F2", "card", ["Debit", "Credit"]),
        "paypal": BrandSpec("paypal", "PayPal Holdings", "WALLET", "#003087", "#EFF6FF", "card", ["Digital Wallet", "B2C"]),
        "plaid": BrandSpec("plaid", "Plaid Open Banking", "OPEN_BANKING", "#000000", "#F8FAFC", "server", ["ACH", "Auth"]),
        "apple_pay": BrandSpec("apple_pay", "Apple Pay", "WALLET", "#000000", "#F8FAFC", "card", ["NFC", "Secure Enclave"]),
        "google_pay": BrandSpec("google_pay", "Google Pay", "WALLET", "#4285F4", "#EFF6FF", "card", ["Tokenized EMV", "Android"]),
        "pix": BrandSpec("pix", "PIX Banco Central", "INSTANT_RAIL", "#32BCAD", "#ECFDF5", "card", ["Instant 24/7", "QR Code"]),
        "pse": BrandSpec("pse", "PSE Pagos Seguros", "BANK_TRANSFER", "#004B87", "#EFF6FF", "card", ["ACH Debit", "Colombia"]),

        # 5. OBSERVABILIDAD & SRE
        "prometheus": BrandSpec("prometheus", "Prometheus Telemetry", "MONITORING", "#E6522C", "#FFF7ED", "server", ["Time Series", "Alerts"]),
        "grafana": BrandSpec("grafana", "Grafana Labs", "VISUALIZATION", "#F46800", "#FFF7ED", "laptop", ["NOC Wall", "Dashboards"]),
        "pagerduty": BrandSpec("pagerduty", "PagerDuty Incident Management", "ALERTING", "#06AC38", "#F0FDF4", "alert", ["On-Call", "Escalation"]),
        "datadog": BrandSpec("datadog", "Datadog Cloud Monitoring", "APM", "#632CA6", "#F5EEFF", "laptop", ["Traces", "Logs"]),
        "elasticsearch": BrandSpec("elasticsearch", "Elasticsearch Kibana", "SEARCH_LOGS", "#005571", "#EFF8FF", "file", ["Lucene", "ELK Stack"]),
        "opentelemetry": BrandSpec("opentelemetry", "OpenTelemetry (OTel)", "TRACING", "#000000", "#F8FAFC", "server", ["Distributed Traces", "Spans"]),

        # 6. FRAMEWORKS & LENGUAJES
        "react": BrandSpec("react", "React.js SPA", "FRONTEND", "#61DAFB", "#F0FDFF", "laptop", ["Virtual DOM", "Components"]),
        "nextjs": BrandSpec("nextjs", "Next.js Framework", "FULLSTACK", "#000000", "#F8FAFC", "laptop", ["SSR", "API Routes"]),
        "nodejs": BrandSpec("nodejs", "Node.js V8", "RUNTIME", "#339933", "#F0FDF4", "server", ["Async I/O", "Event Loop"]),
        "python": BrandSpec("python", "Python ML / FastAPI", "BACKEND_AI", "#3776AB", "#EFF6FF", "server", ["FastAPI", "Pandas"]),
        "golang": BrandSpec("golang", "Go Lang Microservices", "BACKEND_HIGH_PERF", "#00ADD8", "#F0F9FF", "server", ["Goroutines", "gRPC"]),

        # 7. COMUNICACIÓN & SAAS
        "slack": BrandSpec("slack", "Slack API", "COMMUNICATION", "#4A154B", "#FAF5FF", "users", ["Webhooks", "Bots"]),
        "whatsapp": BrandSpec("whatsapp", "WhatsApp Business API", "MESSAGING", "#25D366", "#F0FDF4", "users", ["Conversational", "Meta"]),
        "sap": BrandSpec("sap", "SAP ERP Enterprise", "ERP", "#008FD3", "#EFF8FF", "database", ["Financials", "Accounting"]),
        "shopify": BrandSpec("shopify", "Shopify E-commerce", "ECOMMERCE", "#7AB55C", "#F0FDF4", "card", ["Checkout", "GraphQL"]),
        "github": BrandSpec("github", "GitHub Enterprise", "VCS_CICD", "#181717", "#F8FAFC", "server", ["Actions", "Git"])
    }

    @classmethod
    def match_brand(cls, text: str) -> Optional[BrandSpec]:
        """Detecta automáticamente si un texto o nombre de componente corresponde a una marca conocida."""
        t_low = text.lower().strip()
        for brand_key, spec in cls._BRANDS.items():
            if brand_key in t_low or spec.display_name.lower() in t_low:
                return spec
            # Chequear tags
            for tag in spec.tech_tags:
                if tag.lower() in t_low and len(tag) > 2:
                    return spec
        return None

    @classmethod
    def get_all_brands(cls) -> List[BrandSpec]:
        return list(cls._BRANDS.values())

    @classmethod
    def count(cls) -> int:
        return len(cls._BRANDS)
