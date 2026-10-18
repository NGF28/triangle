# Triangle Classifier

A small Python classifier for finite, positive triangle side lengths. Invalid
or degenerate triples return `"Invalid"`. Valid triples return `"Equilateral"`,
`"Isosceles"`, or `"Scalene"`; right triangles receive the `"Right "` prefix.

## Run the tests

```console
python -m pip install -r requirements.txt
python -m pytest
```

## Equivalence classes and boundaries

- **Invalid:** one or more sides are non-positive, or the two shorter sides
  sum to less than or equal to the longest side. Equality is the degenerate
  boundary and is invalid.
- **Equilateral:** all three positive sides are equal.
- **Isosceles:** exactly two positive sides are equal; this includes
  right-isosceles triangles.
- **Scalene:** all positive sides differ; this includes right-scalene
  triangles.
- **Right-angle subset:** the two shorter sides satisfy the Pythagorean
  relationship with the longest side, using a floating-point tolerance.

The equality boundary is covered with `(1, 2, 3)`, while `(3, 4, 5)` and
`(5, 5, 5*sqrt(2))` check integer and non-integer right triangles. The latter
also checks that floating-point values are compared with a tolerance rather
than exact equality.

An equilateral triangle cannot also be right: if all sides have length `s`,
the Pythagorean equation would require `s^2 + s^2 = s^2`, which is impossible for
positive `s`.

## Copilot Review Log

| Test | Copilot-suggested? | Kept / edited / rejected | Why |
|---|---|---|---|
| `test_classifies_triangle_cases` | Yes - Copilot-assisted draft | Edited | Expanded the cases to check invalid, all side classes, right classification, and the non-integer right-isosceles case against the specification. |
| `test_degenerate_boundary_is_invalid` | Yes - Copilot-assisted draft | Kept | I checked that the test correctly rejects a triangle with sides (1, 2, 3). Since 1 + 2 = 3, it does not satisfy the strict triangle inequality and should return "Invalid". |
| `test_right_triangle_tolerance` (reviewed candidate) | No — not an actual inline completion | Rejected | A draft check using `a**2 + b**2 == c**2` would fail the required `5, 5, 5*sqrt(2)` case; the implemented test instead passes those sides to `classify_triangle` and expects `"Right Isosceles"`. |
| `test_stained_glass_customer_flow` | No — customer acceptance test | Kept | Written from the customer criteria without Copilot, as required. |
| `test_valid_triangle_returns_true` | fill in — Copilot-assisted | Kept | I checked the test, it uses valid triangle sides (3,4,5). since the sum of any 2 sides is greater than the 3rd side, the fuction should bne true. |
| `test_right_triangle_with_non_integer_sides` | fill in  — Copilot-assisted | Kept | I checked that the test correctly identifies a right isosceles triangle using non-integer sides. This is important because floating-point calculations can have small rounding errors, so the classifier should use math.isclose() instead of ==. |


**Review limitation:** this workspace did not expose VS Code's inline
autocomplete interface. Copilot assisted with drafting and reviewing the unit
tests, but the log does not claim that the candidates were accepted from the
inline autocomplete UI.

## Acceptance criteria

1. For positive side lengths satisfying the strict triangle inequality,
   `classify_triangle()` returns the correct side class and never `"Invalid"`.
2. If any side is non-positive or the two shorter sides sum to less than or
   equal to the longest side, `classify_triangle()` returns `"Invalid"` without
   raising an exception.
3. For a valid right triangle, the returned shape string starts with `"Right "`
   so the studio can identify the piece that needs reinforced corners.

`test_acceptance.py` checks all three criteria end-to-end through
`classify_triangle()`.

## AI-use disclosure

Tool: GitHub Copilot (this assistant, running in VS Code via Copilot SDK). It
was used to draft and review the unit tests and README. The specification,
edge cases, equality-boundary rejection, and non-integer right-triangle
expectation were checked against the prompt, and the test suite verifies those
behaviors. VS Code inline autocomplete itself was not available in this
workspace; no other AI tool was used.