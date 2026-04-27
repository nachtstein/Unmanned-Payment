class PaymentProcessor:
    def process(self, amount, currency="USD"):
        print(f"결제 요청: {amount} {currency}")
        # 리버길드 0% 수수료 로직 적용
        return {"status": "success", "fee": 0.0}
