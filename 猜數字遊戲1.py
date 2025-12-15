import random

answer = random.randint(0, 100)
guess = None

print("🎯 猜數字遊戲開始！")
print("請猜一個 0 到 100 之間的整數")

while guess != answer:
    guess = int(input("請輸入你的猜測："))

    if guess > answer:
        print("太大了！再小一點 👇")
    elif guess < answer:
        print("太小了！再大一點 👆")
    else:
        print("🎉 恭喜你，猜中了！答案是", answer)
import random

answer = random.randint(0, 100)
guess = None

print("🎯 猜數字遊戲開始！")
print("請猜一個 0 到 100 之間的整數")

while guess != answer:
    guess = int(input("請輸入你的猜測："))

    if guess > answer:
        print("太大了！再小一點 👇")
    elif guess < answer:
        print("太小了！再大一點 👆")
    else:
        print("🎉 恭喜你，猜中了！答案是", answer)
