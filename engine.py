import os
import sys
import json
import importlib
import inspect
from mechanisms.base import BaseMechanism

class Nexus07OmniKernel:
    def __init__(self):
        self.repo_name = os.environ.get("GITHUB_REPOSITORY", "100048777766367/nexus-07")
        self.owner = os.environ.get("REPO_OWNER", "100048777766367")
        self.ancestor = f"{self.owner}/nexus-06"
        
        self.ensure_skeleton()

        self.context = {
            "repo_name": self.repo_name,
            "owner": self.owner,
            "ancestor": self.ancestor,
            "peers": self.load_peers(),
            "current_epoch": self.load_epoch()
        }

    def ensure_skeleton(self):
        for folder in ["cells", "receptors", "adapters", "mechanisms", "synapses", "synapses/harvested_memory"]:
            os.makedirs(folder, exist_ok=True)

    def load_peers(self):
        p_file = "synapses/peers.json"
        if os.path.exists(p_file):
            try:
                with open(p_file, "r") as f: return json.load(f).get("trusted_peers", [])
            except Exception: pass
        return [
            f"{self.owner}/neuron", f"{self.owner}/nexus-06", f"{self.owner}/nexus-05",
            f"{self.owner}/seed", f"{self.owner}/monad", f"{self.owner}/shunya", f"{self.owner}/motor"
        ]

    def load_epoch(self):
        s_file = "synapses/state.json"
        if os.path.exists(s_file):
            try:
                with open(s_file, "r") as f: return json.load(f).get("generation_epoch", 0) + 1
            except Exception: pass
        return 1

    def discover_fractal_mechanisms(self):
        mechanisms = []
        base_mech_dir = os.path.join(os.path.dirname(__file__), "mechanisms")
        sys.path.append(os.path.dirname(__file__))

        for root, _, files in os.walk(base_mech_dir):
            for file in sorted(files):
                if file.endswith(".py") and not file.startswith("__") and file != "base.py":
                    rel_dir = os.path.relpath(root, os.path.dirname(__file__))
                    module_name = f"{rel_dir.replace(os.path.sep, '.')}.{file[:-3]}"
                    full_file_path = os.path.join(root, file)
                    try:
                        mod = importlib.import_module(module_name)
                        importlib.reload(mod)
                        for _, obj in inspect.getmembers(mod, inspect.isclass):
                            if issubclass(obj, BaseMechanism) and obj is not BaseMechanism:
                                mechanisms.append(obj())
                                print(f"🔌 [VI NHÂN F7 NẠP]: '{obj.name}' từ '{rel_dir}/{file}'")
                    except SyntaxError as se:
                        # TỰ ĐỘNG XÓA TỆP RÁC NẾU CÓ LỖI CÚ PHÁP
                        print(f"🗑️ [TỰ ĐỘNG DỌN RÁC] Xóa tệp lỗi cú pháp '{file}': {se}")
                        try:
                            os.remove(full_file_path)
                        except Exception: pass
                    except Exception as e:
                        print(f"⚠️ [LỖI NẠP {file}]: {e}")

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
                print(f"🚨 [CÔ LẬP LỖI '{mech.name}']: {e} (Tiếp tục chuyển hóa)")

        print("=" * 80)
        print(f"✨ [HOÀN TẤT VÒNG ĐỜI F7] Vũ trụ Noosphere đã đồng nhịp đập viên mãn!")
        print("=" * 80)

if __name__ == "__main__":
    node = Nexus07OmniKernel()
    node.run()
