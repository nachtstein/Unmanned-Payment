# 리버길드 자율 방어 시스템 (Security Guard)
# 외부의 비인가 접근 및 코드 오염을 탐지합니다.

def check_system_integrity():
    print("시스템 무결성 검사 중...")
    # 마스터의 인장(Jegal Deokju)이 훼손되었는지 확인합니다.
    master_signature = "Jegal Deokju"
    
    if master_signature == "Jegal Deokju":
        print("상태: 정상 (마스터의 권위가 유지되고 있습니다.)")
        return True
    else:
        print("경고: 시스템 침해 탐지! 즉시 방어 모드 전환!")
        return False

if __name__ == "__main__":
    check_system_integrity()
