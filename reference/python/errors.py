"""
Aura TCK reference implementation exception hierarchy.

Organized by architectural layer:
    - ParsingError: JSON parsing, numeric type detection
    - ValidationError: EES model validation, type checking
    - CanonicalizationError: Canonical form generation (CSS)
    - OracleError: Oracle comparison and verification
    - TestVectorError: Test fixture validation
"""


class AuraError(Exception):
    """Base exception for all Aura TCK errors."""


# ============================================================================
# ParsingError
# ============================================================================


class ParsingError(AuraError):
    """Raised during parsing phase."""


class InvalidJSONError(ParsingError):
    """Raised when JSON parsing fails."""


class UnsupportedNumericTypeError(ParsingError):
    """Raised when unsupported numeric type (float, etc.) is encountered."""


# ============================================================================
# ValidationError
# ============================================================================


class ValidationError(AuraError):
    """Raised during EES model validation."""


class TypeValidationError(ValidationError):
    """Raised when type validation fails."""


class RequiredFieldError(ValidationError):
    """Raised when a required field is missing."""


class ValueConstraintError(ValidationError):
    """Raised when a value constraint is violated."""


class CryptographicTypeError(ValueConstraintError):
    """Raised when cryptographic type validation fails."""


class InvalidSHA256DigestError(CryptographicTypeError):
    """Raised when SHA256Digest validation fails."""


class InvalidPublicKeyError(CryptographicTypeError):
    """Raised when PublicKey validation fails."""


class InvalidSignatureError(CryptographicTypeError):
    """Raised when Signature validation fails."""


class InvalidKeyIdentifierError(CryptographicTypeError):
    """Raised when KeyIdentifier validation fails."""


# ============================================================================
# CanonicalizationError
# ============================================================================


class CanonicalizationError(AuraError):
    """Raised during canonical form generation (CSS)."""


class CanonicalOrderingError(CanonicalizationError):
    """Raised when canonical ordering fails."""


class CanonicalEncodingError(CanonicalizationError):
    """Raised when canonical encoding fails."""


class DeterminismError(CanonicalizationError):
    """Raised when determinism check fails."""


# ============================================================================
# OracleError
# ============================================================================


class OracleError(AuraError):
    """Raised during Oracle comparison."""


class OracleMismatchError(OracleError):
    """Raised when Oracle comparison mismatches."""


class OracleVersionMismatchError(OracleError):
    """Raised when Oracle version mismatches."""


class OracleSignatureError(OracleError):
    """Raised when Oracle signature verification fails."""


# ============================================================================
# TestVectorError
# ============================================================================


class TestVectorError(AuraError):
    """Raised during test vector processing."""


class TestVectorFormatError(TestVectorError):
    """Raised when test vector format is invalid."""


class TestVectorExpectationError(TestVectorError):
    """Raised when test vector expectation is not met."""


__all__ = [
    "AuraError",
    "CanonicalEncodingError",
    "CanonicalOrderingError",
    "CanonicalizationError",
    "CryptographicTypeError",
    "DeterminismError",
    "InvalidJSONError",
    "InvalidKeyIdentifierError",
    "InvalidPublicKeyError",
    "InvalidSHA256DigestError",
    "InvalidSignatureError",
    "OracleError",
    "OracleMismatchError",
    "OracleSignatureError",
    "OracleVersionMismatchError",
    "ParsingError",
    "RequiredFieldError",
    "TestVectorError",
    "TestVectorExpectationError",
    "TestVectorFormatError",
    "TypeValidationError",
    "UnsupportedNumericTypeError",
    "ValidationError",
    "ValueConstraintError",
]
