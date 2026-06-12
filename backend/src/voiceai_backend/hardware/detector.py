from __future__ import annotations

import psutil

try:
    import torch
except Exception:  # pragma: no cover - fallback when torch is unavailable at import time
    torch = None

from voiceai_backend.hardware.schemas import CpuInfo, GpuDevice, GpuReport, MemoryInfo


class GpuDetector:
    def detect(self) -> GpuReport:
        memory = psutil.virtual_memory()
        cpu = CpuInfo(
            physical_cores=psutil.cpu_count(logical=False) or 0,
            logical_cores=psutil.cpu_count(logical=True) or 0,
            usage_percent=psutil.cpu_percent(interval=0.1),
        )
        memory_info = MemoryInfo(
            total_mb=int(memory.total / 1024 / 1024),
            available_mb=int(memory.available / 1024 / 1024),
            usage_percent=memory.percent,
        )

        devices: list[GpuDevice] = []
        cuda_available = bool(torch and torch.cuda.is_available())
        if cuda_available and torch:
            for index in range(torch.cuda.device_count()):
                props = torch.cuda.get_device_properties(index)
                free_bytes, total_bytes = torch.cuda.mem_get_info(index)
                devices.append(
                    GpuDevice(
                        index=index,
                        name=props.name,
                        memory_total_mb=int(total_bytes / 1024 / 1024),
                        memory_free_mb=int(free_bytes / 1024 / 1024),
                        is_cuda=True,
                    )
                )

        return GpuReport(cuda_available=cuda_available, devices=devices, cpu=cpu, memory=memory_info)
