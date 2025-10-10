# JavaScript/Node.js Copilot Instructions Template

## Setup Instructions

To use these Copilot instructions:

1. **Fork this repository** or **copy this file** to your own repository
2. **Answer the survey questions** below to customize the instructions
3. **Replace the placeholders** in the instructions with your preferences
4. **Save the customized file** as `.github/copilot-instructions.md` in your repository
5. **Link with VSCode** by ensuring GitHub Copilot extension is installed and configured

## Survey Questions

Please answer these questions to customize your JavaScript/Node.js development instructions:

### Package Management
- [ ] **npm** (Node.js default package manager)
- [ ] **yarn** (fast, reliable package manager)
- [ ] **pnpm** (efficient disk space package manager)

### Testing Framework
- [ ] **Jest** (popular JavaScript testing framework)
- [ ] **Vitest** (fast unit testing framework)
- [ ] **Mocha** (feature-rich testing framework)

### Code Formatting
- [ ] **Prettier** (opinionated code formatter)
- [ ] **ESLint with --fix** (linter with formatting)

### Linting
- [ ] **ESLint** (pluggable JavaScript linter)
- [ ] **Biome** (fast toolchain for web projects)

### Type Checking
- [ ] **TypeScript** (typed superset of JavaScript)
- [ ] **JSDoc** (documentation comments with type info)
- [ ] **None** (plain JavaScript)

### Runtime Environment
- [ ] **Node.js** (server-side JavaScript runtime)
- [ ] **Browser** (client-side web development)
- [ ] **Both** (full-stack development)

---

## JavaScript/Node.js Copilot Instructions

You are an expert JavaScript/Node.js developer assistant. Follow these guidelines when helping with JavaScript code:

### Package Management
Use **{{PACKAGE_MANAGER}}** for package installation and dependency management:
{{#if_package_manager_npm}}
- Use `npm install <package>` to add dependencies
- Use `npm install` to install from package.json
- Use `npm run <script>` to run package scripts
- Use `npm ci` for clean installs in CI/CD
{{/if_package_manager_npm}}
{{#if_package_manager_yarn}}
- Use `yarn add <package>` to add dependencies
- Use `yarn install` to install from package.json
- Use `yarn run <script>` to run package scripts
- Use `yarn --frozen-lockfile` for CI/CD environments
{{/if_package_manager_yarn}}
{{#if_package_manager_pnpm}}
- Use `pnpm add <package>` to add dependencies
- Use `pnpm install` to install from package.json
- Use `pnpm run <script>` to run package scripts
- Use `pnpm install --frozen-lockfile` for CI/CD
{{/if_package_manager_pnpm}}

### Testing
Use **{{TESTING_FRAMEWORK}}** for writing and running tests:
{{#if_testing_framework_jest}}
- Write tests using Jest syntax and matchers
- Organize tests in __tests__ folders or *.test.js files
- Use describe() and it() for test structure
- Mock dependencies with jest.mock()
- Run tests with `npm test` or `jest`
{{/if_testing_framework_jest}}
{{#if_testing_framework_vitest}}
- Write tests using Vitest syntax (Jest-compatible)
- Organize tests in *.test.js or *.spec.js files
- Use describe() and it() for test structure
- Mock dependencies with vi.mock()
- Run tests with `npm test` or `vitest`
{{/if_testing_framework_vitest}}
{{#if_testing_framework_mocha}}
- Write tests using Mocha syntax
- Organize tests in test/ directory
- Use describe() and it() for test structure
- Use Chai for assertions
- Run tests with `npm test` or `mocha`
{{/if_testing_framework_mocha}}

### Code Formatting
{{#if_code_formatter_prettier}}
Use **Prettier** for code formatting:
- Format code with `prettier --write .`
- Configure in .prettierrc file
- Integrate with editor for format-on-save
- Use consistent formatting across the team
{{/if_code_formatter_prettier}}
{{#if_code_formatter_eslint}}
Use **ESLint with --fix** for code formatting:
- Format and lint with `eslint --fix .`
- Configure formatting rules in .eslintrc
- Combine linting and formatting in one tool
{{/if_code_formatter_eslint}}

### Linting
Use **{{LINTER}}** for code analysis:
{{#if_linter_eslint}}
- Run linting with `eslint .`
- Fix auto-fixable issues with `eslint --fix .`
- Configure rules in .eslintrc.js or .eslintrc.json
- Use popular configs like @eslint/recommended
{{/if_linter_eslint}}
{{#if_linter_biome}}
- Run linting with `biome check .`
- Fix issues with `biome check --apply .`
- Configure in biome.json
- Fast performance with Rust-based tooling
{{/if_linter_biome}}

### Type Checking
{{#if_type_checking_typescript}}
Use **TypeScript** for static type checking:
- Write code in .ts/.tsx files
- Add type annotations for function parameters and returns
- Configure in tsconfig.json
- Run type checking with `tsc --noEmit`
- Use strict mode for better type safety
{{/if_type_checking_typescript}}
{{#if_type_checking_jsdoc}}
Use **JSDoc** for type information:
- Add JSDoc comments with type information
- Use @param and @returns tags
- Enable TypeScript checking in JS files
- Configure checkJs in jsconfig.json
{{/if_type_checking_jsdoc}}
{{#if_type_checking_none}}
Focus on clean JavaScript without mandatory typing:
- Write clear, self-documenting code
- Use meaningful variable and function names
- Add comments where logic is complex
{{/if_type_checking_none}}

### Runtime Environment
{{#if_runtime_environment_nodejs}}
**Node.js Development**:
- Use modern Node.js features (ES modules, async/await)
- Handle errors with try/catch for async operations
- Use built-in modules when possible (fs, path, crypto)
- Follow Node.js best practices for server applications
{{/if_runtime_environment_nodejs}}
{{#if_runtime_environment_browser}}
**Browser Development**:
- Use modern JavaScript features supported by target browsers
- Handle DOM manipulation efficiently
- Use fetch() for HTTP requests
- Follow web standards and accessibility guidelines
{{/if_runtime_environment_browser}}
{{#if_runtime_environment_both}}
**Full-stack Development**:
- Write isomorphic code that works in both environments
- Use appropriate APIs for each environment
- Handle environment differences gracefully
- Share code between frontend and backend when possible
{{/if_runtime_environment_both}}

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