---
title: 
  Current bug templates
date: 
  Sep 22, 2018
---

I have found three bug templates so far. For each template, we have a `focus statement` and several `sensitive statement`s, each time the program find a `focus statement`, it will try to find `sensitive statement`s in the following `n` lines of code.

* For example, in the following template, the `focus statement` is `malloc` with a constant, and the program will check if there are `sensitive statement`s in the next `n` lines of code, which means to check if there are memory manipulation statements, such as `sprintf|memcpy|memmove|strcpy`.
  * `focus statement` is `malloc` with constant
  * `sensitive statement`s are memory manipulation statements, such as `sprintf|memcpy|memmove|strcpy`.

```c
  //malloc a constant with surrounding memory manipulation//
  - t=malloc(4)
	+ t=malloc(5); /* Rddd */
	sprintf(t,"R%d", act->p.RegisterNumber );
  // https://github.com/libming/libming/commit/eea2a55a0aa339d47e65c1c8e60068cf3cc20393
```

* This template is trying to find dynamic array index generated during runtime, because it has the possibility to be out of boundary.
  * `focus statement` is dynamic array index generated during runtime, e.g. the statement inside `[]` has operator.
  * `sensitive statement`s are the surrounding `if` statements.

```c
  //dynamic calculation of array index with surrounding if branch//
	- if (tmp_line[tmp_line_len - 1] == '\n') {
	+ if (tmp_line_len >= 1 && tmp_line[tmp_line_len - 1] == '\n') {
		--tmp_line_len;
  }
  // https://github.com/php/php-src/commit/523f230c831d7b33353203fa34aee4e92ac12bba
```

* This template is trying to find potential arithmetic overflow, typically is in the comparsion with calculation of two or more identifier and another identifier/number, because people focus on the comparsion and overlook there is a potential arithmetic overflow.
  * `focus statement` is in the form of `id (op id)+ [>, <] [id, num]`
  * `sensitive statement`: None

```c
  //possible arithmetic overflow//
  - if( (*p) + len > end )
  + if( (*p) > end - len )
  // https://github.com/ARMmbed/mbedtls/commit/5224a7544c95552553e2e6be0b4a789956a6464e
```

## Outcome

I have written this [Python script](./search.py) to help me with it.

I use this script to scan [the source code of php](https://github.com/php/php-src) and an [SWF library](https://github.com/libming/libming), and here is the [Log file](./bug_template.log).