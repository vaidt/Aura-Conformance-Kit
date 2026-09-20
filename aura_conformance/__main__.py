"""CLI entry point for the Aura Conformance Kit."""

from __future__ import annotations

import sys

from aura_conformance.certificate import CertificateGenerator


def main(argv: list[str] | None = None) -> int:
    """Run the minimal Aura conformance CLI."""
    args = list(sys.argv[1:] if argv is None else argv)
    if args != ["run"]:
        raise SystemExit("usage: python -m aura_conformance run")

    generator = CertificateGenerator()
    certificate = generator.build_certificate(
        contract_id="AIC-000",
        contract_version="1.0.0",
        consensus=True,
        score=100,
    )
    generator.save_certificate(certificate)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
