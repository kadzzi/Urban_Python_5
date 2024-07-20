from time import sleep


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for i in range(len(self.users)):
            if self.users[i].nickname == nickname and self.users[i].password == hash(password):
                self.current_user = self.users[i]

    def register(self, nickname, password, age):
        if nickname in [self.users[x].nickname for x in range(len(self.users))]:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)  # Раз уж зарегистрировался, то сразу и зашел

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            if isinstance(video, Video):
                if video.title not in [self.videos[x].title for x in range(len(self.videos))]:
                    self.videos.append(video)

    def get_videos(self, key_str):
        result = []
        for video in self.videos:
            if key_str.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, exact_title):
        for video in self.videos:
            if video.title == exact_title:
                if self.current_user is None:
                    print('Войдите в аккаунт, чтобы смотреть видео')
                elif self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    self.playback(video)

    def playback(self, video):
        for second in range(video.duration):
            sleep(1)
            video.time_now += 1
            print(video.time_now, end=' ')
        video.time_now = 0
        print('Конец видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

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
print(ur.current_user.nickname)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
