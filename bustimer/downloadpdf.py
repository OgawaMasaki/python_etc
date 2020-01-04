import urllib3


download_url = "http://www.it-hiroshima.ac.jp/about/bustimeH31.12-R2.1.pdf"
request_methods = urllib3.PoolManager()
response = request_methods.request('GET', download_url)
f = open('data/src/bustimer.pdf', 'wb')
f.write(response.data)
f.close()