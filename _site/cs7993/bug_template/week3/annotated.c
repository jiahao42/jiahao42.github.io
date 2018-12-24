/* Parse the input text into an unescaped cinput, and populate item. */
static cJSON_bool parse_string(cJSON * const item, parse_buffer * const input_buffer)
{
    FILE *log_parse_string = fopen("parse_string: start", "w");
    const unsigned char *input_pointer = buffer_at_offset(input_buffer) + 1;
    const unsigned char *input_end = buffer_at_offset(input_buffer) + 1;
    unsigned char *output_pointer = NULL;
    unsigned char *output = NULL;

    /* not a string */
    log_parse_string = fopen("parse_string: input_buffer)[0] != \'\"\'", "w");
    if (buffer_at_offset(input_buffer)[0] != '\"')
    {
        goto fail;
    }

    {
        /* calculate approximate size of the output (overestimate) */
        size_t allocation_length = 0;
        size_t skipped_bytes = 0;
        while (((size_t)(input_end - input_buffer->content) < input_buffer->length) && (*input_end != '\"'))
        {
            log_parse_string = fopen("parse_string: *input_end != \'\"\'", "w");
            /* is escape sequence */
            if (input_end[0] == '\\')
            {
                log_parse_string = fopen("parse_string: input_end[0] == \'\\\'", "w");
                if ((size_t)(input_end + 1 - input_buffer->content) >= input_buffer->length)
                {
                    /* prevent buffer overflow when last input character is a backslash */
                    goto fail;
                }
                skipped_bytes++;
                input_end++;
            }
            input_end++;
        }
        if (((size_t)(input_end - input_buffer->content) >= input_buffer->length) || (*input_end != '\"'))
        {
            log_parse_string = fopen("parse_string: *input_end != \'\"\'", "w");
            goto fail; /* string ended unexpectedly */
        }

        /* This is at most how much we need for the output */
        allocation_length = (size_t) (input_end - buffer_at_offset(input_buffer)) - skipped_bytes;
        output = (unsigned char*)input_buffer->hooks.allocate(allocation_length + sizeof(""));
        if (output == NULL)
        {
            /* oom */
            log_parse_string = fopen("parse_string: output == NULL", "w");
            goto fail; /* allocation failure */
        }
    }

    output_pointer = output;
    /* loop through the string literal */
    while (input_pointer < input_end)
    {
        if (*input_pointer != '\\')
        {
            log_parse_string = fopen("parse_string: *input_pointer != \'\\\'", "w");
            *output_pointer++ = *input_pointer++;
        }
        /* escape sequence */
        else
        {
            unsigned char sequence_length = 2;
            if ((input_end - input_pointer) < 1)
            {
                goto fail;
            }

            switch (input_pointer[1])
            {
                case 'b':
                log_parse_string = fopen("parse_string: input_pointer[1] != \'b\'", "w");
                    *output_pointer++ = '\b';
                    break;
                case 'f':
                log_parse_string = fopen("parse_string: input_pointer[1] != \'f\'", "w");
                    *output_pointer++ = '\f';
                    break;
                case 'n':
                log_parse_string = fopen("parse_string: input_pointer[1] != \'n\'", "w");
                    *output_pointer++ = '\n';
                    break;
                case 'r':
                log_parse_string = fopen("parse_string: input_pointer[1] != \'r\'", "w");
                    *output_pointer++ = '\r';
                    break;
                case 't':
                log_parse_string = fopen("parse_string: input_pointer[1] != \'r\'", "w");
                    *output_pointer++ = '\t';
                    break;
                case '\"':
                case '\\':
                case '/':
                    log_parse_string = fopen("parse_string: input_pointer[1] != \'\"|\\|/\'", "w");
                    *output_pointer++ = input_pointer[1];
                    break;

                /* UTF-16 literal */
                case 'u':
                    log_parse_string = fopen("parse_string: input_pointer[1] != \'u\'", "w");
                    sequence_length = utf16_literal_to_utf8(input_pointer, input_end, &output_pointer);
                    if (sequence_length == 0)
                    {
                        /* failed to convert UTF16-literal to UTF-8 */
                        goto fail;
                    }
                    break;

                default:
                    goto fail;
            }
            input_pointer += sequence_length;
        }
    }

    /* zero terminate the output */
    *output_pointer = '\0';
    log_parse_string = fopen("parse_string: *output_pointer = \'\\0\'", "w");

    item->type = cJSON_String;
    item->valuestring = (char*)output;

    input_buffer->offset = (size_t) (input_end - input_buffer->content);
    input_buffer->offset++;

    log_parse_string = fopen("parse_string: return true", "w");
    fclose(log_parse_string);
    return true;

fail:
    if (output != NULL)
    {
        input_buffer->hooks.deallocate(output);
    }

    if (input_pointer != NULL)
    {
        input_buffer->offset = (size_t)(input_pointer - input_buffer->content);
    }
    log_parse_string = fopen("parse_string: return false", "w");
    fclose(log_parse_string);
    return false;
}