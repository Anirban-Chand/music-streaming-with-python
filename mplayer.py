import requests
import webbrowser
import bs4

song_name = input('Song Name & Artist: ')
song_name = song_name + ' soundcloud'
print('Searching...')
res = requests.get(f"http://google.com/search?q={song_name}")
res.raise_for_status()

soup = bs4.BeautifulSoup(res.content, 'html5lib')
linkElems = soup.findAll('a')
# example - "unforgiven metallica", "animals by maroon5", "shape of you, ed sheeran"  

all_h3_links = []
for link in linkElems:
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
        neat_link = link.get('href').split("?q=")[1].split("&sa=U")[0]
        all_h3_links.append(neat_link)
        print(f"{len(all_h3_links)}. {neat_link}")

print(f'Playing -> {all_h3_links[0]}')
webbrowser.open(all_h3_links[0])
