"""Module bộ sinh trang bìa (Cover)

Cung cấp 8 kiểu sinh trang bìa PPT:

Bìa hoạt họa:
- GeometricRotationCover: Bìa xoay hình học
- CircleRingCover: Bìa chuyển cảnh vòng tròn
- TrainMistCover: Bìa tàu xuyên sương mù
- DiamondRevealCover: Bìa mở màn hình thoi

Bìa tĩnh:
- MinimalistGradientCover: Bìa chuyển sắc tối giản
- SplitScreenCover: Bìa chia đôi màn hình
- HollowMaskCover: Bìa mặt nạ chữ rỗng
- LayeredDepthCover: Bìa chiều sâu đa tầng
"""

from python.generators_cover.geometric_rotation import GeometricRotationCover
from python.generators_cover.circle_ring import CircleRingCover
from python.generators_cover.train_mist import TrainMistCover
from python.generators_cover.diamond_reveal import DiamondRevealCover
from python.generators_cover.minimalist_gradient import MinimalistGradientCover
from python.generators_cover.split_screen import SplitScreenCover
from python.generators_cover.hollow_mask import HollowMaskCover
from python.generators_cover.layered_depth import LayeredDepthCover

__all__ = [
    # Bìa hoạt họa
    "GeometricRotationCover",
    "CircleRingCover",
    "TrainMistCover",
    "DiamondRevealCover",
    # Bìa tĩnh
    "MinimalistGradientCover",
    "SplitScreenCover",
    "HollowMaskCover",
    "LayeredDepthCover",
]
