# File Rename Tool

A Python utility that automates the process of batch renaming files with consistent naming patterns.

## Why I Built This

As I was working with large collections of images and documents, I found myself spending significant time manually renaming files to follow consistent naming conventions. This repetitive task seemed perfect for automation, so I created this tool to:

1. Save time on routine file management tasks
2. Ensure consistency in file naming across projects
3. Practice Python's file system operations
4. Create a practical utility that solves a real problem

## Features

- Batch rename all files in a directory with a single command
- Custom prefix support for personalized naming schemes
- Sequential numbering to maintain file order
- Automatic extension preservation
- Simple command-line interface
- No external dependencies

## Before and After

**Before:**
```
random1.jpg, document2.pdf, image_old.png, ...
```

**After:**
```
project-1.jpg, project-2.pdf, project-3.png, ...
```

## Installation

No installation required! Just download the script and run it with Python 3.x.

## Usage

1. Place the `main.py` script in a convenient location
2. Run the script with the target directory as a command-line argument:

```sh
python main.py /path/to/your/files/
```

3. Enter your desired prefix when prompted
4. All files in the specified directory will be renamed instantly

## Example

```sh
$ python main.py ./documents/
Enter the Prefix you want to use for each file e.g. nucleus: nucleus-1.jpg, nucleus-2.jpg,...
report
```

This will rename all files in the `./documents/` directory to follow the pattern: `report-1.extension`, `report-2.extension`, etc.

## What I Learned

This project helped me develop skills in:
- Working with file system operations in Python
- Handling file paths and extensions
- Processing command-line arguments
- Creating user interfaces for simple utilities
- Error handling for file operations

## Technical Implementation

The tool uses:
- `os` module for file operations and directory listing
- `sys` module for command-line arguments
- String manipulation for filename generation
- File extension handling

## Future Improvements

I plan to enhance this tool with:
- A preview mode to see changes before applying
- Options for different numbering formats (padding with zeros, etc.)
- Support for filtering files by extension
- A simple GUI using Tkinter
- Undo functionality to revert recent changes

## Important Notes

- **Always backup your files before batch renaming**
- The tool will rename ALL files in the specified directory
- Files are numbered based on their order in the directory listing

## License

This project is open source and available for anyone to use and modify.


