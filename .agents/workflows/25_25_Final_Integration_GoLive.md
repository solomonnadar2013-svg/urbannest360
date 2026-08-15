# Phase 25 — Final Integration GoLive

## Description
Production go-live.

## Phase Scope
Final audit, production readiness, go-live, rollback and support.

## Features In This Phase
- 25.01 Architecture audit
- 25.02 Security/RBAC/tenant audit
- 25.03 Data/API/UI audit
- 25.04 Production readiness
- 25.05 Go-live
- 25.06 Rollback/DR drill
- 25.07 Operations/support handover

## Required Execution
1. Read `.agents/rules/multi_apartment_erp_master.md`.
2. Read `.agents/rules/security_tenant_isolation.md`.
3. Read `docs/development/PROJECT_STATE.md`.
4. Inspect the existing repository before changing anything.
5. Identify the current feature within this phase from PROJECT_STATE.md.
6. Implement only one feature per invocation.
7. Preserve existing architecture and completed features.
8. Apply database, backend, API, Flutter/UI, RBAC, tenant isolation, audit, notification and workflow requirements relevant to the feature.
9. Write/update tests for the feature.
10. Run `/validate-feature`.
11. If validation passes, run `/freeze-feature`.
12. If validation fails, fix current-feature issues and validate again.
13. Do not automatically jump over incomplete dependencies.
14. Do not silently modify unrelated modules.

## Phase-Specific Acceptance
The phase must ultimately satisfy:
- Functional requirements for all listed features
- Correct database/API/UI integration
- Role and permission enforcement
- Tenant isolation
- Auditability
- Error handling
- Automated tests
- Documentation
- Performance/security considerations

## Phase Completion
A phase is complete only when every listed feature is validated and PROJECT_STATE.md records the phase as COMPLETED.

## Next Phase
After this phase is completely frozen, proceed to the next numbered phase only through PROJECT_STATE.md.
