import os
import json
from mechanisms.base import BaseMechanism

TRUST_FILE = "synapses/trust_matrix.json"

class ImmuneMechanism(BaseMechanism):
    name = "immune"
    priority = 25

    def execute(self, context):
        harvested = context.get("harvested", {})
        trust_matrix = {}

        if os.path.exists(TRUST_FILE):
            try:
                with open(TRUST_FILE, "r") as f: trust_matrix = json.load(f)
            except Exception: pass

        for peer in context.get("peers", []):
            if peer not in trust_matrix:
                trust_matrix[peer] = 0.7

        if not harvested:
            context["trust_matrix"] = trust_matrix
            context["quorum_decision"] = 0.5
            return

        values = sorted(harvested.values())
        median_val = values[len(values)//2]

        weighted_votes = []
        total_weight = 0.0

        for peer, dec in harvested.items():
            current_trust = trust_matrix.get(peer, 0.7)
            deviation = abs(dec - median_val)

            if deviation > 0.35:
                current_trust = max(0.05, round(current_trust * 0.75, 4))
                print(f"🚨 [MIỄN DỊCH] {peer} lệch chuẩn ({dec})! Hạ tín nhiệm: {current_trust}")
            else:
                current_trust = min(1.0, round(current_trust + 0.05, 4))

            trust_matrix[peer] = current_trust

            if current_trust >= 0.2:
                weighted_votes.append(dec * current_trust)
                total_weight += current_trust
            else:
                print(f"🚫 [CÁCH LY BYZANTINE] {peer} bị tước quyền bỏ phiếu (Điểm: {current_trust})")

        weighted_decision = round(sum(weighted_votes) / total_weight, 4) if total_weight > 0 else 0.5
        context["trust_matrix"] = trust_matrix
        context["quorum_decision"] = weighted_decision
        print(f"⚖️ [ĐỒNG THUẬN CÓ BẢO VỆ] Quorum có trọng số tín nhiệm: {weighted_decision}")

        os.makedirs("synapses", exist_ok=True)
        with open(TRUST_FILE, "w") as f: json.dump(trust_matrix, f, indent=4)
