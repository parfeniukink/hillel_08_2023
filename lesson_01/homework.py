# MRO


class A:
    pass


class B(A):
    pass


class D(A, B):  # MRO error
    pass


print(D())


# Black formatter
def calcu(name: str = "", age: int = 12):
    return 12


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
