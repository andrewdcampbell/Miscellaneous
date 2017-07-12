# To get a text file of all commit messages for a repository:
# git log --format=%B > ~/Downloads/commits.txt

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

font_path = "/Library/Fonts/DIN Condensed Bold.ttf"

# Read the whole text.
text = open(path.join(d, 'alice.txt')).read().upper()

# read the mask / color image 
cap_coloring = np.array(Image.open(path.join(d, "cap_logo.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(font_path=font_path, background_color="black", max_words=5000, 
				mask=cap_coloring, stopwords=stopwords, max_font_size=250, 
				min_font_size=12, font_step=2, random_state=42)

# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(cap_coloring)
wc.recolor(color_func=image_colors)

# save
wc.to_file(path.join(d, "cap_logo_wordcloud.png"))