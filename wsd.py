'''
Original Challenge, Bonus 1

input:
    queue (array of integers),
    num_taps (integer)
output: result (integer)

assumptions: 
    each tap flows at a rate of 100ml per second,
    you can start filling your bottle as soon as a tap is available
'''


def calculate_time_1(queue: list, num_taps: int) -> float:
    # validate input
    if type(queue) != list:
        raise TypeError('Invalid argument. "queue" should be a list.')
    else:
        for i in queue:
            if type(i) != int or i <= 0:
                raise Exception(
                    'Invalid argument. "queue" should be a list of integers over 0.')
    if type(num_taps) != int or num_taps <= 0:
        raise Exception(
            'Invalid argument. "num_taps" should be an integer over 0.')
    # move someone to each tap
    time = []
    for _ in range(num_taps):
        if len(queue) > 0:
            time.append(queue.pop(0))
        else:
            time.append(0)
    # move rest of the queue to the next available tap
    for _ in range(len(queue)):
        min_index = time.index(min(time))
        time[min_index] += queue.pop(0)
    # get max time and convert to seconds
    result = max(time) / 100
    return f'{result} seconds'


'''
Bonus 1, Bonus 2

input:
    queue (array of integers),
    num_taps (integer),
    walking_time (integer)
output: result (integer)

assumptions: 
    each tap flows at a rate of 100ml per second,
    it takes the same amount of time to walk to each tap
'''


def calculate_time_2(queue: list, num_taps: int, walking_time: int) -> float:
    # validate input
    if type(queue) != list:
        raise TypeError('Invalid argument. "queue" should be a list.')
    else:
        for i in queue:
            if type(i) != int or i <= 0:
                raise Exception(
                    'Invalid argument. "queue" should be a list of integers over 0.')
    if type(num_taps) != int or num_taps <= 0:
        raise Exception(
            'Invalid argument. "taps" should be an integer over 0.')
    if type(walking_time) != int or walking_time <= 0:
        raise Exception(
            'Invalid argument. "walking_time" should be an integer over 0.')
    # move someone to each tap
    time = []
    walking_time *= 100
    for _ in range(num_taps):
        if len(queue) > 0:
            time.append(walking_time + queue.pop(0))
        else:
            time.append(0)
    # move rest of the queue to the next available tap
    for _ in range(len(queue)):
        min_index = time.index(min(time))
        time[min_index] += walking_time + queue.pop(0)
    # get max time and convert to seconds
    result = max(time) / 100
    return f'{result} seconds'


'''
Bonus 1, Bonus 3

input:
    queue (array of integers),
    num_taps (integer),
    walking_time (integer),
    flow_rate (array of integers)
output: result (integer)

assumption: it takes the same amount of time to walk to each tap
'''


def calculate_time_3(queue: list, num_taps: int, walking_time: int, flow_rate: list) -> float:
    # validate input
    if type(queue) != list:
        raise TypeError('Invalid argument. "queue" should be a list.')
    else:
        for i in queue:
            if type(i) != int or i <= 0:
                raise Exception(
                    'Invalid argument. "queue" should be a list of integers over 0.')
    if type(num_taps) != int or num_taps <= 0:
        raise Exception(
            'Invalid argument. "num_taps" should be an integer over 0.')
    if type(walking_time) != int or walking_time <= 0:
        raise Exception(
            'Invalid argument. "walking_time" should be an integer over 0.')
    if type(flow_rate) != list:
        raise TypeError('Invalid argument. "flow_rate" should be a list.')
    else:
        for i in flow_rate:
            if type(i) != int or i <= 0:
                raise Exception(
                    'Invalid argument. "flow_rate" should be a list of integers over 0.')
    if num_taps != len(flow_rate):
        raise Exception(
            'Length of "flow_rate" array must equal "num_taps". Pass in the "flow_rate" for each tap.')
    # move someone to each tap
    time = []
    walking_time *= 100
    for i in range(num_taps):
        if len(queue) > 0:
            time.append(walking_time + (queue.pop(0) * (100 / flow_rate[i])))
        else:
            time.append(0)
    # move rest of the queue to the next available tap
    for _ in range(len(queue)):
        min_index = time.index(min(time))
        time[min_index] += walking_time + \
            (queue.pop(0) * (100 / flow_rate[min_index]))
    # get max time and convert to seconds
    result = max(time) / 100
    return f'{result} seconds'


print(calculate_time_1([200, 400, 600, 800, 1000], 3))
print(calculate_time_2([200, 400, 600, 800, 1000], 3, 2))
print(calculate_time_3([200, 400, 600, 800, 1000], 3, 2, [50, 100, 200]))
print('-------------')
print(calculate_time_1([800, 400, 600, 200, 1000], 3))
print(calculate_time_2([800, 400, 600, 200, 1000], 3, 2))
print(calculate_time_3([800, 400, 600, 200, 1000], 3, 2, [50, 100, 200]))
print('-------------')
print(calculate_time_1([1000, 400, 800, 200, 600], 3))
print(calculate_time_2([1000, 400, 800, 200, 600], 3, 2))
print(calculate_time_3([1000, 400, 800, 200, 600], 3, 2, [50, 100, 200]))
print('-------------')
print(calculate_time_1([600, 800, 400, 1000, 200], 3))
print(calculate_time_2([600, 800, 400, 1000, 200], 3, 2))
print(calculate_time_3([600, 800, 400, 1000, 200], 3, 2, [50, 100, 200]))
print('-------------')
print(calculate_time_1([600, 200, 1000, 400, 800], 3))
print(calculate_time_2([600, 200, 1000, 400, 800], 3, 2))
print(calculate_time_3([600, 200, 1000, 400, 800], 3, 2, [50, 100, 200]))
print('-------------')
print(calculate_time_1([400, 800, 1000, 600, 200], 3))
print(calculate_time_2([400, 800, 1000, 600, 200], 3, 2))
print(calculate_time_3([400, 800, 1000, 600, 200], 3, 2, [50, 100, 200]))

'''
Bonus 4

No. A faster tap means that it takes less time to fill up a water bottle. Walking time and the amount of water in each bottle are fixed. Flow rate and time are reciprocal so if you increase the flow rate of a specific tap, the time taken to fill a bottle at that tap decreases. As flow rate tends to infinity, time tends to zero.
'''
