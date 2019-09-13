#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:06:43 2019

@author: Md. Hasnain
Description: This project is to search the char from given decimal or hex
ascii value and show the bitmap with '-' and '*' in the output

Input params:
    1. The input file name with .bdf extention
    2. Ascii code in decimal or hex
Output:
    1. Input ascii in decimal and hex
    2. Bitmap in '-' and '*' format
"""
import sys

"""
This function search the ascii_code from the given file.
Input:
    1. ascii code in int or hex
    2. File name string
Output:
    1. bitmap array(empty if not found)
"""
def searchChar(ascii_code, file_name):
    search_text = 'ENCODING ' + str(ascii_code)
    bitmap_array = []
    found = False
    take_input = False
    with open(file_name) as dataFile:
        for num, line in enumerate(dataFile, 1):
            if search_text == line.rstrip():
                found = True
            
            if found and line.rstrip() == 'BITMAP':
                take_input = True
                
            if found and line.rstrip() == 'ENDCHAR':
                take_input = False
                break
                
            if take_input and line.rstrip() != 'BITMAP':
                bitmap_array.append(line.rstrip())
                
    return bitmap_array

"""
This function converts the given hex value to binary value.
Input:
    1. hex value
    2. output format(4 or 8)
Output:
    1. binary value of the given hex
"""
def hex2bin(hex_str, out_format = 4):
    int_value = int(hex_str, 16)
    if(out_format == 8):
        output_length = 8 * ((len(hex_str) + 1 ) // 2) # Byte length output i.e input A is printed as 00001010
    else:
        output_length = (len(hex_str)) * 4 # Nibble length output i.e input A is printed as 1010

    bin_value = f'{int_value:0{output_length}b}' # new style
    return bin_value

"""
Program first starts from here.
1. Get the input file name from the comand line arguments.
    a. If file name is not okay stop the process
2. Get the input ascii code from the user
    a. If input is invalid print invalid input message
    b. Find the char for given ascii code from the given file
3. If not found print the not found message
4. If found convert the hex bitmap to binary
5. Print the binary bitmap values with '-' and '*'
6. Ask user for search again
7. If search again go to step 2
   Else terminate the programm
"""
start_process = True
if len(sys.argv) > 1:
    input_file = sys.argv[1]
    if not input_file.endswith('.bdf'):
        print ('ファイルがありません')
        start_process = False
        
else:
    print ('ファイルがありません')
    start_process = False

while start_process:
    input_data = input ("エンコード番号を入力してください ")
    try:
        is_hex = input_data.startswith('0x')
        if is_hex:
            ascii_code_int = int(input_data, 16)
            ascii_code_hex = input_data
        else:
            ascii_code_int = int(input_data)
            ascii_code_hex = hex(ascii_code_int)
    except ValueError:
        print("入力データが不正です")
        break
    
    bitmap_array = searchChar(str(ascii_code_int), input_file)
    
    if not bitmap_array:
        print('該当のデータがありません')
    else:
        output = 'エンコード: ' + str(ascii_code_int) + ' (' + str(ascii_code_hex) + ')'
        print(output)
        print('ビットマップ:')
        for bitmap in bitmap_array:
            bin_data = hex2bin(bitmap, 8)
            bin_data_array = list(bin_data)
            
            line = ''
            for char in bin_data_array:
                if char == '0':
                    line += '-'
                else:
                    line += '*'
            print(line)
        
    again = input ("もう一度検索する([Y]es/[N]o) ")
    
    if again == 'N':
        break
