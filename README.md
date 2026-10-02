# VibeNet — Social Media Platform

A Python-based social media platform built with object-oriented design to manage users, posts, comments, and application data.

## Overview

VibeNet models core social-media functionality through three primary classes:

- `User` — stores user identity, profile information, and posts
- `Post` — represents posts, engagement, comments, authorship, and dates
- `VibeNet` — manages users and posts and provides application-level operations

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
- Interactive command-line functionality when integrated with the application interface

## Technical Concepts

- Python
- Object-Oriented Programming
- Classes and objects
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

## Running the Project

This repository contains the core VibeNet classes from the original project.

```bash
python src/vibenet.py
```

The class module is intended to be integrated with the project's application/interface code and data files.

## Limitations

This version is an educational project and is not intended for production deployment. In particular, authentication/security features would require additional work such as secure password hashing, stronger validation, and more comprehensive error handling.

## Future Improvements

- Add automated unit tests
- Replace plaintext password handling with secure password hashing
- Improve input and file validation
- Add database-backed persistence
- Expand the application into a web/API service
