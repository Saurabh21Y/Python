# File Management System (CLI Based)

## Project Overview

The File Management System is a command-line application developed using Python File Handling concepts. The project allows users to perform CRUD (Create, Read, Update, Delete) operations on files within the project's working directory.

The system provides a simple interactive menu where users can create new files, read existing files, update file contents or names, and delete files safely.

---

# Objective

The primary objective of this project is to understand and implement file handling operations in Python while building a practical file management utility.

---

# Scope

The application will operate only within the current project directory and will not modify files outside the designated workspace.

---

# Functional Requirements

## 1. Display Available Files

### Description

The system shall display all files and folders present in the current working directory before performing any operation.

### Expected Output

* List all available files
* List all available folders
* Display serial numbers for easy identification

---

## 2. Create File

### Description

The system shall allow users to create a new file.

### User Inputs

* File Name
* Initial Content (Optional)

### Validation Rules

* File name must not be empty.
* File should not already exist.

### Success Message

```text
File Created Successfully
```

### Failure Message

```text
File Already Exists
```

---

## 3. Read File

### Description

The system shall allow users to read the contents of an existing file.

### User Inputs

* File Name

### Validation Rules

* File must exist.
* Selected item must be a file.

### Expected Output

* Display complete file content.

### Failure Message

```text
File Does Not Exist
```

---

## 4. Update File

### Description

The system shall allow users to modify existing files.

### Supported Operations

#### 4.1 Rename File

* Change the name of an existing file.

#### 4.2 Overwrite File Content

* Replace the entire content of the file.

#### 4.3 Append Content

* Add new content at the end of the file.

### Validation Rules

* File must exist.
* Selected item must be a valid file.

### Success Message

```text
File Updated Successfully
```

---

## 5. Delete File

### Description

The system shall allow users to remove an existing file.

### User Inputs

* File Name

### Validation Rules

* File must exist.
* Selected item must be a file.

### Success Message

```text
File Removed Successfully
```

### Failure Message

```text
No Such File Exists
```

---

# Error Handling Requirements

The application shall handle runtime exceptions gracefully.

### Possible Errors

* File Not Found
* Invalid File Name
* Permission Denied
* Invalid User Input
* Unexpected Runtime Error

### Expected Behavior

The application must:

* Prevent program crashes.
* Display meaningful error messages.
* Continue execution whenever possible.

---

# Non-Functional Requirements

## Performance

* Operations should execute instantly for small and medium-sized files.

## Reliability

* The application should not terminate unexpectedly.

## Usability

* Menu-driven interface.
* Easy-to-understand prompts.
* Clear success and failure messages.

## Maintainability

* Code should be modular and function-based.
* Each operation should be implemented in a separate function.

---

# Technologies Used

* Python 3.x
* File Handling
* pathlib Module
* os Module
* Exception Handling

---

# Project Structure

```text
project/
│
├── main.py
│
├── create_file()
├── read_file()
├── update_file()
├── delete_file()
│
└── read_file_and_folder()
```

---

# Future Enhancements

The following features may be added in future versions:

* Folder CRUD Operations
* File Search
* Copy File
* Move File
* File Statistics
* File Size Information
* Last Modified Date
* Trash Bin Recovery
* Multiple File Operations
* Activity Logging
* User Authentication

---

# Conclusion

This project demonstrates practical implementation of Python File Handling by building a complete CRUD-based File Management System. It provides hands-on experience with file operations, exception handling, path management, and modular programming concepts.
