#!/usr/bin/env python3
# Author ID: lkumar12

def read_file_string(file_name):
    f = open(file_name, 'r')
    read_data = f.read()   
    f.close() 
    print(read_data)
    return read_data

def read_file_list(file_name):
    f = open('data.txt', 'r')
    read_data = f.read()
    f.close()
    list_of_lines = read_data.splitlines()
    return list_of_lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))