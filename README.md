# build-deepep

Pre-built Linux wheels for [DeepEP](https://github.com/deepseek-ai/DeepEP), across Python, PyTorch,
CUDA, and CPU architectures.

## Installation

Following the PyTorch convention, artifacts are published to a separate index for each CUDA
version. Wheel versions identify the upstream source revision, CUDA version, PyTorch version, and
C++ ABI used for the build, as in
`deep-ep==1.2.1+1300811.cu12.8torch2.10.0cxx11abiTRUE`, and require the matching PyTorch release.

Pre-built wheels are available on [Astral's GPU indexes](https://wheels.astralhosted.com/index.html).
For example, to install a CUDA 12.8 build:

```console
$ uv add deep-ep --index astral-cu128=https://wheels.astralhosted.com/simple/cu128/
```

This configures the index and uses it as the source for `deep-ep`:

```toml
[tool.uv.sources]
deep-ep = { index = "astral-cu128" }

[[tool.uv.index]]
name = "astral-cu128"
url = "https://wheels.astralhosted.com/simple/cu128/"
```

Or, with `uv pip`:

```console
$ uv pip install --index https://wheels.astralhosted.com/simple/cu128/ deep-ep
```

## Supported versions

Wheels are available for the following `deep-ep` versions:

- [`1.2.1`](https://github.com/astral-sh-build/build-deepep/releases/tag/v1.2.1-r1)

The latest release, DeepEP 1.2.1, supports the following combinations:

| PyTorch | Python    | `x86_64` CUDA | `aarch64` CUDA |
| ------- | --------- | ------------- | -------------- |
| 2.7.1   | 3.9–3.13  | 12.8          | 12.8           |
| 2.8.0   | 3.9–3.13  | 12.8, 12.9    | 12.9           |
| 2.9.0   | 3.10–3.14 | 12.8, 12.9    | 12.8, 12.9     |
| 2.10.0  | 3.10–3.14 | 12.8, 12.9    | 12.8, 12.9     |

## License

build-deepep is licensed under the [Apache License, Version 2.0](LICENSE).

<div align="center">
  <a target="_blank" href="https://astral.sh" style="background:none">
    <img src="https://raw.githubusercontent.com/astral-sh/ruff/main/assets/svg/Astral.svg" alt="Made by Astral">
  </a>
</div>
