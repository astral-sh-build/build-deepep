import importlib
from importlib.metadata import version

import pytest
import torch


@pytest.fixture(scope="module")
def device() -> torch.device:
    assert torch.cuda.is_available(), "The tests must run on a CUDA GPU"
    device = torch.device("cuda")
    assert torch.cuda.get_device_capability(device)[0] >= 9
    return device


def test_published_cuda_wheel(device: torch.device) -> None:
    assert version("deep-ep") == "1.2.1+cu.12.8.torch.2.10"
    assert torch.__version__ == "2.10.0+cu128"
    assert torch.version.cuda == "12.8"
    assert torch.cuda.get_device_name(device)


@pytest.mark.parametrize("module_name", ["deep_ep", "deep_ep_cpp"])
def test_native_module(device: torch.device, module_name: str) -> None:
    assert importlib.import_module(module_name) is not None


def test_native_dispatch_configuration(device: torch.device) -> None:
    import deep_ep
    import deep_ep_cpp

    assert deep_ep.Buffer is not None
    assert deep_ep.Config is deep_ep_cpp.Config
    assert hasattr(deep_ep_cpp, "Buffer")


def test_hopper_gpu_collective_support(device: torch.device) -> None:
    assert torch.cuda.nccl.version() is not None
    assert torch.cuda.get_device_capability(device)[0] >= 9
