from diaries.DiarySample import DiarySample
from diaries.NagataniDiary import NagataniDiary
from diaries.YoheiDiary import YoheiDiary
from diaries.omagariDiary import omagariDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),NagataniDiary(),omagariDiary(),YoheiDiary()]

# ユーザーに検索したい著者名を入力させる
search_author = input("検索したい著者の名前を入力してください: ")

print(f"\n--- {search_author}の日記 ---")

# 🔍 キーワード入力
keyword = input("🔍 検索キーワード（空欄なら全件表示）: ").strip().lower()

# 検索処理
for d in diaries:
    # 検索条件: date, summary, author
    date = d.get_date().lower()
    summary = d.get_summary().lower()
    author = d.get_author().lower()

    if author == search_author.lower() and (keyword == '' or keyword in date or keyword in summary or keyword in author):
        print("---------------------------------")
        print(d.get_date())
        print(d.get_summary())
        print(d.get_author())
        print()
