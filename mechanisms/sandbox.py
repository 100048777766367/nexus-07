from mechanisms.base import BaseMechanism

class SandboxMechanism(BaseMechanism):
    name = "sandbox"
    priority = 31

    def simulate_future(self, decision, candidate_action):
        pain = abs(decision - 0.5) * candidate_action
        stability = 1.0 - abs(decision - 0.5)
        return round((pain * 0.6) + ((1.0 - stability) * 0.4), 4)

    def execute(self, context):
        raw = context.get("final_decision", 0.5)
        sims = []
        for factor in [0.85, 0.95, 1.0, 1.05, 1.15]:
            cand = max(0.01, min(0.99, round(raw * factor, 4)))
            loss = self.simulate_future(cand, factor)
            sims.append((loss, cand))
        sims.sort(key=lambda x: x[0])
        best_loss, opt_dec = sims[0]
        context["final_decision"] = opt_dec
        print(f"✨ [GIẢ LẬP WHAT-IF] Điều biến kịch bản tối ưu: {opt_dec} (Loss={best_loss})")
