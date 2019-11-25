"""
1. Test if the lines do not intersect and are parallel eg. ([0, 0], [1, 1]), [(0, 1), (1, 2)]
2. Test if there is one intersection point eg. ([0, 0], [10, 10]), ([-5, 5], [6, 5])
3. Test if there are infinite intersection points (co-incident) eg. ([0, 0], [1, 1]), ([0, 0], [1, 1])
4. Test if lines are points eg. ([0, 0], [0, 0]), ([1, 1], [1, 1])
5. Test if the lines do not intersect but aren't parallel eg. ([0, 0], [3, 3]) ([-5, 2], [-1, 2])
6. Test if both lines share one co-ordinate set eg. ([0, 0], [1, 1]), ([0, 0], [0, -5])
"""