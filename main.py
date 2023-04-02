import requests as rq
from bs4 import BeautifulSoup
import array as arr
import tkinter as tk
import webbrowser as wb

window = tk.Tk()


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
import os
def read_more(i):
    
    wb.open(f'{read_more_queue[i]}')

    
def Main_Body(queue,author_queue,time_queue,read_more_queue,date_queue):
    try:
        msg = tk.Label(text="News Stand", foreground="black" , background="red", master= window,width = 100).pack()
        
        
        headline = tk.Label(text=f"{queue[0]}", foreground = "black", background="gray", width = 100).pack()
        summary = tk.Label(text=f"{article_queue[0]}", foreground = "black", background= "#ffbd8a",justify="center",wraplength=700, width = 100 ).pack()
        full_news_btn = tk.Button(text="Read more", bg="black", fg="white", border=5, default="active",command= lambda : read_more(0)).pack()

        headline = tk.Label(text=f"{queue[1]}", foreground = "black", background="gray", width = 100).pack()
        summary = tk.Label(text=f"{article_queue[1]}", foreground = "black", background= "#ffbd8a",justify="center",wraplength=700, width = 100 ).pack()
        full_news_btn = tk.Button(text="Read more", bg="black", fg="white", border=5, default="active",command= lambda : read_more(1)).pack()

        headline = tk.Label(text=f"{queue[2]}", foreground = "black", background="gray", width = 100).pack()
        summary = tk.Label(text=f"{article_queue[2]}", foreground = "black", background= "#ffbd8a",justify="center",wraplength=700, width = 100 ).pack()
        full_news_btn = tk.Button(text="Read more", bg="black", fg="white", border=5, default="active",command= lambda : read_more(2)).pack()

        headline = tk.Label(text=f"{queue[3]}", foreground = "black", background="gray", width = 100).pack()
        summary = tk.Label(text=f"{article_queue[3]}", foreground = "black", background= "#ffbd8a",justify="center",wraplength=700, width = 100 ).pack()
        full_news_btn = tk.Button(text="Read more", bg="black", fg="white", border=5, default="active",command= lambda : read_more(3)).pack()


        headline = tk.Label(text=f"{queue[4]}", foreground = "black", background="gray", width = 100).pack()
        summary = tk.Label(text=f"{article_queue[4]}", foreground = "black", background= "#ffbd8a",justify="center",wraplength=700, width = 100 ).pack()
        full_news_btn = tk.Button(text="Read more", bg="black", fg="white", border=5, default="active",command= lambda : read_more(4)).pack()



        
            # print(f'\n"{queue[i]}"') 
            # print(f'\n{article_queue[i]}')
            # print(f"Author: {author_queue[i]}")
            # print(f"{date_queue[i]} {time_queue[i]}")
            # print(f"Read Full Article: {read_more_queue[i]}")
            
    except:
        if (queue == None):
            print("list is empty")




def Save_Articles(search , article_queue):
    
    for i in range(len(queue)):
        if search in queue[i]:
            with open(f'saved/article{i}','w',encoding="utf-8") as f:                            #change file location here
                f.write(f'{article_queue[i]}')
                print("File Saved !!!")


if __name__ == '__main__' :
    Main_Body(queue, author_queue, time_queue, read_more_queue, date_queue)
    window.mainloop()
    # print("\nHeadlines will change after few minutes .....")
    # ch = 1
    # while ch == 1:
    #     print("\nDo you want to save any article?")
    #     search = input("-> write keywords\n")
    #     Save_Articles(search, article_queue)

    #     ch = input("Save another article (1 or 0):")
