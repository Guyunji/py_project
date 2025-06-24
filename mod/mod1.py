print('mod/mod1.py 시작')

print('모듈 이름:', __name__)
PI = 3.14 # 변수

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

print('mod/mod1.py 끝')

if __name__ == '__main__':
    # 실행포인트트
    # mode1 프로그램의 처음 실행위치 X, 모듈로써 역할
    # 테스트 : PT 변수 선언/할당, add함수, sub함수
    print(PI)
    print(add(10,3))
    print(add(10,9))
    