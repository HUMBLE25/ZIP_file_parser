# 수도코드
# 1. 사용자로부터 ZIP 파일 경로 입력 받기
# 2. 해당 파일이 존재하는지 확인
#    - 존재하지 않으면 오류 메시지 출력 후 종료
# 3. 파일을 바이너리 모드('rb')로 열기
# 4. 파일 데이터를 읽고 변수에 저장
# 5. ZIP 파일 시그니처 확인
#    - 시그니처(0x50 0x4B 0x03 0x04)를 비교하여 ZIP 파일 여부 확인
#    - ZIP 파일이 아니라면 오류 메시지 출력 후 종료
# 6. ZIP 파일 내 압축된 파일 개수 확인
#    - 중앙 디렉토리 헤더의 시그니처(0x50 0x4B 0x01 0x02)를 카운트하여 파일 개수 계산
# 7. 분석 결과 출력
#    - ZIP 파일 여부 및 압축된 파일 개수 출력


import os

def is_zip_file(binary_data):
    # ZIP 파일의 시그니처 확인 (0x50 0x4B 0x03 0x04)
    return binary_data[:4] == b'PK\x03\x04'

def count_files_in_zip(binary_data):
    # ZIP 파일 내 파일 개수를 확인하는 간단한 방법
    return binary_data.count(b'PK\x01\x02')

def analyze_zip():
    # 1. 사용자로부터 ZIP 파일 경로 입력 받기
    zip_path = input("ZIP 파일 경로를 입력하세요: ")
    
    # 2. 파일이 존재하는지 확인
    if not os.path.isfile(zip_path):
        print("오류: 파일이 존재하지 않습니다.")
        return
    
    try:
        # 3. 파일을 바이너리 모드('rb')로 열기
        with open(zip_path, 'rb') as zip_file:
            # 4. 파일 데이터를 읽고 변수에 저장
            binary_data = zip_file.read()
        
        # 5. ZIP 파일 시그니처 확인
        if not is_zip_file(binary_data):
            print("오류: 입력된 파일은 ZIP 파일이 아닙니다.")
            return
        
        # 6. ZIP 파일 내 압축된 파일 개수 확인
        file_count = count_files_in_zip(binary_data)
        
        # 7. 분석 결과 출력
        print(f"ZIP 파일이 확인되었습니다. 압축된 파일 개수: {file_count}")
    
    except Exception as e:
        print(f"오류 발생: {e}")

# 실행
if __name__ == "__main__":
    analyze_zip()
