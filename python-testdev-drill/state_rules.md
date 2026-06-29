# State Update Rules

## After Question Is Issued

1. Immediately sync `last_active_module`, `last_active_mode`, and `last_batch_size`.
2. Immediately write the issued question into the module's `last_round_questions`.
3. Immediately treat the issued question as part of the current seen-question flow for future de-duplication.
4. Do this in both `刷题模式` and `做题模式`; do not wait for the user to ask for progress saving.

## After User Submits Code

1. Evaluate the answer.
2. If the score is `8/10` or above, move `next_question` forward.
3. If the score is below `8/10`, add the question to `mistakes` if it is not already there, then move `next_question` according to the current drill flow.
4. In `做题模式`, any score below `8/10` counts as a weak point and must enter the wrong-question notebook without duplicate insertion.

## After User Says `给出答案`

1. Provide the standard answer.
2. Append the current question to `mistakes`.
3. Append the current question to `answer_given_questions`.
4. Treat the current question as already seen for all future de-duplication in both `刷题模式` and `做题模式`.
5. Move `next_question` forward.

## After Module Switch

1. Load the target module's saved state.
2. Leave all other module states unchanged.
3. Continue from the target module's `next_question`.

## After Expanding a Module

1. Append new questions at the end.
2. Keep existing question numbers stable.
3. Update the module snapshot.
4. Do not re-ask old questions unless the user explicitly asks for review.
5. `性能测试面试题` and `中间件面试题` must be expanded only inside their own module banks, never appended under `自动化测试题`.
6. `数据库面试题` must be expanded only inside its own module bank, never appended under `自动化测试题` or any other module.
7. `Linux面试题` must be expanded only inside its own module bank, never appended under `自动化测试题` or any other module.
