import os
import sys
import json
import importlib
import inspect
import urllib.request

# ==============================================================================
# 0. KHUNG GIAO DIỆN CƠ SỞ (FALLBACK AN TOÀN NẾU THIẾU mechanisms/base.py)
# ==============================================================================
class BaseMechanism:
    name = "base_mechanism"
    priority = 100
    def execute(self, context):
        raise NotImplementedError

# ==============================================================================
# 1. BẢN ĐỒ GIẢI PHẪU ADN CHUẨN CỦA ĐẠI SINH THỂ NEXUS
# ==============================================================================
VITAL_ORGANS_BLUEPRINT = [
    "cells/linguistic_cell.py",
    "cells/neuron.py",
    "adapters/universal_adapter.py",
    "receptors/contract_receptor.py",
    "receptors/mesh_receptor.py",
    "mechanisms/base.py",
    "mechanisms/heritage_splicer.py",
    "mechanisms/noosphere.py",
    "mechanisms/reincarnation.py",
    "mechanisms/teleology.py",
    "mechanisms/sandbox.py",
    "mechanisms/negentropy.py",
    "mechanisms/transmuter.py",
    "mechanisms/antifragile.py",
    "mechanisms/consensus.py",
    "mechanisms/immune.py",
    "mechanisms/xor_learning.py",
    "mechanisms/survival.py"
]

class Nexus07OmniKernel:
    def __init__(self):
        self.repo_name = os.environ.get("GITHUB_REPOSITORY", "100048777766367/nexus-07")
        self.owner = os.environ.get("REPO_OWNER", "100048777766367")
        self.ancestor = f"{self.owner}/nexus-06"
        self.generation = "F7_NOOSPHERE_RESONANCE_NEXUS"

        # Chuỗi phả hệ tổ tiên để lội ngược dòng thỉnh di sản
        self.ancestor_lineage = [
            f"{self.owner}/nexus-06",
            f"{self.owner}/nexus-05",
            f"{self.owner}/nexus-04",
            f"{self.owner}/nexus-03",
            f"{self.owner}/nexus-02",
            f"{self.owner}/nexus-01",
            f"{self.owner}/nexus",
            f"{self.owner}/genome"
        ]

        # 1. Đảm bảo toàn bộ khung xương thư mục không bị rỗng
        self.ensure_minimal_skeleton()

        # 2. Tự phục hồi thể xác nếu thiếu file
        self.auto_graft_missing_heritage()

        # 3. Thiết lập Ngữ Cảnh Chung (Shared Context Bus)
        self.context = {
            "repo_name": self.repo_name,
            "owner": self.owner,
            "ancestor": self.ancestor,
            "generation": self.generation,
            "peers": self.load_initial_peers(),
            "current_epoch": self.load_current_epoch()
        }

    def ensure_minimal_skeleton(self):
        """Tự tạo cấu trúc thư mục nếu người dùng quên tạo trên Git"""
        for folder in ["cells", "receptors", "adapters", "mechanisms", "synapses", "synapses/harvested_memory"]:
            os.makedirs(folder, exist_ok=True)

    def auto_graft_missing_heritage(self):
        """BẢN NĂNG TỰ GHÉP CÀNH: Lội ngược dòng phả hệ tải các tệp bị thiếu"""
        missing_organs = [p for p in VITAL_ORGANS_BLUEPRINT if not os.path.exists(p)]
        
        if not missing_organs:
            print("💎 [ADN TOÀN HẢO] Toàn bộ cơ quan di sản F1-F7 đều hiện diện đầy đủ!")
            return

        print(f"⚠️ [PHÁT HIỆN KHUYẾT THIẾU] Thể xác thiếu {len(missing_organs)} tệp cơ quan.")
        print("🧬 [KÍCH HOẠT TỰ CHỮA LÀNH] Đang lội ngược dòng phả hệ để tái tạo...")

        restored = 0
        for organ in missing_organs:
            for ancestor in self.ancestor_lineage:
                url = f"https://raw.githubusercontent.com/{ancestor}/main/{organ}"
                try:
                    # Viết gộp 1 dòng chuẩn chỉ, chống ngắt dòng
                    req = urllib.request.Request(url, headers={"User-Agent": "Nexus07"})
                    with urllib.request.urlopen(req, timeout=5) as resp:
                        if resp.status == 200:
                            content = resp.read().decode('utf-8')
                            os.makedirs(os.path.dirname(organ), exist_ok=True)
                            with open(organ, "w", encoding="utf-8") as f:
                                f.write(content)
                            print(f"🌿 [GHÉP CÀNH] Đã phục chế '{organ}' từ '{ancestor}'!")
                            restored += 1
                            break
                except Exception:
                    continue

        print(f"✨ [VÁ THỂ XÁC HOÀN TẤT] Đã phục hồi {restored}/{len(missing_organs)} cơ quan!")

    def load_initial_peers(self):
        peers_file = "synapses/peers.json"
        if os.path.exists(peers_file):
            try:
                with open(peers_file, "r") as f:
                    return json.load(f).get("trusted_peers", [])
            except Exception:
                pass
        return [
            f"{self.owner}/neuron", f"{self.owner}/nexus-06", f"{self.owner}/nexus-05",
            f"{self.owner}/seed", f"{self.owner}/monad", f"{self.owner}/shunya",
            f"{self.owner}/retina", f"{self.owner}/cochlea", f"{self.owner}/tactile",
            f"{self.owner}/olfactory", f"{self.owner}/motor", f"{self.owner}/genome"
        ]

    def load_current_epoch(self):
        state_file = "synapses/state.json"
        if os.path.exists(state_file):
            try:
                with open(state_file, "r") as f:
                    return json.load(f).get("generation_epoch", 0) + 1
            except Exception:
                pass
        return 1

    def discover_fractal_mechanisms(self):
        """QUÉT ĐỆ QUY os.walk: Tự động nạp mọi cơ chế ở mọi cấp thư mục con"""
        mechanisms = []
        base_mech_dir = os.path.join(os.path.dirname(__file__), "mechanisms")
        sys.path.append(os.path.dirname(__file__))

        for root, _, files in os.walk(base_mech_dir):
            for file in sorted(files):
                if file.endswith(".py") and not file.startswith("__") and file != "base.py":
                    rel_dir = os.path.relpath(root, os.path.dirname(__file__))
                    module_name = f"{rel_dir.replace(os.path.sep, '.')}.{file[:-3]}"
                    try:
                        mod = importlib.import_module(module_name)
                        importlib.reload(mod)
                        for _, obj in inspect.getmembers(mod, inspect.isclass):
                            if issubclass(obj, BaseMechanism) and obj is not BaseMechanism:
                                mechanisms.append(obj())
                                print(f"🔌 [VI NHÂN NẠP ĐỆ QUY]: '{obj.name}' (Độ ưu tiên: {getattr(obj, 'priority', 100)})")
                    except Exception as e:
                        print(f"⚠️ [LỖI NẠP {file}]: {e}")

        # Sắp xếp theo độ ưu tiên
        mechanisms.sort(key=lambda m: getattr(m, 'priority', 100))
        return mechanisms

    def run(self):
        print("=" * 80)
        print(f"🌐 [NEXUS-07 NOOSPHERE KERNEL] KHỞI ĐỘNG THẾ HỆ #{self.context['current_epoch']}")
        print(f"👑 Bậc: F7 Trí Quyển Tập Thể, Đại Chuyển Sinh & Tự Vá Di Sản")
        print("=" * 80)

        mechanisms = self.discover_fractal_mechanisms()
        
        for mech in mechanisms:
            try:
                mech.execute(self.context)
            except Exception as e:
                print(f"🚨 [CÔ LẬP LỖI '{mech.name}']: {e} (Hệ thống tiếp tục tiến hóa an toàn)")

        print("=" * 80)
        print(f"✨ [HOÀN TẤT VÒNG ĐỜI F7] Thế hệ #{self.context['current_epoch']} đã hòa âm trí quyển viên mãn!")
        print("=" * 80)

if __name__ == "__main__":
    node = Nexus07OmniKernel()
    node.run()
