"""Certificate generation utilities used by tests and smoke checks."""

from __future__ import annotations

import json
from pathlib import Path


class CertificateGenerator:
    """Build and persist Aura conformance certificates."""

    def __init__(self, output_path: str = "certificate.json") -> None:
        self.output_path = Path(output_path)

    def build_certificate(
        self,
        *,
        contract_id: str,
        contract_version: str,
        consensus: bool,
        score: int,
        errors: list[str] | None = None,
    ) -> dict[str, str | int | bool | list[str]]:
        """Build a certificate payload."""
        certificate: dict[str, str | int | bool | list[str]] = {
            "contract_id": contract_id,
            "contract_version": contract_version,
            "consensus": consensus,
            "score": score if consensus else 0,
        }
        if not consensus:
            certificate["errors"] = [] if errors is None else errors
        return certificate

    def save_certificate(
        self, certificate: dict[str, str | int | bool | list[str]]
    ) -> None:
        """Write a certificate payload to disk as JSON."""
        self.output_path.write_text(
            json.dumps(certificate, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
