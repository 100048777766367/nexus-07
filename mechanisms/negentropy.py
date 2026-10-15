import os
import json
import math
from mechanisms.base import BaseMechanism

REPORT_FILE = "synapses/negentropy_report.json"

class NegentropyMechanism(BaseMechanism):
    """
    ĐỘNG CƠ ENTROPY ÂM (SCHRÖDINGER NEGENTROPY):
    Đo lường mức độ hỗn loạn, tự động cắt tỉa các liên kết vô dụng và thanh lọc ký ức rác.
    """
    name = "negentropy"
    priority = 42

    def calculate_entropy(self, weights):
        """Tính toán Entropy thông tin Shannon của bầy nơ-ron"""
        entropy = 0.0
        total = sum(abs(w) for w in weights) or 1.0
        for w in weights:
            p = abs(w) / total
            if p > 0:
                entropy -= p * math.log2(p)
        return round(entropy, 4)

    def execute(self, context):
        swarm_weights = context.get("swarm_weights", [])
        flat_weights = [w for cell in swarm_weights for w in cell] if swarm_weights else [0.5]
        
        current_entropy = self.calculate_entropy(flat_weights)
        pruned_synapses = 0

        # CẮT TỈA SYNAPSE (Synaptic Pruning): Ép các trọng số quá nhỏ về 0 tuyệt đối để giải phóng RAM
        cleaned_weights = []
        for cell in swarm_weights:
            pruned_cell = []
            for w in cell:
                if abs(w) < 0.005:  # Trọng số quá nhỏ, không còn giá trị dẫn truyền
                    pruned_cell.append(0.0)
                    pruned_synapses += 1
                else:
                    pruned_cell.append(w)
            cleaned_weights.append(pruned_cell)

        context["swarm_weights"] = cleaned_weights

        report = {
            "epoch": context.get("current_epoch", 1),
            "shannon_entropy": current_entropy,
            "pruned_synapses_count": pruned_synapses,
            "system_health": "Crystal_Pure" if current_entropy < 3.0 else "Stable"
        }

        os.makedirs("synapses", exist_ok=True)
        with open(REPORT_FILE, "w") as f:
            json.dump(report, f, indent=4)

        print(f"🍃 [ENTROPY ÂM] Đã thanh lọc {pruned_synapses} synapse thoái hóa. Chỉ số Entropy hệ thống: {current_entropy}")
