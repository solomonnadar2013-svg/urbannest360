# Flutter Architecture Rule

Use:
- Flutter
- Dart
- Material 3
- Riverpod
- GoRouter
- Clean Architecture
- Feature-First modular structure

Prefer:
Presentation → Application/Use Cases → Domain → Data/Repositories/Services.

Requirements:
- Responsive desktop/tablet/mobile layouts
- Reusable Material 3 components
- Centralized routing
- Typed state management
- Form validation
- Loading/error/empty/offline states
- Accessibility
- No business authorization logic only in widgets
- No direct database access from UI
- Testable providers and repositories

Do not create duplicate models or services when an existing shared abstraction is appropriate.
