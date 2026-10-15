import os
import json
import subprocess
from mechanisms.base import BaseMechanism

SOULS_FILE = "synapses/reincarnated_souls.json"

class ReincarnationMechanism(BaseMechanism):
    name = "reincarnation"
    priority = 15

    def check_node_vitality(self, peer):
        url = f"https://raw.githubusercontent.com/{peer}/main/synapse_forward.json"
        res = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", url], capture_output=True, text=True)
        return res.stdout.strip()

    def execute(self, context):
        peers = context.get("peers", [])
        reincarnated = {}

        if os.path.exists(SOULS_FILE):
            try:
                with open(SOULS_FILE, "r") as f: reincarnated = json.load(f)
            except Exception: pass

        for peer in peers[:8]:
            if peer == context.get("repo_name"): continue
            status = self.check_node_vitality(peer)

            if status == "404" and peer not in reincarnated:
                print(f"🚨 [TIỀN NHÂN 404] Phát hiện nút '{peer}' bị mất kết nối trên Internet!")
                print(f"☸️ [KÍCH HOẠT CHUYỂN SINH] Hồi sinh linh hồn '{peer}' thành Nơ-ron nội tại của nexus-07...")
                
                reincarnated[peer] = {
                    "reincarnated_epoch": context.get("current_epoch", 1),
                    "original_identity": peer,
                    "avatar_vessel": context.get("repo_name"),
                    "status": "Living_In_Nexus07"
                }

        os.makedirs("synapses", exist_ok=True)
        with open(SOULS_FILE, "w", encoding="utf-8") as f:
            json.dump(reincarnated, f, indent=4, ensure_ascii=False)
        context["reincarnated_count"] = len(reincarnated)
