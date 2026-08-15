# AI Governance Rule

AI features must:
- respect tenant isolation
- respect user/role/resource permissions
- use approved data sources
- avoid exposing secrets or private data
- log important AI requests/actions
- use human approval for sensitive actions
- never execute financial, permission, deletion or security overrides without configured authorization
- provide traceable tool/action context where applicable
- support cost/model/provider governance
- fail safely when authorization or context is uncertain
