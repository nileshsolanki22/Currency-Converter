import re,sys,urllib.request

if len(sys.argv)<2:
	print("Usage is currency_converter.py <amt>")
	sys.exit()
if not (sys.argv[1]).isdigit():
	print("argument should be a number")
	sys.exit()	
	
amt = sys.argv[1]
#print(amt)
URL = "https://www.google.com/finance/converter?a="+amt+"&from=USD&to=INR"

with urllib.request.urlopen(URL) as response:
	htmlText = str(response.read())
regex = re.compile("<span.*?>(.*)</span>")

output = regex.search(htmlText)

if output:
	#print(output.group(1))
	print(amt+" USD = "+output.group(1))
	