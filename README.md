# VibeNet — Social Media Platform

A Python-based social media platform built with object-oriented design to manage users, posts, comments, and application data.

## Overview

VibeNet separates the application's data model from its command-line interface:

- `vibenet.py` — defines the `Post`, `User`, and `VibeNet` classes and application data operations
- `main.py` — provides authentication, menus, post interaction, searching, and the program entry point

## Features

- Object-oriented application structure
- User login and account creation
- Password requirement validation
- User and post management
- Post creation, editing, and deletion
- Ownership checks for post modification
- Likes and comments
- Engagement-score calculation
- Hashtag search
- Engagement- and date-based newsfeed sorting
- User sorting by follower/following counts
- Date-range post searching
- File-based loading of users, posts, and comments

## Technical Concepts

- Python
- Object-Oriented Programming
- Dictionaries and lists
- File I/O
- Date/time processing
- String processing
- Sorting and filtering
- Modular program design
- Command-line interfaces

## Project Structure

```text
VibeNet/
├── README.md
├── .gitignore
└── src/
    ├── main.py
    └── vibenet.py
```

## Architecture

```text
main.py
   │
   │ imports
   ▼
vibenet.py
   ├── Post
   ├── User
   └── VibeNet
```

The separation keeps the application's core classes and data operations independent from the command-line interface and user interaction logic.

## Running the Project

The application currently expects the original project data files:

```text
users.txt
posts.txt
post_comments.txt
```

These files are intentionally not included in the repository until the project data can be reviewed and sanitized.

From the project directory, run:

```bash
python src/main.py
```

If the data files are stored in a different location, the file paths in `main.py` should be updated accordingly.

## Security Note

This is an educational project. Passwords are currently stored and compared directly in memory/file data rather than using secure password hashing. The project should therefore not be presented as implementing production-grade authentication.

## Future Improvements

- Add automated unit tests
- Implement secure password hashing
- Improve input and file validation
- Handle malformed data files gracefully
- Replace flat-file persistence with a database
- Separate additional services from the CLI layer
- Expand the application into a web/API service
