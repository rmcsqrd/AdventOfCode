import random
import time

def RawDataRegen():
    raw_data = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 13, 1, 19, 1, 9, 19, 23, 2, 23, 13, 27, 1, 27, 9,
                31, 2, 31, 6, 35, 1, 5, 35, 39, 1, 10, 39, 43, 2, 43, 6, 47, 1, 10, 47, 51, 2, 6, 51, 55, 1, 5, 55, 59, 1,
                59, 9, 63, 1, 13, 63, 67, 2, 6, 67, 71, 1, 5, 71, 75, 2, 6, 75, 79, 2, 79, 6, 83, 1, 13, 83, 87, 1, 9,
                87, 91, 1, 9, 91, 95, 1, 5, 95, 99, 1, 5, 99, 103, 2, 13, 103, 107, 1, 6, 107, 111, 1, 9, 111, 115, 2,
                6, 115, 119, 1, 13, 119, 123, 1, 123, 6, 127, 1, 127, 5, 131, 2, 10, 131, 135, 2, 135, 10, 139, 1, 13,
                139, 143, 1, 10, 143, 147, 1, 2, 147, 151, 1, 6, 151, 0, 99, 2, 14, 0, 0]
    return raw_data

def OpCodeReader(data):
    opcodes = data[0: len(data): 4]
    for cnt in range(len(opcodes)):
        position = cnt * 4
        operation = data[position]
        if operation == 1:
            data[data[position + 3]] = data[data[position + 1]] + data[data[position + 2]]
        if operation == 2:
            data[data[position + 3]] = data[data[position + 1]] * data[data[position + 2]]
        if operation == 99:
            break
    return data[0]

def RandOpCodeReader(data):
    result = 0
    while result != 19690720:
        data = RawDataRegen()
        noun = random.randint(0, 100)
        verb = random.randint(0, 100)
        data[1] = noun
        data[2] = verb
        result = OpCodeReader(data)

    return data[1], data[2]

if __name__ == '__main__':
    start_time = time.time()
    # test cases
    test_data_example = [1,9,10,3,2,3,11,0,99,30,40,50]
    test_data1 = [1,0,0,0,99]
    test_data2 = [2,3,0,3,99]
    test_data3 = [2,4,4,5,99,0]
    test_data4 = [1,1,1,4,99,5,6,0,99]

    # solve part 1 with actual data
    # note position 1 and 2 (indexes from 0) were originally 0, 0
    raw_data = RawDataRegen()  # mutable lists are being fussy
    result = OpCodeReader(raw_data)
    print('Day 2 Part 1 = ')
    print(result)

    # solve part 2
    raw_data = RawDataRegen()
    noun, verb = RandOpCodeReader(raw_data)
    print('Day 2 Part 2 = ')
    print(noun, verb)
    print(100*noun + verb)


    print("--- %s seconds ---" % (time.time() - start_time))


