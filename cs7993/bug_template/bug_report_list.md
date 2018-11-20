---
title:
  Bug reports
---

* [cJSON](#cJSON)
  * [Bug in cJSON.c cJSON_SetNumberHelper #138](#Bug in cJSON.c cJSON_SetNumberHelper #138)
  * [Bug in cJSON_AddItemToObject #106](#Bug in cJSON_AddItemToObject #106)
  * [Invalid pointer returned if reallocate fails in ensure function #189](#Invalid pointer returned if reallocate fails in ensure function #189)
  * [String deallocated before use #248](#String deallocated before use #248)
* [iniparser](#iniparser)
  * ini file parser
  * [Empty string with quotes. #70](#Empty string with quotes. #70)
* [http-parser](#http-parser)
  * [Heap out-of-bounds read in strtoul (68345541)](#Heap out-of-bounds read in strtoul (68345541))
* [myhtml](#myhtml)
  * Fast C/C++ HTML 5 Parser. Using threads.
  * [fix charef parsing #152](#fix charef parsing #152)
* [json-parser](#json-parser)
  * [heap buffer overflow on some inputs #68](#heap buffer overflow on some inputs #68)
* [mongoose](#mongoose)
  * Mongoose Embedded Web Server Library - Mongoose is more than an embedded webserver. It is a multi-protocol embedded networking library with functions including TCP, HTTP client and server, WebSocket client and server, MQTT client and broker and much more.
  * [websocket client bug #631](#websocket client bug #631)
* [Firefox](#Firefox)
  * [Iframe injection & content spoofing & scripts execution via json viewer](#CVE-2018-5176)
    * [CVE-2018-5176](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5176)
* [poco](#poco)
  * The POCO C++ Libraries are powerful cross-platform C++ libraries for building network- and internet-based applications that run on desktop, server, mobile, IoT, and embedded systems.
  * [Zip Decompress Parent Path Injection #1968](#Zip Decompress Parent Path Injection #1968)
* [CImg](#CImg)
  * The CImg Library is a small and open-source C++ toolkit for image processing.
  * [other testcases lead to heap overflow by loading crafted images #185](#other testcases lead to heap overflow by loading crafted images #185)
    * [CVE-2018-7640](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-7640)
* [ImageMagick](#ImageMagick)
  * ImageMagick is a free and open-source software suite for displaying, converting, and editing raster image and vector image files.
  * [heap-buffer-overflow in SVGStripString of svg.c #1336](#heap-buffer-overflow in SVGStripString of svg.c #1336)
    * [CVE-2018-18023](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-18023)
  * [heap-buffer-overflow in EncodeImage of pict.c #1335](#heap-buffer-overflow in EncodeImage of pict.c #1335)
    * [CVE-2018-18025](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-18025)
  * [heap-buffer-overflow in MagickCore #1156](#heap-buffer-overflow in MagickCore #1156)
    * [CVE-2018-11625](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11625)

<a name="cJSON">

### Project Name: [cJSON](https://github.com/DaveGamble/cJSON)

<a name="Bug in cJSON.c cJSON_SetNumberHelper #138">

### 1. [Bug in cJSON.c cJSON_SetNumberHelper #138](https://github.com/DaveGamble/cJSON/issues/138)

[**Description**](https://github.com/DaveGamble/cJSON/issues/138)

> cJSON.c line 231 :
> object->valueint = cJSON_Number;
> 
> may be it is type?
> 
> object->type = cJSON_Number;
> object->valueint = number;

[**Patch code:**](https://github.com/DaveGamble/cJSON/commit/ef34500693e8c4a2849d41a4bd66fd19c9ec46c2)

```diff
    {
-        object->valueint = cJSON_Number;
+        object->valueint = (int)number;
    }
```

[**Full function:**](https://github.com/DaveGamble/cJSON/commit/ef34500693e8c4a2849d41a4bd66fd19c9ec46c2)

```c
 /* don't ask me, but the original cJSON_SetNumberValue returns an integer or double */
 CJSON_PUBLIC(double) cJSON_SetNumberHelper(cJSON *object, double number)
 {
     if (number >= INT_MAX)
     {
         object->valueint = INT_MAX;
     }
     else if (number <= INT_MIN)
     {
         object->valueint = INT_MIN;
    }
    else
    {
        object->valueint = (int)number;
    }
     return object->valuedouble = number;
 }
```

**Comments**:

Should be able to discovered by comparing to the output of other JSON parser

---

<a name="Bug in cJSON_AddItemToObject #106">

### 2. [Bug in cJSON_AddItemToObject #106](https://github.com/DaveGamble/cJSON/issues/106)

[**Description**](https://github.com/DaveGamble/cJSON/issues/106)

> In cJSON_AddItemToObject,
>
> /* free old key and set new one */
> if (item->string)
> {
> 	cJSON_free(item->string);
> }
>
> Shouldn't this be:
>
> if (!(item->type & cJSON_StringIsConst) && item->string)
> {
>     cJSON_free(item->string);
> }
>
> Thanks!
> Diego.


[**Patch code:**](https://github.com/DaveGamble/cJSON/commit/702fd95af3408b157167bfd30728c66a212aeae7)

```diff
    /* free old key and set new one */
-    if (item->string)
+    if (!(item->type & cJSON_StringIsConst) && item->string)
```

[**Full function:**](https://github.com/DaveGamble/cJSON/commit/702fd95af3408b157167bfd30728c66a212aeae7)

```c
 void   cJSON_AddItemToObject(cJSON *object, const char *string, cJSON *item)
 {
     if (!item)
     {
         return;
    }
     /* free old key and set new one */
    if (!(item->type & cJSON_StringIsConst) && item->string)
    {
        cJSON_free(item->string);
    }
     item->string = (char*)cJSON_strdup((const unsigned char*)string);
 
     cJSON_AddItemToArray(object,item);
 }
```

**Comments**:

Should be able to discovered given certain input

---

<a name="Invalid pointer returned if reallocate fails in ensure function #189">

### 3. [Invalid pointer returned if reallocate fails in ensure function #189](https://github.com/DaveGamble/cJSON/issues/189)

[**Description**](https://github.com/DaveGamble/cJSON/issues/189)

> Q: The calls to reallocate is assumed to return a valid pointer. If it fails, NULL should be returned instead of newbuffer + p->offset.

> A: This is definitely a bug and most likely also a security issue, since an attacker could make realloc fail at exactly the right moment while also providing a big JSON (big offset), thereby potentially producing a pointer to an arbitrary memory address that will be written to by cJSON later on.


[**Patch code:**](https://github.com/DaveGamble/cJSON/commit/954d61e5e7cb9dc6c480fc28ac1cdceca07dd5bd)

```diff
+        if (newbuffer == NULL)
+        {
+            p->hooks.deallocate(p->buffer);
+            p->length = 0;
+            p->buffer = NULL;
+             return NULL;
+        }
```

[**Full function:**](https://github.com/DaveGamble/cJSON/commit/954d61e5e7cb9dc6c480fc28ac1cdceca07dd5bd)

```c
 /* realloc printbuffer if necessary to have at least "needed" bytes more */
 static unsigned char* ensure(printbuffer * const p, size_t needed)
 {
     unsigned char *newbuffer = NULL;
     size_t newsize = 0;
 
     if ((p == NULL) || (p->buffer == NULL))
     {
         return NULL;
     }
 
     if ((p->length > 0) && (p->offset >= p->length))
     {
         /* make sure that offset is valid */
         return NULL;
     }
 
     if (needed > INT_MAX)
     {
         /* sizes bigger than INT_MAX are currently not supported */
         return NULL;
     }
 
     needed += p->offset + 1;
     if (needed <= p->length)
     {
         return p->buffer + p->offset;
     }
 
     if (p->noalloc) {
         return NULL;
     }
 
     /* calculate new buffer size */
     if (needed > (INT_MAX / 2))
     {
         /* overflow of int, use INT_MAX if possible */
         if (needed <= INT_MAX)
         {
             newsize = INT_MAX;
         }
         else
         {
             return NULL;
         }
     }
     else
     {
         newsize = needed * 2;
     }
 
     if (p->hooks.reallocate != NULL)
    {
        /* reallocate with realloc if available */
        newbuffer = (unsigned char*)p->hooks.reallocate(p->buffer, newsize);
        if (newbuffer == NULL)
        {
            p->hooks.deallocate(p->buffer);
            p->length = 0;
            p->buffer = NULL;
             return NULL;
        }
    }
    else
    {
         /* otherwise reallocate manually */
         newbuffer = (unsigned char*)p->hooks.allocate(newsize);
         if (!newbuffer)
         {
             p->hooks.deallocate(p->buffer);
             p->length = 0;
             p->buffer = NULL;
 
             return NULL;
         }
         if (newbuffer)
         {
             memcpy(newbuffer, p->buffer, p->offset + 1);
         }
         p->hooks.deallocate(p->buffer);
     }
     p->length = newsize;
     p->buffer = newbuffer;
 
     return newbuffer + p->offset;
 }
```

**Comments**:

This is a security issue.

---

<a name="String deallocated before use #248">

### 4. [String deallocated before use #248](https://github.com/DaveGamble/cJSON/issues/248)

[**Description:**](https://github.com/DaveGamble/cJSON/issues/248) 

> add_item_to_object: Fix use-after-free when string is aliased
> 
> If the `string` property of the item that is added is an alias to the
> `string` parameter of `add_item_to_object`, and `constant` is false,
> `cJSON_strdup` would access the string after it has been freed.

[**Patch code:**](https://github.com/FSMaxB/cJSON/commit/22a7d04fa004462e0dca35c3cc7809bea38e65f9)

```diff
static cJSON_bool add_item_to_object(cJSON * const object, const char * const string, cJSON * const item, const internal_hooks * const hooks, const cJSON_bool constant_key)
{
+    char *new_key = NULL;
+    int new_type = cJSON_Invalid;
     if ((object == NULL) || (string == NULL) || (item == NULL))
    {
        return false;
    }
-     if (!(item->type & cJSON_StringIsConst) && (item->string != NULL))
-    {
-        hooks->deallocate(item->string);
-    }
     if (constant_key)
    {
-        item->string = (char*)cast_away_const(string);
-        item->type |= cJSON_StringIsConst;
+        new_key = (char*)cast_away_const(string);
+        new_type = item->type | cJSON_StringIsConst;
    }
    else
    {
-        char *key = (char*)cJSON_strdup((const unsigned char*)string, hooks);
-        if (key == NULL)
+        new_key = (char*)cJSON_strdup((const unsigned char*)string, hooks);
+        if (new_key == NULL)
        {
            return false;
        }
-         item->string = key;
-        item->type &= ~cJSON_StringIsConst;
+        new_type = item->type & ~cJSON_StringIsConst;
    }
+     if (!(item->type & cJSON_StringIsConst) && (item->string != NULL))
+    {
+        hooks->deallocate(item->string);
+    }
+     item->string = new_key;
+    item->type = new_type;
     return add_item_to_array(object, item);
}
```

[**Full function:**](https://github.com/FSMaxB/cJSON/commit/22a7d04fa004462e0dca35c3cc7809bea38e65f9)

```c
// The same as above
```

**Comments**:

This is a security issue

---

<a name="iniparser">

### Project Name: [iniparser](https://github.com/ndevilla/iniparser/)

<a name="Empty string with quotes. #70">

### 1. [Empty string with quotes. #70](https://github.com/ndevilla/iniparser/issues/70)

[**Description:**](https://github.com/ndevilla/iniparser/issues/70) 

> for example:
> ```filter = ""```

> this code can't handle it

```
} else if (sscanf (line, "%[^=] = \"%[^\"]\"", key, value) == 2
       ||  sscanf (line, "%[^=] = '%[^\']'",   key, value) == 2) {
```

> this string will be processed in

```
} else if (sscanf (line, "%[^=] = %[^;#]", key, value) == 2) {
```

> the condition

```
if (!strcmp(value, "\"\"") || (!strcmp(value, "''"))) {
        value[0]=0 ;
}
```

> will not be processed.

> result:
> load = ""
> save = """"
> load = """"
> save = """"""
> etc.

[**Patch code:**](https://github.com/ndevilla/iniparser/commit/54716a77d621373ad3428170af6dacf9f106c264)

```diff
+         sta = LINE_VALUE ;
+     } else if (sscanf (line, "%[^=] = %[^;#]", key, value) == 2) {
+         /* Usual key=value without quotes, with or + without comments */
+         strstrip(key);
+         strlwc(key, key, len);
+         strstrip(value);
        /*
         * sscanf cannot handle '' or "" as empty values
         * this is done here
         */
        if (!strcmp(value, "\"\"") || (!strcmp(value, "''"))) {
            value[0]=0 ;
        }
-        sta = LINE_VALUE ;
-    } else if (sscanf (line, "%[^=] = %[^;#]", key, value) == 2) {
-        /* Usual key=value without quotes, with or without comments */
-        strstrip(key);
-        strlwc(key, key, len);
-        strstrip(value);

```

[**Full function:**](https://github.com/ndevilla/iniparser/commit/54716a77d621373ad3428170af6dacf9f106c264)

```c
 /*-------------------------------------------------------------------------*/
 /**
   @brief    Load a single line from an INI file
   @param    input_line  Input line, may be concatenated multi-line input
   @param    section     Output space to store section
   @param    key         Output space to store key
   @param    value       Output space to store value
   @return   line_status value
  */
 /*--------------------------------------------------------------------------*/
 static line_status iniparser_line(
     const char * input_line,
     char * section,
     char * key,
     char * value)
 {
     line_status sta ;
     char * line = NULL;
     size_t      len ;
 
     line = xstrdup(input_line);
     len = strstrip(line);
 
     sta = LINE_UNPROCESSED ;
     if (len<1) {
         /* Empty line */
         sta = LINE_EMPTY ;
     } else if (line[0]=='#' || line[0]==';') {
         /* Comment line */
         sta = LINE_COMMENT ;
     } else if (line[0]=='[' && line[len-1]==']') {
         /* Section name */
         sscanf(line, "[%[^]]", section);
         strstrip(section);
         strlwc(section, section, len);
         sta = LINE_SECTION ;
     } else if (sscanf (line, "%[^=] = \"%[^\"]\"", key, value) == 2
            ||  sscanf (line, "%[^=] = '%[^\']'",   key, value) == 2) {
         /* Usual key=value with quotes, with or without comments */
        strstrip(key);
        strlwc(key, key, len);
        /* Don't strip spaces from values surrounded with quotes */
        sta = LINE_VALUE ;
    } else if (sscanf (line, "%[^=] = %[^;#]", key, value) == 2) {
        /* Usual key=value without quotes, with or without comments */
        strstrip(key);
        strlwc(key, key, len);
        strstrip(value);
        /*
         * sscanf cannot handle '' or "" as empty values
         * this is done here
         */
        if (!strcmp(value, "\"\"") || (!strcmp(value, "''"))) {
            value[0]=0 ;
        }
        sta = LINE_VALUE ;
    } else if (sscanf (line, "%[^=] = %[^;#]", key, value) == 2) {
        /* Usual key=value without quotes, with or without comments */
        strstrip(key);
        strlwc(key, key, len);
        strstrip(value);
         sta = LINE_VALUE ;
    } else if (sscanf(line, "%[^=] = %[;#]", key, value)==2
           ||  sscanf(line, "%[^=] %[=]", key, value) == 2) {
         /*
          * Special cases:
          * key=
          * key=;
          * key=#
          */
         strstrip(key);
         strlwc(key, key, len);
         value[0]=0 ;
         sta = LINE_VALUE ;
     } else {
         /* Generate syntax error */
         sta = LINE_ERROR ;
     }
 
     free(line);
     return sta ;
 }
```

**Comments**:

---

<a name="http-parser">

## Project Name: [http-parser](https://github.com/nodejs/http-parser/)

<a name="Heap out-of-bounds read in strtoul (68345541)">

### 1. [Heap out-of-bounds read in strtoul (68345541) #408](https://github.com/nodejs/http-parser/issues/408)

[**Description:**](https://github.com/nodejs/http-parser/issues/408) 

> src: fix out-of-bounds read through `strtoul`

> `strtoul` will attempt to lookup the next digit up until it will stumble upon an invalid one. However, for an unterminated string as an input value, this results in out-of-bounds read.

> Remove `strtoul` call, and replace it with simple loop.


[**Patch code:**](https://github.com/nodejs/http-parser/commit/9ce7316de31f90d8485706a1ab8ef623404c2d8c)

```diff
  if (u->field_set & (1 << UF_PORT)) {
-     /* Don't bother with endp; we've already validated the string */
-     unsigned long v = strtoul(buf + u->field_data[UF_PORT] .off, NULL, 10);
-      /* Ports have a max value of 2^16 */
-     if (v > 0xffff) {
-       return 1;
+     uint16_t off;
+     uint16_t len;
+     const char* p;
+     const char* end;
+     unsigned long v;
+      off = u->field_data[UF_PORT].off;
+     len = u->field_data[UF_PORT].len;
+     end = buf + off + len;
+      /* NOTE: The characters are already validated and are in the [0-9] range */
+     assert(off + len <= buflen && "Port number overflow");
+     v = 0;
+     for (p = buf + off; p < end; p++) {
+       v *= 10;
+       v += *p - '0';
+        /* Ports have a max value of 2^16 */
+       if (v > 0xffff) {
+         return 1;
+       }
    }
```

[**Full function:**](https://github.com/nodejs/http-parser/commit/9ce7316de31f90d8485706a1ab8ef623404c2d8c)

```c
 void
 http_parser_url_init(struct http_parser_url *u) {
   memset(u, 0, sizeof(*u));
 }
 
 int
 http_parser_parse_url(const char *buf, size_t buflen, int is_connect,
                       struct http_parser_url *u)
 {
   enum state s;
   const char *p;
   enum http_parser_url_fields uf, old_uf;
   int found_at = 0;
 
   u->port = u->field_set = 0;
   s = is_connect ? s_req_server_start : s_req_spaces_before_url;
   old_uf = UF_MAX;
 
   for (p = buf; p < buf + buflen; p++) {
     s = parse_url_char(s, *p);
 
     /* Figure out the next field that we're operating on */
     switch (s) {
       case s_dead:
         return 1;
 
       /* Skip delimeters */
       case s_req_schema_slash:
       case s_req_schema_slash_slash:
       case s_req_server_start:
       case s_req_query_string_start:
       case s_req_fragment_start:
         continue;
 
       case s_req_schema:
         uf = UF_SCHEMA;
         break;
 
       case s_req_server_with_at:
         found_at = 1;
 
       /* FALLTHROUGH */
       case s_req_server:
         uf = UF_HOST;
         break;
 
       case s_req_path:
         uf = UF_PATH;
         break;
 
       case s_req_query_string:
         uf = UF_QUERY;
         break;
 
       case s_req_fragment:
         uf = UF_FRAGMENT;
         break;
 
       default:
         assert(!"Unexpected state");
         return 1;
     }
 
     /* Nothing's changed; soldier on */
     if (uf == old_uf) {
       u->field_data[uf].len++;
       continue;
     }
 
     u->field_data[uf].off = p - buf;
     u->field_data[uf].len = 1;
 
     u->field_set |= (1 << uf);
     old_uf = uf;
   }
 
   /* host must be present if there is a schema */
   /* parsing http:///toto will fail */
   if ((u->field_set & (1 << UF_SCHEMA)) &&
       (u->field_set & (1 << UF_HOST)) == 0) {
     return 1;
   }
 
   if (u->field_set & (1 << UF_HOST)) {
     if (http_parse_host(buf, u, found_at) != 0) {
       return 1;
     }
   }
 
   /* CONNECT requests can only contain "hostname:port" */
   if (is_connect && u->field_set != ((1 << UF_HOST)|(1 << UF_PORT))) {
     return 1;
  }
   if (u->field_set & (1 << UF_PORT)) {
    /* Don't bother with endp; we've already validated the string */
    unsigned long v = strtoul(buf + u->field_data[UF_PORT].off, NULL, 10);
     /* Ports have a max value of 2^16 */
    if (v > 0xffff) {
      return 1;
    uint16_t off;
    uint16_t len;
    const char* p;
    const char* end;
    unsigned long v;
     off = u->field_data[UF_PORT].off;
    len = u->field_data[UF_PORT].len;
    end = buf + off + len;
     /* NOTE: The characters are already validated and are in the [0-9] range */
    assert(off + len <= buflen && "Port number overflow");
    v = 0;
    for (p = buf + off; p < end; p++) {
      v *= 10;
      v += *p - '0';
       /* Ports have a max value of 2^16 */
      if (v > 0xffff) {
        return 1;
      }
    }
     u->port = (uint16_t) v;
   }
 
   return 0;
 }
```

**Comments**: 

---

<a name="myhtml">

### Project Name: [myhtml](https://github.com/lexborisov/myhtml/)

<a name="fix charef parsing #152">

### 1. [fix charef parsing #152]](https://github.com/lexborisov/myhtml/pull/152)

[**Description**](https://github.com/lexborisov/myhtml/pull/152)

> fix bugs like this:   
> &redirect => ®direct

[**Patch code:**](https://github.com/lexborisov/myhtml/pull/152)

```diff
-    if(named_character_references[pos].codepoints_len)
-        return &named_character_references[pos];
-    else if(result->last_entry) {
+    if(result->last_entry) {
        *offset = result->last_offset;
        return result->last_entry;
    }
    
-    return &named_character_references[pos];
+    return &named_character_references[0];
}
```

[**Full function:**](https://github.com/lexborisov/myhtml/pull/152)

```c
 const charef_entry_t * myhtml_charef_find_by_pos(size_t pos, const char *begin, size_t *offset, size_t size, charef_entry_result_t *result)
 {
     unsigned const char* u_begin = (unsigned const char*)begin;
     
     if(u_begin[*offset] == '&') {
         result->is_done = 1;
         
         if(result->curr_entry->codepoints_len)
             return result->curr_entry;
         else if(result->last_entry) {
             *offset = result->last_offset;
             return result->last_entry;
         }
         
         return &named_character_references[0];
     }
     
     result->is_done = 0;
     
     while (named_character_references[pos].ch)
     {
         if(named_character_references[pos].ch == u_begin[*offset])
         {
             if(u_begin[*offset] == ';') {
                 result->is_done = 1;
                 
                 result->curr_entry = &named_character_references[pos];
                 return result->curr_entry;
             }
             
             (*offset)++;
             
             if(named_character_references[pos].next == 0) {
                 result->is_done = 1;
                 return &named_character_references[pos];
             }
             
             if(*offset >= size)
             {
                 result->curr_entry = &named_character_references[pos];
                 
                 if(named_character_references[pos].codepoints_len) {
                     result->last_offset = *offset;
                     result->last_entry = &named_character_references[pos];
                 }
                 
                 return result->curr_entry;
             }
             
             if(u_begin[*offset] == '&') {
                 result->is_done = 1;
                 result->curr_entry = &named_character_references[pos];
                 
                 if(result->curr_entry->codepoints_len)
                     return result->curr_entry;
                 else if(result->last_entry) {
                     *offset = result->last_offset;
                     return result->last_entry;
                 }
                 
                 return &named_character_references[0];
             }
             
             if(named_character_references[pos].codepoints_len) {
                 result->last_offset = *offset;
                 result->last_entry = &named_character_references[pos];
             }
             
             pos = named_character_references[pos].next;
         }
         else if(u_begin[*offset] > named_character_references[pos].ch) {
             pos++;
         }
         else {
             break;
         }
     }
    
    result->is_done = 1;
    
    if(result->last_entry) {
        *offset = result->last_offset;
        return result->last_entry;
    }
    return &named_character_references[0];
}
```

**Comments**:


---


<a name="json-parser">

### Project Name: [json-parser](https://github.com/udp/json-parser/)

<a name="heap buffer overflow on some inputs #68">

### 1. [heap buffer overflow on some inputs #68](https://github.com/udp/json-parser/issues/68)

[**Description**](https://github.com/udp/json-parser/issues/68)

> Explanation if you need it for your thesis: When json-parser reads a unicode character, it reads 4 or 6 characters immediately without going back around the main loop which usually processes one byte at a time. To prevent this from causing a buffer overrun, there was an error condition if end - state.ptr < 4 to check that 4 bytes were actually available to read. However, this check was performed on the 'u' character of the \uXXXX, which would return >= 4 even if the input truncated at \uXXX. To fix this, the error condition has been changed to end - state.ptr <= 4.

[**Patch code:**](https://github.com/udp/json-parser/commit/b42439a2927a879f40698e4861e727c4265c13e6)

```diff
-                    if (end - state.ptr < 4 || 
+                    if (end - state.ptr <= 4 || 
                        (uc_b1 = hex_value (*++ state.ptr)) == 0xFF ||
                        (uc_b2 = hex_value (*++ state.ptr)) == 0xFF ||
                        (uc_b3 = hex_value (*++ state.ptr)) == 0xFF ||
                         (uc_b4 = hex_value (*++ state.ptr)) == 0xFF)
                     {
                         sprintf (error, "Invalid character value `%c` (at %d:%d)", b, line_and_col);
                         goto e_failed;
                     }
 
                     uc_b1 = (uc_b1 << 4) | uc_b2;
                     uc_b2 = (uc_b3 << 4) | uc_b4;
                     uchar = (uc_b1 << 8) | uc_b2;
 
                    if ((uchar & 0xF800) == 0xD800) {
                        json_uchar uchar2;
                        
                        if (end - state.ptr < 6 || (*++ state.ptr) != '\\' || (*++ state.ptr) != 'u' ||
-                        if (end - state.ptr <= 6 || (*++ state.ptr) != '\\' || (*++ state.ptr) != 'u' ||
+                            (uc_b1 = hex_value (*++ state.ptr)) == 0xFF ||
                            (uc_b2 = hex_value (*++ state.ptr)) == 0xFF ||
```

[**Full function:**](https://github.com/udp/json-parser/blob/b42439a2927a879f40698e4861e727c4265c13e6/json.c#L221)

Too long, omitted, see [here](https://github.com/udp/json-parser/blob/b42439a2927a879f40698e4861e727c4265c13e6/json.c#L221)


**Comments**:


---


<a name="mongoose">

### Project Name: [mongoose](https://github.com/cesanta/mongoose)

<a name="websocket client bug #631">

### 1. [websocket client bug #631](https://github.com/cesanta/mongoose/issues/631)

[**Description**](https://github.com/cesanta/mongoose/issues/631)

> the function mg_http_common_url_parse(...) has a bug，when parse url, such as:
> ws://localhost:8080/ws => host=locahost:8080, path=/ws
> now result is => host=localhost:8080, path=ws (that is error,not leading /)

> the error occur because on the functio,code is:

```
if (*url == '/') {
  url++;     ==> that is error
  break;
}
```

> Fix url path parsing

> The url parser had two bugs:

- `http://example.com` -> `GET // HTTP/1.1`

- `foo://bar/baz` -> path is `"baz"` instead of `"/baz"`

> Now the path returned by  `mg_http_common_url_parse` always starts with `/`.


[**Patch code:**](https://github.com/cesanta/mongoose/commit/29d6c4ac04d4eb5c7eca295a77c8df47fb04f12f)

```diff
@@ -7540,7 +7540,6 @@ static int mg_http_common_url_parse(const char *url, const char *schema,
      return -1;
    }
    if (*url == '/') {
-      url++;
      break;
    }
    if (*url == ':') *port_i = addr_len;
@@ -7632,7 +7631,7 @@ struct mg_connection *mg_connect_http(struct mg_mgr *mgr,
    /* If the port was addred by us, restore the original host. */
    if (port_i >= 0) addr[port_i] = '\0';
-    mg_printf(nc, "%s /%s HTTP/1.1\r\nHost: %s\r\nContent-Length: %" SIZE_T_FMT
+    mg_printf(nc, "%s %s HTTP/1.1\r\nHost: %s\r\nContent-Length: %" SIZE_T_FMT
```

[**Full function:**](https://github.com/cesanta/mongoose/commit/29d6c4ac04d4eb5c7eca295a77c8df47fb04f12f)

```c
 static int mg_http_common_url_parse(const char *url, const char *schema,
                                     const char *schema_tls, int *use_ssl,
                                     char **addr, int *port_i,
                                     const char **path) {
   int addr_len = 0;
 
   if (memcmp(url, schema, strlen(schema)) == 0) {
     url += strlen(schema);
   } else if (memcmp(url, schema_tls, strlen(schema_tls)) == 0) {
     url += strlen(schema_tls);
     *use_ssl = 1;
 #ifndef MG_ENABLE_SSL
     return -1; /* SSL is not enabled, cannot do HTTPS URLs */
 #endif
   }
 
   while (*url != '\0') {
     *addr = (char *) MG_REALLOC(*addr, addr_len + 5 /* space for port too. */);
     if (*addr == NULL) {
       DBG(("OOM"));
      return -1;
    }
    if (*url == '/') {
      url++;
      break;
    }
    if (*url == ':') *port_i = addr_len;
@@ -7632,7 +7631,7 @@ struct mg_connection *mg_connect_http(struct mg_mgr *mgr,
    /* If the port was addred by us, restore the original host. */
    if (port_i >= 0) addr[port_i] = '\0';
     mg_printf(nc, "%s /%s HTTP/1.1\r\nHost: %s\r\nContent-Length: %" SIZE_T_FMT
    mg_printf(nc, "%s %s HTTP/1.1\r\nHost: %s\r\nContent-Length: %" SIZE_T_FMT
                  "\r\n%s\r\n%s",
              post_data == NULL ? "GET" : "POST", path, addr,
              post_data == NULL ? 0 : strlen(post_data),
               extra_headers == NULL ? "" : extra_headers,
               post_data == NULL ? "" : post_data);
   }
 
   MG_FREE(addr);
   return nc;
 }
```

**Comments**:


---


<a name="Firefox">

### Project Name: [Firefox](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5176)

<a name="Iframe injection & content spoofing & scripts execution via json viewer">

### 1. [Iframe injection & content spoofing & scripts execution via json viewer](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5176)

[**Description**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5176)

> The JSON Viewer displays clickable hyperlinks for strings that are parseable as URLs, including "javascript:" links. If a JSON file contains malicious JavaScript script embedded as "javascript:" links, users may be tricked into clicking and running this code in the context of the JSON Viewer. This can allow for the theft of cookies and authorization tokens which are accessible to that context. This vulnerability affects Firefox < 60.

[**Patch code:**](https://bugzilla.mozilla.org/attachment.cgi?id=8957304&action=edit)

```diff
       // Render the value (summary) using Reps library.
       return Rep(Object.assign({}, props, {
         cropLimit: 50,
         noGrip: true,
-        omitLinkHref: false,
+        openLink(str) {
+          try {
+            let u = new URL(str);
+            if (u.protocol == "https:" || u.protocol == "http:") {
+              window.open(str, "_blank");
+            }
+          } catch (ex) { /* the link might be bust, then we do nothing */ }
+        },
       }));
```

[**Full function:**](https://bugzilla.mozilla.org/show_bug.cgi?id=1442840)

```c
// omitted
```

**Comments**:


---


<a name="poco">

### Project Name: [poco](https://github.com/pocoproject/poco)

<a name="Zip Decompress Parent Path Injection #1968">

### 1. [Zip Decompress Parent Path Injection #1968](https://github.com/pocoproject/poco/issues/1968)

[**Description**](https://github.com/pocoproject/poco/issues/1968)

> By manipulation of the Zip input file header, the contents of the zip archive can be written to an arbitrary parent path of the user.

> Expected behavior   
> Throw an exception if filename contains a parent directory reference. isValidPath() (ZipCommon.cpp) should check if the filename contains a tilde character.

> Actual behavior   
> By inserting a tilde-slash (~/) in the filename area of the zip header, files can be written to the user's home directory.

> Steps to reproduce the problem   
> Use the sample-unzip samle application as follows:

```
$ ./sample-unzip -f vuln.zip SOME_OUT_DIR
vuln.zip contains a file foo. foo includes the string bar
```



[**Patch code:**](https://github.com/pocoproject/poco/commit/f5b2cf3dd6976ae53b2f3c9618b0087a0646cc7d)

```diff
Zip/src/Decompress.cpp
@@ -80,7 +80,7 @@ bool Decompress::handleZipEntry(std::istream& zipStream, const ZipLocalFileHeade
		{
			std::string dirName = hdr.getFileName();
			if (!ZipCommon::isValidPath(dirName))
-				throw ZipException("Illegal entry name " + dirName + " containing parent directory reference");
+				throw ZipException("Illegal entry name " + dirName);
			Poco::Path dir(_outDir, dirName);
			dir.makeDirectory();
			Poco::File aFile(dir);
@@ -100,7 +100,7 @@ bool Decompress::handleZipEntry(std::istream& zipStream, const ZipLocalFileHeade
		}
 		if (!ZipCommon::isValidPath(fileName))
-			throw ZipException("Illegal entry name " + fileName + " containing parent directory reference");
+			throw ZipException("Illegal entry name " + fileName);
 		Poco::Path file(fileName);
		file.makeFile();

Zip/src/ZipCommon.cpp
@@ -21,15 +22,26 @@ namespace Zip {
 bool ZipCommon::isValidPath(const std::string& path)
{
+ 	if (!Path(path).isRelative())
+		return false;
+	if (path == "..")
+		return false;
-	if (path.compare(0, 3, "../") == 0)
+	if ((path.size() >= 3) && path.compare(0, 3, "../") == 0)
+		return false;
+	if ((path.size() >= 3) && path.compare(0, 3, "..\\") == 0)
+		return false;
+	if (path.find("/../") != std::string::npos)
+		return false;
+	if (path.find("\\..\\") != std::string::npos)
+		return false;
+	if (path.find("/..\\") != std::string::npos)
		return false;
-	if (path.compare(0, 3, "..\\") == 0)
+	if (path.find("\\../") != std::string::npos)
		return false;
-	if (path.find("/..") != std::string::npos)
+	if ((path.size() >= 2) && path.compare(0, 2, "~/") == 0)
		return false;
-	if (path.find("\\..") != std::string::npos)
+	if (path.size() > 0 && (path[0] == '/' || path[0] == '\\'))
		return false;
	return true;
}
```

[**Full function:**](https://github.com/pocoproject/poco/commit/f5b2cf3dd6976ae53b2f3c9618b0087a0646cc7d)

```c

```

**Comments**:


---


<a name="CImg">

### Project Name: [CImg](https://github.com/dtschump/CImg)

<a name="other testcases lead to heap overflow by loading crafted images #185">

### 1. [other testcases lead to heap overflow by loading crafted images #185](https://github.com/dtschump/CImg/issues/185)

[**Description**](https://github.com/dtschump/CImg/issues/185)

> An issue was discovered in CImg v.220. A heap-based buffer over-read in load_bmp in CImg.h occurs when loading a crafted bmp image, a different vulnerability than CVE-2018-7588. This is in a Monochrome case, aka case 1.

[**Patch code:**]()

```diff
@@ -48331,7 +48331,7 @@ namespace cimg_library_suffixed {
      if (header_size>40) cimg::fseek(nfile,header_size - 40,SEEK_CUR);
       const int
-        dx_bytes = (bpp==1)?(dx/8 + (dx%8?1:0)):((bpp==4)?(dx/2 + (dx%2)):(dx*bpp/8)),
+        dx_bytes = (bpp==1)?(dx/8 + (dx%8?1:0)):((bpp==4)?(dx/2 + (dx%2)):(int)((longT)dx*bpp/8)),
        align_bytes = (4 - dx_bytes%4)%4;
      const ulongT
        cimg_iobuffer = (ulongT)24*1024*1024,
@@ -48363,10 +48363,10 @@ namespace cimg_library_suffixed {
      }
       // Read pixel data
-      assign(dx,cimg::abs(dy),1,3);
+      assign(dx,cimg::abs(dy),1,3,0);
      switch (bpp) {
-      case 1 : { // Monochrome
+        for (int y = height() - 1; y>=0; --y) {
        if (colormap._width>=2) for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
@@ -48384,7 +48384,7 @@ namespace cimg_library_suffixed {
        }
      } break;
      case 4 : { // 16 colors
-        for (int y = height() - 1; y>=0; --y) {
+        if (colormap._width>=16) for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
@@ -48402,8 +48402,8 @@ namespace cimg_library_suffixed {
          ptrs+=align_bytes;
        }
      } break;
-      case 8 : { //  256 colors
-        for (int y = height() - 1; y>=0; --y) {
+      case 8 : { // 256 colors
+        if (colormap._width>=256) for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
```

[**Full function:**](https://github.com/dtschump/CImg/commit/10af1e8c1ad2a58a0a3342a856bae63e8f257abb)

The function is too long, see [here](https://github.com/dtschump/CImg/commit/10af1e8c1ad2a58a0a3342a856bae63e8f257abb)

**Comments**:

---



<a name="ImageMagick">

### Project Name: [ImageMagick](https://github.com/ImageMagick/ImageMagick)

<a name="heap-buffer-overflow in SVGStripString of svg.c #1336">

### 1. [heap-buffer-overflow in SVGStripString of svg.c #1336](https://github.com/ImageMagick/ImageMagick/issues/1336)

[**Description**](https://github.com/ImageMagick/ImageMagick/issues/1336)

In ImageMagick 7.0.8-13 Q16, there is a heap-based buffer over-read in the SVGStripString function of coders/svg.c, which allows attackers to cause a denial of service via a crafted SVG image file.

[**Patch code:**](https://github.com/ImageMagick/ImageMagick6/commit/a5db4873626f702d2ddd8bc293573493e0a412c0)

```diff
      {
        for ( ; *p != '\0'; p++)
          if ((*p == '*') && (*(p+1) == '/'))
-            break;
+            {
+              p+=2;
+              break;
+            }
        if (*p == '\0')
          break;
-        p+=2;
      }
    *q++=(*p);
  }
```

[**Full function:**](https://github.com/ImageMagick/ImageMagick6/commit/a5db4873626f702d2ddd8bc293573493e0a412c0)

```c
 static void SVGStripString(const MagickBooleanType trim,char *message)
 {
   register char
     *p,
     *q;
 
   size_t
     length;
 
   assert(message != (char *) NULL);
   if (*message == '\0')
     return;
   /*
     Remove comment.
   */
   q=message;
   for (p=message; *p != '\0'; p++)
   {
     if ((*p == '/') && (*(p+1) == '*'))
      {
        for ( ; *p != '\0'; p++)
          if ((*p == '*') && (*(p+1) == '/'))
            break;
            {
              p+=2;
              break;
            }
        if (*p == '\0')
          break;
        p+=2;
      }
    *q++=(*p);
  }
   *q='\0';
   if (trim != MagickFalse)
     {
       /*
         Remove whitespace.
       */
       length=strlen(message);
       p=message;
       while (isspace((int) ((unsigned char) *p)) != 0)
         p++;
       if ((*p == '\'') || (*p == '"'))
         p++;
       q=message+length-1;
       while ((isspace((int) ((unsigned char) *q)) != 0) && (q > p))
         q--;
       if (q > p)
         if ((*q == '\'') || (*q == '"'))
           q--;
       (void) memmove(message,p,(size_t) (q-p+1));
       message[q-p+1]='\0';
     }
   /*
     Convert newlines to a space.
   */
   for (p=message; *p != '\0'; p++)
     if (*p == '\n')
       *p=' ';
 }
```

**Comments**:


---

<a name="heap-buffer-overflow in EncodeImage of pict.c #1335">

### 1. [heap-buffer-overflow in EncodeImage of pict.c #1335](https://github.com/ImageMagick/ImageMagick/issues/1335)

[**Description**](https://github.com/ImageMagick/ImageMagick/issues/1335)

In ImageMagick 7.0.8-13 Q16, there is a heap-based buffer over-read in the EncodeImage function of coders/pict.c, which allows attackers to cause a denial of service via a crafted SVG image file.

[**Patch code:**]()

```diff
@@ -444,7 +444,7 @@ static unsigned char *DecodeImage(Image *blob,Image *image,
    bytes_per_line=width;
  row_bytes=(size_t) (image->columns | 0x8000);
  if (image->storage_class == DirectClass)
-    row_bytes=(size_t) (4*(image->columns | 0x8000));
+    row_bytes=(size_t) ((4*image->columns) | 0x8000);
  /*
    Allocate pixel and scanline buffer.
  */
@@ -1778,7 +1778,7 @@ static MagickBooleanType WritePICTImage(const ImageInfo *image_info,
  /*
    Allocate memory.
  */
-  bytes_per_line=image->columns | 0x8000;
+  bytes_per_line=image->columns;
  if (storage_class == DirectClass)
    bytes_per_line*=image->alpha_trait != UndefinedPixelTrait ? 4 : 3;
  buffer=(unsigned char *) AcquireQuantumMemory(PictInfoSize,sizeof(*buffer));
@@ -1799,7 +1799,8 @@ static MagickBooleanType WritePICTImage(const ImageInfo *image_info,
      ThrowWriterException(ResourceLimitError,"MemoryAllocationFailed");
    }
  (void) memset(scanline,0,row_bytes);
-  (void) memset(packed_scanline,0,(size_t) (row_bytes+2*MaxCount));
+  (void) memset(packed_scanline,0,(size_t) (row_bytes+2*MaxCount)*
+    sizeof(*packed_scanline));
  /*
    Write header, header size, size bounding box, version, and reserved.
  */
```

[**Full function:**](https://github.com/ImageMagick/ImageMagick/commit/1a22fc0c8837838e60daecc0bf01648f359dd6fd#diff-9f0be979d8a302c3f34029647fc77cbdR450)

too long, see [here](https://github.com/ImageMagick/ImageMagick/commit/1a22fc0c8837838e60daecc0bf01648f359dd6fd#diff-9f0be979d8a302c3f34029647fc77cbdR450)

**Comments**:


---



<a name="heap-buffer-overflow in MagickCore #1156">


### 1. [heap-buffer-overflow in MagickCore #1156](https://github.com/ImageMagick/ImageMagick/issues/1156)

[**Description**](https://github.com/ImageMagick/ImageMagick/issues/1156)

In ImageMagick 7.0.7-37 Q16, SetGrayscaleImage in the quantize.c file allows attackers to cause a heap-based buffer over-read via a crafted file.

[**Patch code:**]()

```diff
  if (image->type != GrayscaleType)
    (void) TransformImageColorspace(image,GRAYColorspace,exception);
  if (image->storage_class == PseudoClass)
-    colormap_index=(ssize_t *) AcquireQuantumMemory(image->colors,
+    colormap_index=(ssize_t *) AcquireQuantumMemory(image->colors+1,
      sizeof(*colormap_index));
  else
-    colormap_index=(ssize_t *) AcquireQuantumMemory(MaxColormapSize,
+    colormap_index=(ssize_t *) AcquireQuantumMemory(MaxColormapSize+1,
      sizeof(*colormap_index));
  if (colormap_index == (ssize_t *) NULL)
    ThrowBinaryException(ResourceLimitError,"MemoryAllocationFailed",
```

[**Full function:**](https://github.com/ImageMagick/ImageMagick/commit/5294966898532a6bd54699fbf04edf18902513ac#diff-b422c231973548d46a04db74c7cb8e58R3448)

too long, see [here](https://github.com/ImageMagick/ImageMagick/commit/5294966898532a6bd54699fbf04edf18902513ac#diff-b422c231973548d46a04db74c7cb8e58R3448)

**Comments**:


---



<a name="">

### Project Name: []()

### 1. []()

[**Description**]()



[**Patch code:**]()

```diff

```

[**Full function:**]()

```c

```

**Comments**:


---



<a name="">

### Project Name: []()

### 1. []()

[**Description**]()



[**Patch code:**]()

```diff

```

[**Full function:**]()

```c

```

**Comments**:


---



<a name="">

### Project Name: []()

### 1. []()

[**Description**]()



[**Patch code:**]()

```diff

```

[**Full function:**]()

```c

```

**Comments**:


---



<a name="">

### Project Name: []()

### 1. []()

[**Description**]()



[**Patch code:**]()

```diff

```

[**Full function:**]()

```c

```

**Comments**:


---



<a name="">

### Project Name: []()

### 1. []()

[**Description**]()



[**Patch code:**]()

```diff

```

[**Full function:**]()

```c

```

**Comments**:


---