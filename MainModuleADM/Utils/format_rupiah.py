from typing import Union


def i_format_rupiah(value: Union[str, float, int], money_code: str = 'Rp', with_decimal: bool = False,
                  titik_format: bool = False):
    str_value = str(float(value))
    separate_decimal = str_value.split(".")
    after_decimal = separate_decimal[0]
    before_decimal = separate_decimal[1]

    reverse = after_decimal[::-1]
    temp_reverse_value = ""

    for index, val in enumerate(reverse):
        if (index + 1) % 3 == 0 and index + 1 != len(reverse):
            temp_reverse_value = temp_reverse_value + val + "."
        else:
            temp_reverse_value = temp_reverse_value + val

    temp_result = temp_reverse_value[::-1]

    # return "Rp " + temp_result  + "," + before_decimal
    if with_decimal:
        if titik_format:
            return f"{money_code}{temp_result.replace('.', ',')}.{before_decimal}"
        else:
            return f"{money_code}{temp_result},{before_decimal}"
    else:
        if titik_format:
            return f"{money_code}{temp_result.replace('.', ',')}"
        else:
            return f"{money_code}{temp_result}"


def i_format_terbilang(value: Union[str, float, int], money_code: Union[str, None] = 'Rupiah'):
    angka = ["", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam",
             "Tujuh", "Delapan", "Sembilan", "Sepuluh", "Sebelas"]
    # hasil = " "
    n = int(value)
    if 0 <= n <= 11:
        hasil = angka[n]
    elif n < 20:
        hasil = i_format_terbilang(n - 10, money_code) + " Belas "
    elif n < 100:
        hasil = i_format_terbilang(n / 10, money_code) + " Puluh " + i_format_terbilang(n % 10, money_code)
    elif n < 200:
        hasil = " Seratus " + i_format_terbilang(n - 100, money_code)
    elif n < 1000:
        hasil = i_format_terbilang(n / 100, money_code) + " Ratus " + i_format_terbilang(n % 100, money_code)
    elif n < 2000:
        hasil = " Seribu " + i_format_terbilang(n - 1000, money_code)
    elif n < 1000000:
        hasil = i_format_terbilang(n / 1000, money_code) + " Ribu " + i_format_terbilang(n % 1000, money_code)
    elif n < 1000000000:
        hasil = i_format_terbilang(n / 1000000, money_code) + " Juta " + i_format_terbilang(n % 1000000, money_code)
    elif n < 1000000000000:
        hasil = i_format_terbilang(n / 1000000000, money_code) + " Milyar " + i_format_terbilang(n % 1000000000, money_code)
    elif n < 1000000000000000:
        hasil = i_format_terbilang(n / 1000000000000, money_code) + " Triliyun " + i_format_terbilang(n % 1000000000000,
                                                                                                  money_code)
    elif n == 1000000000000000:
        hasil = "Satu Kuadriliun"
    else:
        hasil = "Angka Hanya Sampai Satu Kuadriliun"

    if money_code is not None and money_code != '':
        if money_code in hasil:
            hasil = hasil.replace(money_code, '')

        return f"{hasil.lstrip().rstrip().replace('  ', ' ')} {money_code}"
    else:
        return hasil.lstrip().rstrip().replace('  ', ' ')
