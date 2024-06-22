import csv, requests
from fake_useragent import UserAgent
from http import HTTPStatus

def get_websites(csv_path: str) -> list[str]:
    websites: list[str] = []
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])
        return websites


def get_user_agent() -> str:
    ua = UserAgent()
    return ua.chrome

def get_status(status_code: int) -> str:
    for value in HTTPStatus:
        if value == status_code:
            description: str = f'({value} {value.name}) {value.description}'
            return description

    return '(???) unknown status code'


def check_websites(websites: str, user_agent):
    try:
        code: int = requests.get(websites, headers={'User-agent': user_agent}).status_code
        print(websites, get_status(code))
    except Exception:
        print(f'**Could not get information for website: "{websites}"')

def main():
    sites: list[str] = get_websites('websites.csv')
    user_agent: str = get_user_agent()

    for site in sites:
        check_websites(site, user_agent)

if __name__ == '__main__':
    main()
