"""
Test if:
1. the lines do not intersect and are parallel eg. ([0, 0], [1, 1]), [(0, 1), (1, 2)]
2. there is one intersection point eg. ([0, 0], [10, 10]), ([-5, 5], [26, 5])
3. there are infinite intersection points (co-incident) eg. ([0, 0], [10, 10]), ([0, 0], [10, 10])
4. lines are points eg. ([0, 0], [0, 0]), ([1, 1], [1, 1])
5. the lines do not intersect but aren't parallel eg. ([0, 0], [3, 3]) ([-5, 2], [-1, 2])
6. both lines share one co-ordinate set eg. ([0, 0], [1, 1]), ([0, 0], [0, -5])
"""