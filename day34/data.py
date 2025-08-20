
import requests


QUIZ_API = "https://opentdb.com/api.php"

try:
    r_quiz = requests.get(
        url=QUIZ_API,
        params={
            "amount": 10,
            "type": "boolean"
        }
    )
    r_quiz.raise_for_status()
except requests.exceptions.HTTPError as err:
    SystemExit(err)


question_data = r_quiz.json()['results']
print(type(question_data))