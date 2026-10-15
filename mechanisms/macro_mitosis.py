import os
import json
from mechanisms.base import BaseMechanism

CAPSULE_FILE = "synapses/seed_capsule.json"

class MacroMitosisMechanism(BaseMechanism):
    """
    CƠ CHẾ ĐẠI PHÂN BÀO (MACRO-MITOSIS):
    Khi thế hệ đạt mốc trưởng thành (mỗi 10 epoch), tự động đóng gói toàn bộ
    tinh hoa ADN thành một Nang Bào Tử sẵn sàng kích hoạt để khai sinh một repo độc lập.
    """
    name = "macro_mitosis"
    priority = 48

    def execute(self, context):
        epoch = context.get("current_epoch", 1)

        # Cứ mỗi 10 thế hệ tiến hóa, hệ thống tích lũy đủ năng lượng để sinh sản cấp repo
        if epoch % 10 == 0:
            print("🧬 [ĐẠI PHÂN BÀO CẤP REPO] Tích lũy đủ năng lượng sinh sản! Đang đóng gói Nang Bào Tử...")

            seed_capsule = {
                "parent_lineage": context.get("repo_name"),
                "procreation_epoch": epoch,
                "offspring_generation": "F7_SOVEREIGN_OFFSPRING",
                "genetic_payload": {
                    "master_decision": context.get("final_decision", 0.5),
                    "knowledge_graph_snapshot": context.get("knowledge_graph_summary", "None"),
                    "trusted_peers": context.get("peers", []),
                    "docker_runtime": "python:3.14-slim"
                },
                "instructions_for_gestation": [
                    "1. Create new repo: nexus-06-child",
                    "2. Inject genetic_payload into initial synapses/state.json",
                    "3. Run workflow to birth new autonomous ecosystem node"
                ]
            }

            os.makedirs("synapses", exist_ok=True)
            with open(CAPSULE_FILE, "w", encoding="utf-8") as f:
                json.dump(seed_capsule, f, indent=4, ensure_ascii=False)

            print(f"👑 [SINH SẢN THÀNH CÔNG] Nang Bào Tử '{CAPSULE_FILE}' đã sẵn sàng đẻ ra repo F7!")
