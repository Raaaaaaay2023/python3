#1
# n = int(input())
# a = list(map(int, input("seperate with space").split()))
# x = int(input())

# count = 0
# for i in range(n):
#     if a[i] == x:
#         count += 1

# print(count)

#2
# n = int(input())
# a = list(map(int, input("seperate with space").split()))
# x = int(input())

# min=a[0]
# for i in range(1,n):
#     if abs(a[i]-x)<abs(min-x):
#         min=a[i]

# print(min)

#3
eng_values = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

rus_values = {'А': 1, 'Б': 3, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 1, 'Ё': 3, 'Ж': 5, 'З': 5, 'И': 1, 'Й': 4, 'К': 2, 'Л': 2, 'М': 2, 'Н': 1, 'О': 1, 'П': 2, 'Р': 1, 'С': 1, 'Т': 1, 'У': 2, 'Ф': 10, 'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Щ': 10, 'Ъ': 10, 'Ы': 4, 'Ь': 3, 'Э': 8, 'Ю': 8, 'Я': 3}

def calculate_score(word):
    score = 0
    for letter in word:
        if letter.upper() in eng_values:
            score += eng_values[letter.upper()]
        elif letter.upper() in rus_values:
            score += rus_values[letter.upper()]
    return score

word = input()
print(calculate_score(word))