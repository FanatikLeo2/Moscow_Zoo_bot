
TOKEN = 'YOUR_TOKEN'

help_list = f'/start - Запуска бота\n' \
            f'/help - Список команд\n' \
            f'/viktorina - Викторина! Узнай свое тотемное животное!\n' \
            f'/opekun - «Возьми животное под опеку» («Клуб друзей») — Узнать подробнее про систему опекунство'

quiz = {
    'У тебя хороший режим сна?': ['Да', 'Нет', 'Всегда когда можно', 'Живу ночью'],
    'Хорошо ли видишь в темноте?': ['Да', 'Нет', 'Что это такое', 'Нормально'],
    'Быстро ли ты бегаешь?': ['Да', 'Нет', 'Быстрее всех', 'Я не бегаю'],
    'Любишь ли ты высоту?': ['Да', 'Нет', 'Боюсь высоты', 'Люблю полетать']
}

quiz_result = {'cat': {'answer': ['Всегда когда можно', 'Что это такое', 'Да', 'Боюсь высоты'],
                       'photo': './Images/cat.jpg',
                       'text': 'Да ты же у нас Кот!'},
               'lion': {'answer': ['Да', 'Нормально', 'Нет', 'Нет'],
                        'photo': './Images/lion.jpeg',
                        'text': 'Да ты же у нас Лев!'},
               'tiger': {'answer': ['Нет', 'Да', 'Быстрее всех', 'Нет'],
                         'photo': './Images/tiger.jpeg',
                         'text': 'Да ты же у нас Тигр!'},
               'owl': {'answer': ['Живу ночью', 'Да', 'Я не бегаю', 'Люблю полетать'],
                       'photo': './Images/owl.jpg',
                       'text': 'Да ты же у нас Сова!'},
               }

user_selection = {}

guardianship_system = """«Возьми животное под опеку» («Клуб друзей») — это одна из программ, помогающих зоопарку заботиться о его обитателях. Программа позволяет с помощью пожертвования на любую сумму внести свой вклад в развитие зоопарка и сохранение биоразнообразия планеты.\n
Сейчас в Московском зоопарке живёт около 6 000 животных, представляющих примерно 1 100 биологических видов мировой фауны. Каждое животное уникально, и все требуют внимание и уход. Из ежедневного рациона питания животного как раз и рассчитывается стоимость его опеки.\n
Взять под опеку можно разных обитателей зоопарка, например, слона, льва, суриката или фламинго. Это возможность помочь любимому животному или даже реализовать детскую мечту подружиться с настоящим диким зверем. Почётный статус опекуна позволяет круглый год навещать подопечного, быть в курсе событий его жизни и самочувствия.\n
Участником программы может стать любой неравнодушный: и ребёнок, и большая корпорация. Поддержка опекунов помогает зоопарку улучшать условия для животных и повышать уровень их благополучия."""