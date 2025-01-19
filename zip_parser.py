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
# 7. 분석 결과 출력, 바이너리 파일 출력
#    - ZIP 파일 여부 및 압축된 파일 개수 출력

import sys
import shutil
import sys
from pathlib import Path

def is_zip_file(binary_data):
    # ZIP 파일의 시그니처 확인 (0×50 0×4B 0x03 0×04)
    return binary_data[:4] == b'PK\x03\x04'

def count_files_in_zip(binary_data):
    # ZIP 파일 내 파일 개수를 확인하는 간단한 방법
    return binary_data.count(b'PK\x01\x02')

# 입력받은 ZIP 파일을 bin 파일로 반환
def parse_zip(zip_path, output_dir=None):
    # 입력 파일 경로 설정
    zip_path = Path(zip_path)
    
    # 입력 파일 존재 확인
    if not zip_path.exists():
        raise FileNotFoundError(f"ZIP 파일을 찾을 수 없습니다: {zip_path}")

    # 출력 파일 설정
    if output_dir is None:
        output_dir = Path.cwd()
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

    # 출력 파일 경로 설정
    output_path = output_dir / f"{zip_path.stem}.bin"

    # ZIP 파일을 바이너리로 변환 및 복사
    try:
        with open(zip_path, 'rb') as source:
            binary_data = source.read()
            if not is_zip_file(binary_data):
                raise ValueError(f"ZIP 파일이 아닙니다: {zip_path}")
            with open(output_path, 'wb') as dest:
                shutil.copyfileobj(source, dest)
        print(f"ZIP 파일 내 파일 개수: {count_files_in_zip(binary_data)}")
        return str(output_path)
    except Exception as e:
        print(f"파일 변환 중 오류가 발생했습니다: {e}")
        raise

# 터미널에서 실행
if __name__ == "__main__":
    # 파일 입력 확인
    if len(sys.argv) < 2:
        print("사용법: python3 ParseZIP.py <zip_file_path> [output_directory]")
        sys.exit(1)
    
		# 파일 변환
    zip_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        output_path = parse_zip(zip_path, output_dir)
        print(f"파일이 성공적으로 저장되었습니다: {output_path}")
    except Exception as e:
        print(f"파일 변환 중 오류가 발생했습니다: {e}")
        sys.exit(1)
