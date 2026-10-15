import os
import json
import time
import hashlib
from mechanisms.base import BaseMechanism

class SurvivalMechanism(BaseMechanism):
    name = "survival"
    priority = 50

    def execute(self, context):
        current_time = int(time.time())
        current_epoch = context.get("current_epoch", 1)
        final_decision = context.get("final_decision", 0.5)
        peers = context.get("peers", [])

        prev_cid = "GENESIS_NEXUS04_CID"
        if os.path.exists("synapses/state.json"):
            try:
                with open("synapses/state.json", "r") as f:
                    prev_cid = json.load(f).get("quantum_cid", "GENESIS_NEXUS04_CID")
            except Exception: pass

        chain_seed = f"{prev_cid}_{current_epoch}_{current_time}_{final_decision}".encode()
        new_quantum_cid = hashlib.shake_256(chain_seed).hexdigest(64)

        node_dna = {
            "identity": context.get("repo_name"),
            "generation": "F5_OMNI_TRANSMUTER_NEXUS",
            "generation_epoch": current_epoch,
            "architecture": "Nexus05_Fractal_OmniTransmuter",
            "prev_cid": prev_cid
        }

        # GÓI TIN TIẾN: MANG TRỌN VẸN 5 DẠNG THỨC BIẾN HÌNH CHO TOÀN BỘ 11 TẦNG
        fwd_packet = {
            "contract": "bodhi.nexus.v5",
            "node_dna": node_dna,
            "generation_epoch": current_epoch,
            "timestamp": current_time,
            "decision": final_decision,
            "command_pulse": [final_decision, round(1.0 - final_decision, 4)],
            "transmuted_ecosystem_signals": context.get("transmuted_signals", {}),
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
