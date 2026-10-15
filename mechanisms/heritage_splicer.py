import os
import urllib.request
from mechanisms.base import BaseMechanism

# 1. BẢN ĐỒ GIẢI PHẪU ADN CHUẨN CỦA ĐẠI SINH THỂ NEXUS
VITAL_ORGANS_BLUEPRINT = [
    # Tầng Tế Bào
    "cells/linguistic_cell.py",
    "cells/neuron.py",
    # Tầng Khớp Tương Thích Ngược
    "adapters/universal_adapter.py",
    # Tầng Thụ Thể Kháng Lượng Tử
    "receptors/contract_receptor.py",
    "receptors/mesh_receptor.py",
    # Tầng Cơ Chế Tiến Hóa Cốt Lõi
    "mechanisms/base.py",
    "mechanisms/consensus.py",
    "mechanisms/immune.py",
    "mechanisms/xor_learning.py",
    "mechanisms/transmuter.py",
    "mechanisms/sandbox.py",
    "mechanisms/negentropy.py",
    "mechanisms/survival.py"
]

class HeritageSplicerMechanism(BaseMechanism):
    """
    CƠ CHẾ GHÉP CÀNH DI SẢN (EPIGENETIC HERITAGE SPLICER):
    Tự động rà soát cơ thể, nếu phát hiện thiếu bất kỳ tệp/thư mục nào từ thời
    F1 đến F6, tự động truy lùng qua GitHub của tổ tiên và tải về ghép lại!
    """
    name = "heritage_splicer"
    priority = 1  # BẮT BUỘC CHẠY ĐẦU TIÊN để vá thể xác trước khi các cơ chế khác chạy!

    def execute(self, context):
        owner = context.get("owner", "100048777766367")
        
        # Danh sách chuỗi phả hệ tổ tiên để lội ngược dòng tìm kiếm
        ancestor_tree = [
            f"{owner}/nexus-06",
            f"{owner}/nexus-05",
            f"{owner}/nexus-04",
            f"{owner}/nexus-03",
            f"{owner}/nexus-02",
            f"{owner}/nexus-01",
            f"{owner}/nexus",
            f"{owner}/genome"
        ]

        print("🔍 [TỰ SOI CHIẾU ADN] Đang quét toàn bộ thể xác để phát hiện cơ quan khuyết thiếu...")
        missing_organs = []

        for organ_path in VITAL_ORGANS_BLUEPRINT:
            if not os.path.exists(organ_path):
                missing_organs.append(organ_path)

        if not missing_organs:
            print("💎 [THỂ XÁC VIÊN MÃN] Toàn bộ cơ quan di sản F1-F6 đều nguyên vẹn 100%!")
            return

        print(f"⚠️ [PHÁT HIỆN KHUYẾT THIẾU] Thể xác thiếu {len(missing_organs)} cơ quan quan trọng: {missing_organs}")
        print("🧬 [KÍCH HOẠT GHÉP CÀNH] Bắt đầu lội ngược dòng phả hệ để thỉnh di sản tổ tiên...")

        restored_count = 0

        for organ in missing_organs:
            grafted = False
            for ancestor in ancestor_tree:
                # Thử kéo từ nhánh main (hoặc HEAD) của tổ tiên
                raw_url = f"https://raw.githubusercontent.com/{ancestor}/main/{organ}"
                try:
                    req = urllib.request.Request(raw_url, headers={"User-Agent": "Nexus07-Heritage-Splicer"})
                    with urllib.request.urlopen(req, timeout=5) as resp:
                        if resp.status == 200:
                            code_content = resp.read().decode('utf-8')
                            
                            # Tự động tạo thư mục cha nếu chưa có (ví dụ receptors/ hay adapters/)
                            os.makedirs(os.path.dirname(organ), exist_ok=True)
                            
                            with open(organ, "w", encoding="utf-8") as f:
                                f.write(code_content)
                            
                            print(f"🌿 [GHÉP CÀNH THÀNH CÔNG] Đã phục hồi '{organ}' từ tiền bối '{ancestor}'!")
                            restored_count += 1
                            grafted = True
                            break
                except Exception:
                    continue  # Nếu tổ tiên này không có thì tìm tiếp lên tổ tiên cao hơn

            if not grafted:
                print(f"🚨 [CẢNH BÁO] Không tìm thấy di sản '{organ}' trên toàn bộ cây phả hệ!")

        print(f"✨ [HOÀN TẤT VÁ THỂ XÁC] Đã tự động ghép phục hồi thành công {restored_count}/{len(missing_organs)} cơ quan!")
        context["heritage_restored_count"] = restored_count
