users = {
'8600120484741452':'Abubakr Siddiq\nHamkorbank\nUzcard\nXizmat xaqqi - 0.01%', 
'9860170112477915':'Muxamadsharif\nIpak Yo`li Bank\nHUMO',
'4463090019386948':'Muxamadsharif\nSanoat Qurilish Bank\nVISA Classic',
}
karta = input('Karta raqamini kiriting.\n')
if karta in users:
	print(users[karta])
else:
	print('Karta topilmadi!')
	