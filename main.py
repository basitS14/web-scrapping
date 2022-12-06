import requests as rq
from bs4 import BeautifulSoup
import array as arr


queue = [] 
author_queue = [] 
time_queue = [] 
date_queue = []
read_more_queue = []
article_queue = []
html_file = rq.get('https://www.inshorts.com/en/read').text

soup = BeautifulSoup(html_file,'lxml')

news_card = soup.find_all('div', class_ = 'news-card z-depth-1')
source_card = soup.find_all('div', class_ = 'news-card-footer news-right-box')
publishers = soup.find_all('div', class_ = "news-card-author-time news-card-author-time-in-title")



for card in news_card:
        headlines = card.find('span',itemprop='headline').text
        queue.append(headlines)

        articals = card.find('div', itemprop = 'articleBody').text
        article_queue.append(articals)

for link in source_card:
    read_more = link.a['href']
    read_more_queue.append(read_more)


for publishers in publishers:
    author_name = publishers.find('span', class_ = "author").text
    author_queue.append(author_name)

    time = publishers.find('span', class_ = "time").text
    time_queue.append(time)

    date = publishers.find('span', clas = "date").text
    date_queue.append(date)

def Main_Body(queue,author_queue,time_queue,read_more_queue,date_queue):
    try:
        for i in  range(len(read_more_queue)):
            print(f'\n"{queue[i]}"') 
            print(f"Author: {author_queue[i]}")
            print(f"{date_queue[i]} {time_queue[i]}")
            print(f"Read Full Article: {read_more_queue[i]}")

    except:
        if (queue == None):
            print("list is empty")




def Save_Articles(search , article_queue):
    
    for i in range(len(queue)):
        if search in queue[i]:
            with open(f'saved/article{i}','w',encoding="utf-8") as f:
                f.write(f'{article_queue[i]}')
                print("File Saved !!!")


if __name__ == '__main__' :
    Main_Body(queue, author_queue, time_queue, read_more_queue, date_queue)
    print("\nHeadlines will change after few minutes .....")
    ch = 1
    while ch == 1:
        print("\nDo you want to save any article?")
        search = input("-> write keywords\n")
        Save_Articles(search, article_queue)

        ch = input("Save another article (1 or 0):")