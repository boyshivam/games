import requests

class QuestionList:

    # request for questions according to custom parameters
    def __init__(self):
        parameters = {
            'amount': {str(self.amount())},
            'catergory': f"{self.catergory()}",
            'type': 'boolean',
            'difficulty': f'{self.difficulty()}'
        }
        response = requests.get("https://opentdb.com/api.php", params=parameters)
        response.raise_for_status()
        self.questions = response.json()['results']


    # how many questions you want
    def amount(self):
        amount = input("Enter the number of questions you want(upto 30): ")
        if amount.isdigit():
            return amount
        else:
            print("Enter digits only.")
            return


    # select difficulty of the questions
    def difficulty(self):
        select_difficulty = input("Enter difficulty between 'easy', 'medium' and 'hard'.").lower()
        if select_difficulty == "easy" or select_difficulty == 'medium' or select_difficulty == 'hard':
            return select_difficulty
        else:
            print("Select from the given options only.")
            return

    # select catergory of question
    def catergory(self):
        catergories = {
            'Animals': '27',
            'Anime & Manga': '31',
            'Computers': '18',
            'Films': '11',
            'General_knowledge' : '9',
            'History' : '23',
            'Science & nature' : '17',
            'Sports': '21',
            'Vehicles' : '28',
        }
        options = ""
        list = [key for key, value in catergories.items()]
        for item in list:
            options += f"{item}\n"
        select_catergory = input(f"Enter the catergory from the following options:\n{options}").title()
        item_num = catergories[select_catergory]
        return item_num


