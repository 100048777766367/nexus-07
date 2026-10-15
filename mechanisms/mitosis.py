import os
import json
from mechanisms.base import BaseMechanism

MAX_FILE_LINES = 95

class MitosisMechanism(BaseMechanism):
    name = "mitosis"
    priority = 5

    def check_and_divide(self, file_path, context):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if len(lines) > MAX_FILE_LINES and not file_path.endswith(("_worker.py", "_shield.py")):
            base_name = os.path.basename(file_path)[:-3]
            dir_name = os.path.join(os.path.dirname(file_path), f"{base_name}_organ")

            print(f"⚡ [PHÂN BÀO HỢP CHUẨN] Tệp '{base_name}.py' ({len(lines)} dòng) bắt đầu phân bào...")
            os.makedirs(dir_name, exist_ok=True)

            epoch = context.get("current_epoch", 1)

            worker_code = f'''# [CON TRƯỞNG: {base_name.upper()}_WORKER]
from mechanisms.base import BaseMechanism

class {base_name.capitalize()}Worker(BaseMechanism):
    name = "{base_name}_worker"
    priority = 25

    def execute(self, context):
        print("⚙️ [{base_name.upper()}_WORKER] Đang chấp hành nhiệm vụ con trưởng.")
'''
            shield_code = f'''# [CON THỨ: {base_name.upper()}_SHIELD]
from mechanisms.base import BaseMechanism

class {base_name.capitalize()}Shield(BaseMechanism):
    name = "{base_name}_shield"
    priority = 26

    def execute(self, context):
        print("🛡️ [{base_name.upper()}_SHIELD] Màng lọc bảo vệ tế bào con.")
'''
            with open(os.path.join(dir_name, f"{base_name}_worker.py"), "w", encoding="utf-8") as f:
                f.write(worker_code)
            with open(os.path.join(dir_name, f"{base_name}_shield.py"), "w", encoding="utf-8") as f:
                f.write(shield_code)

            manifest = {
                "parent": f"{base_name}.py",
                "epoch": epoch,
                "consecration": "Swarm_Endorsed_F7",
                "offspring": [f"{base_name}_worker.py", f"{base_name}_shield.py"]
            }
            with open(os.path.join(dir_name, ".lineage_manifest.json"), "w", encoding="utf-8") as mf:
                json.dump(manifest, mf, indent=4)

            context["memorial_retiree"] = {
                "name": f"{base_name}.py",
                "merit": f"Đã phân bào thành công thư mục {base_name}_organ vào thế hệ #{epoch}"
            }

            os.rename(file_path, file_path + ".ancestral_relic")
            print(f"👑 [PHONG TƯỚC THÀNH CÔNG] Cơ quan '{base_name}_organ' đã tiếp nhận sứ mệnh!")

    def execute(self, context):
        mech_dir = "mechanisms"
        if not os.path.exists(mech_dir): return
        for root, _, files in os.walk(mech_dir):
            for file in files:
                if file.endswith(".py") and not file.startswith("__") and file != "base.py" and file != "mitosis.py":
                    try:
                        self.check_and_divide(os.path.join(root, file), context)
                    except Exception as e:
                        print(f"⚠️ [MITOSIS NOTICE]: {e}")
