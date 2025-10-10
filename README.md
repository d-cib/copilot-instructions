# Copilot Instructions

A collection of customizable GitHub Copilot instruction templates for various programming languages and frameworks. These templates help you create personalized Copilot instructions based on your development preferences.

## 🚀 Quick Start

### Option 1: Fork This Repository
1. Fork this repository to your GitHub account
2. Clone your fork locally
3. Run the customization script to generate your personalized instructions
4. The script will create a `.github/copilot-instructions.md` file in your repository

### Option 2: Copy Template to Your Project
1. Download the template file for your language (e.g., `templates/python.md`)
2. Copy it to your project repository
3. Use the customization script or manually customize the template
4. Save the result as `.github/copilot-instructions.md` in your project

## 📋 Available Templates

### Python (`templates/python.md`)
Customize your Python development experience with preferences for:
- **Package Management**: UV vs pip
- **Testing Framework**: pytest vs unittest  
- **Code Formatting**: black vs autopep8 vs ruff format
- **Linting**: ruff vs flake8 vs pylint
- **Type Checking**: mypy vs pyright vs none

### JavaScript/Node.js (`templates/javascript.md`)
Customize your JavaScript/Node.js development experience with preferences for:
- **Package Management**: npm vs yarn vs pnpm
- **Testing Framework**: Jest vs Vitest vs Mocha
- **Code Formatting**: Prettier vs ESLint --fix
- **Linting**: ESLint vs Biome
- **Type Checking**: TypeScript vs JSDoc vs none
- **Runtime Environment**: Node.js vs Browser vs Both

## 🛠️ Usage

### Interactive Customization (Recommended)

```bash
# Navigate to your project or forked repository
cd your-project

# Run the interactive customization script
python scripts/customize.py

# Follow the prompts to answer survey questions
# The script will generate .github/copilot-instructions.md
```

### Using Configuration File

```bash
# Create a config file with your preferences
cat > copilot_config.json << EOF
{
  "package_manager": "uv",
  "testing_framework": "pytest",
  "code_formatter": "black",
  "linter": "ruff",
  "type_checker": "mypy"
}
EOF

# Generate instructions using the config file
python scripts/customize.py --config copilot_config.json
```

### Command Line Options

```bash
python scripts/customize.py [OPTIONS]

Options:
  -t, --template TEMPLATE    Template file to use (default: templates/python.md)
  -c, --config CONFIG        JSON config file with responses
  -o, --output OUTPUT        Output file path (default: .github/copilot-instructions.md)
  --save-config             Save responses to config file for future use
  -h, --help               Show help message
```

## 📁 Directory Structure

```
copilot-instructions/
├── templates/           # Template files for different languages
│   └── python.md       # Python template with survey questions
├── scripts/            # Customization scripts
│   └── customize.py    # Main customization script
├── examples/           # Example customized files
│   └── python_customized_example.md
└── README.md          # This file
```

## 🎯 How It Works

1. **Templates**: Each template contains survey questions and instruction content with placeholders
2. **Survey**: Answer questions about your preferences (tools, frameworks, etc.)
3. **Processing**: The script replaces placeholders and conditional blocks based on your answers
4. **Output**: A customized `.github/copilot-instructions.md` file is generated
5. **GitHub Integration**: GitHub Copilot automatically uses these instructions in VS Code

## 🔧 Creating New Templates

To add support for a new language or framework:

1. Create a new template file in `templates/` directory
2. Include survey questions at the top with checkboxes
3. Use placeholders like `{{VARIABLE_NAME}}` for simple substitutions
4. Use conditional blocks like `{{#if_condition}}...{{/if_condition}}` for optional content
5. Update the customization script if needed to handle new survey questions

### Template Syntax

- **Simple placeholders**: `{{VARIABLE_NAME}}`
- **Conditional blocks**: `{{#if_condition}}content{{/if_condition}}`
- **Survey format**: Use checkboxes `- [ ]` for options

Example:
```markdown
### Package Manager
- [ ] **npm** (Node.js package manager)
- [ ] **yarn** (alternative package manager)

Use **{{PACKAGE_MANAGER}}** for dependency management:
{{#if_package_manager_npm}}
- Run `npm install` to install dependencies
{{/if_package_manager_npm}}
{{#if_package_manager_yarn}}  
- Run `yarn install` to install dependencies
{{/if_package_manager_yarn}}
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add new templates or improve existing ones
4. Test your changes
5. Submit a pull request

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## 🔗 Related Links

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code GitHub Copilot Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
