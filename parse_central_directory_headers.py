import struct
from utils import format_file_signature, parse_modification_time

def parse_central_directory_headers(binary_data):
    offset = 0
    file_count = 0

    while offset < len(binary_data):
        # 중앙 디렉토리 헤더 시그니처 확인
        if binary_data[offset:offset+4] != b'PK\x01\x02':
            offset += 1
            continue
        
        # 중앙 디렉토리 헤더 파싱
        header = struct.unpack('<4s2H2H2H3L5H2L', binary_data[offset:offset+46])
        file_signature = header[0]
        version_made_by = header[1]
        version_needed = header[2]
        general_purpose_flag = header[3]
        compression_method = header[4]
        mod_time = header[5]
        mod_date = header[6]
        crc32 = header[7]
        compressed_size = header[8]
        uncompressed_size = header[9]
        file_name_length = header[10]
        extra_field_length = header[11]
        file_comment_length = header[12]
        disk_start_number = header[13]
        internal_file_attributes = header[14]
        external_file_attributes = header[15]
        local_header_offset = header[16]

        # 파일 이름, 추가 필드, 파일 코멘트 읽기
        file_name = binary_data[offset+46:offset+46+file_name_length].decode('utf-8')
        extra_field = binary_data[offset+46+file_name_length:offset+46+file_name_length+extra_field_length]
        file_comment = binary_data[offset+46+file_name_length+extra_field_length:offset+46+file_name_length+extra_field_length+file_comment_length]

        # 파일 시그니처를 0x 형식으로 출력
        file_signature_hex = format_file_signature(file_signature)

        # 수정 시간 변환
        mod_datetime = parse_modification_time(mod_time, mod_date)

        # 출력
        print(f"Central Directory File header File signature (Magic Number): {file_signature_hex}")
        print(f"Version made by: {version_made_by}")
        print(f"Version needed to extract (minimum): {version_needed}")
        print(f"Flags: {general_purpose_flag}")
        print(f"Compression method: {compression_method}")
        print(f"Moditime/Modidate: {mod_datetime}")
        print(f"Compressed Size/Uncompressed Size: {compressed_size}/{uncompressed_size}")
        print(f"File Name Length/Extra Field Length: {file_name_length}/{extra_field_length}")
        print(f"File Comment Length: {file_comment_length}")
        print(f"Disk Start Number: {disk_start_number}")
        print(f"Internal Attribute: {internal_file_attributes}")
        print(f"External Attribute: {external_file_attributes}")
        print(f"Local Header: {local_header_offset}")
        print(f"File Name: {file_name}")
        print("-----------------------")

        # 다음 파일로 이동
        offset += 46 + file_name_length + extra_field_length + file_comment_length
        file_count += 1