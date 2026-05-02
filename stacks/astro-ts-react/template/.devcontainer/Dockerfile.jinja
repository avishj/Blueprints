# syntax=docker/dockerfile:1

# uv v0.11.7
FROM ghcr.io/astral-sh/uv:0.11.7@sha256:240fb85ab0f263ef12f492d8476aa3a2e4e1e333f7d67fbdd923d00a506a516a AS uv

# bun v1.3.12
FROM oven/bun:1.3.12@sha256:8956c7667fa17beb6e3c664115e66bdacfe502da5d99603626e74c197bdef160 AS bun

# 2.1.7
FROM mcr.microsoft.com/devcontainers/base:2.1.7@sha256:aa263c6fdd7c1bc990eead3922224fe8afbf5d85eaf3b6b9260786ab94d74933

COPY --from=uv /uv /uvx /usr/local/bin/
COPY --from=bun /usr/local/bin/bun /usr/local/bin/bunx /usr/local/bin/

# rust-just 1.50.0
RUN UV_TOOL_BIN_DIR=/usr/local/bin UV_TOOL_DIR=/opt/uv-tools uv tool install rust-just==1.50.0
