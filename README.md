# ZIP_file_parser

A project to create a ZIP file parsing program to better understand the ZIP file format.

## Purpose
This project was created to understand the ZIP file format by parsing ZIP files. By examining the structure of ZIP files, we can gain insights into how they are organized and how data is stored within them.

## Description
The ZIP_file_parser project is a Python program that parses ZIP files and extracts information about the files contained within them. It reads the local file headers, central directory headers, and the end of central directory record to provide detailed information about each file in the ZIP archive.

## Installation
To install and run the ZIP_file_parser, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/HUMBLE25/ZIP_file_parser.git
    cd ZIP_file_parser
    ```

2. Ensure you have Python installed on your system. This project requires Python 3.x.

## Usage
To run the ZIP_file_parser, use the following command:

```sh
python zip_parser.py <zip_file_path>
```

For example, to parse the provided example file test.zip, use the following command:

Example
The example file test.zip is provided in the repository. You can use this file to see how the parser works and what kind of output it generates.

This will output detailed information about the files contained in test.zip, including their headers and other metadata.

Repository
You can find the repository for this project at: https://github.com/HUMBLE25/ZIP_file_parser.git