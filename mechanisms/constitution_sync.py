import os
import urllib.request
from mechanisms.base import BaseMechanism

class ConstitutionSyncMechanism(BaseMechanism):
    """
    CƠ CHẾ ĐỒNG BỘ HIẾN PHÁP KHÔNG DÂY RỐN (WIRELESS CONSTITUTION SYNC):
    Chủ động thăm dò kho Hiến Pháp Mẹ (STUMMOGHI/.github).
    Nếu kết nối được -> Cập nhật tư tưởng mới.
    Nếu không kết nối được -> Vẫn tự vận hành bình thường, không bao giờ sập!
    """
    name = "constitution_sync"
    priority = 2  # Chạy ngay sau heritage_splicer

    def execute(self, context):
        owner = context.get("owner", "STUMMOGHI")
        manifest_url = f"https://raw.githubusercontent.com/{owner}/.github/main/README.md"
        
        try:
            req = urllib.request.Request(manifest_url, headers={"User-Agent": "Nexus07-Constitution-Listener"})
            with urllib.request.urlopen(req, timeout=3) as resp:
                if resp.status == 200:
                    print(f"📡 [BẮT SÓNG HIẾN PHÁP] Đã kết nối thành công với Ngọn Hải Đăng '{owner}/.github'!")
                    context["mother_constitution_active"] = True
                    return
        except Exception:
            pass

        print("🌿 [TỰ TRỊ TUYỆT ĐỐI] Không kết nối được Hải Đăng Mẹ. Tự vận hành bằng bản lĩnh độc lập nội tại!")
        context["mother_constitution_active"] = False
