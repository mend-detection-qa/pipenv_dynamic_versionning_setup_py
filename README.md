# Pipenv Test Case 9: setup.py Fallback

## What This Tests
Tests detection of Python version from setup.py when no higher-priority files specify a version.

## Expected
>=3.7 found through SetupPyPythonRequires

## Files
- `Pipfile` - No requires section
- `setup.py` - Contains `python_requires=">=3.7"`

## Expected Behavior
Your version detection tool should detect **Python >=3.7** from setup.py.

## Priority
This is the **seventh priority** (lowest) detection method for Pipenv projects.

## Note
setup.py is the last fallback option for Python version detection in Pipenv projects.
