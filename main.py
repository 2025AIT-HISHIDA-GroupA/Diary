from diaries.DiarySample import DiarySample
from diaries.NagataniDiary import NagataniDiary
from diaries.omagariDiary import omagariDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),NagataniDiary(),omagariDiary()]

# 🔍 キーワード入力
keyword = input("🔍 検索キーワード（空欄なら全件表示）: ").strip().lower()

# 検索処理
for d in diaries:
    # 検索条件: date, summary, author
    date = d.get_date().lower()
    summary = d.get_summary().lower()
    author = d.get_author().lower()

    if keyword == '' or (keyword in date or keyword in summary or keyword in author):
        print("---------------------------------")
        print(d.get_date())
        print(d.get_summary())
        print(d.get_author())
        print()
