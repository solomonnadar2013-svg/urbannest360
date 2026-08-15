# Multi-Apartment ERP — Phase Index

## 01. Master Project
- Objective: Establish global rules
- Workflow: `.agents/workflows/01_01_Master_Project.md`
- Features:
  - 01.01 Global project context
  - 01.02 Technology baseline
  - 01.03 Architecture principles
  - 01.04 Development governance
  - 01.05 Definition of done

## 02. Requirements
- Objective: Freeze requirements
- Workflow: `.agents/workflows/02_02_Requirements.md`
- Features:
  - 02.01 Product vision and scope
  - 02.02 User personas and journeys
  - 02.03 Functional requirements
  - 02.04 Non-functional requirements
  - 02.05 Requirements traceability

## 03. SaaS Architecture
- Objective: Multi-tenancy
- Workflow: `.agents/workflows/03_03_SaaS_Architecture.md`
- Features:
  - 03.01 SaaS control plane
  - 03.02 Tenant lifecycle
  - 03.03 Tenant resolution/context
  - 03.04 Isolation architecture
  - 03.05 Tenant isolation tests

## 04. Society Hierarchy
- Objective: Apartment structure
- Workflow: `.agents/workflows/04_04_Society_Hierarchy.md`
- Features:
  - 04.01 Society model
  - 04.02 Building/Wing/Block model
  - 04.03 Floor and Unit model
  - 04.04 Ownership/occupancy/tenancy
  - 04.05 Hierarchy validation

## 05. Authentication RBAC
- Objective: Identity & access
- Workflow: `.agents/workflows/05_05_Authentication_RBAC.md`
- Features:
  - 05.01 Authentication
  - 05.02 User membership
  - 05.03 Role hierarchy
  - 05.04 Permission model
  - 05.05 RBAC enforcement
  - 05.06 Access lifecycle

## 06. Database
- Objective: PostgreSQL/Prisma
- Workflow: `.agents/workflows/06_06_Database.md`
- Features:
  - 06.01 Core tenant/society schema
  - 06.02 User/RBAC schema
  - 06.03 Resident/tenant schema
  - 06.04 Operations schema
  - 06.05 Finance schema
  - 06.06 Audit/document/notification schema
  - 06.07 Prisma migrations and indexes

## 07. UI UX
- Objective: Global design system
- Workflow: `.agents/workflows/07_07_UI_UX.md`
- Features:
  - 07.01 Design tokens
  - 07.02 App shell/navigation
  - 07.03 Dashboard components
  - 07.04 Forms/tables/search
  - 07.05 Responsive states
  - 07.06 Accessibility

## 08. Core ERP
- Objective: Apartment operations
- Workflow: `.agents/workflows/08_08_Core_ERP.md`
- Features:
  - 08.01 Society management
  - 08.02 Owner/resident/household
  - 08.03 Renter/tenant
  - 08.04 Vehicles/parking
  - 08.05 Visitor/security requests
  - 08.06 Maintenance/work orders
  - 08.07 Assets/inventory
  - 08.08 Facilities/booking
  - 08.09 Vendors/staff
  - 08.10 Complaints/community

## 09. Accounting Billing
- Objective: Billing & finance
- Workflow: `.agents/workflows/09_09_Accounting_Billing.md`
- Features:
  - 09.01 Financial setup
  - 09.02 Chart of accounts
  - 09.03 Maintenance billing
  - 09.04 Invoice/receipt
  - 09.05 Payments/collections
  - 09.06 Expenses/payables
  - 09.07 Bank/reconciliation
  - 09.08 Funds/budget
  - 09.09 GST/TDS/tax
  - 09.10 Financial reports/audit

## 10. Security Operations
- Objective: Gate/security
- Workflow: `.agents/workflows/10_10_Security_Operations.md`
- Features:
  - 10.01 Gate management
  - 10.02 Guard management
  - 10.03 Visitor management
  - 10.04 Delivery/vehicle verification
  - 10.05 Patrol/incidents
  - 10.06 Emergency/lost-found
  - 10.07 Security reports/audit

## 11. Workflow Approval
- Objective: Approvals
- Workflow: `.agents/workflows/11_11_Workflow_Approval.md`
- Features:
  - 11.01 Workflow definitions
  - 11.02 States/transitions
  - 11.03 Approval levels/limits
  - 11.04 Maker-checker
  - 11.05 Delegation/escalation
  - 11.06 Decision history

## 12. Notifications
- Objective: Communication
- Workflow: `.agents/workflows/12_12_Notifications.md`
- Features:
  - 12.01 Notification architecture
  - 12.02 Templates/variables
  - 12.03 Push/email/SMS
  - 12.04 WhatsApp/in-app
  - 12.05 Preferences/scheduling
  - 12.06 Delivery/retry/analytics

## 13. Documents
- Objective: Files & records
- Workflow: `.agents/workflows/13_13_Documents.md`
- Features:
  - 13.01 Storage architecture
  - 13.02 Upload/metadata
  - 13.03 Verification/approval
  - 13.04 Versioning/expiry
  - 13.05 Access/sharing
  - 13.06 Retention/archive/audit

## 14. Audit Compliance
- Objective: Accountability
- Workflow: `.agents/workflows/14_14_Audit_Compliance.md`
- Features:
  - 14.01 Audit event model
  - 14.02 Activity/auth/access logs
  - 14.03 Financial/operations/security audit
  - 14.04 Investigation/evidence
  - 14.05 Findings/corrective actions
  - 14.06 Retention/export/reporting

## 15. Analytics Reporting
- Objective: Reports/KPIs
- Workflow: `.agents/workflows/15_15_Analytics_Reporting.md`
- Features:
  - 15.01 Reporting architecture
  - 15.02 Operational dashboards
  - 15.03 Financial/collection analytics
  - 15.04 Maintenance/security analytics
  - 15.05 KPI/comparison/drilldown
  - 15.06 Export/scheduled reports
  - 15.07 BigQuery analytics

## 16. AI ERP
- Objective: Intelligent automation
- Workflow: `.agents/workflows/16_16_AI_ERP.md`
- Features:
  - 16.01 AI architecture
  - 16.02 AI assistant/search
  - 16.03 AI insights/reports
  - 16.04 Domain assistants
  - 16.05 OCR/translation
  - 16.06 Forecast/anomaly/fraud/risk
  - 16.07 AI agents/automation
  - 16.08 AI governance/audit/cost

## 17. SaaS Admin White Label
- Objective: Subscription/white-label
- Workflow: `.agents/workflows/17_17_SaaS_Admin_White_Label.md`
- Features:
  - 17.01 SaaS tenant administration
  - 17.02 Plans/subscriptions
  - 17.03 Feature flags/usage limits
  - 17.04 Custom domains/DNS/SSL
  - 17.05 White-label branding
  - 17.06 SaaS billing/support

## 18. API Integrations
- Objective: Integrations
- Workflow: `.agents/workflows/18_18_API_Integrations.md`
- Features:
  - 18.01 API architecture
  - 18.02 Authentication/authorization APIs
  - 18.03 Core ERP APIs
  - 18.04 Financial APIs
  - 18.05 Webhooks/API keys
  - 18.06 External provider adapters
  - 18.07 API monitoring/versioning

## 19. Cybersecurity
- Objective: Defense in depth
- Workflow: `.agents/workflows/19_19_Cybersecurity.md`
- Features:
  - 19.01 Threat model
  - 19.02 Identity/API/database security
  - 19.03 Encryption/secrets
  - 19.04 Threat/vulnerability management
  - 19.05 Incident response
  - 19.06 Privacy/PII/third-party security

## 20. Backup DR
- Objective: Business continuity
- Workflow: `.agents/workflows/20_20_Backup_DR.md`
- Features:
  - 20.01 Backup architecture
  - 20.02 Database/file backup
  - 20.03 Restore workflows
  - 20.04 Tenant restore
  - 20.05 Disaster recovery
  - 20.06 Business continuity/drills

## 21. DevOps Cloud
- Objective: Cloud deployment
- Workflow: `.agents/workflows/21_21_DevOps_Cloud.md`
- Features:
  - 21.01 Repository/branching
  - 21.02 Docker
  - 21.03 GitHub Actions
  - 21.04 Terraform/GCP
  - 21.05 CI/CD environments
  - 21.06 Monitoring/logging/alerts

## 22. Version Control
- Objective: Releases
- Workflow: `.agents/workflows/22_22_Version_Control.md`
- Features:
  - 22.01 Application/module versions
  - 22.02 Git/release branches
  - 22.03 API/database migrations
  - 22.04 Release approval
  - 22.05 Tenant upgrades
  - 22.06 Rollback/deprecation

## 23. Testing Quality
- Objective: Quality
- Workflow: `.agents/workflows/23_23_Testing_Quality.md`
- Features:
  - 23.01 Flutter tests
  - 23.02 Backend/API tests
  - 23.03 Database tests
  - 23.04 RBAC/tenant isolation tests
  - 23.05 Security tests
  - 23.06 Performance tests
  - 23.07 UAT/regression

## 24. Scalability Performance
- Objective: 5,000+ societies
- Workflow: `.agents/workflows/24_24_Scalability_Performance.md`
- Features:
  - 24.01 Capacity model
  - 24.02 Database performance
  - 24.03 API scaling
  - 24.04 Redis/cache
  - 24.05 Background jobs/queues
  - 24.06 SLOs/observability
  - 24.07 5,000+ society load validation

## 25. Final Integration GoLive
- Objective: Production go-live
- Workflow: `.agents/workflows/25_25_Final_Integration_GoLive.md`
- Features:
  - 25.01 Architecture audit
  - 25.02 Security/RBAC/tenant audit
  - 25.03 Data/API/UI audit
  - 25.04 Production readiness
  - 25.05 Go-live
  - 25.06 Rollback/DR drill
  - 25.07 Operations/support handover

