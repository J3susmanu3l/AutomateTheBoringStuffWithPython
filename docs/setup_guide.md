# Setup Guide for Python Learning Project

## Quick Start

This guide will help you set up the Python learning environment and get started with the exercises.

## Prerequisites

1. **Python 3.8 or higher** installed on your system
2. **Git** for version control
3. **A text editor** (VS Code recommended)

## Step-by-Step Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/AutomateTheBoringStuffWithPython.git
cd AutomateTheBoringStuffWithPython
```

### 2. Create Virtual Environment

```bash
# Create a new virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate

# On Linux/Mac:
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt
```

### 4. Verify Setup

```bash
# Test that everything is working
python src/Reading_and_writing_files.py
```

## Project Structure Explained

```
AutomateTheBoringStuffWithPython/
├── src/                    # Your Python learning files
│   ├── Reading_and_writing_files.py
│   ├── regex.py
│   └── ... (other files)
├── tests/                  # Test files
│   └── test_file_operations.py
├── docs/                   # Documentation
│   └── setup_guide.md
├── data/                   # Data files
├── .venv/                  # Virtual environment (ignored by git)
├── requirements.txt        # Python dependencies
├── README.md              # Project overview
├── LEARNING_LOG.md        # Your learning progress
└── .gitignore             # Git ignore rules
```

## Running Exercises

Each Python file in the `src/` directory is a self-contained exercise:

```bash
# Run file operations exercise
python src/Reading_and_writing_files.py

# Run regex patterns exercise
python src/regex.py

# Run password validation exercise
python src/strong_password_detection.py
```

## Running Tests

```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python tests/test_file_operations.py
```

## Development Workflow

### 1. Start a New Learning Session

```bash
# Make sure you're in the project directory
cd AutomateTheBoringStuffWithPython

# Activate virtual environment
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
```

### 2. Work on Exercises

- Create new Python files in `src/` directory
- Add detailed comments explaining what you learned
- Test your code thoroughly

### 3. Save Your Progress

```bash
# Add your changes to git
git add .

# Commit with a descriptive message
git commit -m "Add new exercise: [describe what you learned]"

# Push to GitHub (after setting up remote)
git push origin main
```

### 4. Update Learning Log

After completing exercises, update `LEARNING_LOG.md` with:
- What you learned
- Challenges you faced
- Solutions you found
- Next steps

## Troubleshooting

### Virtual Environment Issues

**Problem**: `python -m venv .venv` doesn't work
**Solution**: Make sure Python is installed and in your PATH

**Problem**: Can't activate virtual environment
**Solution**: 
- Windows: Use `.venv\Scripts\activate`
- Linux/Mac: Use `source .venv/bin/activate`

### Import Issues

**Problem**: `ModuleNotFoundError`
**Solution**: 
1. Make sure virtual environment is activated
2. Install missing packages: `pip install package_name`
3. Update requirements.txt: `pip freeze > requirements.txt`

### Git Issues

**Problem**: Git not recognized
**Solution**: Install Git from https://git-scm.com/

## Best Practices

1. **Always activate your virtual environment** before working
2. **Commit regularly** to track your progress
3. **Add detailed comments** to your code
4. **Test your code** before moving to the next exercise
5. **Update the learning log** after each session
6. **Keep requirements.txt updated** when adding new packages

## Next Steps

After setting up:
1. Start with `src/Reading_and_writing_files.py`
2. Work through exercises in order
3. Practice with your own variations
4. Document your learning journey

Happy coding! 🐍 