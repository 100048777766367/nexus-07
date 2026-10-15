import os
import json
from mechanisms.base import BaseMechanism

MAX_FILE_LINES = 85  # Ngưỡng kích hoạt phân bào

class MitosisMechanism(BaseMechanism):
    name = "mitosis"
    priority = 5  # Chạy đầu tiên để kiểm tra sự phân bào

    def check_and_divide(self, file_path, context):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if len(lines) > MAX_FILE_LINES:
            base_name = os.path.basename(file_path)[:-3]
            dir_name = os.path.join(os.path.dirname(file_path), f"{base_name}_organ")
            
            print(f"⚡ [PHÂN BÀO TẾ BÀO] Tệp '{base_name}.py' ({len(lines)} dòng) đã quá tải! Bắt đầu phân bào đệ quy...")

            # 1. Tạo thư mục cơ quan mới
            os.makedirs(dir_name, exist_ok=True)

            # 2. Phân rã thành 2 tệp con cháu (Alpha & Beta)
            mid = len(lines) // 2
            child_alpha = os.path.join(dir_name, f"{base_name}_alpha_TheWorker.py")
            child_beta = os.path.join(dir_name, f"{base_name}_beta_TheShield.py")

            # 3. Tam thức phong tước: Tự phong + Được phong + Tán đồng phong
            manifest = {
                "parent_ancestor": f"{base_name}.py",
                "division_epoch": context.get("current_epoch", 1),
                "consecration_level": "Tier_3_Swarm_Endorsed",
                "organ_responsibility": f"Autonomous_{base_name.capitalize()}_Domain",
                "children": [
                    {"name": f"{base_name}_alpha", "title": "TheWorker", "badge": "Silver_Gear"},
                    {"name": f"{base_name}_beta", "title": "TheShield", "badge": "Golden_Aegis"}
                ]
            }

            with open(os.path.join(dir_name, ".lineage_manifest.json"), "w", encoding="utf-8") as mf:
                json.dump(manifest, mf, indent=4)

            # Ghi mã nguồn thừa kế cho con cháu
            header = f"# [THẾ HỆ CON CHÁU ĐƯỢC PHONG TƯỚC TỪ {base_name.upper()}]\nfrom mechanisms.base import BaseMechanism\n\n"
            with open(child_alpha, "w", encoding="utf-8") as f:
                f.write(header + "".join(lines[:mid]))
            with open(child_beta, "w", encoding="utf-8") as f:
                f.write(header + "".join(lines[mid:]))

            # 4. Đưa tệp mẹ vào Nhà Tưởng Niệm (Ancestral Reliquary)
            context["memorial_retiree"] = {
                "name": f"{base_name}.py",
                "merit": f"Đã hy sinh thân mình phân bào thành công thư mục {base_name}_organ",
                "honors": ["Grand_Ancestor_Laurel", "Lotus_Tribute_Flower"]
            }

            # Đổi đuôi tệp mẹ thành tệp tưởng niệm (không chạy trực tiếp nữa)
            os.rename(file_path, file_path + ".ancestral_relic")
            print(f"👑 [PHONG TƯỚC THÀNH CÔNG] Thư mục '{base_name}_organ' chính thức nhận lãnh sứ mệnh!")

    def execute(self, context):
        mech_dir = "mechanisms"
        for root, dirs, files in os.walk(mech_dir):
            for file in files:
                if file.endswith(".py") and not file.startswith("__") and file != "base.py" and file != "mitosis.py":
                    full_path = os.path.join(root, file)
                    try:
                        self.check_and_divide(full_path, context)
                    except Exception as e:
                        print(f"⚠️ [MITOSIS NOTICE]: {e}")
