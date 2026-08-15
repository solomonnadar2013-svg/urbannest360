# Freeze Feature

## Description
Freeze the current feature only after successful validation.

## Steps
1. Read `docs/development/PROJECT_STATE.md`.
2. Confirm the current feature was successfully validated.
3. If validation failed, STOP and report the blockers.
4. Review changed files and ensure no unrelated changes are included.
5. Record:
   - feature ID
   - completion date
   - validation result
   - tests executed
   - migrations
   - security/RBAC result
   - tenant-isolation result
   - known non-critical risks
6. Update `docs/development/PROJECT_STATE.md`:
   - mark the current feature COMPLETED
   - identify the next feature
   - update phase status if the phase is complete
7. Do not modify completed features unless a later dependency requires a documented migration.
8. Generate a completion summary.

## Completion Criteria
The state file accurately reflects the completed feature and next approved task.
