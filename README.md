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



---

# ZIP_file_parser

ZIP 파일 형식을 보다 잘 이해하기 위해 ZIP 파일을 파싱하는 프로그램을 만드는 프로젝트입니다.

## 목적
이 프로젝트는 ZIP 파일을 직접 파싱하여 ZIP 파일 형식을 이해하기 위해 만들어졌습니다. ZIP 파일의 구조를 분석함으로써 파일이 어떻게 구성되고 데이터를 어떻게 저장하는지에 대한 통찰을 얻을 수 있습니다.

## 설명
**ZIP_file_parser** 프로젝트는 ZIP 파일을 파싱하고 해당 ZIP 파일 내 포함된 파일들에 대한 정보를 추출하는 Python 프로그램입니다.  
이 프로그램은 **로컬 파일 헤더(Local File Headers)**, **중앙 디렉터리 헤더(Central Directory Headers)**, 그리고 **중앙 디렉터리 종료 레코드(End of Central Directory Record)** 를 읽어 각 파일에 대한 상세 정보를 제공합니다.

## 설치 방법
ZIP_file_parser를 설치하고 실행하려면 다음 단계를 따르세요:

1. 저장소를 클론합니다:
    ```sh
    git clone https://github.com/HUMBLE25/ZIP_file_parser.git
    cd ZIP_file_parser
    ```

2. Python이 시스템에 설치되어 있는지 확인합니다. 이 프로젝트는 **Python 3.x** 버전을 필요로 합니다.

## 사용법
ZIP_file_parser를 실행하려면 다음 명령어를 사용하세요:

```sh
python zip_parser.py <zip_파일_경로>
```

예를 들어, 제공된 `test.zip` 파일을 파싱하려면 다음 명령어를 입력하면 됩니다:

```sh
python zip_parser.py test.zip
```

## 예제
이 저장소에는 `test.zip` 파일이 포함되어 있으며, 이 파일을 사용하여 파서가 어떻게 작동하는지 확인할 수 있습니다.  
프로그램을 실행하면 `test.zip` 내부의 파일들에 대한 상세한 정보, 헤더, 기타 메타데이터가 출력됩니다.

## 저장소
이 프로젝트의 저장소는 다음에서 확인할 수 있습니다:  
[https://github.com/HUMBLE25/ZIP_file_parser.git](https://github.com/HUMBLE25/ZIP_file_parser.git)