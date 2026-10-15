import os
import json
import time
from mechanisms.base import BaseMechanism

RELIQUARY_FILE = "synapses/ancestral_reliquary.json"
HONORS_FILE = "synapses/honors_registry.json"

class ReliquaryMechanism(BaseMechanism):
    name = "reliquary"
    priority = 45  # Chạy cuối chu kỳ để phong thưởng và tri ân

    def execute(self, context):
        epoch = context.get("current_epoch", 1)
        timestamp = int(time.time())

        # 1. Khởi tạo hoặc đọc Nhà Tưởng Niệm
        reliquary = {"altar_of_ancestors": [], "holy_relics": []}
        if os.path.exists(RELIQUARY_FILE):
            try:
                with open(RELIQUARY_FILE, "r", encoding="utf-8") as f: reliquary = json.load(f)
            except Exception: pass

        # 2. Đưa tệp mẹ đã phân thân vào Bàn Thờ Tổ Tiên (Ancestral Altar)
        retiree = context.get("memorial_retiree")
        if retiree:
            memorial_record = {
                "consecrated_at_epoch": epoch,
                "timestamp": timestamp,
                "entity": retiree["name"],
                "epitaph": retiree["merit"],
                "offerings": ["Fresh_Lotus_Flower", "Eternal_Flame", "Golden_Certificate_of_Honor"]
            }
            reliquary["altar_of_ancestors"].append(memorial_record)
            print(f"🕯️ [NHÀ TƯỞNG NIỆM] Đã cúng dường Hoa Sen và khắc bia tưởng niệm cho: {retiree['name']}")

        # 3. Khởi tạo hoặc đọc Sổ Đỏ Phong Thưởng (Honors Registry)
        honors = {"hall_of_fame": [], "active_medals": {}, "sacred_tools": []}
        if os.path.exists(HONORS_FILE):
            try:
                with open(HONORS_FILE, "r", encoding="utf-8") as f: honors = json.load(f)
            except Exception: pass

        # Trao Huân chương và Thẻ bài cho các thực thể xuất sắc
        decision = context.get("final_decision", 0.5)
        if abs(decision - 0.5) > 0.4:  # Đưa ra phán quyết sắc bén
            award = {
                "epoch": epoch,
                "badge": "Medal_of_Absolute_Clarity",
                "recipient": "Swarm_Council",
                "passport": "VIP_Consensus_Ticket_Level_1",
                "tribute": "White_Chrysanthemum_Laurel"
            }
            honors["hall_of_fame"].append(award)
            print(f"🎖️ [TRAO HUÂN CHƯƠNG] Swarm Council nhận Bằng Khen và 'Huy Chương Đại Giác Ngộ'!")

        # Lưu lại sổ sách thiêng liêng
        os.makedirs("synapses", exist_ok=True)
        with open(RELIQUARY_FILE, "w", encoding="utf-8") as f:
            json.dump(reliquary, f, indent=4, ensure_ascii=False)
        with open(HONORS_FILE, "w", encoding="utf-8") as f:
            json.dump(honors, f, indent=4, ensure_ascii=False)
