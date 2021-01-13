msg = "Python Kursumuza Hoş Geldiniz. Ben Mustafa Bostan"

# sonuc = msg.upper()
# sonuc = msg.lower()
# sonuc = msg.title()
# sonuc = msg.capitalize()

# sonuc = "abc".islower()

# sonuc = "    abc ".strip()
# sonuc = msg.split()
# sonuc = msg.split('.')

# sonuc = "-".join(sonuc)

# index = msg.index('Hoş')
# sonuc = msg.startswith('A')
# sonuc = msg.endswith('n')

sonuc = msg.replace('Mustafa','Mehmet')
sonuc = msg.lower().replace(' ','-').replace('ş','s').replace('.','').replace('ı','i')


print(sonuc)