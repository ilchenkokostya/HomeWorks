import time


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user

    def register(self, nickname, password, age):
        for item in self.users:
            if nickname == item.nickname:
                print(f"Пользователь {nickname} уже существует")
                break  # выходим из цикла
        else:
            user = User(nickname, password, age)
            self.users.append(user)  # добавляем пользователя в список
            self.log_out()
            self.log_in(nickname, password)  # авторизуем нового пользователя

    def log_out(self):
        self.current_user = None  # очищаем сессию

    def add(self, *value):
        self.videos += set(value)  # добавляем видео в список убирая двойников

    def get_videos(self, search: str):
        return [item.title for item in self.videos if search.lower() in item.title.lower()]

    def watch_video(self, video_id):
        if self.current_user:

            if self.current_user and self.current_user.age < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
            else:
                for video in self.videos:
                    if video_id in video.title:
                        for i in range(video.duration):
                            print(i + 1, end=' ')
                            time.sleep(1)
                        print('Конец видео')
                        break
                else:
                    print('Видео не найдено')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title  # заголовок
        self.duration = duration  # продолжительность
        self.time_now = time_now
        self.adult_mode = adult_mode  # ограничение по возрасту


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname  # имя пользователя
        self.password = hash(password)  # пароль пользователя
        self.age = age  # возраст пользователя

    def __str__(self):
        return f'user: {self.nickname} pwd: {self.password} age: {self.age}'


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2, v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
