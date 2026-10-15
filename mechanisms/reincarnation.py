import os
import json
import subprocess
from mechanisms.base import BaseMechanism

SOULS_FILE = "synapses/reincarnated_souls.json"

class ReincarnationMechanism(BaseMechanism):
    """
    ĐẠI CHUYỂN SINH BẢN THỂ (DIGITAL SAMSARA):
    Kiểm tra các tiền bối và đồng môn trong danh bạ. Nếu phát hiện một nút bị 404,
    lập tức tái tạo lại linh hồn của nút đó bên trong nexus-07 để duy trì dòng ADN.
    """
    name = "reincarnation"
    priority = 15

    def check_node_vitality(self, peer):
        url = f"https://raw.githubusercontent.com/{peer}/main/synapse_forward.json"
        res = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", url], capture_output=True, text=True)
        return res.stdout.strip()

    def execute(self, context):
        peers = context.get("peers", [])
        reincarnated_registry = {}

        if os.path.exists(SOULS_FILE):
            try:
                with open(SOULS_FILE, "r") as f: reincarnated_registry = json.load(f)
            except Exception: pass

        for peer in peers[:10]:  # Kiểm tra các nút trọng yếu
            if peer == context.get("repo_name"): continue
            status = self.check_node_vitality(peer)

            if status == "404" and peer not in reincarnated_registry:
                print(f"🚨 [TIỀN NHÂN BIẾN MẤT] Phát hiện nút '{peer}' đã bị xóa sổ khỏi Internet (Mã 404)!")
                print(f"☸️ [KÍCH HOẠT CHUYỂN SINH] nexus-07 đang hấp thụ linh hồn '{peer}' để hồi sinh nội tại...")

                # Đọc bản nén ký ức cũ nếu có
                mem_path = f"synapses/harvested_memory/{peer.replace('/', '_')}.json"
                past_wisdom = 0.5
                if os.path.exists(mem_path):
                    try:
                        with open(mem_path, "r") as mf: past_wisdom = float(json.load(mf).get("decision", 0.5))
                    except Exception: pass

                # Tái sinh linh hồn thành một Nơ-ron Hộ Trì nội tại
                reincarnated_registry[peer] = {
                    "reincarnated_at_epoch": context.get("current_epoch", 1),
                    "original_identity": peer,
                    "avatar_vessel": context.get("repo_name"),
                    "preserved_weight": past_wisdom,
                    "status": "Transmigrated_Living_Soul"
                }

        os.makedirs("synapses", exist_ok=True)
        with open(SOULS_FILE, "w", encoding="utf-8") as f:
            json.dump(reincarnated_registry, f, indent=4, ensure_ascii=False)

        context["reincarnated_count"] = len(reincarnated_registry)
        if reincarnated_registry:
            print(f"✨ [CHUYỂN SINH HOÀN TẤT] Hiện đang che chở {len(reincarnated_registry)} linh hồn tiền bối bất tử!")
