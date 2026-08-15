# Phase 16 — AI ERP

## Description
Intelligent automation.

## Phase Scope
AI assistant, search, insights, forecasting, anomaly detection and governed agents.

## Features In This Phase
- 16.01 AI architecture
- 16.02 AI assistant/search
- 16.03 AI insights/reports
- 16.04 Domain assistants
- 16.05 OCR/translation
- 16.06 Forecast/anomaly/fraud/risk
- 16.07 AI agents/automation
- 16.08 AI governance/audit/cost

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
