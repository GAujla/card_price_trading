ARG VERSION="22.04"
FROM ubuntu:${VERSION} AS base

RUN apt update -y \
    && apt upgrade -y \
    && apt install wget -y \
    && apt install software-properties-common -y

RUN add-apt-repository ppa:deadsnakes \
    && apt update -y \
    && DEBIAN_FRONTEND=noninteractive apt -y install python3.13-nogil python3.13

RUN  wget -qO- https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/usr/bin" sh


ARG USERNAME=card_price_trading
ARG USER_UID=1000
ARG USER_GUID=${USER_UID}

RUN groupadd --gid ${USER_GUID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GUID} -m ${USERNAME} \
    && apt update -y \
    && apt upgrade -y \
    && apt install -y sudo \
    && apt-get install python3-pip -y sudo \
    && echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

USER ${USERNAME}

COPY . /card_price_trading
WORKDIR /card_price_trading
RUN sudo chown -R ${USERNAME}:${USERNAME} /card_price_trading \
    && uv venv && uv add pip && uv sync \
    && uv add pre-commit
