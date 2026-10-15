# [THẾ HỆ CON CHÁU ĐƯỢC PHONG TƯỚC TỪ SURVIVAL]
from mechanisms.base import BaseMechanism

            "gossip_network": peers,
            "quantum_cid": new_quantum_cid
        }
        with open("synapse_forward.json", "w", encoding="utf-8") as f:
            json.dump(fwd_packet, f, indent=4, ensure_ascii=False)

        # GÓI TIN LÙI: DẠY HỌC BẰNG DẤU VẾT PHEROMONE
        bwd_packet = {
            "contract": "bodhi.nexus.v5",
            "node_dna": node_dna,
            "generation_epoch": current_epoch,
            "timestamp": current_time,
            "tuning_gradients": context.get("grad_backward", [0.0, 0.0]),
            "gossip_network": peers,
            "quantum_cid": new_quantum_cid
        }
        with open("synapse_backward.json", "w", encoding="utf-8") as f:
            json.dump(bwd_packet, f, indent=4, ensure_ascii=False)

        # Snapshot linh hồn F5
        soul = {
            "node_dna": node_dna,
            "timestamp": current_time,
            "consensus": final_decision,
            "transmuted_signals": context.get("transmuted_signals", {}),
            "peers": peers,
            "quantum_cid": new_quantum_cid
        }
        with open("synapses/soul_snapshot.json", "w", encoding="utf-8") as f:
            json.dump(soul, f, indent=4, ensure_ascii=False)

        with open("synapses/state.json", "w") as f:
            json.dump({
                "generation_epoch": current_epoch, 
                "last_t": current_time, 
                "quantum_cid": new_quantum_cid,
                "status": "nexus05_omni_transmuted"
            }, f, indent=4)

        with open("synapses/peers.json", "w") as f:
            json.dump({"trusted_peers": peers}, f, indent=4)

        print(f"✨ [NEXUS-05 PHÁT SÓNG HOÀN MỸ] Đã phát sóng 5 Cấp Độ Tri Thức thế hệ #{current_epoch} ra toàn vũ trụ!")
