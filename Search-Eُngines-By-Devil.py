import webbrowser

def Google():
  x = input('Search : ')
  webbrowser.open(
    'https://google.com/search?q=' + x
  Enter()  )

def Bing():
	x = input('Search : ')
	webbrowser.open(
		'https://www.bing.com/search?q=' + x
	Enter()	)

def Go():
	x = input('Search : ')
	webbrowser.open(
		'https://duckduckgo.com/?q=' + x + '&va=z&t=hc&ia=web'
	Enter()	)

def Yahoo():
	x = input('Search : ')
	webbrowser.open(
		'https://yahoo.com/search?q=' + x
	Enter()	)

def Qwant():
	x = input('Search : ')
	webbrowser.open(
		'https://www.qwant.com/?q='+ x +'&t=web'
	Enter()	)

def Yandex():
	x = input('Search : ')
	webbrowser.open(
		'https://yandex.com/search/?text='+ x +'&lr=11500'
	Enter()	)

def Search_Enc():
	x = input('Search : ')
	webbrowser.open(
		'https://www.searchencrypt.com/search?q=' + x
	Enter()	)

def startpage():
	x = input('Search : ')
	webbrowser.open(
		'https://www.startpage.com/sp/search?q=' + x
	Enter()	)

def Ask():
	x = input('Search : ')
	webbrowser.open(
		'https://www.ask.com/web?o=0&l=dir&qo=serpSearchTopBox&q=' + x
	Enter()	)

def Gi():
	x = input('Search : ')
	webbrowser.open(
		'https://gibiru.com/results.html?q='+ x +'#gsc.tab=0&gsc.q='+ x +'&gsc.page=1'
	Enter()	)


def Enter():
	print('''
		Choose Your Search Engine :
		1 = Google
		2 = Bing
		3 = DuckDuckGo
		4 = Yahoo
		5 = Qwant
		6 = Yandex
		7 = Search Encrypt
		8 = StartPage
		9 = Ask
		10 = Gibiru''')
	x = int(input('Choose : '))
	if x == 1:
		Google()
	elif x == 2:
		Bing()
	elif x == 3:
		Go()
	elif x == 4:
		Yahoo()
	elif x == 5:
		Qwant()
	elif x == 6:
		Yandex()
	elif x == 7:
		Search_Enc()
	elif x == 8:
		startpage()
	elif x == 9:
		Ask()
	elif x == 10:
		Gi()
	else :
		print('You Did Choose')


print('''
	Search Engines By Devil :)
	Snap : pz_a9
	IG : qq.hk
	''')
input('Press Enter To See Search Engines....')
 

Enter()