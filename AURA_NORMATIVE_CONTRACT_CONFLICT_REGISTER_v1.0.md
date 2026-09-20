# AURA_NORMATIVE_CONTRACT_CONFLICT_REGISTER_v1.0

Status: EVIDENCE-BASED ADJUDICATION REGISTER

This document is a decision-preparation artifact only. It records unresolved normative and architectural conflicts affecting AURA canonicalization, serialization, Evidence Pack structure, hashing, Oracle verification, and TCK conformance. It does not approve a specification, bind a repository, migrate code, or imply new authority.

## Scope and method

- Scope repositories: `vaidt/aura-specification`, `vaidt/Aura-Conformance-Kit`, `vaidt/Aura-vNEXT`, `vaidt/aura-guard-v1.3`, `vaidt/Aura-Guard`, `vaidt/Crystal-panel-Aura-Protection`.
- Method: evidence collection from accessible repository files, direct reading of README/docs/spec materials, and static scan of implementation sources for forbidden patterns. This register is not a code migration exercise and does not resolve conflicts by implementation preference.
- Authority ordering used for this record: explicitly normative and approved specification evidence, then verified architecture decisions, then implementation behavior, then historical/reference material.
- Result: no normative closure is declared.

NORMATIVE_CONTRACT_STATUS = UNRESOLVED

---

## Repository role analysis

| Repository | Observed Role | Normative Status | Implementation Status | Historical Status |
|---|---|---|---|---|
| `vaidt/aura-specification` | Normative documentation repository for the protocol | UNVERIFIED / DRAFT-ONLY | Not an implementation repo | Historical provenance + current specification source |
| `vaidt/Aura-Conformance-Kit` | TCK / conformance-kit repo | UNVERIFIED | Early implementation scaffolding | Current evidence-gathering repo |
| `vaidt/Aura-vNEXT` | Candidate reference implementation and M0 product loop | CANDIDATE ONLY | Active implementation evidence | Not final normative authority |
| `vaidt/aura-guard-v1.3` | Historical Rust reference / audit middleware | HISTORICAL REFERENCE ONLY | Active legacy implementation | Historical evidence source |
| `vaidt/Aura-Guard` | JS/Python demonstrator / reconciliation repo | NOT NORMATIVE | Active implementation behavior, but not a verified normative source | Historical and engineering reference only |
| `vaidt/Crystal-panel-Aura-Protection` | Ecosystem map / control-plane shell | NOT VERIFIED | Documentation shell / map repo | Historical map evidence |

---

## Full-tree verification and repository access status

| Repository | Search status | Findings | Classification |
|---|---|---|---|
| `vaidt/aura-specification` | Searched and found | APS docs present; APS-001 TODO; APS-100+ drafts; main repository is documentation only | FOUND |
| `vaidt/Aura-Conformance-Kit` | Searched and found | README and docs present; `docs/EES_IMPLEMENTATION_MAP.md` blank; no complete normative contract under `/spec/` observed | FOUND |
| `vaidt/Aura-vNEXT` | Searched and found | `core/canonical`, `docs/contract/M0-EVIDENCE-CONTRACT.md`, and M0 evidence vectors present | FOUND |
| `vaidt/aura-guard-v1.3` | Searched and found | Rust implementation, docs, conformance, D3 canonical file, but no verified normative APS approval | FOUND |
| `vaidt/Aura-Guard` | Searched and found | JS/Python evidence + float/Math.random/datetime usage; not verified as normative | FOUND |
| `vaidt/Crystal-panel-Aura-Protection` | Searched and found | Ecosystem map docs present; top-level repository includes layered documentation shell | FOUND |

Notes:
- GitHub search results are not treated as complete proof of repository completeness.
- Accessible tree inspection did not establish a final approved normative contract.
- No repository was merged, migrated, or used as source of authority for protocol redesign.

---

## Static code scanning results

Patterns scanned: `float`, `double`, `Math.random`, `random`, `uuid`, `time.now`, `datetime.now`, `Utc::now`, Unicode normalization, confusable folding, implicit normalization, map/object serialization, non-explicit UTF-8, canonical byte generation, hash input construction, signature construction.

| Hit / pattern | Repository / file | Observed behavior | Classification |
|---|---|---|---|
| `float` usage in canonicalizer | `vaidt/Aura-Guard/py_verifier/aura_verify.py` | Python numeric canonicalizer implements `_js_number_to_string(float)` and accepts float values | FORBIDDEN_IN_CANONICAL_PATH |
| `Math.random` | `vaidt/Aura-Guard/frontend/src/lib/conformanceCore.js` | Test mutator uses `Math.random()` in tamper probe | FORBIDDEN_IN_CANONICAL_PATH |
| `datetime.now` | `vaidt/Aura-Guard/backend/server.py` | `datetime.now(timezone.utc)` used in health response | ALLOWED_OUTSIDE_CANONICAL_PATH |
| `float` in confidence conversion | `vaidt/Aura-vNEXT/core/models/__init__.py` | Conversion uses `Decimal(repr(float(value)))` | REQUIRES_ARCHITECTURAL_DECISION |
| `uuid` in Rust dependency | `vaidt/aura-guard-v1.3/Cargo.toml` | `uuid = { version = "1", features = ["v4", "serde"] }` | HISTORICAL_REFERENCE |
| Unicode normalization / confusable folding | `vaidt/aura-guard-v1.3` docs and Rust references | Explicit NFKC / hidden-char stripping / confusable fold statements | HISTORICAL_REFERENCE |
| `float` / `double` prohibition in TCK docs | `vaidt/Aura-Conformance-Kit/.github/copilot-instructions.md` | Explicit zero-float runtime rule stated | FORBIDDEN_IN_CANONICAL_PATH |
| RFC 8785 canonicalization and UTF-16 ordering | `vaidt/Aura-vNEXT/core/canonical/__init__.py` | Explicit UTF-16BE sort and no float representation in M0 canonicalizer | ALLOWED_OUTSIDE_CANONICAL_PATH |
| Hash construction | `vaidt/Aura-vNEXT/core/chain` and `/core/canonical` | Canonical bytes hashed with SHA-256; no verified APS statement yet | REQUIRES_ARCHITECTURAL_DECISION |
| Oracle entities | `vaidt/Aura-Conformance-Kit/reference/python/errors.py` | Oracle error types exist but no verified normative format | REQUIRES_ARCHITECTURAL_DECISION |
| `canonical.bin` | multiple repos | Observed as a test fixture or generated output, but status as protocol artifact is unresolved | REQUIRES_ARCHITECTURAL_DECISION |
| `normalization` and Unicode rules | `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md` | Explicitly says no Unicode normalization | FORBIDDEN_IN_CANONICAL_PATH |

---

## Conflict inventory

### C-001 — Canonical Contract

- Conflict ID: C-001
- Topic: Whether a formally normative canonical contract exists and whether `AURA-CANON/1` is normative or only M0 material.
- Normative source: None verified as approved. `vaidt/aura-specification` contains draft APS files, but `APS-001` is marked `TODO`; no approved canonical contract confirmed. `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md` describes a bound M0 canonical form.
- Exact file/path: `vaidt/aura-specification/README.md`; `vaidt/aura-specification/aps/APS-001_PROTOCOL_SPECIFICATION.md` (status TODO); `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`.
- Exact section or symbol: `README.md` §"What Is This Repository?"; `M0-EVIDENCE-CONTRACT.md` §"3. The canonical form — AURA-CANON/1"; `aps/README.md` entry for APS-001.
- Evidence of current status: `aura-specification` explicitly states the repo is a specification repo but APS-001 remains `TODO`; the canonical contract in `Aura-vNEXT` is stated as M0-specific and not a proven protocol-wide authority. No approved APS document was found to codify the canonical contract.
- Conflicting implementation(s): `vaidt/Aura-vNEXT/core/canonical/__init__.py` (M0 canonicalizer, no floats and explicit UTF-16 sort); `vaidt/Aura-Guard/py_verifier/aura_verify.py` (EMCAScript Number::toString float canonicalization); `vaidt/aura-guard-v1.3` historical docs and conformance around hash/chained evidence.
- Historical/reference evidence: `AURA_ECOSYSTEM_RECONNAISSANCE_v1.0.md` in `Crystal-panel-Aura-Protection` describes high-level repo roles; it does not validate APS authority.
- Classification: CONFLICTING_SOURCES
- Impact on TCK: High; canonical byte semantics are currently disputed; TCK cannot safely assert byte-level equivalence without a chosen contract.
- Required decision: Determine whether `AURA-CANON/1` is normative protocol text or a milestone-specific M0 contract lacking authority.
- Decision authority required: Chief Architect / approved APS authority, if and when a normative document is adopted.
- Current disposition: Unresolved; not approved.
- Re-entry condition: Only after an approved APS or constitutionally ratified specification explicitly defines the canonical contract.
- Evidence provenance: `vaidt/aura-specification/README.md`; `vaidt/aura-specification/aps/README.md`; `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/Aura-vNEXT/core/canonical/__init__.py`.

### C-002 — Numeric Domain

- Conflict ID: C-002
- Topic: Whether integers are the only normative numeric type; whether float/double are globally forbidden or only within canonicalization; whether numeric input text is permitted; whether `Decimal` is normative or implementation-only; whether basis-point scaling is part of protocol semantics or M0-only.
- Normative source: APS material is draft and does not resolve this conclusively. `aura-specification` README states `INV-007` zero float runtime as a critical invariant, but that invariant sits in draft status.
- Exact file/path: `vaidt/aura-specification/README.md`; `vaidt/aura-specification/aps/APS-100_PROTOCOL_INVARIANTS.md` (draft); `vaidt/Aura-vNEXT/core/models/__init__.py`; `vaidt/Aura-vNEXT/architecture/decisions/ADR-0005-canonical-form-and-hashing.md`; `vaidt/Aura-Guard/docs/INV_FLT_01_NUMERIC_CANONICALIZATION.md`.
- Exact section or symbol: `README.md` §"Protocol Invariants"; `ADR-0005` §"5. Confidence"; `core/models/__init__.py` `confidence_to_basis_points`; `INV_FLT_01_NUMERIC_CANONICALIZATION.md` `Number::toString` rule.
- Evidence of current status: `Aura-vNEXT` states integers only in canonical form and uses basis-point scaling with `Decimal(repr(float(value)))`; `Aura-Guard` explicitly requires IEEE-754 double behavior in canonicalization. The normative document claims a zero-float invariant without approved implementation policy.
- Conflicting implementation(s): `Aura-vNEXT/core/models/__init__.py` accepts float input and converts to basis points; `Aura-Guard/py_verifier/aura_verify.py` canonicalizes floats by `Number::toString` semantics; TCK instructions explicitly prohibit floats.
- Historical/reference evidence: `aura-guard-v1.3` historically includes float-capable canonicalization in a wider deterministic system but there is no verified APS approval of this as protocol law.
- Classification: REQUIRES_ARCHITECTURAL_DECISION
- Impact on TCK: High; TCK policy says all numeric values are integers, but source code and historical reference material make a stronger distinction between public input, canonical representation, and calculation representation.
- Required decision: Resolve the formal boundary among public input type, internal numeric arithmetic, and canonical representation; define whether `Decimal` is permitted and whether basis points are protocol semantics or M0 behavior.
- Decision authority required: Chief Architect + protocol specification authority; implementation alone cannot decide.
- Current disposition: Unresolved; normative decision outstanding.
- Re-entry condition: When APS-001/APS-200/APS-300 settle the numeric domain and the canonical representation rules.
- Evidence provenance: `vaidt/aura-specification/README.md`; `vaidt/Aura-vNEXT/core/models/__init__.py`; `vaidt/Aura-vNEXT/architecture/decisions/ADR-0005-canonical-form-and-hashing.md`; `vaidt/Aura-Guard/docs/INV_FLT_01_NUMERIC_CANONICALIZATION.md`.

### C-003 — Float Boundary

- Conflict ID: C-003
- Topic: Distinguishing public input type, parser representation, internal calculation representation, canonical representation, and test fixture representation for numeric handling.
- Normative source: No verified normative artifact explicitly defines this boundary.
- Exact file/path: `vaidt/Aura-vNEXT/core/models/__init__.py`; `vaidt/Aura-vNEXT/architecture/decisions/ADR-0004-m0-implementation-toolchain.md`; `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/Aura-Guard/docs/INV_FLT_01_NUMERIC_CANONICALIZATION.md`.
- Exact section or symbol: `confidence_to_basis_points`; `ADR-0004` §"Decision"; `M0-EVIDENCE-CONTRACT.md` §"3. The canonical form — AURA-CANON/1"; `INV_FLT_01_NUMERIC_CANONICALIZATION.md` §"Normative rule".
- Evidence of current status: `Aura-vNEXT` explicitly distinguishes representation layers in design docs, but not as approved protocol law; `Aura-Guard` documents float canonicalization as a formal requirement; TCK instructions state zero-float runtime for all numeric values. This establishes a boundary issue, not a decided contract.
- Conflicting implementation(s): Input layer in `Aura-vNEXT` may accept float-compatible decimal values; canonical layer rejects float; `Aura-Guard` canonicalizer accepts and serializes finite doubles; TCK forbids them globally.
- Historical/reference evidence: `aura-guard-v1.3` and `Aura-Guard` historical docs encode float semantics as explicit model behavior, but no verified protocol status.
- Classification: REQUIRES_ARCHITECTURAL_DECISION
- Impact on TCK: High; the TCK cannot decide whether to reject numeric input at parse time, to compute on decimal internally, or to forbid float even in the public API layer.
- Required decision: Define the five-layer numeric boundary explicitly and separately.
- Decision authority required: Specification authority and protocol design authority.
- Current disposition: Unresolved boundary question.
- Re-entry condition: When the APS defines numeric semantics and the canonical contract draws the line between input, arithmetic, and representation.
- Evidence provenance: `vaidt/Aura-vNEXT/core/models/__init__.py`; `vaidt/Aura-vNEXT/architecture/decisions/ADR-0004-m0-implementation-toolchain.md`; `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/Aura-Guard/docs/INV_FLT_01_NUMERIC_CANONICALIZATION.md`.

### C-004 — Unicode

- Conflict ID: C-004
- Topic: Normative rule for Unicode normalization, preservation of original code points, UTF-8, surrogate handling, malformed Unicode, NFKC/NFC/NFD/NFKD, hidden/control characters.
- Normative source: `Aura-vNEXT` contract explicitly says no Unicode normalization and rejects lone surrogates; TCK instructions also say preserve raw code points. `Aura-Guard` documents confusable folding and NFKC-like normalization; `aura-guard-v1.3` includes docs on hidden characters and normalization. APS documents do not provide a verified final policy.
- Exact file/path: `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/Aura-vNEXT/architecture/decisions/ADR-0005-canonical-form-and-hashing.md`; `vaidt/Aura-Guard/docs/INV_FLT_01_NUMERIC_CANONICALIZATION.md` (float doc); `vaidt/Aura-Guard/README.md`; `vaidt/aura-guard-v1.3/README.md`; `vaidt/Aura-Conformance-Kit/.github/copilot-instructions.md`.
- Exact section or symbol: `ADR-0005` §"3. No normalisation"; `M0-EVIDENCE-CONTRACT.md` §"3. The canonical form — AURA-CANON/1"; TCK instructions "Strict Unicode"; `aura-guard-v1.3` README threat model uses normalization comments.
- Evidence of current status: The various repos disagree: `Aura-vNEXT` forbids normalization, TCK forbids implicit normalization, and `Aura-Guard` includes normalization and confusable folding in a security posture. No approved APS text resolves this globally.
- Conflicting implementation(s): `Aura-vNEXT` canonicalization rejects surrogate-containing strings; `Aura-Guard` documents hidden-character stripping and normalization; `aura-guard-v1.3` historical docs design a shadow normalizer; TCK spec says raw code points preserved.
- Historical/reference evidence: `aura-guard-v1.3` historical docs describe normalization as a threat mitigation strategy. This is historical behavior, not approved normative policy.
- Classification: CONFLICTING_SOURCES
- Impact on TCK: High; canonical byte streams differ if Unicode is normalized or if hidden characters are stripped. This is a direct hash-divergence risk.
- Required decision: Choose globally the exact normative Unicode rule: preserve code points, reject lone surrogates, specify UTF-8 encoding semantics, and decide whether hidden/control characters are preserved or rejected.
- Decision authority required: Protocol specification authority; no implementation can choose this alone.
- Current disposition: Unresolved; conflicting evidence remains.
- Re-entry condition: When APS-001/APS-200 explicitly define Unicode string handling and canonicalization for all implementations.
- Evidence provenance: `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/Aura-vNEXT/architecture/decisions/ADR-0005-canonical-form-and-hashing.md`; `vaidt/Aura-Guard/README.md`; `vaidt/aura-guard-v1.3/README.md`; `vaidt/Aura-Conformance-Kit/.github/copilot-instructions.md`.

### C-005 — Key Ordering

- Conflict ID: C-005
- Topic: Exact normative ordering rule for object/member keys in canonical serialization.
- Normative source: The `Aura-vNEXT` contract says `members sorted by UTF-16 code-unit sequence of their names`, which is a specific rule. `Aura-Guard` says it sorts by native default property ordering (`Object.keys(v).sort()` in JS and `sorted(v.keys())` in Python), which agrees on BMP ASCII but may diverge above the BMP. APS documents do not provide a final approved canonicalization rule.
- Exact file/path: `vaidt/Aura-vNEXT/core/canonical/__init__.py`; `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/Aura-Guard/docs/PHASE_3_AMBIGUITY_REGISTER.md`; `vaidt/Aura-Guard/frontend/src/lib/conformanceCore.js` and `py_verifier/aura_verify.py`.
- Exact section or symbol: `_member_sort_key`, `canonicalise`, `M0-EVIDENCE-CONTRACT.md` §"members sorted ... UTF-16 code-unit sequence"; `PHASE_3_AMBIGUITY_REGISTER.md` §"A-001 — Object-key ordering across Unicode".
- Evidence of current status: `Aura-vNEXT` intentionally uses UTF-16BE sorting; `Aura-Guard` documents this as an unresolved ambiguity; the TCK cannot ignore the canonical ordering contract because different orderings produce different bytes.
- Conflicting implementation(s): `Aura-vNEXT/core/canonical` vs `Aura-Guard` canonicalizer and Python verifier.
- Historical/reference evidence: `AURA-Guard` ambiguity register calls the issue blocking; it is not a normative decision.
- Classification: CONFLICTING_SOURCES
- Impact on TCK: Critical; incompatible ordering yields different canonical bytes and different hashes.
- Required decision: Approve the canonical ordering rule and test vectors for Unicode and astral-plane keys.
- Decision authority required: Protocol specification authority and conformance owner.
- Current disposition: Unresolved; implementation-defined behavior remains under review.
- Re-entry condition: When an approved APS or canonical contract defines the exact key ordering rule and test vectors.
- Evidence provenance: `vaidt/Aura-vNEXT/core/canonical/__init__.py`; `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/Aura-Guard/docs/PHASE_3_AMBIGUITY_REGISTER.md`.

### C-006 — Optionality and Null

- Conflict ID: C-006
- Topic: Whether the protocol distinguishes field absent, field present with null, empty string, empty array, empty object, zero, and false.
- Normative source: `Aura-vNEXT` explicitly says `None != Some("")`, and null is not representable in AURA-CANON/1; absence and empty string are distinct. `Aura-Guard` and TCK documentation do not provide a finalized protocol-wide rule.
- Exact file/path: `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/Aura-vNEXT/core/canonical/__init__.py`; `vaidt/Aura-Conformance-Kit/docs/EES_IMPLEMENTATION_MAP.md` (blank placeholder).
- Exact section or symbol: `M0-EVIDENCE-CONTRACT.md` §"Two further rules"; `_emit` null rejection branch.
- Evidence of current status: M0 docs clearly distinguish absent and empty value in the canonical path. But there is no verified APS statement covering all JSON-like distinctions across all fields and all implementations.
- Conflicting implementation(s): `Aura-vNEXT` forbids null in canonical representation; `Aura-Guard` canonicalization accepts JSON `null` semantics in generic canonicalization; TCK does not yet have normative field mapping from EES.
- Historical/reference evidence: History indicates a broader JSON/JS environment but no normative statement complete enough for all protocol fields.
- Classification: UNDERSPECIFIED
- Impact on TCK: Medium to high; absent vs empty vs null produce distinct canonical bytes and semantic ambiguity affects serialization.
- Required decision: Define explicitly which field states are permitted and how they map to the canonical model.
- Decision authority required: APS author and conformance owner.
- Current disposition: Not yet settled in authoritative APS text.
- Re-entry condition: When APS-200/APS-300 define the data model and canonical JSON profile.
- Evidence provenance: `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/Aura-vNEXT/core/canonical/__init__.py`.

### C-007 — Timestamp Semantics

- Conflict ID: C-007
- Topic: Whether timestamps are required input, optional input, generated internally, excluded from canonicalization, included in canonicalization, part of the hash domain, or operational metadata only.
- Normative source: `Aura-vNEXT` documentation says `timestamp` is recorded input and no clock is read during canonicalization. `Aura-Guard` uses system time in health responses and potentially in runtime components. TCK instructions state no internal timestamps during serialization.
- Exact file/path: `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/Aura-vNEXT/core/models/__init__.py`; `vaidt/Aura-Guard/backend/server.py`; `vaidt/Aura-Conformance-Kit/.github/copilot-instructions.md`.
- Exact section or symbol: `M0-EVIDENCE-CONTRACT.md` §"timestamp is recorded input. No clock is read during canonicalisation."; `backend/server.py` `datetime.now(timezone.utc)`; TCK "No internal timestamps during serialization."
- Evidence of current status: The canonical model treats timestamps as input, not internal clock output. But this has not been elevated to approved protocol-wide semantics or cross-implementation rule across all repos.
- Conflicting implementation(s): `Aura-vNEXT` uses external input; `Aura-Guard` health endpoint reads the system clock; TCK says no internal timestamps in serialization.
- Historical/reference evidence: Historical implementations may use runtime timestamps for operational metadata, but this does not establish protocol law.
- Classification: REQUIRES_ARCHITECTURAL_DECISION
- Impact on TCK: High; clocked values alter canonical bytes and hash domains unless explicitly excluded.
- Required decision: Decide whether timestamps are protocol input, metadata, or excluded from canonical bytes; if included, specify exact format and semantics.
- Decision authority required: Formal protocol author and canonical model authority.
- Current disposition: Partially defined in M0 docs; not approved as general protocol semantics.
- Re-entry condition: When APS-200/APS-300 define timestamp semantics and canonical-domain inclusion.
- Evidence provenance: `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/Aura-Guard/backend/server.py`; `vaidt/Aura-Conformance-Kit/.github/copilot-instructions.md`.

### C-008 — Canonical Bytes

- Conflict ID: C-008
- Topic: Whether `canonical.bin` is an internal test artifact, a conformance artifact, a public protocol representation, or a normative byte-level representation.
- Normative source: The TCK instructions define `canonical.bin` as the final arbiter of correctness. But in `Aura-vNEXT` the canonical form is a textual representation used as a hash preimage; there is no verified APS statement that this byte stream is public protocol output. `Aura-Guard` has canonicalization docs but not a defined `.bin` canonical artifact.
- Exact file/path: `vaidt/Aura-Conformance-Kit/.github/copilot-instructions.md`; `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/Aura-vNEXT/core/canonical/__init__.py`; `vaidt/Aura-Guard/docs/PHASE_3_GOLDEN_VECTOR_PLAN.md`.
- Exact section or symbol: "Byte-Level Truth" in TCK instructions; `canonical_bytes(value)` in `core/canonical/__init__.py`; `M0-EVIDENCE-CONTRACT.md` text about canonical bytes and SHA-256.
- Evidence of current status: The TCK explicitly declares byte-level truth as the final oracle, but the broader protocol does not clearly define whether canonical bytes are part of the public protocol or only conformance artifacts.
- Conflicting implementation(s): `Aura-vNEXT` canonicalization output is a textual UTF-8 form and bytes derived from it; `Aura-Conformance-Kit` treats `canonical.bin` as the final equality target; others reference similar mechanisms but without formal status.
- Historical/reference evidence: Historical docs discuss canonical bytes and hash sequences, but without APS authority.
- Classification: UNDERSPECIFIED
- Impact on TCK: High; without a defined canonical byte status, expected security and conformance semantics remain ambiguous.
- Required decision: Define whether canonical bytes are normative representation, internal test artifact, or both.
- Decision authority required: Normative spec authority and TCK owner.
- Current disposition: Unresolved.
- Re-entry condition: When the spec defines the evidence/canonical representation boundary and conformance artifact expectations.
- Evidence provenance: `vaidt/Aura-Conformance-Kit/.github/copilot-instructions.md`; `vaidt/Aura-vNEXT/core/canonical/__init__.py`; `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`.

### C-009 — Hash Domain

- Conflict ID: C-009
- Topic: Exact input to hashing; whether hashing is over `canonical.bin`; whether metadata is excluded; domain separation; encoding; digest algorithm; ordering and framing rules.
- Normative source: `Aura-vNEXT` contract and docs specify SHA-256 over canonical representation and chain linkage; but exact APS-level domain separation and framing rules are not confirmed. TCK docs say "final arbiter is raw canonical.bin byte stream compared against the Oracle signature", but no formal signature contract is defined.
- Exact file/path: `vaidt/Aura-vNEXT/architecture/decisions/ADR-0005-canonical-form-and-hashing.md`; `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/Aura-Conformance-Kit/.github/copilot-instructions.md`.
- Exact section or symbol: `ADR-0005` §"4. Integrity binding"; `M0-EVIDENCE-CONTRACT` hash sections; TCK instructions "Byte-Level Truth".
- Evidence of current status: Implementation behavior suggests a deterministic SHA-256 over canonical bytes, including domain separation after canonicalization. The exact protocol-level definition is not explicitly approved in APS docs.
- Conflicting implementation(s): `Aura-vNEXT` chain logic and canonicalizer; `Aura-Guard` hash logic and Merkle-based sealing; historical `aura-guard-v1.3` uses chain digests and Merkle manifests but not necessarily same domain.
- Historical/reference evidence: Rust reference implements hash-chained evidence log and Merkle batching; not proven to be same domain as `Aura-vNEXT` M0.
- Classification: UNDERSPECIFIED
- Impact on TCK: High; hash semantics determine pass/fail and the Oracle comparison behavior.
- Required decision: Define precise hash preimage, encoding, domain separation, and what is excluded from the hash input.
- Decision authority required: Protocol author and canonical data model authority.
- Current disposition: Evidence exists for many implementations, but formal APS contract not found.
- Re-entry condition: when APS-200/APS-300 and the conformance runner define the canonical hash domain.
- Evidence provenance: `vaidt/Aura-vNEXT/architecture/decisions/ADR-0005-canonical-form-and-hashing.md`; `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/aura-guard-v1.3/README.md`.

### C-010 — Oracle

- Conflict ID: C-010
- Topic: Normative status and exact semantics of Oracle digest, Oracle signature, signature input, signature encoding, key identification, verification output, failure semantics.
- Normative source: TCK instructions mention Oracle signature as final arbiter, but no actual normative Oracle format under `/spec/` was observed. The repo has `reference/python/errors.py` and some conformance scaffolding, but no verified APS rules or protocol contract.
- Exact file/path: `vaidt/Aura-Conformance-Kit/.github/copilot-instructions.md`; `vaidt/Aura-Conformance-Kit/reference/python/errors.py`; `vaidt/Aura-Conformance-Kit/docs/EES_IMPLEMENTATION_MAP.md`.
- Exact section or symbol: TCK instruction "Byte-Level Truth"; error types like `OracleMismatchError`, `OracleSignatureError`.
- Evidence of current status: A conceptual Oracle exists in scaffolding and error classes, but no approved data format, encoding, public key contract, or verification semantics are present in authoritative normative docs.
- Conflicting implementation(s): No verified oracle contract across repos; implementations differ in how they hash and verify evidence but no single Oracle definition is approved.
- Historical/reference evidence: Historical reference implementations include signature and attestation patterns, but those are not normative APS evidence unless explicitly adopted.
- Classification: UNDERSPECIFIED
- Impact on TCK: Critical; without formal Oracle semantics TCK cannot compare byte streams to a verified signature standard.
- Required decision: Define Oracle digest and signature format, verification output, and failure semantics in a governing spec.
- Decision authority required: Specification authority and TCK design authority.
- Current disposition: Not verified; no final contract found.
- Re-entry condition: Once APS-300/APS-400 define Evidence Pack and Oracle comparison semantics.
- Evidence provenance: `vaidt/Aura-Conformance-Kit/.github/copilot-instructions.md`; `vaidt/Aura-Conformance-Kit/reference/python/errors.py`; `vaidt/Aura-Conformance-Kit/docs/EES_IMPLEMENTATION_MAP.md`.

### C-011 — Evidence Pack

- Conflict ID: C-011
- Topic: Whether APS-300 currently specifies the Evidence Pack schema, required fields, hash-covered fields, canonical serialization, attachment structure, metadata treatment, and verification semantics.
- Normative source: `aura-specification` states APS-300 is DRAFT; no verified formal schema was observed. `Aura-vNEXT` defines an M0 evidence package with a canonical form and verification semantics, but that is expressly M0-specific and not proven to be the APS-300 final model.
- Exact file/path: `vaidt/aura-specification/README.md`; `vaidt/aura-specification/aps/APS-300_EVIDENCE_MODEL.md` (draft); `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/Aura-vNEXT/app/producer/__init__.py`.
- Exact section or symbol: `README.md` APS documents status; `M0-EVIDENCE-CONTRACT` entire contract; producer code for package generation.
- Evidence of current status: The formal Evidence Model is in draft and not approved; M0 evidence package behavior exists but is not proven to be the same as APS-300. This is a direct unresolved contract issue.
- Conflicting implementation(s): `Aura-vNEXT` evidence package and producer/verification workflow vs `aura-guard-v1.3` append-only audit log and Merkle batch model vs `Aura-Guard` evidence bundle flow.
- Historical/reference evidence: `aura-guard-v1.3` includes evidence log semantics and segment manifests, but without a normative mapping to APS-300.
- Classification: CONFLICTING_SOURCES
- Impact on TCK: Very high; evidence structure determines what the TCK verifies and how packages are compared.
- Required decision: Finalize the Evidence Pack schema and verification semantics in the protocol and then align all implementations to the same structure.
- Decision authority required: APS-300 owner and conformance architecture authority.
- Current disposition: Draft and unresolved.
- Re-entry condition: Only after APS-300 is approved and traceability is verified to APS-001.
- Evidence provenance: `vaidt/aura-specification/README.md`; `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; `vaidt/aura-guard-v1.3/README.md`.

### C-012 — TCK Scope

- Conflict ID: C-012
- Topic: Whether the current specification defines positive conformance, negative conformance, canonical byte comparison, cross-language conformance, Oracle verification, failure-code conformance, and deterministic replay.
- Normative source: TCK instructions make byte-level truth and Oracle comparison central, but the repo does not show a verified APS/runner contract defining those requirements. The current `Aura-Conformance-Kit` repo is still in scaffold stages and lacks formal scope statement.
- Exact file/path: `vaidt/Aura-Conformance-Kit/.github/copilot-instructions.md`; `vaidt/Aura-Conformance-Kit/README.md`; `vaidt/Aura-Conformance-Kit/docs/EES_IMPLEMENTATION_MAP.md`.
- Exact section or symbol: "AI Engineering Directives: Aura TCK"; EES map placeholder; `README.md` description of tools.
- Evidence of current status: TCK scaffolding exists, but the normative contract for conformance scope remains unresolved. No approved conformance runner spec or fixture set is present.
- Conflicting implementation(s): `Aura-vNEXT` product loop tests; `Aura-Guard` conformance matrix; `aura-guard-v1.3` conformance harness. All are implementation-specific, not yet normatively bound.
- Historical/reference evidence: Historical `aura-guard-v1.3` conformance harness exists but is not proven to be the active TCK contract.
- Classification: UNDERSPECIFIED
- Impact on TCK: High; implementation without explicit conformance scope is not reviewable as an authoritative certification framework.
- Required decision: Define the positive/negative conformance matrix, canonical byte comparison, Oracle verification, failure semantics, and deterministic replay scope.
- Decision authority required: TCK owner and protocol specification authority.
- Current disposition: Unresolved; no approved conformance-runner spec found.
- Re-entry condition: Once APS-400/APS-500 and the runner spec are approved.
- Evidence provenance: `vaidt/Aura-Conformance-Kit/.github/copilot-instructions.md`; `vaidt/Aura-Conformance-Kit/README.md`; `vaidt/Aura-Conformance-Kit/docs/EES_IMPLEMENTATION_MAP.md`.

---

## Additional evidence notes by question

### C-001 — Canonical Contract

- Normative question: Does a formal canonical contract exist?
- Observed answer: Not verified in approved APS material. `Aura-vNEXT` is a M0 implementation and contract, not proven as the protocol's final canonical contract.
- Current status: UNRESOLVED.

### C-002 — Numeric Domain

- Observed answer: Draft invariants mention zero-float runtime, but implementation code and docs disagree on whether floats are only forbidden in canonicalization or globally forbidden in input calculations.
- Current status: UNRESOLVED.

### C-003 — Float Boundary

- Observed answer: Public input, parser, internal calculation, canonical representation, and fixture representation are all treated differently across repositories.
- Current status: UNRESOLVED.

### C-004 — Unicode

- Observed answer: `Aura-vNEXT` and the TCK want raw code points preserved, while `Aura-Guard` security docs explicitly normalize or strip characters as mitigation.
- Current status: CONFLICTING_SOURCES.

### C-005 — Key Ordering

- Observed answer: `Aura-vNEXT` uses UTF-16BE sorting; `Aura-Guard` notes native sort ordering is ambiguous for Unicode; raw APS authority absent.
- Current status: CONFLICTING_SOURCES.

### C-006 — Optionality and Null

- Observed answer: `Aura-vNEXT` distinguishes absent from empty string and null is forbidden in canonical representation, but no general APS contract defines the whole JSON-like model.
- Current status: UNDERSPECIFIED.

### C-007 — Timestamp Semantics

- Observed answer: `Aura-vNEXT` says timestamps are recorded input; `Aura-Guard` system clock is used in operational code; TCK instructions forbid internal timestamps during serialization.
- Current status: CONFLICTING_SOURCES / REQUIRES_ARCHITECTURAL_DECISION.

### C-008 — Canonical Bytes

- Observed answer: `canonical.bin` is central in TCK instructions but not yet formally classified as protocol-level representation.
- Current status: UNDERSPECIFIED.

### C-009 — Hash Domain

- Observed answer: SHA-256 canonical representation hashing is implementable and documented, but exact APS-level definition is not verified.
- Current status: UNDERSPECIFIED.

### C-010 — Oracle

- Observed answer: Oracle exists conceptually in TCK and errors, but not in a verified normative contract.
- Current status: UNDERSPECIFIED.

### C-011 — Evidence Pack

- Observed answer: APS-300 is draft; M0 package exists but is not proven to be final APS-300 evidence semantics.
- Current status: CONFLICTING_SOURCES.

### C-012 — TCK Scope

- Observed answer: TCK is scaffolded but not yet backed by an approved conformance runner spec, fixture set, and scope definitions.
- Current status: UNDERSPECIFIED.

---

## Architectural decision table

| Decision ID | Question | Current Evidence | Conflict | Decision Required | Blocking TCK? |
|---|---|---|---|---|---|
| D-001 | canonical contract | `aura-specification` draft APS vs `Aura-vNEXT` M0 contract | conflict between draft APS and M0 implementation | Choose whether M0 contract is normative or merely milestone-specific | YES |
| D-002 | float prohibition boundary | TCK says zero float runtime; `Aura-vNEXT` still has float conversion path; `Aura-Guard` canonicalization expects doubles | conflicting rules across layers | Define boundary among input, arithmetic, canonical form, fixtures | YES |
| D-003 | Decimal | `Aura-vNEXT` uses Decimal conversion from float; TCK says integers only | conflicting interpretation | Decide whether Decimal is allowed as exact input or banned from canonical path | YES |
| D-004 | Aura-Guard scope | `Aura-Guard` is a demonstrator with runtime behavior and docs | architecture and scope unclear | Confirm whether it is a reference implementation, a legacy branch, or a separate non-normative prototype | YES |
| D-005 | aura-guard-v1.3 status | Historical Rust repo with conformance logic and Merkle chain | historical vs current authority unresolved | State whether it remains reference-only and non-authoritative | YES |
| D-006 | normative fixture ownership/location | TCK and `Aura-vNEXT` each have fixtures; no APS owner identified | multiple fixture sources | Assign owner and authority of canonical fixtures | YES |
| D-007 | Oracle signature format | TCK mentions Oracle as final arbiter but no spec found | no verified format | Define exact input, encoding, and verification semantics | YES |
| D-008 | canonical.bin status | TCK says byte stream is final arbiter; not formally defined in APS | unverified contract | Define if `canonical.bin` is protocol artifact or TCK artifact | YES |
| D-009 | timestamp semantics | `Aura-vNEXT` says input-only; `Aura-Guard` uses system time | disparate behavior | Specify inclusion/exclusion rules | YES |
| D-010 | whether Aura-vNEXT M0 may serve as TCK basis | `Aura-vNEXT` is candidate but not approved | implementation vs normative authority | Decide if M0 may be used as evidence basis or must wait for APS adoption | YES |

---

## Evidence provenance summary

- `vaidt/aura-specification/README.md` — specification repo claims normative status but the actual APS documents are still draft or TODO.
- `vaidt/aura-specification/aps/README.md` — lists APS documents and notes APS-001 is stored in `/specification`, with statuses still draft or TODO.
- `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md` — explicit canonical contract for M0 and rejection of null/normalization, but not shown as final protocol authority.
- `vaidt/Aura-vNEXT/core/canonical/__init__.py` — canonicalizer with UTF-16 sorting and no floats in canonical path.
- `vaidt/Aura-vNEXT/core/models/__init__.py` — conversion of float-like input to integer basis points, which requires architecture decision.
- `vaidt/Aura-vNEXT/architecture/decisions/ADR-0005-canonical-form-and-hashing.md` — strong design-level rule set but still architectural evidence, not APS approval.
- `vaidt/Aura-Guard/docs/PHASE_3_AMBIGUITY_REGISTER.md` — explicit list of canonicalization ambiguities, blocking decisions, and unresolved dispute criteria.
- `vaidt/Aura-Guard/py_verifier/aura_verify.py` — float canonicalizer and numeric rules contradict TCK zero-float rule.
- `vaidt/Aura-Guard/backend/server.py` — runtime system clock calls contradict time-free canonicalization constraints.
- `vaidt/Aura-Conformance-Kit/.github/copilot-instructions.md` — TCK instructions establish strict zero-float and byte-level truth demands.
- `vaidt/Aura-Conformance-Kit/docs/EES_IMPLEMENTATION_MAP.md` — placeholder map indicates incomplete normative model definition.

---

## TCK implementation gate

```yaml
tck_implementation_gate:
  specification_contract_closed: NO
  canonicalization_contract_closed: NO
  canonical_bytes_defined: NO
  oracle_contract_closed: NO
  conflicting_rules_resolved: NO
  tck_implementation_authorized: NO
  repository_merging_authorized: NO
  code_migration_authorized: NO
```

---

## Final disposition

BLOCKED_PENDING_NORMATIVE_DECISIONS

---

## Required return metadata

- commit hash: Not recorded by the GitHub file-write API for this documentation-only change; this artifact was created as a repository document without a separate Git commit hash available in the tool response.
- files created/modified: `AURA_NORMATIVE_CONTRACT_CONFLICT_REGISTER_v1.0.md`
- complete conflict count: 12
- blocking conflict count: 12
- final gate status: `tck_implementation_gate` as shown above, all `NO`
- list of questions requiring competent architectural decision: C-001, C-002, C-003, C-004, C-005, C-006, C-007, C-008, C-009, C-010, C-011, C-012

This report intentionally does not adjudicate a winner among conflicting rules. It preserves the observed evidence and marks the current state as unresolved pending authoritative normative decisions.
