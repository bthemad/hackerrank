#!/usr/bin/env python

if __name__ == '__main__':
    jars_count, ops_count = map(int, raw_input().strip().split(" "))
    jars = [0] * jars_count

    total_candy = 0
    for i in range(ops_count):
        op = map(int, raw_input().strip().split(" "))
        start_jar = op[0]
        end_jar = op[1]
        candy_count = op[2]
        total_candy += (end_jar - start_jar + 1) * candy_count
    print total_candy / jars_count
