from segno import helpers
# Create a WIFI config with min. error level "L" or better
qrcode = helpers.make_wifi(ssid='xxxxxx', password='xxxxxx', security='WPA')
qrcode.save('xxxxx_principal.png') 
