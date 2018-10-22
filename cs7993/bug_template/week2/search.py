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

DB = {}
"""
propotype: php-src/ext/standard/http_fopen_wrapper.c
static php_stream *php_stream_url_wrap_http_ex(...) {
  ...
	php_stream_write(stream, ZSTR_VAL(req_buf.s), ZSTR_LEN(req_buf.s));
  ...
  if (php_stream_get_line(stream, tmp_line, sizeof(tmp_line) - 1, &tmp_line_len) != NULL) {
    ...
    if (response_code >= 200 && response_code < 400) {
      ...
			switch(response_code) {
				case 403:
					php_stream_notify_error(context, PHP_STREAM_NOTIFY_AUTH_RESULT,
							tmp_line, response_code);
					break;
				default:
					php_stream_notify_error(context, PHP_STREAM_NOTIFY_FAILURE,
							tmp_line, response_code);
			}
			if (tmp_line_len >= 1 && tmp_line[tmp_line_len - 1] == '\n') {
				--tmp_line_len;
				if (tmp_line_len >= 1 &&tmp_line[tmp_line_len - 1] == '\r') {
					--tmp_line_len;
				}
			}
      ...
    }
  }
}
"""
# Assume there are 80 chars at most in one line
# FOCUS_STMTS = r""".{0,80}write.{0,3200}response.{0,3200}403.{0,3200}==\s*\'\\n\'"""# % (ID, OP, DIGIT)
FOCUS_STMTS = r""".{0,80}write.{0,3200}response.{0,3200}==\s*\'\\n\'"""
TEMPLATE = (FOCUS_STMTS)
DB['url_wrap_http_ex'] = TEMPLATE

STEP = 10 # scan the +- STEP lines around FOCUS STMT
POSTFIX = r"""\\.c$\|\\.cpp$""" # only scan these files

def traverse_source(PATH = '.'):
  CMD = 'find %s | grep -E %s | xargs grep -rn -e . ' % (PATH, POSTFIX)
  # print(CMD)
  child = subprocess.Popen(CMD,shell=True,stdout=subprocess.PIPE)
  output = str(child.communicate()[0]).replace('b\'', '').replace('\\\'', '\'').replace('\\\\', '\\').replace('\\t', '\t')
  output = re.sub(r'\\n\.', r'\n.', output)
  # print(output)
  for k in DB:
    res = re.findall(DB[k], output, flags=re.S)
    for s in res:
      print(s)
      print('-' * 77)

if __name__ == '__main__':
  if (len(sys.argv) > 1):
    traverse_source(sys.argv[1])
  else:
    traverse_source()