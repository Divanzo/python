#a,b=map(int, input().split())

#if a>0 and b<=45: 
#	print(f"{a-1} {60+b-45}")

#elif a==0:
#	print(f'{23} {b+60-45}')

#elif a>0:
#	print(f"{a} {b-45}")
a, b = map(int, input().split())

if b < 45:  # 분이 45보다 작으면
    a = (a - 1) % 24  # 시간이 0이면 23으로 변경
    b += 60  # 60분을 더해줌

b -= 45  # 45분 차감
print(a, b)