# Question Bank Guide

## Goal

Organize question banks so each module can progress predictably without repeating questions.

## Rules

- Each module uses its own ordered question sequence.
- Question identifiers should be stable.
- Already asked questions should not be served again inside the same module.
- Questions already answered via `给出答案` should stay marked in `answer_given_questions`.
- New questions should append cleanly without reordering old identifiers unless explicitly migrated.

## Recommended Structure

For each module, keep questions in a stable sequence:
1. basic programming
2. strings and lists
3. dict and set thinking
4. sorting and searching
5. recursion or stack or queue
6. file handling
7. automation-testing utility tasks
8. test-development scenarios

## Exhaustion Behavior

If a module has no unseen questions left:
- tell the user clearly
- offer to expand the module or switch modules
