from bs4 import BeautifulSoup 
from urllib.request import * 
from urllib.parse import * 
from os import makedirs 
import os.path, time, re 

# check whether processed before
proc_files = {} 

# Extrac links in the HTML files
def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("links[rel = 'stylesheet']") 
    links += soup.select("a[href]")
    result = [] 

    # extract href properties, and transform the links into absolute link format 
    for a in links: 
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)
    return result 

# Download and save files
def download_file(url):
    o = urlparse(url) 
    savepath = "./"+o.netloc + o.path 
    if re.search(r"/$", savepath): #if folder, index.html 
        savepath += "index.html"
    savedir = os.path.dirname(savepath) 
    # all files downloaded?
    if os.path.exists(savepath): 
        return savepath 
    # Make folder to download
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir) 
    # Download 
    try:
        print("download=", url)
        urlretrieve(url, savepath)
        time.sleep(1) # 1 minute rest 
        return savepath 
    except:
        print("Fail Download: ", url)
        return None 

# HTML parse and download 
def analyze_html(url, root_url):
    savepath = download_file(url) 
    if savepath is None:
        return 
    if savepath in proc_files:
        return # already processed. So no additional working
    proc_files[savepath]=True 
    print("analyze_html=", url) 
    # Extract links 
    html = open(savepath, "r", encoding = "utf-8").read() 
    links = enum_links(html, url) 

    for link_url in links:
        # if not root path, ignore
        if link_url.find(root_url) !=0:
            if not re.search(r".css$", link_url): continue 
        # if HTML,
        if re.search(r".(html|htm)$", link_url):
            # recursively analyzie 
            analyze_html(link_url, root_url)
            continue
        # the rest 
        download_file(link_url)
if __name__ =="__main__":
    # downaload all in the URL 
    url = "https://docs.python.org/3.7/library/"
    analyze_html(url, url)