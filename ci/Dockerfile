FROM continuumio/miniconda3
MAINTAINER OCTO DD team <datadriver@octo.com>

ARG ENV_PY_VERSION
ARG ENV_NAME

COPY ./Makefile .
COPY ./setup.py .
COPY ./setup.cfg .
COPY ./ci/test_requirements.txt ./ci/test_requirements.txt
COPY ./README.rst .

SHELL ["/bin/bash", "-c"]

RUN apt update \
    && apt-get install -y make \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

RUN conda config --set auto_update_conda False \
    && conda install conda=4.5.11 -y \
    && conda install -c conda-forge pandoc anaconda-client=1.7.2 awscli -y

RUN make develop_env ENV_PY_VERSION=${ENV_PY_VERSION} ENV_NAME=${ENV_NAME}
