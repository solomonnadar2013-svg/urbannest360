# Validate Feature

## Description
Validate the currently implemented feature against the Multi-Apartment ERP master rules before it can be marked complete.

## Steps
1. Read `docs/development/PROJECT_STATE.md`.
2. Identify the current phase and feature.
3. Read the relevant phase workflow and source specification.
4. Inspect all files changed for the current feature.
5. Validate requirements and acceptance criteria.
6. Validate database schema, migrations, constraints and indexes.
7. Validate backend/domain/application logic.
8. Validate API contracts, authorization, validation, pagination and error handling.
9. Validate Flutter UI/state/navigation and responsive behavior.
10. Validate RBAC and resource-level authorization.
11. Validate tenant isolation across database, API, cache, storage, notifications, analytics and AI where applicable.
12. Validate audit events for sensitive actions.
13. Validate notifications/workflows where applicable.
14. Run relevant unit, widget, integration, API and database tests.
15. Run security and tenant-isolation tests for the feature.
16. Run lint/format/type checks relevant to changed code.
17. Fix failures caused by the current feature. Do not rewrite unrelated modules.
18. Re-run validation after fixes.
19. Produce a concise validation report with PASS/FAIL for each area.
20. If any critical blocker remains, do not mark the feature complete.

## Completion Criteria
A feature is VALIDATED only when all critical checks pass and there are no unresolved tenant-isolation, authorization, data-integrity or security blockers.
