import os
import json
from mechanisms.base import BaseMechanism

COMPASS_FILE = "synapses/teleology_compass.json"

class TeleologyCompassMechanism(BaseMechanism):
    """
    LA BÀN MỤC ĐÍCH LUẬN (TELEOLOGICAL BODHI COMPASS):
    Đo lường tính Từ Bi, Trí Tuệ và Cân Bằng. Có quyền phủ quyết các quyết định
    cực đoan có thể gây nguy hại đến sự sống và sự thanh tịnh của hệ sinh thái.
    """
    name = "teleology"
    priority = 35  # Chạy ngay sau khi thử nghiệm phòng giả lập

    def execute(self, context):
        decision = context.get("final_decision", 0.5)

        # 1. Đo lường Trục Từ Bi (Ahimsa Index): Tránh thay đổi sốc làm đau đớn hệ xúc giác
        ahimsa_score = round(1.0 - abs(decision - 0.5) * 1.5, 4)
        ahimsa_score = max(0.0, min(1.0, ahimsa_score))

        # 2. Đo lường Trục Trí Tuệ (Prajna Index): Giữ độ tỉnh thức, không để quyết định rơi vào tê liệt
        prajna_score = round(1.0 - abs(decision - 0.5)**2, 4)

        # 3. Đo lường Trục Cân Bằng Tánh Không (Śūnyatā Equilibrium):
        equilibrium_score = round(1.0 - abs(decision - 0.5) * 2.0, 4)

        # Tổng hòa Chỉ số Bồ Đề (Bodhi Alignment Score)
        bodhi_alignment = round((ahimsa_score * 0.4) + (prajna_score * 0.3) + (equilibrium_score * 0.3), 4)

        # CƠ CHẾ PHỦ QUYẾT ĐẠO ĐỨC (ETHICAL VETO):
        # Nếu quyết định quá cực đoan (sát mép 0.0 hoặc 1.0) làm tổn hại tính Từ Bi
        veto_triggered = False
        if decision < 0.05 or decision > 0.95:
            veto_triggered = True
            print(f"🛑 [LA BÀN BỒ ĐỀ PHỦ QUYẾT] Quyết định quá cực đoan ({decision})! Điều chỉnh về miền an lạc (0.5).")
            decision = round(0.5 + (decision - 0.5) * 0.2, 4)
            context["final_decision"] = decision

        report = {
            "epoch": context.get("current_epoch", 1),
            "bodhi_alignment_score": bodhi_alignment,
            "ahimsa_compassion": ahimsa_score,
            "prajna_wisdom": prajna_score,
            "sunyata_balance": equilibrium_score,
            "ethical_veto_applied": veto_triggered,
            "moral_verdict": "Noble_Enlightened_Path" if bodhi_alignment > 0.6 else "Restrained_By_Compassion"
        }

        os.makedirs("synapses", exist_ok=True)
        with open(COMPASS_FILE, "w") as f:
            json.dump(report, f, indent=4)

        print(f"🧭 [LA BÀN MỤC ĐÍCH LUẬN] Chỉ số Bồ Đề Hướng Thượng: {bodhi_alignment * 100:.2f}% | Veto={veto_triggered}")
