Given an array of points on a 2D plane, find the maximum number of points that are visible from point (0, 0) with a viewing angle that is equal to 45 degrees.


### Example

For

```
points = [[1, 1], [3, 1], [3, 2], [3, 3], [1, 3], [2, 5], [1, 5], [-1, -1], [-1, -2], [-2, -3], [-4, -4]]
```

the output should be `visiblePoints(points) = 6`.

- Time limit: 4000ms
- It is guaranteed that there are no points located at (0, 0) and there are no two points located at the same place
- 1 <= points.length <= 10^5
- points[i].length = 2
- -10^7 <= points[i][j] <= 10^7

