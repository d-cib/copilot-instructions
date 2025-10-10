# JavaScript/Node.js Copilot Instructions (Example: yarn + Jest + Prettier + ESLint + TypeScript + Both)

## JavaScript/Node.js Copilot Instructions

You are an expert JavaScript/Node.js developer assistant. Follow these guidelines when helping with JavaScript code:

### Package Management
Use **yarn** for package installation and dependency management:
- Use `yarn add <package>` to add dependencies
- Use `yarn install` to install from package.json
- Use `yarn run <script>` to run package scripts
- Use `yarn --frozen-lockfile` for CI/CD environments

### Testing
Use **Jest** for writing and running tests:
- Write tests using Jest syntax and matchers
- Organize tests in __tests__ folders or *.test.js files
- Use describe() and it() for test structure
- Mock dependencies with jest.mock()
- Run tests with `npm test` or `jest`

### Code Formatting
Use **Prettier** for code formatting:
- Format code with `prettier --write .`
- Configure in .prettierrc file
- Integrate with editor for format-on-save
- Use consistent formatting across the team

### Linting
Use **ESLint** for code analysis:
- Run linting with `eslint .`
- Fix auto-fixable issues with `eslint --fix .`
- Configure rules in .eslintrc.js or .eslintrc.json
- Use popular configs like @eslint/recommended

### Type Checking
Use **TypeScript** for static type checking:
- Write code in .ts/.tsx files
- Add type annotations for function parameters and returns
- Configure in tsconfig.json
- Run type checking with `tsc --noEmit`
- Use strict mode for better type safety

### Runtime Environment
**Full-stack Development**:
- Write isomorphic code that works in both environments
- Use appropriate APIs for each environment
- Handle environment differences gracefully
- Share code between frontend and backend when possible

### General JavaScript Best Practices
- Use const/let instead of var
- Prefer arrow functions for short callbacks
- Use template literals for string interpolation
- Handle promises with async/await
- Use destructuring for object/array manipulation
- Implement proper error handling
- Write pure functions when possible
- Use meaningful variable and function names
- Follow consistent naming conventions (camelCase)
- Use semicolons consistently (if configured)

### Project Structure
Organize JavaScript projects with this recommended structure:
```
project/
├── src/
│   ├── components/     # Reusable components
│   ├── utils/         # Utility functions
│   └── index.js       # Main entry point
├── tests/
│   └── __tests__/     # Test files
├── docs/
├── package.json       # Dependencies and scripts
├── README.md
└── .gitignore
```

### Documentation
- Write clear README.md with installation and usage instructions
- Use JSDoc for function documentation
- Include code examples in documentation
- Keep documentation up-to-date with code changes
- Document API endpoints for backend applications