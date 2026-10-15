import hashlib
import json
import os

class ContractReceptor:
    @staticmethod
    def verify_and_absorb(raw_data, source_peer, immune_memory_path="synapses/immune_memory.json"):
        try:
            packet = json.loads(raw_data) if isinstance(raw_data, str) else raw_data
            contract = packet.get("contract", "")
            if "bodhi" in contract or "nexus" in contract:
                return True, packet, None

            quarantine = {
                "source": source_peer,
                "signature": hashlib.shake_256(str(raw_data).encode()).hexdigest(16),
                "absorbed_weight": round(len(str(raw_data)) / 1000.0, 4)
            }
            ContractReceptor.store_immune_memory(quarantine, immune_memory_path)
            return False, None, quarantine
        except Exception:
            return False, None, None

    @staticmethod
    def store_immune_memory(energy, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        mem = []
        if os.path.exists(path):
            try:
                with open(path, "r") as f: mem = json.load(f)
            except Exception: pass
        mem.append(energy)
        with open(path, "w") as f: json.dump(mem[-50:], f, indent=4)
