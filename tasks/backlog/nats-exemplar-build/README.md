# Feature: Build NATS Asyncio Service Exemplar

**Feature ID**: FEAT-NEB
**Parent Review**: TASK-R7B3
**Status**: Ready for implementation

## Problem

This repo needs a complete NATS asyncio service exemplar ready for `/template-create`. The Claude Desktop exemplar covers all 16 spec requirements but lives in a separate repo.

## Solution

Copy the Claude Desktop exemplar into this repo and apply 4 minor fixes identified in the architectural review (TASK-R7B3, score: 91/100). Skip the cookiecutter step — it adds no value.

## Subtasks

| ID | Title | Wave | Mode | Depends On |
|----|-------|------|------|------------|
| TASK-NEB-001 | Copy exemplar files | 1 | task-work | — |
| TASK-NEB-002 | Apply minor fixes | 1 | task-work | NEB-001 |
| TASK-NEB-003 | Implement integration test | 2 | task-work | NEB-002 |
| TASK-NEB-004 | Verify quality gates | 2 | direct | NEB-002 |

## Execution Strategy

**Wave 1** (sequential): Copy files → apply fixes
**Wave 2** (parallel): Integration test + quality verification
