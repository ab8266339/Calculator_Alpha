from urllib.request import urlopen
import re
input_string = "inverse Laplace transform 1/(s^2+1)"
html5_encoding={
    '\'':'%27',
    ' ':'%20',
}
for key, values in html5_encoding.items():
    input_string = input_string.replace(key, values)
    
#url_input = 'http://api.wolframalpha.com/v2/query?appid=W28765-8VEPU3RR3P&input={}&format=image,plaintext'.format("1 plus 1")
url_input = 'http://api.wolframalpha.com/v2/query?appid=W28765-8VEPU3RR3P&input={}&format=image,plaintext'.format(input_string)
print (url_input)
with urlopen(url_input) as response:
   html = response.read()
   html = html.decode('utf-8')
   html = html.replace("\n","")
   pod_re1 = [r'<pod[^>]*title=\'Result\'[^>]*>.*?</pod>|',
              r'<pod[^>]*title=\'Decimal approximation\'[^>]*>.*?</pod>|',
              r'<pod[^>]*title=\'Alternative representations\'[^>]*>.*?</pod>|',
              r'<pod[^>]*title=\'Series representations\'[^>]*>.*?</pod>|',
              r'<pod[^>]*title=\'Integral representations\'[^>]*>.*?</pod>|',
              r'<pod[^>]*title=\'Solution\'[^>]*>.*?</pod>|',
              r'<pod[^>]*title=\'Substitution\'[^>]*>.*?</pod>|',
              ]
   pod_re = ''
   pod_re = pod_re.join(pod_re1)
   pod_re = r'(' + pod_re[:len(pod_re)-1] + r')'
   print (pod_re)
   pod_div = re.findall(pod_re, html)
   result = re.findall(r'<plaintext>(.*)</plaintext>',pod_div[0])
   #result = re.findall(r'<pod.*?Result>[^(pod)]*<plaintext>(.+)</plaintext>[^(pod)]*</pod>',result)
   print (result)


#<pod[^(pod)]*Result[^(pod)]*>
