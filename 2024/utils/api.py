import requests
from enum import Enum
from os.path import exists


def get_session_id(filename):
    with open(filename) as f:
        return f.read().strip()


def get_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}/input"


YEAR = 2024
SESSION_ID_FILE = "session.cookie"
SESSION = get_session_id(SESSION_ID_FILE)
HEADERS = {
    "User-Agent": "github.com/tomfran/advent-of-code-setup reddit:u/fran-sch, discord:@tomfran#5786"
}
COOKIES = {"session": SESSION}


class Status(Enum):
    PASS = 0
    FAIL = 1
    RATE_LIMIT = 2
    COMPLETED = 3
    NOT_LOGGED_IN = 4
    UNKNOWN = 5


def get_input(day):
    path = f"inputs/{day:02d}"

    if not exists(path):
        url = get_url(YEAR, day)
        response = requests.get(url, headers=HEADERS, cookies=COOKIES)
        if not response.ok:
            raise RuntimeError(
                f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
            )
        with open(path, "w") as f:
            f.write(response.text[:-1])

    with open(path, "r") as f:
        return f.read()


def submit_result(year, day, part, answer):
    payload = {"level": part, "answer": answer}
    r = requests.post(
        f"https://adventofcode.com/{year}/day/{day}/answer",
        data=payload,
        cookies=COOKIES,
        headers=HEADERS,
    )
    response = r.text
    if "That's the right answer" in response:
        return Status.PASS, None
    elif "That's not the right answer" in response:
        return Status.FAIL, None
    elif "You gave an answer too recently" in response:
        return Status.RATE_LIMIT, None
    elif "Did you already complete it?" in response:
        return Status.COMPLETED, None
    elif "[Log In]" in response:
        return Status.NOT_LOGGED_IN, None
    else:
        return Status.UNKNOWN, response
