	if (tmp_line[tmp_line_len - 1] == '\n') {
	if (tmp_line_len >= 1 && tmp_line[tmp_line_len - 1] == '\n') {
		--tmp_line_len;
  }

	//malloc and surrounding memory manipulation//
	t=malloc(5); /* Rddd */
	sprintf(t,"R%d", act->p.RegisterNumber );

	  //possible arithmetic overflow//
  -if( (*p) + len > end )
  +if( (*p) > end - len )