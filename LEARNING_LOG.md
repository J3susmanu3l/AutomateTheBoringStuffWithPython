# Learning Log - Python Journey
## 📅 2025-08-01 - Project Setup and Organization

### What I Learned Today
- **Pathlib Path library module**: 
-  How to write directories path with the Path() function
- How to find the current directory at which the file I am working with is at using the Path.cwd() function
- How to change the directory path using the chdir() function

### Challenges Faced
- Understanding wether the chdir() function actually changes the location of the file in the directory or it just changes it in the terminal
- How the Path() function can be called in multiple ways. Like calling it with a forward slash after the main path

### Solutions Found
tested printing path before changing and after changing it with the next code:
``` python
from pathlib import Path
    import os
    print(Path.cwd())
    os.chdir(Path(r'c:\Users\jesus\OneDrive\Escritorio\AutomateTheBoringStuffWithPython/src'))
    print(Path.cwd())
    # while testing I see that the file location in the terminal changes for the  os.chdir() function, but it actually doesn't 
    # change it in the system. Just in the terminal. It is making me wonder why this is used for.
```
### Next Steps
- finish understaing how absolute vs relative paths and how they are handled
- Learn how to create a new folder or directory
- Getting the Parts of a Filepath


## 📅 2025-07-30 - Project Setup and Organization

### What I Learned Today
- **Virtual Environments**: Set up proper project structure with `.venv`
- **Git Version Control**: Understanding the importance of tracking code changes
- **Project Organization**: Created proper folder structure (src/, tests/, docs/, data/)
- **Requirements Management**: Using `requirements.txt` to track dependencies

### Challenges Faced
- Understanding the difference between global and virtual environments
- Learning when to use different Python packages
- Organizing code files logically

### Solutions Found
- Used `python -m venv .venv` to create isolated environment
- Created comprehensive `.gitignore` to exclude unnecessary files
- Organized code into logical directories

### Next Steps
- [ ] Set up GitHub repository
- [ ] Learn more about file operations
- [ ] Practice with regular expressions

---

## 📅 Previous Learning Sessions

### File Operations (Reading_and_writing_files.py)
**Date**: Recent
**Concepts**: 
- Using `pathlib.Path` for cross-platform file paths
- Understanding file encoding issues
- Basic file reading and writing operations

**Challenges**:
- Had trouble with the `pathlib` import (typo in import statement)
- Understanding the difference between Windows and Unix path separators

**Solutions**:
- Fixed import statement: `from pathlib import Path` (not `path`)
- Used `Path()` function for platform-independent paths

### Regular Expressions (regex.py)
**Date**: Recent
**Concepts**:
- Pattern matching with `re` module
- Using `re.search()`, `re.findall()`, `re.sub()`
- Complex regex patterns for text processing

**Challenges**:
- Regex syntax was confusing at first
- Understanding when to use different regex functions

**Solutions**:
- Started with simple patterns and built up complexity
- Practiced with online regex testers
- Read documentation for each regex function

### Password Validation (strong_password_detection.py)
**Date**: Recent
**Concepts**:
- Input validation techniques
- Using regex for pattern validation
- Creating secure password requirements

**Challenges**:
- Understanding what makes a password "strong"
- Implementing multiple validation rules

**Solutions**:
- Researched password security best practices
- Broke down validation into separate functions
- Used regex to check for required character types

---

## 🎯 Learning Goals for Next Sessions

### Immediate Goals
- [ ] Complete web scraping exercises
- [ ] Learn CSV file processing
- [ ] Practice with Excel file operations
- [ ] Build automation projects

### Long-term Goals
- [ ] Master regular expressions
- [ ] Learn web development with Python
- [ ] Understand data analysis libraries
- [ ] Build real-world automation tools

---

## 📚 Resources Used

### Books
- "Automate the Boring Stuff with Python" by Al Sweigart

### Online Resources
- Python Documentation (docs.python.org)
- Real Python tutorials
- Stack Overflow for problem-solving

### Tools
- VS Code for coding
- Git for version control
- Virtual environments for isolation

---

## 💡 Tips for Future Me

1. **Always use virtual environments** for new projects
2. **Commit code regularly** to track progress
3. **Add detailed comments** explaining what you learned
4. **Test code thoroughly** before moving to next concept
5. **Document challenges** and solutions for future reference

---

*Keep learning and coding! 🚀* 