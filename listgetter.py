import requests

print("This Script Can Help You To Get Custom Proxies")
print('\r\n')


type = str(input("Type ( socks4 / socks5 / proxy ) : "))
cty = str(input("Country (EX : TW / CN / US / all ) : "))
anon = str(input("anonymity ( anonymous / elite / all ) : "))
to = str(input("Timeout : "))
sl = str(input("SSL Mode ( yes / no / all ) : "))
file = str(input("File Name (EX : proxies.txt / socks4.txt / socks5.txt ) : "))
rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype='+str(type)+'&country='+str(cty)+'&anonymity='+str(anon)+'&ssl='+str(sl)+'&timeout='+str(to))
with open(str(file),'wb') as fp:
	fp.write(rsp.content)
