import os
import json
from mechanisms.base import BaseMechanism

class AntifragileMechanism(BaseMechanism):
    name = "antifragile"
    priority = 22  # Chạy ngay sau khi thu thập tín hiệu

    def execute(self, context):
        path = "synapses/immune_memory.json"
        if not os.path.exists(path): return

        try:
            with open(path, "r") as f: antibodies = json.load(f)
            if not antibodies: return

            total_hacker_energy = sum(a.get("absorbed_weight", 0.01) for a in antibodies)
            
            # Chuyển hóa năng lượng tiêu cực thành Gia Tốc Học Tập (Learning Boost)
            evolutionary_momentum = min(0.2, round(total_hacker_energy * 0.02, 4))
            
            # Bồi đắp vào vector tri thức
            v = context.get("wisdom_vector", [0.5, 0.5, 0.5, 0.5])
            v[0] = round((v[0] + evolutionary_momentum) % 1.0, 4)
            context["wisdom_vector"] = v

            print(f"⚡ [PHẢN MONG MANH TỐI HẬU] Hấp thụ {len(antibodies)} kháng thể độc tố! Gia tốc tiến hóa: +{evolutionary_momentum}")
        except Exception: pass
