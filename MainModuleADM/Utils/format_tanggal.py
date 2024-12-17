from datetime import datetime
from dateutil.parser import parse

def i_convert_to_dmy(date_str: str, source_format: str = None) -> str:
    """
    Mengonversi tanggal dari format apapun ke format d-m-y.
    
    :param date_str: Tanggal dalam format asal.
    :param source_format: (Opsional) Format asal dari tanggal, jika diketahui.
    :return: Tanggal dalam format d-m-y (contoh: 17-12-2024).
    """
    try:
        if source_format:
            # Parsing tanggal berdasarkan format sumber
            parsed_date = datetime.strptime(date_str, source_format)
        elif date_str.isdigit() and len(date_str) == 8:
            # Menangani format tanpa pemisah (misal: 19082001 atau 08192001)
            # Coba deteksi d-m-y atau m-d-y
            try:
                parsed_date = datetime.strptime(date_str, "%d%m%Y")  # Format d-m-y
            except ValueError:
                parsed_date = datetime.strptime(date_str, "%m%d%Y")  # Format m-d-y
        else:
            # Jika format tidak diketahui, deteksi otomatis menggunakan dateutil
            parsed_date = parse(date_str)
        # Mengonversi ke format d-m-y
        return parsed_date.strftime("%d-%m-%Y")
    except Exception as e:
        raise ValueError(f"Error parsing date: {e}")


