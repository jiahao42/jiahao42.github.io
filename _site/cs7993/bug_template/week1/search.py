#! /usr/bin/env python3
# -*- coding: utf-8
#
# @File:      search
# @Brief:     search for bug templates
# @Created:   Sep/20/2018
# @Author:    Jiahao Cai
#

import subprocess
import re
import sys

ID = r"""([_a-zA-Z][_a-zA-Z0-9]{0,30})"""
CONSTANT = r"""([A-Z]+)"""
DIGIT = r"""([0-9]+)"""
VALID = r"""(%s|%s)""" % (ID, DIGIT)
OP = r"""(\+|-|\*|/|\%|\+\+|--)"""
SPACES = r"""\s*"""

DB = {} # For potential bug template
"""
  //malloc a constant with surrounding memory manipulation//
  - t=malloc(4)
	+ t=malloc(5); /* Rddd */
	sprintf(t,"R%d", act->p.RegisterNumber );
  https://github.com/libming/libming/commit/eea2a55a0aa339d47e65c1c8e60068cf3cc20393
"""
FOCUS_STMT = r"""^(?!\*\*).*malloc\(%s\).*$""" % (DIGIT)
SENSITIVE_STMTS = r"""(sprintf|memcpy|memmove|strcpy).*$"""
TEMPLATE = (FOCUS_STMT, SENSITIVE_STMTS)
DB['malloc'] = TEMPLATE

"""
  //dynamic calculation of array index with surrounding if branch//
	- if (tmp_line[tmp_line_len - 1] == '\n') {
	+ if (tmp_line_len >= 1 && tmp_line[tmp_line_len - 1] == '\n') {
		--tmp_line_len;
  }
  https://github.com/php/php-src/commit/523f230c831d7b33353203fa34aee4e92ac12bba
"""
FOCUS_STMT = r"""^(?!\*\*).*\[%s%s[^>]%s\].*==.*$""" % (VALID, OP, VALID)
SENSITIVE_STMTS = r"""if\("""
TEMPLATE = (FOCUS_STMT, SENSITIVE_STMTS)
DB['dynamic_index_calculation'] = TEMPLATE

"""
  //possible arithmetic overflow//
  - if( (*p) + len > end )
  + if( (*p) > end - len )
  https://github.com/ARMmbed/mbedtls/commit/5224a7544c95552553e2e6be0b4a789956a6464e
"""
FOCUS_STMT = r"""^(?!\*\*).*%s(%s%s)+[><]%s""" % (ID, OP, ID, ID)
SENSITIVE_STMTS = r"""\$"""
TEMPLATE = (FOCUS_STMT, SENSITIVE_STMTS)
DB['possible_num_overflow'] = TEMPLATE



STEP = 10 # scan the +- STEP lines around FOCUS FUNCTION
POSTFIX = r"""(\.c|\.cpp)""" # only scan these files

def traverse_source(PATH = '.'):
  CMD = 'find %s | grep -E \'^(.)+%s$\'' % (PATH, POSTFIX)
  child = subprocess.Popen(CMD,shell=True,stdout=subprocess.PIPE)
  output = str(child.communicate()[0]).replace('\\n', '\n').replace('b\'', '').replace('\'', '')
  # print(output)
  files = output.strip().split('\n')
  for file in files:
    with open(file, 'r', encoding='ISO-8859-1') as source:
      code = source.readlines()
      for i in range(len(code)):
        for k in DB:
          template = DB[k]
          res = re.search(template[0], code[i].replace(" ", ""))
          if res != None:
            print(str(file)+ ":%d:"%(i + 1), code[i].strip())
            look_around(template, file, code, i) 
            print('-' * 77)

def look_around(template, file, code, cursor):
  # start = cursor - STEP if (cursor - STEP) > 0 else 1
  end = cursor + STEP if (cursor + STEP) < len(code) else len(code)
  for i in range(cursor + 1, end):
    if i == cursor: # don't check this line again
      pass
    res = re.search(template[1], code[i].replace(" ", ""))
    if res != None:
      print(str(file)+ ":%d:"%(i + 1), code[i].strip())

if __name__ == '__main__':
  if (len(sys.argv) > 1):
    traverse_source(sys.argv[1])
  else:
    traverse_source()