"""
Sketion Grand Blind Holdout Dataset (v9.5)
160 Prompts arquitectónicos nunca utilizados durante el desarrollo de Sketion,
distribuidos equitativamente en 8 dominios de la industria:
1. Software / Cloud Architecture (20 casos)
2. Business & Enterprise Strategy (20 casos)
3. Finance & Banking Rails (20 casos)
4. Healthcare & Clinical Zero-Trust (20 casos)
5. Education & E-Learning Platforms (20 casos)
6. Operations & Supply Chain Logistics (20 casos)
7. Science & Aerospace Engineering (20 casos)
8. Product Design & UX Workflows (20 casos)
"""

from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class HoldoutPrompt:
    id: str
    domain: str
    title: str
    prompt_text: str
    complexity: str  # "MEDIUM", "HIGH", "EXTREME"
    expected_entities: List[Dict[str, Any]]


def generate_160_holdout_prompts() -> List[HoldoutPrompt]:
    """Genera la suite completa de 160 prompts arquitectónicos ciegos."""
    prompts: List[HoldoutPrompt] = []

    domains = [
        ("CLOUD_SOFTWARE", "Software & Cloud Architecture", [
            ("Multi-Region Kubernetes Disaster Recovery", ["Route53", "AWS ALB", "EKS Primary", "EKS Standby", "Aurora Multi-AZ", "Kafka MirrorMaker", "Datadog APM"]),
            ("Serverless Event-Driven Video Transcoder", ["S3 Upload", "EventBridge", "AWS Lambda Ingest", "AWS Batch GPU", "DynamoDB Metadata", "CloudFront CDN"]),
            ("Real-Time Collaborative Code Sandbox", ["Cloudflare Workers", "WebSockets Gateway", "Docker Sandbox Pool", "Redis PubSub", "PostgreSQL", "Prometheus"]),
            ("Distributed Graph Neural Network Pipeline", ["GCP PubSub", "Neo4j Graph DB", "PyTorch GPU Workers", "Ray Cluster", "BigQuery Sink", "Grafana"]),
            ("Global Anycast DNS & Edge Compute Mesh", ["Anycast IP Mesh", "Envoy Edge Proxy", "eBPF Kernel Filter", "Redis Edge Cache", "ClickHouse Logs"]),
            ("Zero-Downtime Database Migration Pipeline", ["PostgreSQL Source", "Debezium CDC", "Apache Kafka", "Flink Stream Transformer", "Snowflake Target"]),
            ("Micro-Frontend Single Sign-On Shell", ["Next.js Shell", "Auth0 OIDC", "React MFE Remote 1", "Vue MFE Remote 2", "Tailwind Design System"]),
            ("Autonomous Microservices Mesh Istio", ["Istio Control Plane", "Envoy Sidecars", "Vault PKI mTLS", "Jaeger Distributed Tracing", "K8s Pods"]),
            ("High-Concurrency Webhook Dispatcher", ["RabbitMQ Buffer", "Go Worker Fleet", "Circuit Breaker", "Redis Exponential Backoff", "Postgres DLQ"]),
            ("Enterprise Search Engine Elasticsearch", ["Crawler Bot", "Kafka Ingest", "Logstash ETL", "Elasticsearch Cluster", "Kibana Dashboard"]),
            ("IoT Fleet Firmware OTA Update Pipeline", ["MQTT Broker", "Device Shadow DB", "S3 Firmware Artifact", "Rollout Orchestrator", "Grafana NOC"]),
            ("Multi-Tenant SaaS Isolation Engine", ["Tenant Router", "Cognito RBAC", "Schema-Per-Tenant DB", "Redis Cache Partition", "Stripe Billing"]),
            ("Streaming Fraud Detection Engine", ["Kafka Input Stream", "Flink Complex Event Processing", "Redis Sliding Windows", "ML Scoring Python", "Alert Manager"]),
            ("Geospatial Tile Server Vector Map", ["PostGIS Cluster", "Tilelive Cache", "FastAPI Tile Server", "CloudFront CDN", "Mapbox SDK"]),
            ("Distributed Cron Job Scheduler", ["Etcd Consensus", "Leader Election Node", "Worker Pool Celery", "Redis Queue", "PostgreSQL Logs"]),
            ("Enterprise Feature Flagging Platform", ["Next.js Admin", "Redis Fast KV", "Envoy Filter", "Snowflake Experimentation", "Slack Webhook"]),
            ("High-Availability Redis Cluster Sentinel", ["Client App", "Redis Master", "Redis Replica 1", "Redis Replica 2", "Sentinel Quorum"]),
            ("Secure Secret Management Vault", ["App Microservice", "Vault Agent mTLS", "KMS Auto-Unseal", "Consul Storage", "Audit Log WORM"]),
            ("Data Lakehouse Ingestion Engine", ["Raw Data S3", "Apache Iceberg", "Apache Spark Batch", "Trino Query Engine", "Superset BI"]),
            ("Distributed Tracing OpenTelemetry Collector", ["App Instrumentation", "OTel Collector", "Jaeger Storage", "ClickHouse Traces", "Grafana Tempo"])
        ]),
        ("BUSINESS_STRATEGY", "Business & Enterprise Strategy", [
            ("Corporate Mergers & Acquisitions Value Chain", ["Target Entity Review", "Due Diligence Audit", "Synergy Assessment", "Executive Sign-Off", "Integration Roadmap"]),
            ("Enterprise Digital Transformation Funnel", ["Legacy Audit", "Cloud Readiness", "Pilot MVP Program", "Scale Adoption", "ROI Metric Card"]),
            ("SaaS Customer Lifetime Value Maximizer", ["Lead Acquisition", "Product Onboarding", "Usage Expansion", "Renewal Engine", "Churn Risk Alarm"]),
            ("Global Expansion Market Entry Strategy", ["Regulatory Clearance", "Local Entity Setup", "Banking Switch Partner", "Go-To-Market Launch", "Revenue KPI"]),
            ("Enterprise Procurement & Vendor Sourcing", ["RFP Specification", "Vendor Bidding", "Security Compliance", "Legal Contract", "ERP SAP Ingest"]),
            ("Product-Led Growth (PLG) Conversion Flywheel", ["Freemium Signup", "Time-To-Value Hook", "Feature Paywall", "Self-Serve Upgrade", "Stripe Checkout"]),
            ("Omnichannel Retail Unified Experience", ["Online Store", "Retail POS", "Mobile Loyalty App", "Unified Inventory", "Warehouse Logistics"]),
            ("B2B Sales Pipeline Lead Scoring", ["Marketing Inbound", "HubSpot CRM Score", "SDR Qualification", "Executive Demo", "Deal Closing"]),
            ("Corporate Governance & Board Reporting", ["Quarterly Financials", "Risk Heatmap", "ESG Compliance", "Shareholder Report", "Audit Committee"]),
            ("Strategic Brand Repositioning Architecture", ["Customer Persona Research", "Brand Identity", "Design System", "Omnichannel Rollout", "NPS Metric"]),
            ("Franchise Expansion Model Orchestrator", ["Franchise Agreement", "Site Selection", "Standardized POS", "Supply Chain Link", "Royalty Billing"]),
            ("Customer Support Tiering & SLA Escalation", ["Zendesk Ticket Ingest", "AI Categorizer", "Tier 1 Support", "Tier 2 Engineering", "SLA Monitor"]),
            ("Partner Ecosystem Revenue Sharing", ["Partner Portal", "API Affiliate Tracking", "Attribution Engine", "Payout Ledger", "Tax Report"]),
            ("Executive KPI Dashboard & OKR Alignment", ["Company Vision", "Objective 1: ARR", "Objective 2: Retention", "Objective 3: Security", "Board Gauge"]),
            ("Supply Chain Supplier Risk Mitigation", ["Tier 1 Supplier", "Geopolitical Monitor", "Secondary Factory", "Buffer Inventory", "Audit Trail"]),
            ("Subscription Monetization Tiering Model", ["Starter Tier", "Pro Business Tier", "Enterprise Custom", "Billing Engine", "Stripe Invoicing"]),
            ("Change Management & Talent Upskilling", ["Skills Gap Matrix", "Curriculum Design", "Certification LMS", "Manager Assessment", "Talent Retention"]),
            ("Competitive Intelligence & Moat Defense", ["Market Crawling", "Patent Monitoring", "Feature Matrix", "SWOT Analyzer", "Exec Briefing"]),
            ("CSR & Sustainability Carbon Accounting", ["Scope 1 Direct Emissions", "Scope 2 Grid Electricity", "Scope 3 Supply Chain", "Audit Ledger", "ESG Badge"]),
            ("Crisis Communication & Public PR Runbook", ["Incident Alert", "Executive War Room", "Press Release Draft", "Social Monitoring", "Customer Dispatch"])
        ]),
        ("FINANCE_BANKING", "Finance & Banking Rails", [
            ("Cross-Border Multi-Currency FX Clearing", ["Swift MT103", "ISO 20022 XML", "Liquidity Pool Vault", "FX Rate Engine", "Central Bank Wire"]),
            ("High-Frequency Algorithmic Order Matching", ["FIX Protocol Ingest", "LMAX Disruptor Ring", "In-Memory Book", "PostgreSQL Ledger", "FPGA NIC"]),
            ("Card Issuing & Core Banking Processor", ["Visa DPS Switch", "PIN / CVV HSM Vault", "Ledger Account", "Fraud Scoring ML", "Cardholder App"]),
            ("Instant Real-Time P2P Payment Switch", ["PIX Central Gateway", "QR Code Scanner", "Instant Balance Check", "Settlement Ledger", "Push Alert"]),
            ("Automated Anti-Money Laundering (AML)", ["Transaction Stream", "OFAC Restrictive List", "Sanctions Screening", "SAR Report DIAN", "Risk Pill"]),
            ("Open Banking PSD2 & Account Aggregation", ["Plaid Open API", "OAuth2 Consent Token", "Bank Adapter BankA", "Bank Adapter BankB", "Budgeting UI"]),
            ("Decentralized Custody Multi-Sig Vault", ["Multi-Party Compute (MPC)", "Hardware Key 1", "Hardware Key 2", "Cold Storage Safe", "Audit Trail"]),
            ("Direct Debit ACH Bulk Clearinghouse", ["NACHA Batch Ingest", "ODFI Bank File", "FedACH Switch", "RDFI Bank Settle", "Return File Handler"]),
            ("Consumer Credit Scoring & Underwriting", ["Credit Bureau Equifax", "Bank Statement Analyzer", "Risk Model Python", "Loan Decision Engine", "E-Signature"]),
            ("Automated Merchant Settlement & Split Payout", ["Transaction Batch", "Platform Fee Split", "Tax Withholding DIAN", "Payout Switch ACH", "Merchant Ledger"]),
            ("Point-of-Sale (POS) Smart Terminal Switch", ["Smart POS Terminal", "mTLS Edge Gateway", "EMV Chip Decrypt", "Issuer Switch", "Receipt Printer"]),
            ("Chargeback & Dispute Arbitration Workflow", ["Chargeback Inbound", "Evidence Collector S3", "Issuer Arbitration", "Merchant Ledger Debit", "Doc Sign"]),
            ("Treasury Liquidity & Cash Forecasting", ["Bank Feed Multi-Account", "Forecasting Model", "Sweep Account Rule", "Liquidity Alert", "CFO Dashboard"]),
            ("Electronic Tax Invoicing Real-Time DIAN", ["Invoice Generator", "XML UBL 2.1 Signer", "DIAN Webhook API", "QR Code Stamper", "PDF Delivery"]),
            ("Micro-Lending Installment BNPL Engine", ["Checkout BNPL Button", "Instant KYC Check", "Installment Ledger", "Automated Card Recurring", "Debt Collector"]),
            ("Corporate Expense Card & Policy Enforcement", ["Virtual Card Master", "MCC Merchant Filter", "Receipt OCR Parser", "Accounting ERP Sync", "Manager Mobile"]),
            ("Central Bank Digital Currency (CBDC) Rail", ["Central Bank Node", "Commercial Bank Gateway", "Zero-Knowledge Proof", "Offline Wallet", "Ledger Sink"]),
            ("Securities Escrow & Smart Contract Custody", ["Buyer Funds Vault", "Seller Equity Registry", "Condition Verifier", "Settlement Atomicity", "Notary Trail"]),
            ("Automated Reconciliation Nightly Batch", ["Bank Statement MT940", "Internal DB Ledger", "Discrepancy Resolver", "Accounting Journal", "Audit WORM"]),
            ("Cryptocurrency Fiat On/Off Ramp Gateway", ["Crypto Exchange API", "Fiat Banking Partner", "KYC Verification", "Hot Wallet Custody", "Cold Storage S3"])
        ]),
        ("HEALTHCARE_CLINICAL", "Healthcare & Clinical Zero-Trust", [
            ("HIPAA Electronic Health Record (EHR) Hub", ["Doctor Clinical Portal", "FHIR API Gateway", "Encrypted PHI Postgres", "Audit Trail WORM", "Biometric Sign"]),
            ("Telemedicine Video Consultation Platform", ["WebRTC Video Mesh", "mTLS Session Broker", "Prescription Generator", "Patient App", "Stripe Billing"]),
            ("Hospital IoT Patient Vital Telemetry", ["Bedside ECG Monitor", "MQTT Clinical Broker", "Anomaly Alarm NOC", "Nurse Station Tablet", "HL7 Archiver"]),
            ("AI Medical Imaging DICOM Analysis", ["DICOM PACS Ingest", "GPU Inference Model", "Radiologist UI", "Tumor Segmentation", "Pathology Report"]),
            ("Laboratory Information Management (LIMS)", ["Sample Barcode Scan", "Analyzer Machine", "Quality Control Matrix", "Doctor PDF Portal", "MinIO S3"]),
            ("Clinical Trial Data Compliance Vault", ["Patient Consent ABAC", "Anonymized PHI Sink", "FDA 21 CFR Part 11", "Audit Signature HSM", "Statistician UI"]),
            ("Automated Pharmacy Prescription Dispenser", ["E-Prescription Ingest", "Drug Interaction Check", "Robotic Dispenser", "Pharmacist Sign-Off", "Patient SMS"]),
            ("Emergency Dispatch CAD & Ambulance Router", ["911 Call Ingest", "GPS Ambulance Track", "Hospital Bed Availability", "Triage Nurse Alert", "Route Map"]),
            ("Genomic Sequencing Variant Pipeline", ["FastQ Raw Reads", "Nextflow Pipeline", "Variant Caller GATK", "Snowflake Genome DB", "Clinical Report"]),
            ("Medical Device Firmware Compliance OTA", ["Device Registry", "Crypto Signature HSM", "Bluetooth BLE Sync", "FDA Recall Watchdog", "MinIO Artifact"]),
            ("Patient Portal & Health Insurance Claims", ["Mobile Patient App", "Claim Submission", "Insurance EDI 837", "Eligibility Check", "EOB Statement"]),
            ("ICU Bedside Early Warning Sepsis System", ["Vital Stream Kafka", "Sepsis ML Predictor", "PagerDuty Doctor Call", "Clinical Bedside Pill", "PostgreSQL"]),
            ("Blood Bank Inventory & Cold Chain Tracking", ["Donor Ingest Station", "Blood Type Barcode", "Temperature IoT Sensor", "Hospital Delivery", "Alert Siren"]),
            ("Oncology Radiation Therapy Plan Orchestrator", ["CT Scan 3D Model", "Dose Calculation Core", "Physicist Approval", "Linear Accelerator", "Patient DB"]),
            ("Pediatric Vaccination Tracking Registry", ["Birth Record Link", "Vaccine Schedule Rule", "Clinic Admin Portal", "Parent WhatsApp Reminder", "Health Ministry"]),
            ("Mental Health Conversational Bot Guardrail", ["Patient Mobile Chat", "Sentiment ML Model", "Self-Harm Guardrail", "Human Therapist Handover", "HIPAA Log"]),
            ("Hospital Asset Tracking RFID Beacon", ["Surgical Tray RFID", "Gateway Antenna", "Real-Time Location RTLS", "Sterilization Logger", "Nurse UI"]),
            ("Dental Clinic 3D Intraoral Scan Pipeline", ["3D STL Ingest", "Cloud CAD Designer", "Milling Machine Link", "Dentist Dashboard", "Patient Invoice"]),
            ("Anesthesia Monitoring & Automated Record", ["Anesthesia Machine", "Gas Level Telemetry", "Surgeon Display", "Post-Op Recovery Room", "EHR Sync"]),
            ("Rehabilitation Wearable Motion Tracker", ["Wearable Gyro Sensor", "Bluetooth Mobile", "Physiotherapist Portal", "Gamification Engine", "Recovery Score"])
        ]),
        ("EDUCATION_LEARNING", "Education & E-Learning Platforms", [
            ("Real-Time Interactive Virtual Classroom", ["Teacher WebRTC Stream", "Student Video Grid", "Interactive Whiteboard", "Chat Kafka Bus", "Class Recording S3"]),
            ("Automated Code Grading & Sandbox Runner", ["Student Git Push", "Docker Sandbox Pool", "Unit Test Validator", "Plagiarism Detector", "Gradebook PostgreSQL"]),
            ("AI Adaptive Learning & Skill Tree Engine", ["Student Diagnostic Quiz", "Knowledge Graph Neo4j", "Dynamic Curriculum", "Micro-Learning Cards", "Badge Reward"]),
            ("University Student Information System (SIS)", ["Admissions Portal", "Course Enrollment", "Tuition Billing Stripe", "Transcript Generator", "Faculty Portal"]),
            ("Proctored Online Exam Anti-Cheat System", ["Student Webcam AI", "Screen Lockdown App", "Audio Anomaly Detector", "Proctor Human Dashboard", "Audit Video S3"]),
            ("Learning Management System (LMS) Scorm Hub", ["SCORM Package Ingest", "Course Catalog UI", "Progress Tracking DB", "Certificate Generator", "SSO Google Auth"]),
            ("K-12 Gamified Math Learning Platform", ["Math Quest World", "Real-Time Leaderboard", "Teacher Assignment Hub", "Parent Progress Email", "Avatar Rewards"]),
            ("Language Learning Speech Recognition AI", ["Audio Microphone Ingest", "Wav2Vec Pronunciation", "Phoneme Comparison", "Streak Tracker Redis", "Mobile App"]),
            ("Peer-to-Peer Academic Paper Review", ["Paper Submission PDF", "Double-Blind Assigner", "Reviewer Form", "Plagiarism Checker", "Journal Publisher"]),
            ("Corporate Compliance Training & Certification", ["Video Module Player", "Comprehension Quiz", "SOC2 Compliance Report", "HR Workday Sync", "Certificate PDF"]),
            ("VR Medical Surgery Training Simulator", ["Oculus VR Headset", "3D Anatomy Engine", "Haptic Feedback Broker", "Performance Analytics", "Instructor Tablet"]),
            ("Student Financial Aid & Scholarship Grant", ["FAFSA Application", "Income Verification", "Scholarship Matching", "Disbursement Bank", "Auditor Log"]),
            ("Alumni Mentorship & Job Placement Network", ["Alumni Directory", "Mentor Matching AI", "1-on-1 Chat System", "Job Board Integration", "LinkedIn Sync"]),
            ("Library Digital Asset Management System", ["E-Book EPUB Catalog", "DRM License Vault", "Borrowing Queue Redis", "Student Mobile Reader", "ISBN Database"]),
            ("Campus Smart Card & Dining POS System", ["Student RFID Card", "Dining Hall POS", "Turnstile Gate", "Balance Reload Stripe", "Ledger DB"]),
            ("Music Conservatory Audio Stem Masterclass", ["Multi-Track Audio Upload", "DAW Web Audio API", "Waveform Visualizer", "Professor Feedback", "Cloudflare CDN"]),
            ("Early Childhood Phonics Mobile App", ["Voice Recognition Kit", "Animation Storybook", "Parent Dashboard", "Offline Cache", "Progress Badge"]),
            ("OpenCourseWare Video Streaming Mesh", ["Lecture Video Ingest", "HLS Multi-Bitrate Transcode", "CloudFront CDN", "Subtitle AI Whisper", "Next.js Viewer"]),
            ("Academic Plagiarism & LLM Text Detector", ["Student Essay Upload", "Embedding Cross-Match", "LLM Perplexity Analyzer", "Citation Validator", "Professor Report"]),
            ("Student Mental Wellbeing Support Chat", ["Anonymous Chat Ingest", "Sentiment Triage", "Counselor Matching", "Crisis Escalation", "Confidentiality Vault"])
        ]),
        ("OPERATIONS_LOGISTICS", "Operations & Supply Chain Logistics", [
            ("Autonomous Drone Delivery Fleet Router", ["Order Dispatcher", "Drone Telemetry 4G", "Airspace Conflict Resolver", "Landing Pad Sensor", "Customer Push"]),
            ("Automated Warehouse Robotic Sorting AMR", ["Barcode Scanner Ingest", "Robotic Fleet Kiva", "Sorting Conveyor Belt", "Pick-to-Light System", "ERP SAP WMS"]),
            ("Cold Chain Vaccine IoT Telemetry Pipeline", ["Temperature IoT Probe", "Cellular GPS Tracker", "Spoilage Threat Trigger", "Fleet Dispatcher", "Compliance WORM"]),
            ("Global Container Freight Tracking Port", ["Cargo Manifest XML", "AIS Vessel Satellite", "Port Container Crane", "Customs Broker API", "Shipper Portal"]),
            ("Last-Mile Courier Dynamic Routing Optimizer", ["Package Delivery List", "Traffic Matrix GoogleMaps", "VRP Heuristic Solver", "Driver Mobile App", "Proof of Delivery"]),
            ("Predictive Maintenance Heavy Machinery", ["Vibration IoT Sensor", "Edge FFT Transformer", "ML Failure Predictor", "Maintenance Work Order", "Technician Tablet"]),
            ("Cross-Docking Logistics Hub Real-Time", ["Inbound Truck Dock", "Cross-Dock Conveyor", "Pallet Scan RFID", "Outbound Truck Dock", "Dispatch Ledger"]),
            ("Retail Shelf Out-of-Stock Camera Vision", ["Ceiling Camera Vision", "YOLO Shelf Detector", "Stock Level Alert", "Stockroom Worker Watch", "Inventory DB"]),
            ("Airline Flight Crew Scheduling & Duty Rosters", ["FAA Flight Duty Rules", "Crew Bid Preference", "Genetic Algorithm Solver", "Disruption Re-Scheduler", "Pilot Mobile"]),
            ("City Waste Management Smart Bin Route", ["Ultrasonic Bin Sensor", "Fill-Level Threshold", "Garbage Truck Route", "Driver Navigation", "City Dashboard"]),
            ("Railway Signaling & Train Traffic Control", ["Track Circuit Sensor", "Automatic Train Protection", "Signal Dispatch Desk", "Collision Prevention", "PostgreSQL"]),
            ("Automated Customs Clearance Electronic EDI", ["Import Bill of Lading", "HS Code Classifier", "Tariff Calculation", "Customs Authority API", "Release Stamp"]),
            ("Dark Store Micro-Fulfillment Order Picker", ["10-Min Delivery Order", "Picker Zone Routing", "Bagger Station Check", "Rider Handoff", "Kafka Stream"]),
            ("Fleet Fuel Optimization & Driver Telematics", ["OBD-II Vehicle Tracker", "Speed / Idle Telemetry", "Fuel Card Transaction", "Eco-Score Leaderboard", "Fleet Manager"]),
            ("Supply Chain Traceability Blockchain Ledger", ["Farm Origin Ingest", "Processing Plant Lot", "Cold Transport Scan", "Supermarket QR Stamp", "Immutable Audit"]),
            ("Solar Farm IoT Energy Production Hub", ["Photovoltaic Inverters", "Weather Station Sensor", "Grid Substation Output", "Battery Storage BESS", "Grafana Wall"]),
            ("Water Utility Smart Meter Leak Detection", ["Smart Water Meter AMR", "Acoustic Leak Sensor", "Flow Discrepancy Engine", "Repair Crew Dispatch", "Billing DB"]),
            ("Harbor Tugboat & Pilot Vessel Dispatcher", ["Vessel Arrival Queue", "Tugboat Availability", "Pilot Boarding Assignment", "Tide / Wind Sensor", "Port Authority"]),
            ("Hazardous Material Transport Watchdog", ["Hazmat HazChem Badge", "GPS Geofence Watcher", "Emergency Runbook SRE", "Fire Dept Link", "NOC Monitor"]),
            ("Hotel Automated Linen & Laundry Inventory", ["RFID Linen Tag", "Laundry Tunnel Washer", "Floor Par-Level Monitor", "Housekeeping Cart", "Cost Ledger"])
        ]),
        ("SCIENCE_AEROSPACE", "Science & Aerospace Engineering", [
            ("Orbital Satellite Ground Station Telemetry", ["Parabolic Dish Antenna", "QPSK Demodulator", "Telemetry Telecommand (TM/TC)", "Orbital Propagator", "Flight Director Desk"]),
            ("Astronomical Radio Telescope Interferometer", ["Antenna Array Dish", "Correlator Cluster GPU", "Fourier Transform Pipeline", "FITS File Archive", "Astrophysicist UI"]),
            ("CERN Particle Collision Event Filter", ["LHC Detector Sensor", "Hardware L1 Trigger FPGA", "High-Level Trigger Farm", "ROOT Data Storage", "Scientist Grid"]),
            ("Mars Rover Autonomous Navigation Pipeline", ["Stereo NavCam Vision", "Visual Odometry FPGA", "Hazard Avoidance AI", "Drive Motor Controller", "Earth Deep Space Link"]),
            ("High-Altitude Weather Balloon Telemetry", ["GPS Radiosonde Sensor", "Atmospheric Pressure Probe", "LoRa Radio Transmitter", "Ground Station Receiver", "NOAA Ingest"]),
            ("Hypersonic Wind Tunnel Data Acquisition", ["Piezo Pressure Transducer", "100MHz ADC Digitizer", "Shockwave Schlieren Camera", "HDF5 Raw Storage", "Aerodynamic Model"]),
            ("Fusion Reactor Plasma Magnetic Containment", ["Tokamak Magnetic Coils", "Plasma Interferometer", "Real-Time Plasma Feedback", "Emergency Quench System", "Physics Wall"]),
            ("Quantum Computing Circuit Compiler", ["Qiskit QASM Circuit", "Quantum Gate Optimizer", "Qubit Layout Mapping", "Cryogenic Dilution Fridge", "Quantum Processor"]),
            ("Supercomputer Slurm Job Queue Scheduler", ["User SSH Ingest", "Slurm Master Scheduler", "Infiniband Network Fabric", "Compute Node Cluster", "Lustre Parallel Storage"]),
            ("Earth Observation SAR Satellite Processor", ["Synthetic Aperture Radar", "Doppler Phase Engine", "Terrain Interferometry", "GeoTIFF S3 Bucket", "GIS Analyst Portal"]),
            ("Deep Ocean Submersible ROV Telemetry", ["Sonar Bathymetry", "Acoustic Modem Link", "Hydraulic Robotic Arm", "4K Video Stream", "Research Vessel Bridge"]),
            ("Seismic Earthquake Early Warning Network", ["Seismometer Network", "P-Wave Arrival Detector", "Magnitude Calculation", "Public Siren Alarm", "Geological Survey"]),
            ("CRISPR Gene Editing Laboratory Pipeline", ["Guide RNA Designer", "Cas9 Cleavage Target", "Off-Target Predictor AI", "Sequencing Verification", "Lab LIMS"]),
            ("Atmospheric Carbon LIDAR Sensing Mesh", ["Airborne LIDAR Laser", "Photon Detector Time-of-Flight", "CO2 Concentration Map", "Climate Model Sync", "Science Dashboard"]),
            ("Rocket Launch Vehicle Countdown Controller", ["LOX Fuel Valve Telemetry", "Ignition Squib Sequencer", "Flight Abort Range Safety", "Launch Director Console", "High-Speed Cam"]),
            ("Nanomaterial Electron Microscope Imaging", ["TEM Beam Column", "CCD Camera Sensor", "Atomic Lattice Detector", "Image De-Noiser AI", "Materials Science DB"]),
            ("Particle Accelerator Beam Injection Linac", ["RF Klystron Modulator", "Electron Gun Injector", "Bending Dipole Magnet", "Synchrotron Ring", "Beam Current Monitor"]),
            ("Gravitational Wave Laser Interferometer", ["4km Laser Beam Arm", "Interferometer Photodiode", "Seismic Isolation Mirror", "Matched Filter Pipeline", "Astrophysics Alert"]),
            ("Wildfire Drone Swarm Perimeter Tracker", ["Thermal IR Drone Fleet", "Mesh Radio Relay", "Fire Spread Simulator", "Firefighter Tablet", "Forestry Agency"]),
            ("Biological Tissue 3D Bioprinter Control", ["3D Bio-CAD Slicer", "Hydrogel Syringe Extruder", "Laser Crosslinking UV", "Cell Viability Monitor", "Bio-Engineer UI"])
        ]),
        ("PRODUCT_UX_FLOWS", "Product Design & UX Workflows", [
            ("Mobile Banking Biometric Onboarding KYC", ["Document Scan OCR", "Liveness Facial Match", "Blacklist Sanction Check", "Account Creation Ledger", "Welcome Screen"]),
            ("E-Commerce Multi-Step Checkout Funnel", ["Shopping Cart", "Shipping Address Form", "Payment Method Card/PIX", "3DSecure Verification", "Order Confirmed Hero"]),
            ("SaaS User Invitation & RBAC Onboarding", ["Admin Invite Email", "Magic Link Verification", "Role Selection (Admin/Dev/Viewer)", "Workspace Setup", "App Dashboard"]),
            ("Design System Figma Token Sync Workflow", ["Figma Token JSON", "GitHub Action Action", "Style Dictionary Build", "NPM Package Publish", "React Storybook"]),
            ("Customer Support Live Chat Escalation", ["Web Chat Widget", "AI Bot Intent Match", "Human Agent Desk", "Screen Sharing Tool", "CSAT Rating Form"]),
            ("Subscription Upgrade & Downgrade Modal", ["Current Plan Review", "Feature Comparison Grid", "Proration Calculation", "Stripe Charge Update", "Success Banner"]),
            ("User Account Password Reset & 2FA Flow", ["Forgot Password Request", "SMS OTP Generator", "TOTP Authenticator", "Password Strength Rule", "Session Token"]),
            ("Social Network Feed Infinite Scroll Feed", ["Client Viewport Trigger", "GraphQL Feed Query", "Cursor Pagination Redis", "Image CDN Optimization", "DOM Virtualizer"]),
            ("E-Signature Contract Signing Document", ["PDF Contract Upload", "Signature Field Placement", "Signer Email Dispatch", "Crypto Signature Stamp", "Audit Certificate"]),
            ("Podcast Audio Creator Studio Upload", ["Audio MP3 Dropzone", "Audio Waveform Normalizer", "ID3 Tag & Cover Art", "RSS Feed XML Update", "Spotify Apple Sync"]),
            ("Bug Reporting & Session Replay Widget", ["User Feedback Button", "DOM Snapshot Replay", "Console Error Logger", "Jira Ticket Creator", "Sentry Alert"]),
            ("Marketplace Merchant Storefront Customizer", ["Theme Color Picker", "Drag-Drop Banner Grid", "Product Showcase Carousel", "Live Mobile Preview", "Publish CDN"]),
            ("Travel Booking Flight + Hotel Multi-Cart", ["Flight Search Matrix", "Hotel Room Selector", "Insurance Add-On Modal", "Consolidated Payment", "E-Ticket Wallet"]),
            ("Interactive Product Tour & Onboarding Guide", ["Welcome Modal Dialog", "Spotlight Element Tooltip", "Next Step Indicator", "Completion Checklist", "Confetti Animation"]),
            ("Multi-Language Localization i18n Switcher", ["Language Dropdown", "Crowdin Translation Memory", "RTL Direction Adapter", "Date/Currency Formatter", "Cached Bundle"]),
            ("Job Application Resume Parsing ATS Flow", ["Resume PDF Dropzone", "OpenAI Skill Extractor", "Applicant Scoreboard", "Recruiter Calendar Sync", "Email Trigger"]),
            ("Dark Mode / Light Mode Theme Switching", ["System Preference Hook", "CSS Token Switcher", "Canvas Background Adjust", "Local Storage Persist", "Transition Fade"]),
            ("User Privacy GDPR Cookie Consent Banner", ["Geo-IP Location Check", "Granular Cookie Categories", "Consent Ledger DB", "Google Tag Manager", "Save Preferences"]),
            ("Survey NPS Net Promoter Score Modal", ["Trigger Time Delay", "1-10 Rating Scale", "Qualitative Text Feedback", "Sentiment Categorizer", "Product Team Slack"]),
            ("Mobile App Push Notification Preference", ["Category Toggle List", "Quiet Hours Selector", "APNS/FCM Token Register", "Preferences DynamoDB", "Saved Toast"])
        ])
    ]

    for dom_code, dom_name, prompt_tuples in domains:
        for idx, (title, hints) in enumerate(prompt_tuples):
            p_id = f"HLD-{dom_code[:4]}-{idx+1:02d}"
            p_text = f"Diseña la arquitectura técnica de {title} con alta disponibilidad, resiliencia, observabilidad y seguridad."
            entities = [{"label": h, "role": "service" if "DB" not in h and "Kafka" not in h else ("database" if "DB" in h else "stream")} for h in hints]
            prompts.append(HoldoutPrompt(
                id=p_id,
                domain=dom_name,
                title=title,
                prompt_text=p_text,
                complexity="HIGH",
                expected_entities=entities
            ))

    return prompts
