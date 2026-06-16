import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "YOUR_NEWS_API_KEY"

def get_news():
    topic = entry.get()

    if not topic:
        messagebox.showwarning("warning", "Please enter a topic")
        return
    

    url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&language=en&apiKey={API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()
        print(data)

        news_box.delete(1.0, tk.END)
        if data["status"] == "ok":
            articles = data["articles"][:10]

            if not articles:
                news_box.insert(tk.END, "No news found.")
                return
            
            for i, article in enumerate(articles, start=1):
                title = article["title"]
                source = article["source"]["name"]
                link = article["url"]

                news_box.insert(
                    tk.END,
                    f"{i}. {title}\n"
                    f"Source: {source}\n"
                    f"Link: {link}\n\n"
                )
        else:
            news_box.insert(tk.END, "Failed to fetch news.")

    except Exception as e:
        messagebox.showwarning("Error", str(e))

root = tk.Tk()
root.title("News App")
root.geometry("800x600")

title_label = tk.Label(
    root,
    text="Python News App",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

search_button = tk.Button(
    root,
    text="Search News",
    command=get_news
)
search_button.pack(pady=5)

news_box = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Arial", 11)
)
news_box.pack(
    fill=tk.BOTH,
    expand= True,
    padx=10,
    pady=10
)

root.mainloop()
