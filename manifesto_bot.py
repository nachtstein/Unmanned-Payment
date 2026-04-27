# 리버길드 대외 홍보 및 성명서 생성기

class ManifestoBot:
    def __init__(self):
        self.master_name = "Jegal Dukju"
        self.guild = "River Guild"

    def generate_statement(self, topic):
        statement = f"[{self.guild} 공식 입장]\n"
        statement += f"주제: {topic}에 대하여\n"
        statement += "본 길드는 무인격 결제 시스템을 통해 중개자 없는 세상을 지향합니다.\n"
        statement += "모든 독점적 수수료는 시스템의 엔트로피를 높이는 악입니다.\n"
        statement += f"기준 도수: {self.master_name} Master's Way"
        return statement

if __name__ == "__main__":
    bot = ManifestoBot()
    print(bot.generate_statement("배달 플랫폼 수수료 갑질"))
