# Bootstrap ERP Project

## Description
Prepare a new or existing repository for the Multi-Apartment ERP development workflow without implementing business modules.

## Steps
1. Read the master rules and PROJECT_STATE.md.
2. Inspect the repository structure, Git status, Flutter setup, backend setup and infrastructure setup.
3. Detect whether the project is new or existing.
4. Do not delete or overwrite existing project code.
5. Establish the required folder/module boundaries.
6. Create or validate documentation locations.
7. Validate Flutter/Dart, NestJS/TypeScript, PostgreSQL/Prisma and required tooling.
8. Create baseline configuration only where missing.
9. Run baseline lint/build/test checks.
10. Record all findings in `docs/development/BOOTSTRAP_REPORT.md`.
11. Update PROJECT_STATE.md only to reflect verified facts.
12. Do not begin Phase 02 until Phase 01 acceptance criteria are satisfied.

## Safety
No destructive commands.
No production deployment.
No database destructive reset.
No secret generation in source control.
