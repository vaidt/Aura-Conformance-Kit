import json

import pytest

from aura_conformance.__main__ import main
from aura_conformance.certificate.certificate_generator import CertificateGenerator


def test_build_certificate_consensus_true():
    """
    Testuje tworzenie struktury certyfikatu z pozytywnym wynikiem konsensusu.
    """
    generator = CertificateGenerator()
    cert = generator.build_certificate(
        contract_id="AIC-000",
        contract_version="1.0.0",
        consensus=True,
        score=100,
        errors=["Ten błąd nie powinien się tu znaleźć"],
    )

    assert cert["consensus"] is True
    assert cert["score"] == 100
    assert cert["contract_id"] == "AIC-000"
    assert "errors" not in cert


def test_build_certificate_consensus_false():
    """
    Testuje tworzenie struktury certyfikatu po wystąpieniu błędu krytycznego (Fast-Fail).
    """
    generator = CertificateGenerator()
    cert = generator.build_certificate(
        contract_id="AIC-000",
        contract_version="1.0.0",
        consensus=False,
        score=100,
        errors=["Krytyczny błąd struktury"],
    )

    assert cert["consensus"] is False
    assert cert["score"] == 0
    assert "errors" in cert
    assert cert["errors"][0] == "Krytyczny błąd struktury"


def test_save_certificate(tmp_path):
    """
    Testuje fizyczny zapis certyfikatu na dysk oraz jego poprawność strukturalną po odczycie.
    Wykorzystuje mechanizm tmp_path dostarczany przez pytest.
    """
    # 1. Przygotowanie tymczasowej ścieżki
    test_file = tmp_path / "test_certificate.json"
    generator = CertificateGenerator(output_path=str(test_file))

    # 2. Zbudowanie certyfikatu w pamięci
    cert_data = generator.build_certificate(
        contract_id="AIC-000", contract_version="1.0.0", consensus=True, score=100
    )

    # 3. Zapis na dysk
    generator.save_certificate(cert_data)

    # 4. Weryfikacja istnienia pliku
    assert test_file.exists()

    # 5. Odczyt i weryfikacja zawartości
    with open(test_file, "r", encoding="utf-8") as f:
        saved_data = json.load(f)

    assert saved_data["consensus"] is True
    assert saved_data["contract_id"] == "AIC-000"


def test_build_certificate_requires_errors_for_non_consensus():
    """
    Testuje, że certyfikat negatywny wymaga co najmniej jednego błędu.
    """
    generator = CertificateGenerator()

    with pytest.raises(
        ValueError, match="non-consensus certificates require at least one error"
    ):
        generator.build_certificate(
            contract_id="AIC-000",
            contract_version="1.0.0",
            consensus=False,
            score=100,
            errors=[],
        )


def test_cli_run_creates_certificate(tmp_path, monkeypatch):
    """
    Testuje ścieżkę CLI używaną przez krok smoke test w CI.
    """
    monkeypatch.chdir(tmp_path)

    assert main(["run"]) == 0

    saved_data = json.loads((tmp_path / "certificate.json").read_text(encoding="utf-8"))
    assert saved_data["consensus"] is True
    assert saved_data["contract_id"] == "AIC-000"


def test_cli_run_rejects_invalid_arguments():
    """
    Testuje ścieżkę błędu CLI dla nieprawidłowych argumentów.
    """
    with pytest.raises(SystemExit, match="usage: python -m aura_conformance run"):
        main([])
