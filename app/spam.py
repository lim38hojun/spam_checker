def check_spam(text: str) -> str:
    text = text.lower().strip()
    if text == "":
        return "ham"
    spam_keywords = [
    "free", "win", "prize", "click",
    "buy now", "urgent", "cash", "money", "offer", "deal",
    "bonus", "limited", "guarantee",
    "무료", "당첨", "당첨자", "경품", "클릭",
    "지금 구매", "긴급", "현금", "돈", "제안", "특가",
    "보너스", "한정", "보장"
    ]
    hit = 0
    for kw in spam_keywords:
        print(kw, text)
        if kw in text:
            hit += 1
    return "spam" if hit >= 2 else "ham", hit