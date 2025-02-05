import struct
from utils import format_file_signature

def parse_end_of_central_directory_record(binary_data):
    # 엔드 오브 센트럴 디렉토리 레코드 시그니처 확인
    eocd_signature = b'PK\x05\x06'
    eocd_offset = binary_data.rfind(eocd_signature)
    if eocd_offset == -1:
        print("엔드 오브 센트럴 디렉토리 레코드를 찾을 수 없습니다.")
        return
    
    print(f"엔드 오브 센트럴 디렉토리 레코드 오프셋: {eocd_offset}")
    # 엔드 오브 센트럴 디렉토리 레코드 기본 크기 (24바이트) 읽기
    eocd_base = struct.unpack('<4s4H2L1H', binary_data[eocd_offset:eocd_offset+22])
    file_signature = eocd_base[0]
    disk_number = eocd_base[1]
    disk_with_cd = eocd_base[2]
    total_entries_disk = eocd_base[3]
    total_entries_zip = eocd_base[4]
    size_of_cd = eocd_base[5]
    offset_of_cd = eocd_base[6]
    zip_file_comment_length = eocd_base[7]

    # ZIP 파일 코멘트 읽기
    zip_file_comment = binary_data[eocd_offset+22:eocd_offset+22+zip_file_comment_length].decode('utf-8')

    # 파일 시그니처를 0x 형식으로 출력
    file_signature_hex = format_file_signature(file_signature)

    # 출력
    print("# End of central directory record")
    print(f"File signature (Magic Number): {file_signature_hex}") # 16진수로 표현하는게 필요 | 현재 504b0506
    print(f"Disk Start Number: {disk_number}")
    print(f"Disk # w/cd: {disk_with_cd}")
    print(f"Disk Entry: {total_entries_disk}")
    print(f"Total Entry: {total_entries_zip}")
    print(f"Size of Central Directory: {size_of_cd}")
    print(f"Central Header Offset: {offset_of_cd}")
    print(f"Comment Length: {zip_file_comment_length}")
    print(f"Comment: {zip_file_comment}")