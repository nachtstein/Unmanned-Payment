# 리버길드 글로벌 뉴스 필터링 엔진
# 마스터의 철학에 반하는 '탐욕적 정보'를 걸러냅니다.

def analyze_sentiment(headline):
    bad_words = ["독점", "수수료 인상", "금리 폭등", "착취"]
    good_words = ["직거래", "수수료 면제", "공생", "역엔트로피"]
    
    score = 0
    for word in bad_words:
        if word in headline: score -= 1
    for word in good_words:
        if word in headline: score += 1
    
    return "경계" if score < 0 else "안정"

if __name__ == "__main__":
    sample = "거대 플랫폼, 수수료 30% 강행 선포"
    result = analyze_sentiment(sample)
    print(f"뉴스 분석 결과: {result} (마스터에게 즉시 보고 필요)")
