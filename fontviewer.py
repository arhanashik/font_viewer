#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 16:06:43 2019

@author: academy-4
"""

#ib8x8u.bdf
def searchChar(ascii_code):
    search_text = 'ENCODING ' + str(ascii_code)
    bitmap_array = []
    found = False
    take_input = False
    with open('ib8x8u.bdf') as dataFile:
        for num, line in enumerate(dataFile, 1):
            if search_text == line.rstrip():
                found = True
            
            if found == True and line.rstrip() == 'BITMAP':
                take_input = True
                
            if found == True and line.rstrip() == 'ENDCHAR':
                take_input = False
                break
                
            if take_input == True and line.rstrip() != 'BITMAP':
                bitmap_array.append(line.rstrip())
                
    return bitmap_array

def hex2bin(HexInputStr, outFormat = 4):
    int_value = int(HexInputStr, 16)
    if(outFormat == 8):
        output_length = 8 * ((len(HexInputStr) + 1 ) // 2) # Byte length output i.e input A is printed as 00001010
    else:
        output_length = (len(HexInputStr)) * 4 # Nibble length output i.e input A is printed as 1010


    bin_value = f'{int_value:0{output_length}b}' # new style
    return bin_value

while True:
    input_data = input ("エンコード番号を入力してください ")
    try:
        input_ascii_code = int(input_data)
    except ValueError:
        print("無効入力")
    
    bitmap_array = searchChar(str(input_ascii_code))
    
    if not bitmap_array:
        print('該当のデータがありません')
    else:
        output = 'エンコード: ' + input_data + '(0xXX)'
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
        
    again = input ("again(1): ")
    
    if int(again) != 1:
        break