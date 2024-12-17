from MainModuleADM.Utils.validate import is_strong_password, is_valid_email, is_valid_ktp, is_valid_phone

valid_pass = '@Alfiandm123'
invalid_pass = 'abc'

valid_email = 'alfianitem999@gmail.com'
invalid_email = 'abc'

valid_ktp = '1111111111111111'
invalid_ktp = 'abc'

valid_phone = '0895703340802'
invalid_phone = 'abc'

a = is_strong_password(valid_pass)
b = is_strong_password(invalid_pass)

print(a)
print(b)

c = is_valid_email(valid_email)
d = is_valid_email(invalid_email)

print(c)
print(d)

e = is_valid_ktp(valid_ktp)
f = is_valid_ktp(invalid_ktp)

print(e)
print(f)

g = is_valid_phone(valid_phone)
h = is_valid_phone(invalid_phone)

print(g)
print(h)