from mechanisms.base import BaseMechanism

class SandboxMechanism(BaseMechanism):
    """
    HỘP CÁT GIẢ LẬP NỘI TẠI (MENTAL SANDBOX):
    Mô phỏng các biến thể tương lai để trả lời câu hỏi "Nếu... thì sao?" (What-If).
    Chọn ra phán quyết tối ưu nhất trước khi phát sóng cho các cơ quan.
    """
    name = "sandbox"
    priority = 31  # Chạy ngay sau khi nơ-ron đưa ra phán quyết thô

    def simulate_future(self, decision, candidate_action, context):
        """Ước tính hàm mất mát sinh tồn nếu hành động này được thực thi"""
        pain_risk = abs(decision - 0.5) * candidate_action
        stability_score = 1.0 - abs(decision - 0.5)
        # Điểm tổn hại sinh thái (càng thấp càng an toàn)
        loss_estimate = round((pain_risk * 0.6) + ((1.0 - stability_score) * 0.4), 4)
        return loss_estimate

    def execute(self, context):
        raw_decision = context.get("final_decision", 0.5)
        print(f"🔮 [MENTAL SANDBOX] Đưa phán quyết thô ({raw_decision}) vào phòng giả lập tâm thức...")

        # Thử nghiệm 5 biến thể nhân quả
        variations = [0.8, 0.9, 1.0, 1.1, 1.2]
        simulation_results = []

        for factor in variations:
            test_decision = max(0.01, min(0.99, round(raw_decision * factor, 4)))
            loss = self.simulate_future(test_decision, factor, context)
            simulation_results.append((loss, test_decision))

        # Chọn kịch bản có mức độ tổn hại nhỏ nhất
        simulation_results.sort(key=lambda x: x[0])
        best_loss, optimal_decision = simulation_results[0]

        print(f"✨ [GIẢ LẬP TỐI ƯU] Đã thử 5 tương lai. Chọn kịch bản tổn hại thấp nhất: Loss={best_loss} ──► Điều biến phán quyết: {optimal_decision}")
        context["final_decision"] = optimal_decision
        context["sandbox_simulation"] = {
            "tested_futures": len(variations),
            "lowest_loss": best_loss,
            "optimal_adjusted_decision": optimal_decision
        }
