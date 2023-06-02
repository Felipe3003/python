parede = float(input('largura da parede '))
altura_parede = float(input('altura da parede '))

area =  parede * altura_parede

tinta = area / 2 

print('A sua parede tem a dimensão de {}x{} e sua area é {} m² e ira precisar de {} L de tinta'.format(parede ,altura_parede, area, tinta))