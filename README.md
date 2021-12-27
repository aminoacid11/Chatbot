# EPL Chatbot
This is a simple Chatbot that provides the users numerous informations of English Premier League (EPL) players. <br />
There are 10 different informations that this chatbot can offer: <br />
Player's jersey number, club name, position, birthday, age, height, market value (in pounds), citizenship, national team caps, and the weight.

Intents.json file contains informations for the chatbot to learn the expected questions and chats by the users and to expected responses to it, with tags for each category. <br />
epl.csv file is the dataset from Kaggle, which went through data cleaning process by deleting the unecessary informations and filling in the empty informations through some researchs. <br />
EPL.py file is a file that contains the codes to retrieves and return the EPL players informations from epl.csv file. <br />
chatbot_train.py file is a file that contains the codes to train the chatbot based on the given intents. <br />
chatbot.py is the file that makes the chatbot visible and to communicate with the users. With the given chat from the user, it predicts its class and the appropriate response. It also provide the requested information from the user, which is returned from EPL.py file.

To start the web application, run:
### `python chatbot.py` or `python3 chatbot.py`

Important notes:
When you request for an information to the chatbot, please provide the name of the player at the end of the chat following ":" <br />
Make sure to provide correct full name of the player in order to obtain accurate information. <br />
(e.g. I want to get the jersey number of : Heung Min Son)
