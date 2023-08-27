import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

import matplotlib.font_manager as fm
import re
import collections
import os

os.system('pip install -r requirements.txt')

user = input()
url = f'https://www.google.com/search?q={user}'
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')
text = soup.text

wc1 = WordCloud(max_font_size=200, font_path='./font/malgun.ttf',
                background_color='white', width=800, height=800)

wc1.generate(text)

plt.figure(figsize=(10,8))
plt.imshow(wc1)
plt.tight_layout(pad=0)
plt.axis('off')
plt.show()