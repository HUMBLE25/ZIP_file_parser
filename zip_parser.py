# 구조체로 만들면 출력하기가 쉽지 않을까? 

import sys
from pathlib import Path
from parse_local_file_headers import parse_local_file_headers
from parse_central_directory_headers import parse_central_directory_headers
from parse_end_of_central_directory_record import parse_end_of_central_directory_record

def main():
    # 1. 사용자로부터 ZIP 파일 경로 입력 받기
    if len(sys.argv) < 2:
        print("사용법: python zip_parser.py <zip_file_path>")
        sys.exit(1)
    
    zip_path = Path(sys.argv[1])
    
    # 2. 해당 파일이 존재하는지 확인
    if not zip_path.exists():
        print(f"ZIP 파일을 찾을 수 없습니다: {zip_path}")
        sys.exit(1)
    
    # 3. 파일을 바이너리 모드('rb')로 열기
    with open(zip_path, 'rb') as file:
        # 4. 파일 데이터를 읽고 변수에 저장
        binary_data = file.read()
        
        # 5. ZIP 파일 시그니처 확인
        if not is_zip_file(binary_data):
            print(f"ZIP 파일이 아닙니다: {zip_path}")
            sys.exit(1)
        
        # 6. ZIP 파일 내 압축된 파일 개수 확인
        file_count = count_files_in_zip(binary_data)
        print(f"압축된 파일 개수: {file_count}")
        
        # 6. 로컬 파일 헤더 파싱
        parse_local_file_headers(binary_data)
        
        # 7. 중앙 디렉토리 헤더 파싱
        parse_central_directory_headers(binary_data)
        
        # 8. 엔드 오브 센트럴 디렉토리 레코드 파싱
        parse_end_of_central_directory_record(binary_data)

def is_zip_file(binary_data):
    return binary_data[:4] == b'PK\x03\x04'

def count_files_in_zip(binary_data):
    offset = 0
    file_count = 0
    while offset < len(binary_data):
        if binary_data[offset:offset+4] == b'PK\x01\x02':
            file_count += 1
        offset += 1
    return file_count

if __name__ == "__main__":
    main()