from diaries.DiarySample import DiarySample
from diaries.NagataniDiary import NagataniDiary
from diaries.YoheiDiary import YoheiDiary
from diaries.omagariDiary import omagariDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),NagataniDiary(),omagariDiary(),YoheiDiary()]

# ユーザーに検索したい著者名を入力させる
search_author = input("検索したい著者の名前を入力してください: ")

print(f"\n--- {search_author}の日記 ---")

for d in diaries:
    if d.get_author() == search_author:
        print("---------------------------------")
        print(d.get_date())
        print(d.get_summary())
        print(d.get_author())
        print()
