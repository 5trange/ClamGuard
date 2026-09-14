FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    wget \
    git \
    unzip \
    xz-utils \
    file \
    binutils \
    desktop-file-utils \
    squashfs-tools \
    patchelf \
    libfuse2 \
    fuse \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:${PATH}"
ENV UV_LINK_MODE=copy
ENV APPIMAGE_EXTRACT_AND_RUN=1

WORKDIR /app

# Copy package metadata and README before uv sync.
COPY pyproject.toml uv.lock* README.md ./

RUN uv sync --frozen

# Now copy the actual project.
COPY . .

RUN chmod +x build.py

RUN uv run python build.py production

CMD ["bash"]
