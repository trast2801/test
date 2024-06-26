
team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451


def challenge_result():
    if score1 > score2 or score1 == score2 and team1_time > team2_time:
        return 'Победа команды Мастера кода!'
    elif score1 < score2 or score1 == score2 and team1_time < team2_time:
        return 'Победа команды Волшебники Данных!'
    else:
        return 'Ничья!'

tasks_total = score1 + score2
time_avg = (team1_time + team2_time)/2

print("В команде Мастера кода участников: %d !" % (team1_num))
print("В команде Волшебники данных: %d !" % (team2_num))
print('Итого сегодня в командах участников: %d и %d !\n' % (team1_num, team2_num))

print('Команда Мастера кода решила задач: {0} !'.format(score1))
print('Команда Волшебники данных решила задач: {0} !\n'.format(score2))
print('Мастера кода решили задачи за {0:4.1f} с !'.format(team1_time))
print('Волшебники данных решили задачи за {0:4.1f} с !'.format(team2_time))

print(f'Команды решили {score1} и {score2} задач.\n')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:4.1f} секунды на задачу!.')
print(challenge_result())




