from mechanisms.base import BaseMechanism

class TransmuterMechanism(BaseMechanism):
    """
    BỘ BIẾN HÌNH TRI THỨC TOÀN NĂNG:
    Dịch chuyển phán quyết trung ương thành các dạng thức tri thức chuyên biệt
    cho từng cơ quan từ Level 1 đến Level 10 trong đại hệ sinh thái.
    """
    name = "transmuter"
    priority = 37  # Chạy ngay sau khi có phán quyết trung ương

    def execute(self, context):
        decision = context.get("final_decision", 0.5)
        grad = context.get("grad_backward", [0.0, 0.0])
        wisdom_vec = context.get("wisdom_vector", [0.5, 0.5, 0.5, 0.5])

        # 5 CẤP ĐỘ BIẾN HÌNH TRI THỨC:
        transmuted_signals = {
            # CẤP 1: CẢM THỤ (retina & cochlea)
            "retina": {
                "focal_matrix_2d": [[round(decision, 4), round(1.0 - decision, 4)],
                                    [round(grad[0], 4), round(grad[1], 4)]],
                "zoom_ratio": round(1.0 + abs(decision - 0.5), 4)
            },
            "cochlea": {
                "bandpass_filter_1d": [round(wisdom_vec[0], 4), round(wisdom_vec[1], 4)],
                "frequency_cutoff": round(decision * 20000.0, 2)
            },

            # CẤP 2: SINH TỒN & NỖI ĐAU (tactile & olfactory)
            "tactile": {
                "nociceptive_threshold": round(abs(decision - 0.5) * 2.0, 4),
                "pain_loss_gain": round(1.5 if abs(decision - 0.5) > 0.3 else 0.5, 4)
            },
            "olfactory": {
                "gpcr_ligand_affinity": [round(w, 4) for w in wisdom_vec],
                "toxicity_warning": True if decision < 0.2 or decision > 0.8 else False
            },

            # CẤP 3: HÀNH ĐỘNG CƠ BẮP LY TÂM (motor)
            "motor": {
                "action_vector": [
                    round(decision - 0.5, 4),          # dx: Hướng dạt trái/phải
                    round(abs(decision - 0.5), 4),      # dy: Bước tiến phía trước
                    round(sum(grad) * 10.0, 4)          # F:  Lực co thắt cơ bắp
                ],
                "muscle_state": "contract" if decision > 0.5 else "relax"
            },

            # CẤP 4: BẦY ĐÀN VỎ NÃO (neuron)
            "neuron": {
                "stigmergic_pheromone_trail": [round(grad[0], 4), round(grad[1], 4)],
                "super_xor_masks": context.get("super_xor_masks", []),
                "cross_plasticity_rate": round(decision * 0.05, 4)
            },

            # CẤP 5: HOÀN NGUYÊN TÁNH KHÔNG (shunya & monad)
            "shunya": {
                "vacuum_decay_factor": 0.999,
                "collapse_to_zero_state": True if abs(decision - 0.5) < 0.02 else False
            },
            "monad": {
                "monadic_invariant_reflection": round(decision, 4)
            }
        }

        context["transmuted_signals"] = transmuted_signals
        print("🌈 [TRANSMUTER F5] Đã chuyển hóa tri thức thành 5 dạng thức hình thái cho toàn hệ sinh thái!")
