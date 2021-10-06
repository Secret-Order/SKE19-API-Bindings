# SKE19 API for Python 3

## Prerequisites

- Python 3.7 or later
- pip

## Installation

On Unix-like systems:
```
python3 -m pip install ske19-api
```
---
On Windows:
```
py -m pip install ske19-api
```
or if you've downloaded from Microsoft store:
```
python3 -m pip install ske19-api
```

## Usage

In your Python script, you can create a new client to login to SKE19 API by, and replacing the secret key with the server's key to access the API.
```python
session = SKE19(secret="secret-key", duration=3600)
```

You can then access the API routes with two methods, which are `#get_all_students()` and `#get_student(id: str)` which will return `list[Student]` and `Student` respectively.

```python
session.get_all_students()      # returns: [Student]
session.get_student(id)         # returns: Student(id, name, ...)
```

### The `Student` object

A `Student` has properties that can be easily accessed but are protected it is recommended to use getter methods instead.

Available methods: `#get_id()`, `#get_name_english()`, `#get_name_thai()`, `#get_email()` and `#get_instagram()`.

All methods were already documented, it is recommended to use IDE with code-completion or prediction to work with.