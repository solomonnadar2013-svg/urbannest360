# Multi-Apartment ERP — Antigravity Automation Package

## What this package does

This package turns the 25-phase ERP blueprint into a controlled, one-feature-at-a-time development workflow.

The design uses:
- Workspace Rules in `.agents/rules`
- Workflows in `.agents/workflows`
- Persistent development state in `docs/development/PROJECT_STATE.md`
- Validation workflow
- Freeze workflow
- Architecture gate
- Bootstrap workflow
- 25 phase workflows
- One master development-cycle workflow

Antigravity workspace rules and workflows are supported in `.agents/rules` and `.agents/workflows`; workflows can be invoked as slash commands. Keep each rule/workflow within Antigravity's documented 12,000-character limit. See the official documentation: https://antigravity.google/docs/rules-workflows

## Recommended installation

1. Extract this package into the root of your ERP repository.
2. Merge `.agents/` into your existing `.agents/` folder if one already exists.
3. Merge `docs/development/` into your existing documentation folder.
4. Review `PROJECT_STATE.md`.
5. Do NOT automatically allow destructive commands.
6. Open the repository in Antigravity.
7. Confirm the workspace rules are loaded.
8. Start with `/bootstrap-project`.
9. Then run `/architecture-gate`.
10. After the architecture gate passes, use `/develop-next` or `/run-erp-development-cycle`.

## Main slash commands

- `/bootstrap-project` — prepare/inspect the repository
- `/architecture-gate` — validate architecture before business implementation
- `/develop-next` — implement exactly one current feature, validate, freeze
- `/validate-feature` — validate current feature
- `/freeze-feature` — freeze current feature
- `/run-erp-development-cycle` — route to the current phase and execute one feature

## 25 Phase Commands

- `/01_01_Master_Project` — Phase 01: Master Project
- `/02_02_Requirements` — Phase 02: Requirements
- `/03_03_SaaS_Architecture` — Phase 03: SaaS Architecture
- `/04_04_Society_Hierarchy` — Phase 04: Society Hierarchy
- `/05_05_Authentication_RBAC` — Phase 05: Authentication RBAC
- `/06_06_Database` — Phase 06: Database
- `/07_07_UI_UX` — Phase 07: UI UX
- `/08_08_Core_ERP` — Phase 08: Core ERP
- `/09_09_Accounting_Billing` — Phase 09: Accounting Billing
- `/10_10_Security_Operations` — Phase 10: Security Operations
- `/11_11_Workflow_Approval` — Phase 11: Workflow Approval
- `/12_12_Notifications` — Phase 12: Notifications
- `/13_13_Documents` — Phase 13: Documents
- `/14_14_Audit_Compliance` — Phase 14: Audit Compliance
- `/15_15_Analytics_Reporting` — Phase 15: Analytics Reporting
- `/16_16_AI_ERP` — Phase 16: AI ERP
- `/17_17_SaaS_Admin_White_Label` — Phase 17: SaaS Admin White Label
- `/18_18_API_Integrations` — Phase 18: API Integrations
- `/19_19_Cybersecurity` — Phase 19: Cybersecurity
- `/20_20_Backup_DR` — Phase 20: Backup DR
- `/21_21_DevOps_Cloud` — Phase 21: DevOps Cloud
- `/22_22_Version_Control` — Phase 22: Version Control
- `/23_23_Testing_Quality` — Phase 23: Testing Quality
- `/24_24_Scalability_Performance` — Phase 24: Scalability Performance
- `/25_25_Final_Integration_GoLive` — Phase 25: Final Integration GoLive

## One-by-one automation model

```text
PROJECT_STATE.md
      ↓
Current Phase / Feature
      ↓
Phase Workflow
      ↓
Inspect Dependencies
      ↓
Plan
      ↓
Implement ONE Feature
      ↓
/validate-feature
      ↓
PASS?
 ┌────┴────┐
 NO        YES
 ↓          ↓
Fix      /freeze-feature
            ↓
      Update PROJECT_STATE.md
            ↓
         Next Feature
```

## Important rule

Do not give the AI the entire 25-phase implementation as one coding request.

Use the master architecture as context, then let the state-driven workflow implement one feature at a time.

## Suggested first commands

```text
/bootstrap-project
/architecture-gate
/develop-next
```

After a successful feature freeze:

```text
/develop-next
```

Run it again for the next feature.

## Major-phase approval

For these phases, require human review before proceeding:
- Multi-tenancy
- Authentication/RBAC
- Database
- Accounting
- Cybersecurity
- Backup/DR
- DevOps/Production
- Final Go-Live

## State file

`docs/development/PROJECT_STATE.md` is the source of truth for:
- current phase
- current feature
- completed features
- blockers
- next feature
- protected completed work

Do not mark work complete without validation.

## Permission safety

Antigravity's permission engine supports Deny > Ask > Allow precedence. Keep destructive operations such as production database mutation, secret access, destructive shell commands and production deployment under explicit approval.

## Source

This package is based on the user's Multi-Apartment ERP SaaS master requirements and the 25-phase build sequence.
