# Annotation Guidelines

## Object Classes
- person
- bicycle
- car
- motorcycle
- bus
- truck

## Bounding Boxes
- Enclose the visible target closely.
- Avoid unnecessary background.
- Keep coordinates inside frame boundaries.
- Require `x_min < x_max` and `y_min < y_max`.

## Track IDs
A track ID should represent one object consistently through time.

Review:
- ID switches
- One ID assigned to two objects
- Broken continuity
- Tracks continuing after an object leaves the scene

## Occlusion
Bounding-box overlap alone does not prove occlusion. Overlap cases may be flagged automatically, but final review should be visual.

## Quality Review
Check for missing objects, duplicate boxes, invalid coordinates, class inconsistencies, track ID switches, broken continuity, and out-of-frame annotations.
