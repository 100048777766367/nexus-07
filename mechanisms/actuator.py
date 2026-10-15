from mechanisms.base import BaseMechanism

class ActuatorMechanism(BaseMechanism):
    name = "actuator"
    priority = 36

    def execute(self, context):
        decision = context.get("final_decision", 0.5)
        
        # Chỉ huy chuyên biệt theo từng vai trò cơ quan ngoại vi
        directed_commands = {
            "retina": {
                "action": "adjust_focus",
                "sensitivity": round(decision * 1.5, 4),
                "attention_gate": "high" if decision > 0.5 else "low"
            },
            "motor": {
                "action": "contract_or_relax",
                "torque_pulse": [round(decision, 4), round(1.0 - decision, 4)],
                "intensity": round(abs(decision - 0.5) * 2.0, 4)
            },
            "monad": {
                "action": "dialectical_synthesis",
                "bias_shift": round(decision - 0.5, 4)
            }
        }

        context["directed_commands"] = directed_commands
        print(f"🦾 [ACTIVE ACTUATOR] Đã phân tách lệnh chỉ huy chuyên biệt cho retina, motor và monad.")
