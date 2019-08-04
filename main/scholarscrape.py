import requests as req
import bs4
def scholarscrapy(query):
    url='https://scholar.google.co.in/scholar?q='+query
    res=req.get(url)
    soup=bs4.BeautifulSoup(res.text,'lxml')
    hi=soup.select(".gs_rt")
    html='<html>    <head>    <!--  <link rel="stylesheet" type="text/css" href="gscrape.css"> -->    <style>            .box        {                background-color: dimgrey;    padding-top: 3px;   padding-bottom: 10px;         max-width: 800px;                border: 0px;                padding::0.1rem 0.1rem .5rem 0.1rem;                margin-bottom: 5px;                margin-left: auto;               margin-right:auto;                margin-top: 5px;            text-align: center;                font-size: 100%;                -webkit-transition: background-colour .1s; /                 transition: background-colour .1s;            }            .box:hover            {                background-color: darkgray;            }            .button            {                background-color: blue;                border:none;                color:white;                padding: 10px 20px;                text-align: center;                display: inline-block;                font-size:12px;                text-decoration: none;   -webkit-transition: background-colour .1s; /                 transition: background-colour .1s;           } .button:hover            {                background-color: darkgreen;       </style></head><body>'
    for x in hi:
        try:
            html=html+"<div class='box'>        <p>"
            p=x.contents
            if(len(p)==1):
                m=p[0].attrs
            else:
                m=p[2].attrs
            key='href'
            s=''
            li=(x.find("a").contents)
            for p in li:
                s=s+str(p);
            s=s.replace('<b>','').replace('</b>','')
            html=html+s+'</p>  <a href='        
            if key in m.keys():
                html=html+"'"+m[key]+"' class='button'><b>VISIT</b></a> </div>"
           # else:
             #   html=html+"'#"+"' class='button'><b>Visit</b></a> </div>"
        except:
            html=html+"        <p>I'm sorry,But this is a Citation,Icouldnt display this result.There is no link for this anyway </p> <a href='#' class='button' style='background-color:red;'><b>It Wont Work</b></a> </div> "
    html=html+'</body></html>'
    return html
#scholarscrapy('co2')
