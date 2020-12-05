def greeting(name: str, **kwargs) -> None:
    greet = f'Hello, {name}'
    if 'age' in kwargs:
        greet = greet + f', age - {kwargs["age"]}'
    print(greet)


def sequence(*args) -> list:
    print([i for i in args])


if __name__ == '__main__':
    # greeting('Masha', age=13, bcd=233)
    sequence(3, 1, 5)

# позиционные аргументы - args
# именованные аргументы - kwargs

