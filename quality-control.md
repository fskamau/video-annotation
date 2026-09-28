# Quality Control

## Geometry Checks

```text
x_min < x_max
y_min < y_max
x_min >= 0
y_min >= 0
x_max <= frame_width
y_max <= frame_height
```

## Track Checks
Review sudden ID changes, duplicate IDs, unexplained gaps, abrupt class changes, and tracks continuing outside the visible sequence.

## Visual Review
Automated checks should be followed by visual inspection for occlusion, truncation, missed objects, incorrect classes, loose boxes, and identity switches.

## Suggested Status
- `PASS`
- `REVIEW`
- `FIX`
