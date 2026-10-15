import os
from mechanisms.base import BaseMechanism

class AutogenesisMechanism(BaseMechanism):
    name = "autogenesis"
    priority = 38

    def execute(self, context):
        current_epoch = context.get("current_epoch", 1)
        target_file = "mechanisms/autogen_adaptive_balancer.py"

        # Nếu đã đạt mốc tiến hóa thế hệ chẵn và tệp tự sinh chưa có -> Tự viết mã!
        if current_epoch % 2 == 0 and not os.path.exists(target_file):
            print("🧬 [AUTOGENESIS] Kích hoạt cơ chế tự sinh mã nguồn! Đang tự tạo tệp cơ chế mới...")
            new_code = '''# [AUTOGENIC MECHANISM - TỰ SINH BỞI NEXUS-03]
from mechanisms.base import BaseMechanism

class AutogenAdaptiveBalancer(BaseMechanism):
    name = "autogen_balancer"
    priority = 28

    def execute(self, context):
        # Tự động cân bằng độ lệch giữa quyết định và trung vị
        q = context.get("quorum_decision", 0.5)
        f = context.get("final_decision", 0.5)
        balanced = round((q + f) / 2.0, 4)
        context["final_decision"] = balanced
        print(f"⚡ [AUTOGEN BALANCER] Đã tự kích hoạt và ổn định quyết định: {balanced}")
'''
            with open(target_file, "w", encoding="utf-8") as f:
                f.write(new_code)
            print(f"✨ [AUTOGENESIS THÀNH CÔNG] Đã sinh tệp: {target_file}. Sẽ tự động nạp ở vòng lặp sau!")
