from MainModuleADM.Utils.format_tanggal import i_convert_to_dmy

data1 = '08192001'
data2 = '19082001'
data3 = '20011908'
data4 = '20010819'



hasil1 = i_convert_to_dmy(data1)
hasil2 = i_convert_to_dmy(data2)
hasil3 = i_convert_to_dmy(data3, '%Y%d%m')
hasil4 = i_convert_to_dmy(data4, '%Y%m%d')

print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)

