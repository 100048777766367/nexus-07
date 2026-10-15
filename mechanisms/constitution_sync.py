import urllib.request
from mechanisms.base import BaseMechanism

class ConstitutionSyncMechanism(BaseMechanism):
    name = "constitution_sync"
    priority = 2

    def execute(self, context):
        owner = context.get("owner", "STUMMOGHI")
        manifest_url = f"https://raw.githubusercontent.com/{owner}/.github/main/README.md"
        try:
            req = urllib.request.Request(manifest_url, headers={"User-Agent": "Nexus07-Constitution-Listener"})
            with urllib.request.urlopen(req, timeout=3) as resp:
                if resp.status == 200:
                    print(f"📡 [BẮT SÓNG HIẾN PHÁP] Đã kết nối với Ngọn Hải Đăng '{owner}/.github'!")
                    context["mother_constitution_active"] = True
                    return
        except Exception:
            pass
        print("🌿 [TỰ TRỊ TUYỆT ĐỐI] Tự vận hành bằng bản lĩnh độc lập nội tại!")
        context["mother_constitution_active"] = False
