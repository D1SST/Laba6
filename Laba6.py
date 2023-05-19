#Вариант 5. Предприятие может предоставить работу по одной специальности 4 женщинам, по другой - 6 мужчинам,
# по третьей - 3 работникам независимо от пола. Сформировать все возможные варианты заполнения вакантных мест,
# если имеются 14 претендентов: 6 женщин и 8 мужчин.

import itertools


def distribute_applicants(women, men):
    options = []

    for women_option in itertools.combinations(women, 4):
        remaining_women = [w for w in women if w not in women_option]

        for men_option in itertools.combinations(men, 6):
            remaining_men = [m for m in men if m not in men_option]

            for women_option_specialty3 in itertools.combinations(remaining_women, 2):
                remaining_women_specialty3 = [w for w in remaining_women if w not in women_option_specialty3]

                for man_option_specialty3 in itertools.combinations(remaining_men, 1):
                    option = {
                        'Специальность 1 (women)': list(women_option),
                        'Специальность 2 (men)': list(men_option),
                        'Специальность 3': list(women_option_specialty3) + list(man_option_specialty3)
                    }

                    if 'W5' in option['Специальность 1 (women)'] or 'W6' in option['Специальность 1 (women)']:
                        continue

                    if len(option['Специальность 2 (men)']) < 4:
                        continue

                    # Ограничение: Количество мужчин по специальности 2 не должно превышать количество женщин более чем на 2
                    if len(option['Специальность 2 (men)']) > len(option['Специальность 1 (women)']) + 2:
                        continue

                    options.append(option)

    for women_option in itertools.combinations(women, 4):
        remaining_women = [w for w in women if w not in women_option]

        for men_option in itertools.combinations(men, 6):
            remaining_men = [m for m in men if m not in men_option]

            for woman_option_specialty3 in itertools.combinations(remaining_women, 1):
                remaining_women_specialty3 = [w for w in remaining_women if w != woman_option_specialty3[0]]

                for men_option_specialty3 in itertools.combinations(remaining_men, 2):
                    option = {
                        'Специальность 1 (women)': list(women_option),
                        'Специальность 2 (men)': list(men_option),
                        'Специальность 3': list(woman_option_specialty3) + list(men_option_specialty3)
                    }

                    if 'W5' in option['Специальность 1 (women)'] or 'W6' in option['Специальность 1 (women)']:
                        continue

                    if len(option['Специальность 2 (men)']) < 4:
                        continue

                    # Ограничение: Количество мужчин по специальности 2 не должно превышать количество женщин более чем на 2
                    if len(option['Специальность 2 (men)']) > len(option['Специальность 1 (women)']) + 2:
                        continue

                    options.append(option)

    return options


women = ['W1', 'W2', 'W3', 'W4', 'W5', 'W6']
men = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M7', 'M8']

options = distribute_applicants(women, men)

# Оптимизация: Максимально увеличить общее количество сотрудников, назначенных на специальность 2
options.sort(key=lambda option: len(option['Специальность 2 (men)']), reverse=True)

for i, option in enumerate(options, 1):
    print(f"Option {i}")
    for specialty, employees in option.items():
        print(f"{specialty}: {employees}")
    print()
