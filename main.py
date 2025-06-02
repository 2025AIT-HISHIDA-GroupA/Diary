from diaries.DiarySample import DiarySample
from diaries.NagataniDiary import NagataniDiary
from diaries.YoheiDiary import YoheiDiary
from diaries.omagariDiary import omagariDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(),NagataniDiary(),omagariDiary(),YoheiDiary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
