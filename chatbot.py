# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer

# # Create a new chatbot
# chatbot = ChatBot('My Chatbot')

# # Create a new trainer for the chatbot
# trainer = ChatterBotCorpusTrainer(chatbot)

# # Train the chatbot on the English corpus
# trainer.train("chatterbot.corpus.english")

# # Get a response from the chatbot
# response = chatbot.get_response('Hello, how are you?')

# print(response)

# import requests
# from bs4 import BeautifulSoup

# # The URL of the web page you want to extract images from
# url = "https://example.com"

# # Send a GET request to the URL
# response = requests.get(url)

# # Parse the HTML content of the page using BeautifulSoup
# soup = BeautifulSoup(response.content, "html.parser")

# # Find all image tags on the page
# img_tags = soup.find_all("img")

# # Extract the URLs of the images from the image tags
# img_urls = [img["src"] for img in img_tags]

# # Download each image and save it to a file
# for url in img_urls:
#     response = requests.get(url)
#     with open(url.split("/")[-1], "wb") as f:
#         f.write(response.content)
