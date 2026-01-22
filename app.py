import segno
from segno import helpers

# VCARD Personal
vcard = helpers.make_vcard_data(
    name='Last Name, First Name', 
    displayname='First Name Last Name', 
    email = 'name@email.com',
    url= ['www.email.com','https://www.website.com'],
    
    country= 'country',
    city= 'city',
    cellphone='+phone-number')


qrcode = segno.make(vcard, error='H')
qrcode.save('jica_vcard_.png', scale=4)
