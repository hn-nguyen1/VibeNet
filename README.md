# VibeNet — Social Media Platform

A Python-based social media platform model built with object-oriented programming to manage users, posts, comments, and application data.

## Overview

The original project defines three core classes:

- `User` — stores user identity, profile information, and posts
- `Post` — represents posts, engagement, comments, authorship, and dates
- `VibeNet` — manages users and posts and provides application-level operations

The current repository preserves the original class implementation rather than inventing a new application entry point.

## Features

- Object-oriented application structure
- User and post management
- Post creation and content editing
- Ownership checks for post modification
- Likes and comment tracking
- Engagement-score calculation
- Date-range post searching
- User post retrieval
- File-based loading of users, posts, and comments

## Technical Concepts

- Python
- Object-Oriented Programming
- Dictionaries
- Lists
- File I/O
- Date/time processing
- Data validation
- Search and filtering

## Project Structure

```text
VibeNet/
├── README.md
├── .gitignore
└── src/
    └── vibenet.py
```

## Current Implementation

`src/vibenet.py` contains the original `Post`, `User`, and `VibeNet` classes. The source provided for this project does not include a separate command-line `main.py`, so the repository does not fabricate one.

## Limitations

This version is an educational project and is not intended for production deployment. Authentication/security would require additional work such as secure password hashing, stronger validation, and more comprehensive error handling.

## Future Improvements

- Add a dedicated application entry point using the original project interface, if available
- Add automated unit tests
- Replace plaintext password handling with secure password hashing
- Improve input and file validation
- Add database-backed persistence
- Expand the application into a web/API service
