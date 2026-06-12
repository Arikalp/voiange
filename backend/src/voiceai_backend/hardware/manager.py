from voiceai_backend.hardware.detector import GpuDetector
from voiceai_backend.hardware.schemas import GpuReport


class HardwareManager:
    def __init__(self) -> None:
        self.detector = GpuDetector()

    def get_report(self) -> GpuReport:
        return self.detector.detect()
