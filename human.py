from data import *
import random

YEAR = '2018'
out_humans = []
out_players = []
out_referees = []
out_managers = []


def main():
    append_players()
    append_referees()
    append_managers()
    write('human', ['id', 'name', 'nationality', 'age'], out_humans)
    write('player', ['id', 'team_id', 'number', 'goal'], out_players)
    write('coach', ['id', 'team_id'], out_managers)
    write('referee', ['id', 'type'], out_referees)


def append_players():
    for player in players:
        key_id, player_id, family_name, given_name, birth_date, goal_keeper, defender, \
        midfielder, forward, count_tournaments, list_tournaments, player_wikipedia_link = player

        if YEAR not in list_tournaments:
            continue

        apr = list(filter(lambda p: player_id == p[13] and YEAR in p[2], player_apr))

        if len(apr) == 0:
            continue

        name = f'{given_name} {family_name}'
        team_id, team_name, shirt_number = apr[0][8], apr[0][9], apr[0][16]
        age = '' if birth_date in ['', 'not available'] else 2018 - int(birth_date.split('-')[0])
        goal = 0

        out_humans.append([player_id, name, team_name, age])
        out_players.append([player_id, team_id, shirt_number, goal])


def append_referees():
    for referee in referees:
        key_id, referee_id, family_name, given_name, country_name, confederation_id, \
        confederation_name, confederation_code, referee_wikipedia_link = referee

        apt = list(filter(lambda r: referee_id == r[3] and YEAR in r[2], referee_apt))

        if len(apt) == 0:
            continue

        name = f'{given_name} {family_name}'
        age = random.randint(30, 50)

        out_humans.append([referee_id, name, country_name, age])
        out_referees.append([referee_id, 'head'])


def append_managers():
    for manager in managers:
        key_id, manager_id, family_name, given_name, country_name, manager_wikipedia_link = manager

        apt = list(filter(lambda m: manager_id == m[6] and YEAR in m[2], manager_apt))

        if len(apt) == 0:
            continue

        name = f'{given_name} {family_name}'
        age = random.randint(30, 50)
        team_id, team_name = apt[0][3], apt[0][4]

        out_humans.append([manager_id, name, team_name, age])
        out_managers.append([manager_id, team_id])


if __name__ == '__main__':
    main()
