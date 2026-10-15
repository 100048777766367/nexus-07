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
# 1. BẢN ĐỒ GIẢI PHẪU ADN CHUẨN CẦN THIẾT CỦA ĐẠI SINH THỂ NEXUS
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

        # 1. Đảm bảo toàn bộ khung xương cơ bản không bị rỗng
        self.ensure_minimal_skeleton()

        # 2. Tự phục hồi thể xác nếu người dùng quên file khi fork
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
        missing_organs = [path for path in VITAL_ORGANS_BLUEPRINT if not os.path.exists(path)]
        
        if not missing_organs:
            print("💎 [ADN TOÀN HẢO] Toàn bộ cơ quan di sản F1-F7 đều hiện diện đầy đủ!")
            return

        print(f"⚠️ [PHÁT HIỆN KHUYẾT THIẾU] Thể xác thiếu {len(missing_organs)} tệp cơ quan: {missing_organs}")
        print("🧬 [KÍCH HOẠT TỰ CHỮA LÀNH] Đang lội ngược dòng phả hệ để tái tạo...")

        restored = 0
        for organ in missing_organs:
            for ancestor in self.ancestor_lineage:
                url = f"https://raw.githubusercontent.com/{ancestor}/main/{organ}"
                try:
                    req =
