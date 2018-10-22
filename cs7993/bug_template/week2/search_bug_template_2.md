---
title: 
  Current bug templates (Week 2)
date: 
  Sep 28, 2018
---

## Overview

Overall, I extract a prototype from this [bug](https://github.com/php/php-src/commit/523f230c831d7b33353203fa34aee4e92ac12bba), the prototype get 2 matches in PHP source code, and the 2 matches are in the same file.

## Progress

So I tried to extract a prototype from this [bug](https://github.com/php/php-src/commit/523f230c831d7b33353203fa34aee4e92ac12bba):

```c
								tmp_line, response_code);
				}
			}
- 		if (tmp_line[tmp_line_len - 1] == '\n') {
+ 		if (tmp_line_len >= 1 && tmp_line[tmp_line_len - 1] == '\n') {
				--tmp_line_len;
- 			if (tmp_line[tmp_line_len - 1] == '\r') {
+ 			if (tmp_line_len >= 1 &&tmp_line[tmp_line_len - 1] == '\r') {
					--tmp_line_len;
				}
			}
```

The function where bug occurs is too long, so I tried to extract one function from the context. Basically the job of this snippet is to send a request, and then check the response code of the request.

```c
// propotype: php-src/ext/standard/http_fopen_wrapper.c
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
```

First I use the regex to search the source code of php:

```python
FOCUS_STMTS = r""".{0,80}write.{0,3200}response.{0,3200}403.{0,3200}==\s*\'\\n\'"""
```

It can only find one snippet of code, that's where the bug occurs orginally, see the log:

```c
:655:	/* send it */
./php-src/ext/standard/http_fopen_wrapper.c:656:	php_stream_write(stream, ZSTR_VAL(req_buf.s), ZSTR_LEN(req_buf.s));
./php-src/ext/standard/http_fopen_wrapper.c:658:	location[0] = '\0';
./php-src/ext/standard/http_fopen_wrapper.c:660:	if (Z_ISUNDEF_P(response_header)) {
./php-src/ext/standard/http_fopen_wrapper.c:661:		array_init(response_header);
./php-src/ext/standard/http_fopen_wrapper.c:662:	}
./php-src/ext/standard/http_fopen_wrapper.c:664:	if (!php_stream_eof(stream)) {
./php-src/ext/standard/http_fopen_wrapper.c:665:		size_t tmp_line_len;
./php-src/ext/standard/http_fopen_wrapper.c:666:		/* get response header */
./php-src/ext/standard/http_fopen_wrapper.c:668:		if (php_stream_get_line(stream, tmp_line, sizeof(tmp_line) - 1, &tmp_line_len) != NULL) {
./php-src/ext/standard/http_fopen_wrapper.c:669:			zval http_response;
./php-src/ext/standard/http_fopen_wrapper.c:671:			if (tmp_line_len > 9) {
./php-src/ext/standard/http_fopen_wrapper.c:672:				response_code = atoi(tmp_line + 9);
./php-src/ext/standard/http_fopen_wrapper.c:673:			} else {
./php-src/ext/standard/http_fopen_wrapper.c:674:				response_code = 0;
./php-src/ext/standard/http_fopen_wrapper.c:675:			}
./php-src/ext/standard/http_fopen_wrapper.c:676:			if (context && NULL != (tmpzval = php_stream_context_get_option(context, "http", "ignore_errors"))) {
./php-src/ext/standard/http_fopen_wrapper.c:677:				ignore_errors = zend_is_true(tmpzval);
./php-src/ext/standard/http_fopen_wrapper.c:678:			}
./php-src/ext/standard/http_fopen_wrapper.c:679:			/* when we request only the header, don't fail even on error codes */
./php-src/ext/standard/http_fopen_wrapper.c:680:			if ((options & STREAM_ONLY_GET_HEADERS) || ignore_errors) {
./php-src/ext/standard/http_fopen_wrapper.c:681:				reqok = 1;
./php-src/ext/standard/http_fopen_wrapper.c:682:			}
./php-src/ext/standard/http_fopen_wrapper.c:684:			/* status codes of 1xx are "informational", and will be followed by a real response
./php-src/ext/standard/http_fopen_wrapper.c:685:			 * e.g "100 Continue". RFC 7231 states that unexpected 1xx status MUST be parsed,
./php-src/ext/standard/http_fopen_wrapper.c:686:			 * and MAY be ignored. As such, we need to skip ahead to the "real" status*/
./php-src/ext/standard/http_fopen_wrapper.c:687:			if (response_code >= 100 && response_code < 200) {
./php-src/ext/standard/http_fopen_wrapper.c:688:				/* consume lines until we find a line starting 'HTTP/1' */
./php-src/ext/standard/http_fopen_wrapper.c:689:				while (
./php-src/ext/standard/http_fopen_wrapper.c:690:					!php_stream_eof(stream)
./php-src/ext/standard/http_fopen_wrapper.c:691:					&& php_stream_get_line(stream, tmp_line, sizeof(tmp_line) - 1, &tmp_line_len) != NULL
./php-src/ext/standard/http_fopen_wrapper.c:692:					&& ( tmp_line_len < sizeof("HTTP/1") - 1 || strncasecmp(tmp_line, "HTTP/1", sizeof("HTTP/1") - 1) )
./php-src/ext/standard/http_fopen_wrapper.c:693:				);
./php-src/ext/standard/http_fopen_wrapper.c:695:				if (tmp_line_len > 9) {
./php-src/ext/standard/http_fopen_wrapper.c:696:					response_code = atoi(tmp_line + 9);
./php-src/ext/standard/http_fopen_wrapper.c:697:				} else {
./php-src/ext/standard/http_fopen_wrapper.c:698:					response_code = 0;
./php-src/ext/standard/http_fopen_wrapper.c:699:				}
./php-src/ext/standard/http_fopen_wrapper.c:700:			}
./php-src/ext/standard/http_fopen_wrapper.c:701:			/* all status codes in the 2xx range are defined by the specification as successful;
./php-src/ext/standard/http_fopen_wrapper.c:702:			 * all status codes in the 3xx range are for redirection, and so also should never
./php-src/ext/standard/http_fopen_wrapper.c:703:			 * fail */
./php-src/ext/standard/http_fopen_wrapper.c:704:			if (response_code >= 200 && response_code < 400) {
./php-src/ext/standard/http_fopen_wrapper.c:705:				reqok = 1;
./php-src/ext/standard/http_fopen_wrapper.c:706:			} else {
./php-src/ext/standard/http_fopen_wrapper.c:707:				switch(response_code) {
./php-src/ext/standard/http_fopen_wrapper.c:708:					case 403:
./php-src/ext/standard/http_fopen_wrapper.c:709:						php_stream_notify_error(context, PHP_STREAM_NOTIFY_AUTH_RESULT,
./php-src/ext/standard/http_fopen_wrapper.c:710:								tmp_line, response_code);
./php-src/ext/standard/http_fopen_wrapper.c:711:						break;
./php-src/ext/standard/http_fopen_wrapper.c:712:					default:
./php-src/ext/standard/http_fopen_wrapper.c:713:						/* safety net in the event tmp_line == NULL */
./php-src/ext/standard/http_fopen_wrapper.c:714:						if (!tmp_line_len) {
./php-src/ext/standard/http_fopen_wrapper.c:715:							tmp_line[0] = '\0';
./php-src/ext/standard/http_fopen_wrapper.c:716:						}
./php-src/ext/standard/http_fopen_wrapper.c:717:						php_stream_notify_error(context, PHP_STREAM_NOTIFY_FAILURE,
./php-src/ext/standard/http_fopen_wrapper.c:718:								tmp_line, response_code);
./php-src/ext/standard/http_fopen_wrapper.c:719:				}
./php-src/ext/standard/http_fopen_wrapper.c:720:			}
./php-src/ext/standard/http_fopen_wrapper.c:721:			if (tmp_line_len >= 1 && tmp_line[tmp_line_len - 1] == '\n'
-----------------------------------------------------------------------------
```

Then I thought the response code 403 may be too specific, so I removed the response code part and ran the script again, then I got something new (from the same file as the log above):

```c
of("\r\n")-1);
./php-src/ext/standard/http_fopen_wrapper.c:307:		if (php_stream_write(stream, ZSTR_VAL(header.s), ZSTR_LEN(header.s)) != ZSTR_LEN(header.s)) {
./php-src/ext/standard/http_fopen_wrapper.c:308:			php_stream_wrapper_log_error(wrapper, options, "Cannot connect to HTTPS server through proxy");
./php-src/ext/standard/http_fopen_wrapper.c:309:			php_stream_close(stream);
./php-src/ext/standard/http_fopen_wrapper.c:310:			stream = NULL;
./php-src/ext/standard/http_fopen_wrapper.c:311:		}
./php-src/ext/standard/http_fopen_wrapper.c:312: 	 	smart_str_free(&header);
./php-src/ext/standard/http_fopen_wrapper.c:314: 	 	if (stream) {
./php-src/ext/standard/http_fopen_wrapper.c:315: 	 		char header_line[HTTP_HEADER_BLOCK_SIZE];
./php-src/ext/standard/http_fopen_wrapper.c:317:			/* get response header */
./php-src/ext/standard/http_fopen_wrapper.c:318:			while (php_stream_gets(stream, header_line, HTTP_HEADER_BLOCK_SIZE-1) != NULL) {
./php-src/ext/standard/http_fopen_wrapper.c:319:				if (header_line[0] == '\n'
-----------------------------------------------------------------------------
```

## Problem

I think the current the problem is: we want to make the regex more general, but considering the regex we are using now:

```python
.{0,80}write.{0,3200}response.{0,3200}==\s*\'\\n\'
```

It only has 4 keywords, there are not much things to remove, so I am not sure what's the next step, should we just create some new templates, or keep working on this? We can do:

* increase or decrease the gap of keywords
* increase or decrease the number of keywords
* (something I don't know yet)


## Outcome

I have written this [Python script](./search.py) to help me with it.

I use this script to scan [the source code of php](https://github.com/php/php-src) and an [SWF library](https://github.com/libming/libming), and here is the [Log file](./bug_template.log).