# State Update Rules

## After User Submits Code

1. Evaluate the answer.
2. If correct enough, move `next_question` forward.
3. If the answer is incorrect, keep the same `next_question` until the user improves or asks for the answer.
4. Add the question to `mistakes` only when it is a genuine miss or the user explicitly requests the answer.

## After User Says `给出答案`

1. Provide the standard answer.
2. Append the current question to `mistakes`.
3. Append the current question to `answer_given_questions`.
4. Move `next_question` forward.

## After Module Switch

1. Load the target module's saved state.
2. Leave all other module states unchanged.
3. Continue from the target module's `next_question`.

## After Expanding a Module

1. Append new questions at the end.
2. Keep existing question numbers stable.
3. Update the module snapshot.
4. Do not re-ask old questions unless the user explicitly asks for review.
