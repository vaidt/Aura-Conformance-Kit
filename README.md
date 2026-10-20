# Aura Conformance Kit

> **Repository role:** conformance-process design, test assets, validators, and evidence reporting, to the extent implemented and evidenced at a specific revision.

This repository organizes materials for evaluating implementations against AURA requirements. Describe each capability only when its files, invocation, inputs, and results are available at the referenced commit.

Keep these outcomes distinct: **structural/schema validation**, **cryptographic verification**, **semantic contract checks**, **cross-implementation agreement**, and **end-to-end conformance**. Passing one layer does not imply that the others passed or that every protocol requirement is covered.

A conformance result must identify the contract revision, implementation revision, test/fixture set, verifier version, execution context, and limitations. The kit does not itself ratify protocol semantics or establish G1 governance authority.

> **Scope boundary:** this repository reports bounded technical evidence; it does not confer normative status.

## Prior README description — retained as an earlier repository statement

The text below is preserved from the previous README. Its description of project stage is not independent evidence of the current source tree or implementation status.

### Previous README title (normalized to avoid a duplicate H1)

Aura Conformance Kit to zestaw narzędzi i materiałów pomocniczych służących do weryfikacji zgodności implementacji z wymaganiami Aura.

Projekt ma na celu zorganizowanie standardów, metadanych i procesów potrzebnych do rzetelnego testowania zgodności. Na tym etapie skupiamy się na przygotowaniu struktury projektu i dokumentacji — implementacja kodu pojawi się dopiero po wspólnym przejściu przez fazę projektową i przegląd konfiguracji.
