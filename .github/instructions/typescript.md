# Generic TypeScript/React Development Instructions

## Testing-First Development Workflow

- **Always run tests before completing tasks.**
- Write tests before implementing new features.
- Ensure all tests pass after refactoring.
- Never skip testing—tests are fast and catch errors early.

### Test-Driven Development (TDD) Process

1. Write a failing test first (e.g., `src/[feature].test.ts(x)`).
2. Run tests to see it fail: `npm test`.
3. Implement the minimum code to pass.
4. Run tests to verify.
5. Refactor with confidence, keeping tests running in watch mode.

### Refactoring Cycle

1. Write tests for existing behavior.
2. Extract utilities to `utils/` as pure functions.
3. Write comprehensive unit tests for utilities.
4. Update components to use utilities.
5. Verify no regressions with tests and manual checks.

### Bug Fixes

1. Write a test that reproduces the bug.
2. Fix the bug.
3. Verify the fix with tests.

## Testing Commands

```bash
npm test                # Run all tests once
npm test -- --watch     # Watch mode
npm test -- --coverage  # Coverage report
npm test -- src/utils/expirationUtils.test.ts  # Specific file
npm test -- -t "should calculate days to expiration"  # Pattern
```

## Test File Organization

- Place pure utility function tests in `utils/*.test.ts`.
- Place component smoke tests in `pages/*.test.tsx`.
- Use `tests/setup.ts` for global test setup.

## Code Organization Principles

- Extract business logic into pure utility functions in `utils/`.
- Keep React components focused on rendering and state.
- Test pure functions in isolation (unit tests).
- Use smoke/component tests for React components.

## Testing Strategy

1. **Unit Tests**: Test pure functions, fast and isolated.
2. **Component Smoke Tests**: Ensure components render and basic interactions work.
3. **Integration Tests**: (Optional/future) Test full data flow and API integration.

## Common Patterns

- Validate input in utility functions.
- Handle edge cases and invalid data.
- Use strong typing for grouped/aggregated data.
- Use React Testing Library for component tests.
- Prefer semantic queries and async handling in tests.

## Troubleshooting

- Use verbose reporters for failing tests.
- Ensure import paths are correct and relative.
- Ignore act() warnings unless they indicate real issues.
- Ensure test files are named correctly and in the right directory.

## Development Workflow

1. Start test watcher: `npm test -- --watch`
2. Start dev server: `npm run dev`
3. Make code changes; tests and browser auto-refresh.
4. Before committing: run all tests and build for production.

## Linting

- Use ESLint for code quality: `npm run lint`
- Auto-fix issues: `npm run lint -- --fix`

## Best Practices

- Use TypeScript strict mode if possible.
- Add JSDoc comments to utilities.
- Document testing patterns and examples.
- Keep code and tests clean, focused, and maintainable.

---

