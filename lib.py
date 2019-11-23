#!/usr/bin/python
# -*- coding: UTF-8 -*-

restricted_word_file = "./限制词列表.txt"

def read_restricted_word_list():
    file = open(restricted_word_file,"r",encoding='utf8')
    restricted_word_list=file.readlines()
    restricted_word_list = [w.replace('\n','').replace('\r','') for w in restricted_word_list]
    return restricted_word_list

if __name__=='__main__':
    read_restricted_word_list()