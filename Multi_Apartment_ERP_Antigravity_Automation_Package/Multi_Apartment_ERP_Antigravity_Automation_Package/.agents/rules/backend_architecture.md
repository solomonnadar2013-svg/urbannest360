# Backend Architecture Rule

Use NestJS + TypeScript + REST/OpenAPI + PostgreSQL/Prisma + Redis.

Keep:
Controller → Application/Use Case → Domain → Repository/Infrastructure.

Requirements:
- DTO validation
- authentication middleware/guards
- tenant context
- authorization guards/policies
- transactions
- idempotency for retryable financial operations
- pagination/filtering/sorting
- structured errors
- correlation/request IDs
- audit events
- OpenAPI documentation
- secure logging
- automated tests

Never put critical business rules only in controllers or Flutter.
