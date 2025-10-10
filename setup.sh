#!/bin/bash

# Copilot Instructions Setup Script
# This script helps you quickly set up customized copilot instructions

set -e

echo "🚀 Copilot Instructions Setup"
echo "=============================="
echo ""

# Check if we're in the right directory
if [ ! -f "scripts/customize.py" ]; then
    echo "❌ Error: Please run this script from the copilot-instructions repository root"
    echo "   Expected to find scripts/customize.py"
    exit 1
fi

# Check Python availability
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "❌ Error: Python is required but not found"
    echo "   Please install Python 3.6 or later"
    exit 1
fi

# Use python3 if available, otherwise python
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

echo "✅ Found Python: $($PYTHON_CMD --version)"
echo ""

# Ask user which language they want to customize
echo "📚 Available templates:"
echo "  1) Python (python.md)"
echo ""
read -p "Select template [1]: " template_choice
template_choice=${template_choice:-1}

case $template_choice in
    1)
        template="templates/python.md"
        echo "Selected: Python template"
        ;;
    *)
        echo "❌ Invalid selection"
        exit 1
        ;;
esac

echo ""

# Ask if they want to use interactive mode or provide a config file
echo "🔧 Configuration options:"
echo "  1) Interactive survey (recommended for first-time users)"
echo "  2) Use existing config file"
echo ""
read -p "Choose option [1]: " config_choice
config_choice=${config_choice:-1}

case $config_choice in
    1)
        echo "Starting interactive survey..."
        echo ""
        $PYTHON_CMD scripts/customize.py --template "$template" --save-config
        ;;
    2)
        read -p "Enter path to config file: " config_file
        if [ ! -f "$config_file" ]; then
            echo "❌ Error: Config file not found: $config_file"
            exit 1
        fi
        $PYTHON_CMD scripts/customize.py --template "$template" --config "$config_file"
        ;;
    *)
        echo "❌ Invalid selection"
        exit 1
        ;;
esac

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📝 Next steps:"
echo "  1. Review the generated .github/copilot-instructions.md file"
echo "  2. Commit and push it to your repository"
echo "  3. GitHub Copilot will automatically use these instructions in VS Code"
echo ""
echo "💡 Tip: You can re-run this setup anytime to update your preferences"