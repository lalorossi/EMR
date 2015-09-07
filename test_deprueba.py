Saldo=0
def Recarga(monto):
	Saldo+=monto
	if monto==196:
		Saldo+=34
	elif monto==368:
		Saldo+=92
	return Saldo

def test_recarga():
	assert Recarga(1)=1
	assert Recarga(197)=197
	assert Recarga(196)=230
	assert Recarga(367)=367
	assert Recarga(368)=460