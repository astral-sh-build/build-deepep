#!/bin/bash
# Script to prepare the build environment for DeepEP.
#
# Example usage:
#   ./prepare_for_build.sh v1.2.1

set -euxo pipefail

# When run from CI, this script is in build_scripts/prepare_for_build.sh
# and needs to reference patches from that directory
export SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
export ROOT=`pwd`

if [ $# -ne 1 ]; then
    echo "Usage: $0 <deepep-version>"
    echo "Example: $0 v1.2.1"
    exit 1
fi

DEEPEP_VERSION=$1

# Apply patches if the directory exists for this version.
if [ -d "${SCRIPT_DIR}/patches/${DEEPEP_VERSION}" ]; then
    for patch in "${SCRIPT_DIR}/patches/${DEEPEP_VERSION}"/*.patch; do
        if [ -f "${patch}" ]; then
            patch -p1 -d ${ROOT} -i ${patch}
        fi
    done
fi
