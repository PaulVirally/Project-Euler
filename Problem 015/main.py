class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, pt):
        return abs(self.x - pt.x) + abs(self.y - pt.y)

    def __str__(self):
        return '({0}, {1})'.format(self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return ((self.x == other.x) and (self.y == other.y))

    def __ne__(self, other):
        return ((self.x != other.x) or (self.y != other.y))

for n in range(20):

    end = Point(n, n)
    start = Point(0, 0)
    paths = [[end]]
    for i in range(n+1):
        for j in range(n+1):
            # print('{0}/20, {1}/20 <-- {2}'.format(i, j, len(paths)))
            pos1 = Point(n-i, n-j)
            pos2 = Point(n-j, n-i)

            # Remove duplicates
            new_paths = []
            for path in paths:
                if path not in new_paths:
                    new_paths.append(path)
            paths = new_paths

            for path in paths:
                last_point = path[-1]
                if last_point.distance(pos1) == 1:
                    # Only add a path if it is going back up, not back to the end
                    if last_point.x >= pos1.x and last_point.y >= pos1.y:
                        paths.append(path + [pos1])

                if last_point.distance(pos2) == 1:
                    # Only add a path if it is going back up, not back to the end                
                    if last_point.x >= pos2.x and last_point.y >= pos2.y:                
                        paths.append(path + [pos2])

    unique_solutions = []
    for path in paths:
        if path not in unique_solutions:
            if path[-1] == start:
                unique_solutions.append(path)

    count = 0
    for path in unique_solutions:
        if path[0] == end and path[-1] == start:
            count += 1

    print('n: {0} --> {1}'.format(n, count))