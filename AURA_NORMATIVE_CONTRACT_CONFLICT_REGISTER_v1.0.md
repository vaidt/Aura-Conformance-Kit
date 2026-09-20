# AURA_NORMATIVE_CONTRACT_CONFLICT_REGISTER_v1.1

Status: PROPOSED DECISION REQUEST

This document is a proposed evidence register and decision-preparation artifact only. It does not establish normative authority, does not create governance competence, does not ratify a specification, does not close M1, and does not authorize TCK implementation, repository merging, or code migration.

## 1. Document metadata

| Field | Value |
|---|---|
| document_type | DECISION_REQUEST |
| document_status | PROPOSED |
| normative_authority_created | NO |
| architectural_decision_created | NO |
| governance_competence_established | NO |
| m1_closed | NO |
| tck_implementation_authorized | NO |
| repository_merging_authorized | NO |
| code_migration_authorized | NO |
| final_disposition | BLOCKED_PENDING_NORMATIVE_DECISIONS |

## 2. Governing principle

Implementation behavior MUST NOT silently become protocol law.

The order of authority for this request is:
1. explicitly normative and approved specification evidence, if verified;
2. explicitly recorded and valid architectural decisions, if verified;
3. existing implementation behavior;
4. historical/reference material.

Where the specification is incomplete or contradictory, the issue remains unresolved.

## 3. Scope and method

Repositories in scope:
- `vaidt/aura-specification`
- `vaidt/Aura-Conformance-Kit`
- `vaidt/Aura-vNEXT`
- `vaidt/aura-guard-v1.3`
- `vaidt/Aura-Guard`
- `vaidt/Crystal-panel-Aura-Protection`

Method:
- repository inspection and evidence collection;
- static scan of implementation sources for patterns relevant to canonicalization, determinism, and Unicode rules;
- collection of explicit statements from spec and architecture docs;
- no implementation migration;
- no code rewrite;
- no protocol redesign;
- no certification by implementation preference.

## 4. Current control status

| Status | Value |
|---|---|
| specification_contract_closed | NO |
| canonicalization_contract_closed | NO |
| canonical_bytes_defined | NO |
| oracle_contract_closed | NO |
| conflicting_rules_resolved | NO |
| tck_implementation_authorized | NO |
| repository_merging_authorized | NO |
| code_migration_authorized | NO |

## 5. Decision layers

### 5.1 Normative decisions (ND-*)

These decisions directly govern protocol behavior.

- ND-001: Status normatywny `AURA-CANON/1`
- ND-002: Domena typów liczbowych
- ND-003: Granica użycia floatów
- ND-004: Polityka Unicode
- ND-005: Kolejność kluczy
- ND-006: Optionality i `null`
- ND-007: Semantyka timestampów
- ND-008: Status `canonical.bin`
- ND-009: Hash domain
- ND-010: Oracle contract
- ND-011: Evidence Pack contract
- ND-012: Zakres i warunki TCK

### 5.2 Architectural decisions (AD-*)

These decisions govern implementation organization and boundaries.

- AD-001: Rola `Aura-vNEXT`
- AD-002: Status `Aura-Guard`
- AD-003: Status `aura-guard-v1.3`
- AD-004: Właściciel canonical fixtures
- AD-005: Zakres repozytoriów i relacje między nimi
- AD-006: Relacja Python ↔ Rust
- AD-007: TCK repo role / ownership
- AD-008: Evidence provenance and traceability model
- AD-009: Accepted implementation basis for early TCK work
- AD-010: Decision traceability model and review gates

### 5.3 Governance prerequisite decisions (GD-*)

These decisions establish competence and formal approval authority.

- GD-001: Kto ma kompetencję do zatwierdzania APS
- GD-002: Kto ma kompetencję do przyjęcia `AURA-CANON/1`
- GD-003: Jaki jest mechanizm ratyfikacji i podpisu decyzji
- GD-004: Jakie warunki zamykają kontrakt i aktywują TCK
- GD-005: Kto może autoryzować implementację i certyfikację

## 6. Decision register

### ND-001 — Status normatywny AURA-CANON/1

| Field | Value |
|---|---|
| ID | ND-001 |
| Topic | Status normatywny `AURA-CANON/1` |
| Category | Normative |
| Required decision role | specification authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | DRAFT |
| Evidence | `vaidt/aura-specification` draft APS; `vaidt/Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; repo-specific implementation code |
| Required ruling | Determine whether `AURA-CANON/1` is protocol law or M0-specific implementation contract |
| Current disposition | Unresolved |
| Re-entry condition | After specification-level approval |

### ND-002 — Domena typów liczbowych

| Field | Value |
|---|---|
| ID | ND-002 |
| Topic | Domena typów liczbowych |
| Category | Normative |
| Required decision role | protocol authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | DRAFT |
| Evidence | `aura-specification` draft invariant statements; `Aura-vNEXT/core/models/__init__.py`; `Aura-Guard/docs/INV_FLT_01_NUMERIC_CANONICALIZATION.md` |
| Required ruling | Define whether the protocol permits only integers, or also decimal/float paths with explicit boundary rules |
| Current disposition | Unresolved |
| Re-entry condition | After APS-001/APS-200/APS-300 settle numeric semantics |

### ND-003 — Granica użycia floatów

| Field | Value |
|---|---|
| ID | ND-003 |
| Topic | Granica użycia floatów |
| Category | Normative |
| Required decision role | protocol authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | DRAFT |
| Evidence | `Aura-vNEXT/core/models/__init__.py` conversion via `Decimal(repr(float(value)))`; `Aura-Guard/docs/INV_FLT_01_NUMERIC_CANONICALIZATION.md`; TCK instructions requiring zero-float runtime |
| Required ruling | Explicitly split public input type, parser representation, internal arithmetic, canonical representation, and fixture representation |
| Current disposition | Boundary unresolved |
| Re-entry condition | After data model and canonicalization contract is approved |

### ND-004 — Polityka Unicode

| Field | Value |
|---|---|
| ID | ND-004 |
| Topic | Polityka Unicode |
| Category | Normative |
| Required decision role | protocol authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | DRAFT |
| Evidence | `Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md` forbids normalization; TCK instructions require raw code points; `Aura-Guard` docs discuss normalization and confusable folding |
| Required ruling | Define normalization, surrogate policy, malformed Unicode handling, and hidden/control character handling |
| Current disposition | Conflicting sources |
| Re-entry condition | After authoritative text on canonical string semantics is approved |

### ND-005 — Kolejność kluczy

| Field | Value |
|---|---|
| ID | ND-005 |
| Topic | Kolejność kluczy |
| Category | Normative |
| Required decision role | protocol authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | DRAFT |
| Evidence | `Aura-vNEXT/core/canonical/__init__.py` sorting by UTF-16BE order; `Aura-Guard/docs/PHASE_3_AMBIGUITY_REGISTER.md` flags object-key ordering as unresolved |
| Required ruling | Approve exact ordering rule: UTF-16 code unit, code point, byte order, or otherwise |
| Current disposition | Conflicting sources |
| Re-entry condition | After canonicalization contract is approved |

### ND-006 — Optionality i `null`

| Field | Value |
|---|---|
| ID | ND-006 |
| Topic | Optionality i `null` |
| Category | Normative |
| Required decision role | data model authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | DRAFT |
| Evidence | `Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md` distinguishes absent vs empty string and forbids null in canonical form; no final APS-wide rule found |
| Required ruling | Define semantics for absent, null, empty string, empty array, empty object, zero, false |
| Current disposition | Underspecified |
| Re-entry condition | After APS-200/APS-300 data model is approved |

### ND-007 — Semantyka timestampów

| Field | Value |
|---|---|
| ID | ND-007 |
| Topic | Semantyka timestampów |
| Category | Normative |
| Required decision role | protocol authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | DRAFT |
| Evidence | `Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md` says timestamps are recorded input; TCK instructions forbid internal timestamps during serialization; `Aura-Guard/backend/server.py` uses `datetime.now()` |
| Required ruling | Define whether timestamp is input, metadata, or excluded from canonicalization and hash domain |
| Current disposition | Incomplete and conflicting |
| Re-entry condition | After canonical model and evidence model approval |

### ND-008 — Status `canonical.bin`

| Field | Value |
|---|---|
| ID | ND-008 |
| Topic | Status `canonical.bin` |
| Category | Normative |
| Required decision role | protocol authority / TCK authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | DRAFT |
| Evidence | TCK instructions declare raw byte stream as final arbiter; `Aura-vNEXT` emits canonical bytes as part of M0 evidence; no approved protocol document defines its public status |
| Required ruling | Declare whether `canonical.bin` is protocol artifact, test artifact, or both |
| Current disposition | Underspecified |
| Re-entry condition | After canonicalization and evidence contract approval |

### ND-009 — Hash domain

| Field | Value |
|---|---|
| ID | ND-009 |
| Topic | Hash domain |
| Category | Normative |
| Required decision role | protocol authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | DRAFT |
| Evidence | `Aura-vNEXT/architecture/decisions/ADR-0005-canonical-form-and-hashing.md`; `Aura-vNEXT/docs/contract/M0-EVIDENCE-CONTRACT.md`; historical Rust reference implements hash-chained log |
| Required ruling | Define exact hash preimage, encoding, domain separation, metadata exclusion, and framing rules |
| Current disposition | Underspecified |
| Re-entry condition | After canonical representation and evidence pack approval |

### ND-010 — Oracle contract

| Field | Value |
|---|---|
| ID | ND-010 |
| Topic | Oracle contract |
| Category | Normative |
| Required decision role | TCK authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | DRAFT |
| Evidence | TCK instructions mention Oracle signature as final arbiter; repo contains error types but no approved Oracle format under `/spec/` |
| Required ruling | Define Oracle digest, signature structure, signing key identification, verification output, and failure semantics |
| Current disposition | No verified normative Oracle contract |
| Re-entry condition | After canonical bytes and evidence model approval |

### ND-011 — Evidence Pack contract

| Field | Value |
|---|---|
| ID | ND-011 |
| Topic | Evidence Pack contract |
| Category | Normative |
| Required decision role | specification authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | DRAFT |
| Evidence | `aura-specification` marks APS-300 as `DRAFT`; `Aura-vNEXT` has an M0 package and verification flow |
| Required ruling | Approve Evidence Pack schema, required fields, hash coverage, canonical serialization, attachment rules, and verification semantics |
| Current disposition | Draft / not verified |
| Re-entry condition | After APS-300 approval |

### ND-012 — Zakres i warunki TCK

| Field | Value |
|---|---|
| ID | ND-012 |
| Topic | Zakres i warunki TCK |
| Category | Normative |
| Required decision role | TCK authority / specification authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | DRAFT |
| Evidence | TCK instructions exist; conformance runner spec and fixture set not verified as approved; `docs/EES_IMPLEMENTATION_MAP.md` is still placeholder |
| Required ruling | Define positive conformance, negative conformance, canonical byte comparison, cross-language conformance, Oracle verification, failure code conformance, deterministic replay |
| Current disposition | Underspecified |
| Re-entry condition | After normative contract and approved fixtures are in place |

## 7. Architectural decisions (AD-*)

### AD-001 — Rola `Aura-vNEXT`

| Field | Value |
|---|---|
| ID | AD-001 |
| Topic | Rola `Aura-vNEXT` |
| Required decision role | architecture authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | active M0 implementation and product loop; strong canonicalization claims; not verified as protocol authority |
| Required ruling | Determine whether `Aura-vNEXT` is a candidate reference implementation, a development branch, or a protocol-authoritative implementation |

### AD-002 — Status `Aura-Guard`

| Field | Value |
|---|---|
| ID | AD-002 |
| Topic | Status `Aura-Guard` |
| Required decision role | architecture authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | JS/Python implementation with float canonicalization and time/random usage; not verified as normative |
| Required ruling | Classify as demonstrator, historical reference, reconciliation repo, or separate non-normative prototype |

### AD-003 — Status `aura-guard-v1.3`

| Field | Value |
|---|---|
| ID | AD-003 |
| Topic | Status `aura-guard-v1.3` |
| Required decision role | architecture authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | robust Rust reference with hash chain and Merkle functionality; historical provenance present; normative authority not verified |
| Required ruling | Determine whether it is historical reference only or can be used as comparative evidence |

### AD-004 — Właściciel canonical fixtures

| Field | Value |
|---|---|
| ID | AD-004 |
| Topic | Właściciel canonical fixtures |
| Required decision role | architecture authority / TCK authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | multiple repositories carry fixture-like material; no verified source-of-truth established |
| Required ruling | Designate canonical fixture owner and authoritative repo for reference vectors |

### AD-005 — Zakres repozytoriów i relacje między nimi

| Field | Value |
|---|---|
| ID | AD-005 |
| Topic | Relacja repozytoriów |
| Required decision role | architecture authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | multiple repositories exist with overlapping roles and partial conformance material |
| Required ruling | Define responsibility boundaries and non-authoritative status of each repo |

### AD-006 — Relacja Python ↔ Rust

| Field | Value |
|---|---|
| ID | AD-006 |
| Topic | Relacja Python ↔ Rust |
| Required decision role | architecture authority / conformance owner |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | `Aura-vNEXT` is Python; `aura-guard-v1.3` is Rust; prior conformance work exists but no approved cross-language contract |
| Required ruling | Define whether cross-language equivalence is a required protocol property or a later-phase exercise |

### AD-007 — TCK repo role / ownership

| Field | Value |
|---|---|
| ID | AD-007 |
| Topic | TCK repo role / ownership |
| Required decision role | governance authority / architecture authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | `Aura-Conformance-Kit` contains TCK scaffolding, but no approved governance ownership is established |
| Required ruling | Identify which repository is authorized to maintain the TCK and issue conformance results |

### AD-008 — Evidence provenance and traceability model

| Field | Value |
|---|---|
| ID | AD-008 |
| Topic | Evidence provenance and traceability |
| Required decision role | architecture authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | multiple repositories have implementation evidence and historical materials; no single traceability model is approved |
| Required ruling | Define how evidence is assigned, traced, and classified by authority |

### AD-009 — Accepted implementation basis for early TCK work

| Field | Value |
|---|---|
| ID | AD-009 |
| Topic | Accepted implementation basis for early TCK work |
| Required decision role | architecture authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | `Aura-vNEXT` is a candidate implementation, but not yet approved as basis for protocol-wide TCK |
| Required ruling | Decide whether early TCK work may use `Aura-vNEXT` evidence as candidate basis or must wait for normative adoption |

### AD-010 — Decision traceability model and review gates

| Field | Value |
|---|---|
| ID | AD-010 |
| Topic | Decision traceability model and review gates |
| Required decision role | architecture authority / governance authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | current document records conflicts and status, but no formal review gate or traceability model has been established |
| Required ruling | Define how decisions are captured, reviewed, and escalated |

## 8. Governance prerequisite decisions (GD-*)

### GD-001 — Kto ma kompetencję do zatwierdzania APS

| Field | Value |
|---|---|
| ID | GD-001 |
| Topic | Kompetencja do zatwierdzania APS |
| Required decision role | governance authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | no verified governance document establishing this competence |
| Required ruling | Define formal APS approval authority |

### GD-002 — Kto ma kompetencję do przyjęcia `AURA-CANON/1`

| Field | Value |
|---|---|
| ID | GD-002 |
| Topic | Kompetencja do przyjęcia `AURA-CANON/1` |
| Required decision role | governance authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | no verified approval method documented |
| Required ruling | Define formal authority for canonical contract approval |

### GD-003 — Mechanizm ratyfikacji i podpisu decyzji

| Field | Value |
|---|---|
| ID | GD-003 |
| Topic | Mechanizm ratyfikacji i podpisu decyzji |
| Required decision role | governance authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | no verified ratification workflow observed |
| Required ruling | Define who may ratify or sign a decision and under what evidence standard |

### GD-004 — Warunki zamknięcia kontraktu i aktywacji TCK

| Field | Value |
|---|---|
| ID | GD-004 |
| Topic | Warunki zamknięcia kontraktu i aktywacji TCK |
| Required decision role | governance authority / TCK authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | current evidence shows multiple unresolved constraints; no closure criteria established |
| Required ruling | Define measurable conditions for specification closure and TCK authorization |

### GD-005 — Kto może autoryzować implementację i certyfikację

| Field | Value |
|---|---|
| ID | GD-005 |
| Topic | Autorzyzacja implementacji i certyfikacji |
| Required decision role | governance authority |
| Current competent holder | NOT_VERIFIED |
| Competence status | NOT_VERIFIED |
| Decision status | PENDING |
| Closure status | PROPOSED |
| Evidence | current work is blocked, with no verified approval authority |
| Required ruling | Define final authorization pathway for TCK implementation and certification |

## 9. Observed unresolved conflicts

| Conflict | Classification | Evidence summary |
|---|---|---|
| canonical contract is not verified | CONFLICTING_SOURCES | draft APS vs M0 implementation contract |
| float rules not fully resolved | REQUIRES_ARCHITECTURAL_DECISION | TCK global prohibition vs implementation-layer float usage |
| Unicode policy unresolved | CONFLICTING_SOURCES | raw preservation vs normalization/folding |
| key ordering unresolved | CONFLICTING_SOURCES | UTF-16 ordering vs native ordering ambiguity |
| null/optionality semantics unresolved | UNDERSPECIFIED | absent vs empty vs null not finalized |
| timestamp semantics unresolved | REQUIRES_ARCHITECTURAL_DECISION | input timestamps vs runtime clock usage |
| canonical.bin status unresolved | UNDERSPECIFIED | final arbiter in TCK but not formally defined |
| hash domain unresolved | UNDERSPECIFIED | multiple implementations and draft docs |
| Oracle contract unresolved | UNDERSPECIFIED | no approved Oracle format |
| Evidence Pack contract unresolved | CONFLICTING_SOURCES | APS-300 draft vs M0 package |
| TCK scope unresolved | UNDERSPECIFIED | no approved conformance runner spec |
| governance competence unresolved | NOT_VERIFIED | no verified authority established |

## 10. Formal closure criteria

A decision is only considered closed when all of the following are true:

1. a verified normative source exists;
2. required decision role is explicitly identified and verified as competent;
3. the decision is recorded in a governing repository or authoritative document;
4. the evidence trail is recorded and traceable;
5. conflicting sources are explicitly resolved or scoped as deferred;
6. the decision is approved or ratified by the competent authority;
7. the closure status is not merely `DRAFT` or `PROPOSED` but `DECIDED` or higher;
8. the decision is effective for the relevant implementation and conformance boundary.

Closure states:
- DRAFT
- PROPOSED
- DECIDED
- APPROVED
- RATIFIED
- EFFECTIVE
- SUPERSEDED

## 11. Final status

```text
Final disposition:
BLOCKED_PENDING_NORMATIVE_DECISIONS
```

This document remains a proposed evidence register and decision request. It does not create normative authority, does not establish governance competence, does not close M1, and does not authorize TCK implementation, repository merging, or code migration.

This file has been updated to reflect the approved control position: treat the document as a decision-preparation artifact, not as a final ADR or ratified governance act.
