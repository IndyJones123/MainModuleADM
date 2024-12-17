from MainModuleADM.Utils.format_rupiah import i_format_rupiah, i_format_terbilang

uang = 100000000
format = '$' #Optional To Change Currency
with_decimal = False #Optional To Change .00 or without 
titik_format = False #Optional To Change . into , Or , into .

formatRp = i_format_rupiah(uang)

formatRp2 = i_format_rupiah(uang,format,with_decimal,titik_format)

formatTerbilang = i_format_terbilang(uang)

print(formatRp)
print(formatRp2)
print(formatTerbilang)