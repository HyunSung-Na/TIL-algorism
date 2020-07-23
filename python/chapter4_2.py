# 파이썬 함수 특징
#Decorator & Closer

# 파이썬 변수 범위

from dis import dis
b = 10


def func_v3(a):
    print(a)
    print(b)
    b = 5


print('Ex1-1')
print(dis(func_v3))
print()
# Closer 클로저
# 반환되는 내부함수에 대해서 선언 된 연결을 가지고 참조하는 방식
# 반환 당시 함수 유효범위를 벗어난 변수 또는 메소드에 직접 접근이 가능하다.

a = 10

print('Ex2-1 -', a + 10)
print('Ex2-2 -', a + 100)

print()
print()

# 클래스 이용


class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('class >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성


avg_cls = Averager()

# 누적 확인

print('Ex3-1 -', avg_cls(15))
print('Ex3-2 -', avg_cls(35))
print('Ex3-3 -', avg_cls(40))

print()
print()

# 클로저 사용


def closer_avg1():
    serise = []

    def average(v):
        serise.append(v)
        print('def >>> {} / {}'.format(serise, len(serise)))
        return sum(serise) / len(serise)

    return average


avg_closure1 = closer_avg1()

print('Ex4-1', avg_closure1(15))
print('Ex4-2', avg_closure1(35))
print('Ex4-3', avg_closure1(40))

print('Ex5-1 -', dir(avg_closure1))
print()
print('Ex5-2 -', dir(avg_closure1.__code__))
print()
print('Ex5-3 -', avg_closure1.__code__.co_freevars)
print()
print('Ex5-4 -', dir(avg_closure1.__closure__[0]))
print()
print('Ex5-4 -', dir(avg_closure1.__closure__[0].cell_contents))
