from googlesearch import search
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.request

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def google_scrape(url):
    opener = AppURLopener()
    response = opener.open(url)
    soup = BeautifulSoup(response, "html.parser")
    return soup.title.text

def fun(query):
 html='<html><head>    <!-- Compiled and minified CSS --><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">   <!-- Compiled and minified JavaScript --><script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>             </head> <body> <div class="row"><div class="coloumn"'
 try:
  for url in search(query,stop=10):
    try:
      a = google_scrape(url)
      html=html+'   <div class="col s12 m6 l4">        <div class="card blue-grey darken-1"><div class="card-content white-text"><span class="card-title"><p style="font-size:1.5rem">'+a+'</span><p></div><div class="card-action"><a href="'+url+'">This is the link</a></div>         </div>       </div>    '
    except: 
      html=html+'   <div class="col s12 m6 l4">        <div class="card blue-grey darken-1"><div class="card-content white-text"><span class="card-title"><p style="font-size:1.5rem">go check on check this man </span><p></div><div class="card-action"><a href="'+url+'">This is the link</a></div>         </div>       </div>    '  

  html=html+'  </div>  </div> </body></html>'    
  return html
 except:
  html='<html><body>Please check the internet</body></html>'
  return html   






