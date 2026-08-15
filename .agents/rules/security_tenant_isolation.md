# Security & Tenant Isolation Rule

Always enforce:
- tenant context on every tenant-scoped request
- backend authorization
- resource-level permission checks
- row/data scope validation
- audit logging for sensitive mutations
- secure document access
- secure secrets handling
- safe error messages
- input validation
- rate limiting where appropriate
- no cross-tenant cache keys
- no cross-tenant storage paths
- no cross-tenant analytics or AI retrieval

For every data query ask:
1. What tenant owns this record?
2. What society/building/unit scope applies?
3. What role/permission allows this action?
4. Should this event be audited?
5. Could the response reveal another tenant's data?

Never bypass these checks for UI convenience or development shortcuts.
