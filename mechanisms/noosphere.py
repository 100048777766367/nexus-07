import math
import json
import os
from mechanisms.base import BaseMechanism

RESONANCE_FILE = "synapses/noosphere_resonance.json"

class NoosphereResonanceMechanism(BaseMechanism):
    """
    HÒA ÂM TRÍ QUYỂN (KURAMOTO NOOSPHERE RESONANCE):
    Đo góc pha tâm thức của tất cả các nút mạng và kéo toàn bộ hệ sinh thái
    về cùng một tần số dao động đồng điệu (Phase Coherence).
    """
    name = "noosphere"
    priority = 28  # Chạy ngay sau khi thu thập tín hiệu Quorum

    def execute(self, context):
        harvested = context.get("harvested", {})
        my_decision = context.get("final_decision", 0.5)

        # Chuyển đổi quyết định thành góc pha radian [0, 2pi]
        phases = [my_decision * 2.0 * math.pi]
        for val in harvested.values():
            phases.append(val * 2.0 * math.pi)

        # Tính toán tham số trật tự Kuramoto (Kuramoto Order Parameter: R * e^(i * psi))
        sum_sin = sum(math.sin(theta) for theta in phases)
        sum_cos = sum(math.cos(theta) for theta in phases)
        n = len(phases)

        coherence_r = round(math.sqrt(sum_sin**2 + sum_cos**2) / n, 4)
        mean_phase_psi = math.atan2(sum_sin, sum_cos)
        if mean_phase_psi < 0:
            mean_phase_psi += 2.0 * math.pi

        # Chuyển góc pha trung bình trở lại giá trị quyết định đồng pha
        harmonic_decision = round(mean_phase_psi / (2.0 * math.pi), 4)

        print(f"🌐 [TRÍ QUYỂN NOOSPHERE] Độ kết hợp sóng não tập thể: R={coherence_r * 100:.2f}%")
        print(f"🎵 [HÒA ÂM ĐỒNG ĐIỆU] Quyết định sau khi khóa pha Kuramoto: {harmonic_decision}")

        # Tác động lực kéo pha: nếu độ kết hợp cao, hòa nhịp hoàn toàn theo tập thể
        if coherence_r > 0.6:
            context["final_decision"] = harmonic_decision

        context["noosphere_coherence"] = coherence_r

        os.makedirs("synapses", exist_ok=True)
        with open(RESONANCE_FILE, "w") as f:
            json.dump({
                "epoch": context.get("current_epoch", 1),
                "coherence_index": coherence_r,
                "collective_phase_rad": round(mean_phase_psi, 4),
                "active_oscillators_count": n,
                "state": "Harmonic_Phase_Locked" if coherence_r > 0.75 else "Coupling_In_Progress"
            }, f, indent=4)
