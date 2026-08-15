# Run ERP Development Cycle

## Description
Drive the Multi-Apartment ERP one feature at a time using PROJECT_STATE.md. This workflow is intentionally conservative: it never skips dependencies and never implements multiple business features in one invocation.

## Steps
1. Read `docs/development/PROJECT_STATE.md`.
2. Determine the current phase.
3. Call the matching phase workflow:
   - 01 → `/01_Master_Project`
   - 02 → `/02_Requirements`
   - 03 → `/03_SaaS_Architecture`
   - 04 → `/04_Society_Hierarchy`
   - 05 → `/05_Authentication_RBAC`
   - 06 → `/06_Database`
   - 07 → `/07_UI_UX`
   - 08 → `/08_Core_ERP`
   - 09 → `/09_Accounting_Billing`
   - 10 → `/10_Security_Operations`
   - 11 → `/11_Workflow_Approval`
   - 12 → `/12_Notifications`
   - 13 → `/13_Documents`
   - 14 → `/14_Audit_Compliance`
   - 15 → `/15_Analytics_Reporting`
   - 16 → `/16_AI_ERP`
   - 17 → `/17_SaaS_Admin_White_Label`
   - 18 → `/18_API_Integrations`
   - 19 → `/19_Cybersecurity`
   - 20 → `/20_Backup_DR`
   - 21 → `/21_DevOps_Cloud`
   - 22 → `/22_Version_Control`
   - 23 → `/23_Testing_Quality`
   - 24 → `/24_Scalability_Performance`
   - 25 → `/25_Final_Integration_GoLive`
4. The called phase workflow must implement only the single feature specified by PROJECT_STATE.md.
5. Validation and freeze are mandatory.
6. Stop after one feature is completed.
7. Read PROJECT_STATE.md again and report the next feature.

## Safety
This workflow is intentionally one-feature-per-run. Do not loop through the entire ERP automatically.
