import requests
from bs4 import BeautifulSoup
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'football.settings')
django.setup()

from main.models import Teams, Players, Coach

teams_list = []


def get_teams():
    url = 'https://www.uefa.com/uefaeuropaleague/clubs/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    teams = soup.find_all('div', class_='team team-is-club')
    for team in teams:
        team_url = team.find('a', class_='team-wrap').get('href')
        teams_list.append(team_url)



def get_team(link):

    url = 'https://www.uefa.com' + link
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    name = soup.find('span', itemprop='name').text
    badge_tag = soup.find('pk-badge').get('src')

    country = soup.find('span', class_='team-country-name').text

    goals, goals_conceded, possession, passings_accuracy, balls_recovered, tackles_won, clean_sheets, saves, distance_covered, yellow_cards, red_cards = None, None, None, None, None, None, None, None, None, None, None

    stat_elements = soup.find_all('div', class_='stats-module__single-stat')

    for element in stat_elements:
        value_element = element.find('div', {'slot': 'stat-value'})
        if value_element:
            value = value_element.get_text(strip=True)
        else:
            value = None

        label_element = element.find('div', {'slot': 'stat-label'})
        if label_element:
            label = label_element.get_text(strip=True)
        else:
            label = None

        try:
            if label == 'Goals':
                goals = value
            elif label == 'Goals conceded':
                goals_conceded = value
            elif label == 'Possession (%)':
                possession = float(value.split('%')[0])
            elif label == 'Passing accuracy (%)':
                passings_accuracy = float(value.split('%')[0])
            elif label == 'Balls recovered':
                balls_recovered = value
            elif label == 'Tackles won':
                tackles_won = value
            elif label == 'Clean sheets':
                clean_sheets = value
            elif label == 'Saves':
                saves = value
            elif label == 'Distance covered (km)':
                distance_covered = float(value)
            elif label == 'Yellow cards':
                yellow_cards = value
            elif label == 'Red cards':
                red_cards = value

        except (ValueError, AttributeError):
            # Обработка случаев, когда данные отсутствуют или не могут быть преобразованы
            pass

    try:
        # Создаем команду
        team = Teams.objects.create(
            name=name,
            country=country,
            logo=badge_tag,
            goals=goals,
            goals_conceded=goals_conceded,
            possession=possession,
            passings_accuracy=passings_accuracy,
            balls_recovered=balls_recovered,
            tackles_won=tackles_won,
            clean_sheets=clean_sheets,
            saves=saves,
            distance_covered=distance_covered,
            yellow_cards=yellow_cards,
            red_cards=red_cards,
            league_id=2
        )
        return team
    except Exception as e:
        print(f"Ошибка при создании команды: {e}")
        return None


def get_players(link, id):
    url = 'https://www.uefa.com' + link + 'squad/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Нахождение всех строк таблицы с помощью BeautifulSoup
    rows = soup.find_all('pk-table-row', class_='row--squadlist')

    # Цикл для извлечения информации о каждом футболисте
    for row in rows:
        full_name = row.find(itemprop='name').get_text(strip=True)
        print(full_name)
        nationality = row.find('div', itemprop='country').get_text(strip=True)

        # Поиск ячейки с возрастом
        age_cell = row.find('pk-table-cell', {'column-key': 'age'})
        age = age_cell.get_text(strip=True) if age_cell else "N/A"

        # Поиск ячейки с количеством сыгранных матчей
        matches_cell = row.find('pk-table-cell', {'column-key': 'matches'})
        matches_played = matches_cell.get_text(strip=True) if matches_cell else "N/A"

        # Поиск ячейки с фото
        image_cell = row.find('pk-avatar')
        image_url = image_cell['src'] if image_cell else "N/A"

        # Вывод информации о каждом футболисте
        print(f"Full Name: {full_name}")  # Убираем звездочку из имени, если она есть
        print(f"Nationality: {nationality}")
        print(f"Age: {age}")
        print(f"Matches Played: {matches_played}")
        print(f"Image URL: {image_url}")
        print("-------------------")

        # Создаем футболиста
        player = Players.objects.create(
            name=full_name,
            age=age,
            nationality=nationality,
            photo=image_url,
            matches_played=matches_played,
            team_id=id)

def get_coach(link, id):
    url = 'https://www.uefa.com' + link + 'squad/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    coach_cell = soup.find('pk-table-cell', {'column-key': 'coach'})
    coach_name = coach_cell.find('span', {'slot': 'primary'}).get_text(strip=True)
    coach_image = coach_cell.find('pk-avatar')['src']

    print("Name of the coach:", coach_name)
    print("Image URL of the coach:", coach_image)

    coach = Coach.objects.create(
        name=coach_name,
        photo=coach_image,
        team_id=id)


id = 177
get_teams()
# for team in teams_list:
#     get_team(team)
# #
for team in teams_list:
    get_players(team, id)
    get_coach(team, id)
    id += 1


# id = 80
# get_teams()
#
# for team in teams_list:
#     get_coach(team, id)
#     id += 1



