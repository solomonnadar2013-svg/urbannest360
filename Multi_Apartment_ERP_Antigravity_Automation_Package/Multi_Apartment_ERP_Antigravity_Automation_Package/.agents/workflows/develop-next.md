# Develop Next ERP Feature

## Description
Autonomously implement exactly one approved feature at a time from PROJECT_STATE.md, then validate and freeze it.

## Steps
1. Read `.agents/rules/multi_apartment_erp_master.md`.
2. Read `.agents/rules/security_tenant_isolation.md`.
3. Read `docs/development/PROJECT_STATE.md`.
4. Determine the current phase and feature.
5. Read the corresponding phase workflow under `.agents/workflows/`.
6. Inspect the existing repository and identify the actual current implementation state.
7. Check dependencies. If a required dependency is incomplete or contradictory, STOP and report it. Do not guess.
8. Create a concise implementation plan for the single current feature.
9. Implement only the current feature and its strictly necessary dependencies.
10. Update database, backend, API, Flutter/UI, RBAC, tenant isolation, audit, notifications and workflow pieces required by the feature.
11. Do not implement the next feature in the same run.
12. Run relevant tests and static checks.
13. Call `/validate-feature`.
14. If validation passes, call `/freeze-feature`.
15. If validation fails, fix only current-feature issues and repeat validation.
16. If a critical blocker cannot be safely resolved, STOP without marking completion.
17. End with:
   - implemented feature
   - files changed
   - tests run
   - validation result
   - state update
   - next feature

## Safety
Never skip validation.
Never bypass authorization.
Never bypass tenant isolation.
Never modify completed features without a documented dependency/migration.
Never claim completion if acceptance criteria are not met.
