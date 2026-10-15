import math
import json
import os
from mechanisms.base import BaseMechanism

RESONANCE_FILE = "synapses/noosphere_resonance.json"

class NoosphereResonanceMechanism(BaseMechanism):
    name = "noosphere"
    priority = 28

    def execute(self, context):
        harvested = context.get("harvested", {})
        my_decision = context.get("final_decision", 0.5)

        phases = [my_decision * 2.0 * math.pi]
        for val in harvested.values():
            phases.append(val * 2.0 * math.pi)

        sum_sin = sum(math.sin(t) for t in phases)
        sum_cos = sum(math.cos(t) for t in phases)
        n = len(phases)

        coherence_r = round(math.sqrt(sum_sin**2 + sum_cos**2) / n, 4)
        mean_phase = math.atan2(sum_sin, sum_cos)
        if mean_phase < 0: mean_phase += 2.0 * math.pi
        harmonic_decision = round(mean_phase / (2.0 * math.pi), 4)

        print(f"🌐 [TRÍ QUYỂN NOOSPHERE] Độ kết hợp sóng não: R={coherence_r * 100:.2f}% | Quyết định đồng pha: {harmonic_decision}")

        if coherence_r > 0.6:
            context["final_decision"] = harmonic_decision

        context["noosphere_coherence"] = coherence_r

        os.makedirs("synapses", exist_ok=True)
        with open(RESONANCE_FILE, "w") as f:
            json.dump({
                "epoch": context.get("current_epoch", 1),
                "coherence_index": coherence_r,
                "collective_phase_rad": round(mean_phase, 4),
                "active_oscillators": n,
                "status": "Harmonic_Phase_Locked" if coherence_r > 0.75 else "Coupling_In_Progress"
            }, f, indent=4)
