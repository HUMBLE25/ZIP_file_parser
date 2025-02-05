import struct
from utils import format_file_signature, parse_modification_time


def parse_local_file_headers(binary_data):
    offset = 0
    file_count = 0

    while offset < len(binary_data):
        if binary_data[offset:offset+4] != b'PK\x03\x04':
            # print("로컬 파일 헤더를 찾을 수 없습니다.")
            break
        
        # 고정된 30바이트 읽기
        header = struct.unpack('<4s5H3L2H', binary_data[offset:offset+30])
        file_signature = header[0]
        version_needed = header[1]
        general_purpose_flag = header[2]
        compression_method = header[3]
        mod_time = header[4]
        mod_date = header[5]
        crc32 = header[6]
        compressed_size = header[7]
        uncompressed_size = header[8]
        file_name_length = header[9]
        extra_field_length = header[10]

        # 파일 이름과 추가 필드 읽기
        file_name_bytes = binary_data[offset+30:offset+30+file_name_length]
        extra_field = binary_data[offset+30+file_name_length:offset+30+file_name_length+extra_field_length]

        try:
            file_name = file_name_bytes.decode('utf-8')
        except UnicodeDecodeError:
            file_name = file_name_bytes.decode('latin1')
        
        # 파일 시그니처를 0x 형식으로 출력
        file_signature_hex = '0x' + file_signature[::-1].hex()

        # MS-DOS 시간과 날짜 변환
        mod_datetime = parse_modification_time(mod_time, mod_date)

        print(f"# File {file_count}.")
        print(f"Local File Header File signature (Magic Number): {file_signature_hex}")
        print(f"Version needed to extract: {version_needed}")
        print(f"Flags: {general_purpose_flag}")
        print(f"Compression method: {compression_method}")
        print(f"Moditime/Modidate: {mod_datetime}")
        print(f"Compressed Size/Uncompressed Size: {compressed_size}/{uncompressed_size}")
        print(f"File Name Length/Extra Field Length: {file_name_length}/{extra_field_length}")
        print(f"File Name: {file_name}")
        print("-----------------------")

        offset += 30 + file_name_length + extra_field_length + compressed_size
        file_count += 1