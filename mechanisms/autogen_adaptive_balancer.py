# [AUTOGENIC MECHANISM - TỰ SINH BỞI NEXUS-03]
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
