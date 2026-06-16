# Module Contract

## Purpose

This file defines how modules are created, expanded, and maintained inside `python-testdev-drill`.

## Required Module Fields

Each module must keep:
- `module_name`
- `completed_through`
- `next_question`
- `asked_questions`
- `mistakes`
- `answer_given_questions`

## Isolation Rules

- Progress is isolated by module.
- Mistakes are isolated by module.
- Asked-question history is isolated by module.
- Switching modules must never overwrite another module's state.

## Expansion Rules

When a new module is added:
1. Assign a stable module name.
2. Create an ordered question bank for that module.
3. Initialize empty progress and mistake data.
4. Persist the module in `state.md`.

## Resume Rules

When the user names a module:
- load that module's state
- continue from `next_question`
- preserve all other modules untouched
