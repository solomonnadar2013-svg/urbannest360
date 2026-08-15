# Phase 08 — Core ERP

## Description
Apartment operations.

## Phase Scope
Society, resident, tenant, visitor, maintenance, facility, vendor and operational modules.

## Features In This Phase
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
