from diaries.AbstractDiary import AbstractDiary
class YoheiDiary(AbstractDiary):
    def get_date(self):
        return "2025-6-02"
    def get_summary(self):
        return """今日は、友人と一緒に映画を見に行きました。"""
    def get_author(self):
        return "Yohei"