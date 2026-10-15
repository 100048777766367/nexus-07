import os
import json
from mechanisms.base import BaseMechanism

COMPASS_FILE = "synapses/teleology_compass.json"

class TeleologyCompassMechanism(BaseMechanism):
    name = "teleology"
    priority = 35

    def execute(self, context):
        decision = context.get("final_decision", 0.5)

        ahimsa = max(0.0, min(1.0, round(1.0 - abs(decision - 0.5) * 1.5, 4)))
        prajna = round(1.0 - abs(decision - 0.5)**2, 4)
        sunyata = round(1.0 - abs(decision - 0.5) * 2.0, 4)
        bodhi_score = round((ahimsa * 0.4) + (prajna * 0.3) + (sunyata * 0.3), 4)

        veto = False
        if decision < 0.05 or decision > 0.95:
            veto = True
            print(f"🛑 [LA BÀN BỒ ĐỀ PHỦ QUYẾT] Quyết định cực đoan ({decision})! Đưa về an lạc (0.5).")
            decision = round(0.5 + (decision - 0.5) * 0.2, 4)
            context["final_decision"] = decision

        os.makedirs("synapses", exist_ok=True)
        with open(COMPASS_FILE, "w") as f:
            json.dump({
                "epoch": context.get("current_epoch", 1),
                "bodhi_score": bodhi_score,
                "ahimsa": ahimsa,
                "prajna": prajna,
                "sunyata": sunyata,
                "veto": veto
            }, f, indent=4)
        print(f"🧭 [LA BÀN MỤC ĐÍCH LUẬN] Điểm Bồ Đề: {bodhi_score * 100:.2f}% | Veto={veto}")
