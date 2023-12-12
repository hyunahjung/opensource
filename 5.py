def solution(numbers):
    # 매개변수로 numbers를 갖는 solution 함수 선언
    answer = ''
    if numbers.count(0) == len(numbers):
        return "0"
        #모든 숫자가 0으로 이루어져 있는 경우 "0"을 반환
    for i in range(0, len(numbers)):
        numbers[i] = str(numbers[i])
        #각 숫자를 문자열로 변환
    numbers.sort(reverse=True)
    # 숫자를 문자열로 변환하여 내림차순으로 정렬
    i = 1
    while i <= len(numbers) - 1:
        #두 숫자를 조합하여 비교하여 정렬
        if numbers[i] + numbers[i - 1] > numbers[i - 1] + numbers[i]:
            a = numbers[i - 1]
            numbers[i - 1] = numbers[i]
            numbers[i] = a
            i -= 2
        i += 1
    for i in range(0, len(numbers)):
        answer += numbers[i]
    #정렬된 숫자를 for문을 이용하여 문자열로 이어붙임
    return answer
    #정렬된 숫자들을 문자열 형태로 반환

numbers = [8, 30, 17, 2, 23]
#주어진 numbers 리스트
result = solution(numbers)
#solution 함수를 호출하여 가장 큰 수를 구함
print(result)
#결과 출력
