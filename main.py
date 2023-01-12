from data import *
import random

YEAR = '2018'
out_humans = []
out_players = []
out_referees = []
out_managers = []
out_referee_teams = []


def main():
    append_players()
    append_managers()
    append_referees()
    write('human', ['id', 'name', 'nationality', 'age'], out_humans)
    write('player', ['id', 'team_id', 'number', 'goal'], out_players)
    write('coach', ['id', 'team_id'], out_managers)
    write('referee', ['id', 'type'], out_referees)
    write('referee_team', ['id', 'head_id', 'assistant1_id', 'assistant2_id', 'fourth_id', 'var_id'], out_referee_teams)


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


def append_referees():
    head_referees = []

    for head_referee in referees:
        apt = list(filter(lambda r: head_referee[1] == r[3] and YEAR in r[2], referee_apt))
        if len(apt) == 0:
            continue

        head_referees.append(head_referee)
        append_referee(head_referee, 'head')

    head_ref_ids = list(map(lambda r: r[1], head_referees))
    other_refs = list(filter(lambda r: r[1] not in head_ref_ids, referees))

    assist1 = other_refs[:10]
    assist2 = other_refs[10:20]
    fourth = other_refs[20:30]
    var = other_refs[30:40]

    all_team_names = list(map(lambda t: t[2], teams))

    for i in range(55):
        ref_team_id = f'RT-{"0" if i < 9 else ""}{i + 1}'

        r1 = head_referees[i] if i < len(head_referees) else random.choice(head_referees)
        r2 = assist1[i] if i < len(assist1) else random.choice(assist1)
        r3 = assist2[i] if i < len(assist2) else random.choice(assist2)
        r4 = fourth[i] if i < len(fourth) else random.choice(fourth)
        r5 = var[i] if i < len(var) else random.choice(var)

        out_referee_teams.append([ref_team_id, r1[1], r2[1], r3[1], r4[1], r5[1]])

        all_refs = [r1, r2, r3, r4, r5]

        match = [m for m in matches if ref_team_id == m[8]][0]
        team_id1, team_id2 = match[1], match[2]
        team1 = list(filter(lambda t: team_id1 == t[1], teams))[0]
        team2 = list(filter(lambda t: team_id2 == t[1], teams))[0]
        team1_name, team2_name = team1[2], team2[2]

        for ref in all_refs:
            if ref[4] in [team1_name, team2_name]:
                ref[4] = random.choice(list(filter(lambda tn: tn not in [team1_name, team2_name], all_team_names)))

    for ref in assist1:
        append_referee(ref, 'assistant1')
    for ref in assist2:
        append_referee(ref, 'assistant2')
    for ref in fourth:
        append_referee(ref, 'fourth')
    for ref in var:
        append_referee(ref, 'var')


def append_referee(referee, ref_type):
    key_id, referee_id, family_name, given_name, country_name, confederation_id, \
    confederation_name, confederation_code, referee_wikipedia_link = referee

    name = f'{given_name} {family_name}'
    age = random.randint(30, 50)

    out_humans.append([referee_id, name, country_name, age])
    out_referees.append([referee_id, ref_type])


if __name__ == '__main__':
    main()
