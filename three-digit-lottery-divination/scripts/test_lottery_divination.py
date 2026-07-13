#!/usr/bin/env python3

import unittest

from lottery_divination import (
    Draw,
    _extract_digits,
    analyze_draws,
    changed_trigrams,
    derive_number,
    expected_next_issue,
)


class LotteryDivinationTests(unittest.TestCase):
    def setUp(self):
        self.draws = [
            Draw("26105", "2026-04-25", (2, 1, 7)),
            Draw("26104", "2026-04-24", (7, 8, 6)),
            Draw("26103", "2026-04-23", (9, 0, 1)),
            Draw("26102", "2026-04-22", (4, 9, 0)),
            Draw("26101", "2026-04-21", (0, 9, 0)),
        ]

    def test_extract_digits_accepts_both_api_formats(self):
        self.assertEqual(_extract_digits("3 5 2"), (3, 5, 2))
        self.assertEqual(_extract_digits("9,2,3"), (9, 2, 3))

    def test_extract_digits_rejects_extra_values(self):
        with self.assertRaises(ValueError):
            _extract_digits("3 5 2 8 1")

    def test_expected_next_issue_preserves_prefix(self):
        self.assertEqual(expected_next_issue("26183", 2), "26184")
        self.assertEqual(expected_next_issue("2026183", 4), "2026184")
        self.assertEqual(expected_next_issue("26999", 2), "27001")

    def test_fifth_line_changes_qian_to_li(self):
        self.assertEqual(changed_trigrams(1, 5, 5), (3, 5))

    def test_statistics_are_position_specific(self):
        summary, counts, omissions = analyze_draws(self.draws)
        self.assertEqual(counts[0][2], 1)
        self.assertEqual(counts[1][9], 2)
        self.assertEqual(counts[2][0], 2)
        self.assertEqual(omissions[0][2], 0)
        self.assertEqual(summary["forms"]["pair"], 1)

    def test_derivation_is_deterministic(self):
        _, counts, omissions = analyze_draws(self.draws)
        first = derive_number(self.draws, "26106", counts, omissions)
        second = derive_number(self.draws, "26106", counts, omissions)
        self.assertEqual(first, second)
        self.assertRegex(first["selected_number"], r"^[0-9]{3}$")

    def test_every_draw_contributes_to_history_seed(self):
        _, counts, omissions = analyze_draws(self.draws)
        original = derive_number(self.draws, "26106", counts, omissions)
        changed_draws = list(self.draws)
        changed_draws[-1] = Draw("26101", "2026-04-21", (0, 9, 1))
        _, changed_counts, changed_omissions = analyze_draws(changed_draws)
        changed = derive_number(
            changed_draws, "26106", changed_counts, changed_omissions
        )
        self.assertNotEqual(original["history_seed"], changed["history_seed"])


if __name__ == "__main__":
    unittest.main()
