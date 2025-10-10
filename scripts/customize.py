#!/usr/bin/env python3
"""
Copilot Instructions Customization Script

This script processes survey responses and generates customized copilot instruction files.
"""

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, Any


def load_template(template_path: str) -> str:
    """Load a template file."""
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Template file not found: {template_path}")
        sys.exit(1)


def process_template(template: str, responses: Dict[str, Any]) -> str:
    """Process template with user responses."""
    result = template
    
    # Replace simple placeholders
    for key, value in responses.items():
        placeholder = f"{{{{{key.upper()}}}}}"
        result = result.replace(placeholder, str(value))
    
    # Process conditional blocks
    result = process_conditionals(result, responses)
    
    return result


def process_conditionals(template: str, responses: Dict[str, Any]) -> str:
    """Process conditional blocks in the template."""
    import re
    
    # Pattern to match conditional blocks: {{#if_condition}}...{{/if_condition}}
    pattern = r'\{\{#if_([^}]+)\}\}(.*?)\{\{/if_\1\}\}'
    
    def replace_conditional(match):
        condition = match.group(1)
        content = match.group(2)
        
        # Check if condition is met based on responses
        if should_include_block(condition, responses):
            return content
        else:
            return ""
    
    # Process all conditional blocks
    while re.search(pattern, template, re.DOTALL):
        template = re.sub(pattern, replace_conditional, template, flags=re.DOTALL)
    
    return template


def should_include_block(condition: str, responses: Dict[str, Any]) -> bool:
    """Determine if a conditional block should be included."""
    # Parse condition like "package_manager_uv" 
    parts = condition.split('_')
    
    if len(parts) >= 2:
        category = '_'.join(parts[:-1])  # e.g., "package_manager"
        option = parts[-1]  # e.g., "uv"
        
        # Check if this option was selected for this category
        return responses.get(category, '').lower() == option.lower()
    
    return False


def interactive_survey(template_path: str) -> Dict[str, Any]:
    """Run interactive survey to collect user preferences."""
    # Determine language from template path
    template_name = Path(template_path).stem.lower()
    
    if template_name == 'python':
        return python_survey()
    elif template_name == 'javascript':
        return javascript_survey()
    else:
        print(f"No interactive survey available for template: {template_name}")
        print("Please provide a configuration file with --config option")
        sys.exit(1)


def python_survey() -> Dict[str, Any]:
    """Run interactive survey for Python preferences."""
    print("Python Copilot Instructions Customization")
    print("=" * 45)
    print()
    
    responses = {}
    
    # Package Management
    print("1. Package Management:")
    print("   a) UV (modern, fast Python package installer)")
    print("   b) pip (traditional Python package installer)")
    choice = input("   Choose (a/b): ").strip().lower()
    responses['package_manager'] = 'uv' if choice == 'a' else 'pip'
    print()
    
    # Testing Framework
    print("2. Testing Framework:")
    print("   a) pytest (popular third-party testing framework)")
    print("   b) unittest (built-in Python testing framework)")
    choice = input("   Choose (a/b): ").strip().lower()
    responses['testing_framework'] = 'pytest' if choice == 'a' else 'unittest'
    print()
    
    # Code Formatting
    print("3. Code Formatting:")
    print("   a) black (opinionated code formatter)")
    print("   b) autopep8 (PEP 8 compliant formatter)")
    print("   c) ruff format (fast Rust-based formatter)")
    choice = input("   Choose (a/b/c): ").strip().lower()
    if choice == 'a':
        responses['code_formatter'] = 'black'
    elif choice == 'b':
        responses['code_formatter'] = 'autopep8'
    else:
        responses['code_formatter'] = 'ruff_format'
    print()
    
    # Linting
    print("4. Linting:")
    print("   a) ruff (fast Rust-based linter)")
    print("   b) flake8 (traditional Python linter)")
    print("   c) pylint (comprehensive Python linter)")
    choice = input("   Choose (a/b/c): ").strip().lower()
    if choice == 'a':
        responses['linter'] = 'ruff'
    elif choice == 'b':
        responses['linter'] = 'flake8'
    else:
        responses['linter'] = 'pylint'
    print()
    
    # Type Checking
    print("5. Type Checking:")
    print("   a) mypy (static type checker)")
    print("   b) pyright (Microsoft's type checker)")
    print("   c) None (no type checking)")
    choice = input("   Choose (a/b/c): ").strip().lower()
    if choice == 'a':
        responses['type_checker'] = 'mypy'
    elif choice == 'b':
        responses['type_checker'] = 'pyright'
    else:
        responses['type_checker'] = 'none'
    print()
    
    return responses


def javascript_survey() -> Dict[str, Any]:
    """Run interactive survey for JavaScript preferences."""
    print("JavaScript/Node.js Copilot Instructions Customization")
    print("=" * 55)
    print()
    
    responses = {}
    
    # Package Management
    print("1. Package Management:")
    print("   a) npm (Node.js default package manager)")
    print("   b) yarn (fast, reliable package manager)")
    print("   c) pnpm (efficient disk space package manager)")
    choice = input("   Choose (a/b/c): ").strip().lower()
    if choice == 'a':
        responses['package_manager'] = 'npm'
    elif choice == 'b':
        responses['package_manager'] = 'yarn'
    else:
        responses['package_manager'] = 'pnpm'
    print()
    
    # Testing Framework
    print("2. Testing Framework:")
    print("   a) Jest (popular JavaScript testing framework)")
    print("   b) Vitest (fast unit testing framework)")
    print("   c) Mocha (feature-rich testing framework)")
    choice = input("   Choose (a/b/c): ").strip().lower()
    if choice == 'a':
        responses['testing_framework'] = 'jest'
    elif choice == 'b':
        responses['testing_framework'] = 'vitest'
    else:
        responses['testing_framework'] = 'mocha'
    print()
    
    # Code Formatting
    print("3. Code Formatting:")
    print("   a) Prettier (opinionated code formatter)")
    print("   b) ESLint with --fix (linter with formatting)")
    choice = input("   Choose (a/b): ").strip().lower()
    responses['code_formatter'] = 'prettier' if choice == 'a' else 'eslint'
    print()
    
    # Linting
    print("4. Linting:")
    print("   a) ESLint (pluggable JavaScript linter)")
    print("   b) Biome (fast toolchain for web projects)")
    choice = input("   Choose (a/b): ").strip().lower()
    responses['linter'] = 'eslint' if choice == 'a' else 'biome'
    print()
    
    # Type Checking
    print("5. Type Checking:")
    print("   a) TypeScript (typed superset of JavaScript)")
    print("   b) JSDoc (documentation comments with type info)")
    print("   c) None (plain JavaScript)")
    choice = input("   Choose (a/b/c): ").strip().lower()
    if choice == 'a':
        responses['type_checking'] = 'typescript'
    elif choice == 'b':
        responses['type_checking'] = 'jsdoc'
    else:
        responses['type_checking'] = 'none'
    print()
    
    # Runtime Environment
    print("6. Runtime Environment:")
    print("   a) Node.js (server-side JavaScript runtime)")
    print("   b) Browser (client-side web development)")
    print("   c) Both (full-stack development)")
    choice = input("   Choose (a/b/c): ").strip().lower()
    if choice == 'a':
        responses['runtime_environment'] = 'nodejs'
    elif choice == 'b':
        responses['runtime_environment'] = 'browser'
    else:
        responses['runtime_environment'] = 'both'
    print()
    
    return responses


def save_responses(responses: Dict[str, Any], output_dir: str) -> None:
    """Save responses to a JSON file for future reference."""
    os.makedirs(output_dir, exist_ok=True)
    config_file = os.path.join(output_dir, 'copilot_config.json')
    
    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(responses, f, indent=2)
    
    print(f"Configuration saved to: {config_file}")


def main():
    parser = argparse.ArgumentParser(description='Customize Copilot Instructions')
    parser.add_argument('--template', '-t', default='templates/python.md', 
                       help='Template file to use (default: templates/python.md)')
    parser.add_argument('--config', '-c', 
                       help='JSON config file with responses (interactive if not provided)')
    parser.add_argument('--output', '-o', default='.github/copilot-instructions.md',
                       help='Output file path (default: .github/copilot-instructions.md)')
    parser.add_argument('--save-config', action='store_true',
                       help='Save responses to config file for future use')
    
    args = parser.parse_args()
    
    # Determine the script's directory to find templates
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    template_path = repo_root / args.template
    
    # Load responses
    if args.config:
        try:
            with open(args.config, 'r', encoding='utf-8') as f:
                responses = json.load(f)
            print(f"Loaded configuration from: {args.config}")
        except FileNotFoundError:
            print(f"Error: Config file not found: {args.config}")
            sys.exit(1)
    else:
        responses = interactive_survey(str(template_path))
        
        if args.save_config:
            output_dir = os.path.dirname(args.output)
            save_responses(responses, output_dir if output_dir else '.')
    
    # Load and process template
    template = load_template(str(template_path))
    customized_content = process_template(template, responses)
    
    # Ensure output directory exists
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Write customized instructions
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(customized_content)
    
    # Basic validation
    if validate_output(customized_content):
        print(f"✅ Customized instructions saved to: {args.output}")
    else:
        print(f"⚠️  Instructions saved to: {args.output} (with warnings)")
    
    print()
    print("Next steps:")
    print("1. Review the generated instructions")
    print("2. Commit the file to your repository")
    print("3. GitHub Copilot will automatically use these instructions in VS Code")


def validate_output(content: str) -> bool:
    """Basic validation of the generated content."""
    warnings = []
    
    # Check for unreplaced placeholders
    import re
    unreplaced = re.findall(r'\{\{[^}]+\}\}', content)
    if unreplaced:
        warnings.append(f"Found unreplaced placeholders: {unreplaced}")
    
    # Note: Skipping empty line validation as it's normal with conditional templates
    
    if warnings:
        print("⚠️  Validation warnings:")
        for warning in warnings:
            print(f"   - {warning}")
        return False
    
    return True


if __name__ == '__main__':
    main()