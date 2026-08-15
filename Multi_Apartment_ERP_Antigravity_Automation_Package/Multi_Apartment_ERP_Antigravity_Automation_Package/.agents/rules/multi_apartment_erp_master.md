# Multi-Apartment ERP — Master Development Rule

## Purpose
These are non-negotiable engineering rules for the Multi-Apartment ERP SaaS project.

## Product Scope
Build a production-ready, multi-tenant apartment/society ERP SaaS supporting 5,000+ societies/apartment organizations and unlimited tenants.

## Technology Baseline
- Flutter + Dart + Material 3 + Riverpod + GoRouter
- Clean Architecture + Feature-First Modular Architecture
- NestJS + TypeScript + REST/OpenAPI
- PostgreSQL + Prisma
- Redis
- Firebase Authentication / Google Cloud Identity Platform
- Firebase Cloud Messaging
- Google Cloud Storage
- Google Cloud Run
- Cloud Functions / Cloud Run Jobs
- Cloud Scheduler
- Google Secret Manager
- Cloud Logging + Cloud Monitoring + Error Reporting
- Git + GitHub + GitHub Actions + Docker + Terraform
- PostgreSQL operational reporting + BigQuery advanced analytics

## Architecture Rules
1. Backend business rules are authoritative.
2. UI visibility is never a security boundary.
3. Every tenant-scoped operation must carry and validate tenant context.
4. Never permit cross-tenant data access, cache access, file access, notifications, analytics or AI retrieval.
5. Use modular feature boundaries and avoid duplicated business logic.
6. Preserve backward compatibility unless a documented migration is approved.
7. Do not modify unrelated completed features.
8. Do not silently remove requested functionality.
9. Prefer explicit, testable abstractions over hidden magic.
10. Keep database migrations reversible where practical and document irreversible changes.

## Security Rules
1. Least privilege is mandatory.
2. Enforce authorization server-side.
3. Validate tenant, society, building/unit and resource scope.
4. Sensitive actions require appropriate permission and audit logging.
5. Financial actions must respect separation of duties.
6. Never expose secrets, credentials, private keys or tokens in source code or logs.
7. Never disable security checks just to make tests pass.
8. Treat uploaded documents and external input as untrusted.
9. Do not weaken production security for convenience.

## Role Separation
- Super Admin → SaaS platform administration
- Local Admin → assigned society administration
- Society Manager → operational execution
- Accountant → prepare/record financial transactions
- Treasurer → financial review/approval
- Committee → governance/major decisions
- Auditor → independent review/audit
- Resident → own/unit-authorized services
- Renter/Tenant → tenancy- and permission-scoped services
- Vendor → assigned work/vendor operations
- Staff → assigned operational work
- Security → assigned security operations

## Required Validation for Every Feature
- Requirements
- Architecture
- Database
- Backend/service
- API
- Flutter/UI
- RBAC
- Tenant isolation
- Audit
- Notifications/workflow where applicable
- Error handling
- Automated tests
- Security review
- Performance considerations

## Working Rules
1. Read PROJECT_STATE.md before starting.
2. Read the relevant phase specification before coding.
3. Inspect the existing repository before creating files.
4. Reuse existing abstractions when appropriate.
5. Do not overwrite working code blindly.
6. Keep changes focused on the current feature.
7. Run the smallest relevant test suite first, then broader tests.
8. Update PROJECT_STATE.md only after validation.
9. If a dependency is missing, STOP and report it.
10. If requirements conflict, STOP and report the conflict instead of guessing.

## Completion
A feature is complete only when its acceptance criteria pass and the validation workflow reports no critical blocker.

## Production Rule
Never claim production-ready while critical security, tenant-isolation, data-integrity, migration, reliability or test gaps remain.
