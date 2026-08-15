# Architecture Gate

## Description
Review the current architecture before business-module implementation.

## Steps
1. Read the master rule.
2. Read PROJECT_STATE.md.
3. Inspect architecture documents available in the repository.
4. Check product, SaaS, multi-tenant, hierarchy, user, RBAC, database, API, security and UI boundaries.
5. Identify contradictions, missing dependencies, duplicate responsibilities and scalability risks.
6. Validate tenant isolation design.
7. Validate role/permission boundaries.
8. Validate database ownership and API ownership.
9. Validate module boundaries and dependency direction.
10. Produce `docs/development/ARCHITECTURE_GATE_REPORT.md`.
11. Do not implement business modules during this workflow.
12. Mark the architecture gate PASS only when critical blockers are resolved or explicitly risk-accepted.
