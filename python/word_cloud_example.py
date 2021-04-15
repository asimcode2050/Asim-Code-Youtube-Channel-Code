# https://youtu.be/t6xVoDQETZM
import nltk
from wordcloud import WordCloud
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

freq_dist = nltk.FreqDist({'internet':20,'software':10,'python':100,'asim':50,'code':200})
word_cloud = WordCloud().generate_from_frequencies(freq_dist)
plt.imshow(word_cloud,interpolation="bilinear")
plt.axis("off")
plt.show()
