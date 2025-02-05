from datetime import datetime

def parse_dos_time(dos_time):
    second = (dos_time & 0x1F) * 2
    minute = (dos_time >> 5) & 0x3F
    hour = (dos_time >> 11) & 0x1F
    return hour, minute, second

def parse_dos_date(dos_date):
    day = dos_date & 0x1F
    month = (dos_date >> 5) & 0x0F
    year = ((dos_date >> 9) & 0x7F) + 1980
    return year, month, day

def format_file_signature(file_signature):
    return '0x' + file_signature[::-1].hex()

def parse_modification_time(mod_time, mod_date):
    hour, minute, second = parse_dos_time(mod_time)
    year, month, day = parse_dos_date(mod_date)
    return datetime(year, month, day, hour, minute, second)