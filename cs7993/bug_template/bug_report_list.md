---
title:
  Bug reports
---

Last updated: 13:00, Nov, 25, 2018

* [cJSON](#cJSON)
  * [Bug in cJSON.c cJSON_SetNumberHelper #138](#Bug in cJSON.c cJSON_SetNumberHelper #138)
  * [Bug in cJSON_AddItemToObject #106](#Bug in cJSON_AddItemToObject #106)
  * [Invalid pointer returned if reallocate fails in ensure function #189](#Invalid pointer returned if reallocate fails in ensure function #189)
  * [String deallocated before use #248](#String deallocated before use #248)
* [ArduinoJson](#ArduinoJson)
  * [Update QuotedString.cpp #81](#Update QuotedString.cpp #81)
    * [CVE-2015-4590](https://nvd.nist.gov/vuln/detail/CVE-2015-4590)
  * [get<String> returns -0 for 0 #808](#get<String> returns -0 for 0 #808)
* [json-parser](#json-parser)
  * [heap buffer overflow on some inputs #68](#heap buffer overflow on some inputs #68)
* [json-c](#json-c)
  * [Empty strings and unicode zero values break json parsing. #53](#Empty strings and unicode zero values break json parsing. #53)
* [jansson](#jansson)
  * Jansson is a C library for encoding, decoding and manipulating JSON data.
  * [Stack exhaustion parsing a JSON file #282](#Stack exhaustion parsing a JSON file #282)
    * [CVE-2016-4425](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-4425)
* [iniparser](#iniparser)
  * ini file parser
  * [Empty string with quotes. #70](#Empty string with quotes. #70)
* [http-parser](#http-parser)
  * [Heap out-of-bounds read in strtoul (68345541)](#Heap out-of-bounds read in strtoul (68345541))
* [myhtml](#myhtml)
  * Fast C/C++ HTML 5 Parser. Using threads.
  * [fix charef parsing #152](#fix charef parsing #152)
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
  * [double free when load bmp image #184](#double free when load bmp image #184)
    * [CVE-2018-7589](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-7589)
  * [a heap overflow when load a bmp image #183](#a heap overflow when load a bmp image #183)
    * [CVE-2018-7588](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-7588)
* [ImageMagick](#ImageMagick)
  * ImageMagick is a free and open-source software suite for displaying, converting, and editing raster image and vector image files.
  * [heap-buffer-overflow in SVGStripString of svg.c #1336](#heap-buffer-overflow in SVGStripString of svg.c #1336)
    * [CVE-2018-18023](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-18023)
  * [heap-buffer-overflow in EncodeImage of pict.c #1335](#heap-buffer-overflow in EncodeImage of pict.c #1335)
    * [CVE-2018-18025](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-18025)
  * [heap-buffer-overflow in MagickCore #1156](#heap-buffer-overflow in MagickCore #1156)
    * [CVE-2018-11625](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-11625)
  * [heap-buffer-overflow #1009](#heap-buffer-overflow #1009)
    * [CVE-2018-9135](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-9135)
  * [Stack over-read in MagickCore/accelerate.c due to type mismatch #967](#Stack over-read in MagickCore/accelerate.c due to type mismatch #967)
    * [CVE-2018-6930](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-6930)
  * [out-of-bounds read in coders/sun.c:582:57 #375](#out-of-bounds read in coders/sun.c:582:57 #375)
    * [CVE-2017-6500](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-6500)
* [FFmpeg](#FFmpeg)
  * FFmpeg is a collection of libraries and tools to process multimedia content such as audio, video, subtitles and related metadata.
  * [integer overflow and out of array access](#integer overflow and out of array access)
    * [CVE-2018-1999011](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1999011)
  * [Fix multiple runtime error: index 256 out of bounds](#Fix multiple runtime error: index 256 out of bounds)
    * [CVE-2017-9995](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-9995)
  * [http: make length/offset-related variables unsigned.](#http: make length/offset-related variables unsigned.)
    * [CVE-2016-10190](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-10190)
  * [FFmpeg before 2017-01-24 has an out-of-bounds write caused by a heap-based buffer overflow](#FFmpeg before 2017-01-24 has an out-of-bounds write caused by a heap-based buffer overflow)
    * [CVE-2017-7865](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-7865)
  * [FFmpeg before 2017-01-23 has an out-of-bounds write caused by a stack-based buffer overflow](#FFmpeg before 2017-01-23 has an out-of-bounds write caused by a stack-based buffer overflow)
    * [CVE-2017-7866](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-7866)
* [OpenCV](#OpenCV)
  * [Out of bounds write causes Segmentation Fault #9723](#Out of bounds write causes Segmentation Fault #9723)
    * [CVE-2017-1000450](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-1000450)
  * [A heap based buffer overflow happens in cv::Jpeg2KDecoder::readComponent8u #10541](#A heap based buffer overflow happens in cv::Jpeg2KDecoder::readComponent8u #10541)
    * [CVE-2018-5268](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-5268)

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

### 1. [fix charef parsing #152](https://github.com/lexborisov/myhtml/pull/152)

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
      break;
    }
    if (*url == ':') *port_i = addr_len;
@@ -7632,7 +7631,7 @@ struct mg_connection *mg_connect_http(struct mg_mgr *mgr,
    /* If the port was addred by us, restore the original host. */
    if (port_i >= 0) addr[port_i] = '\0';
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

see [here](https://github.com/pocoproject/poco/commit/f5b2cf3dd6976ae53b2f3c9618b0087a0646cc7d)

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

<a name="double free when load bmp image #184">

### 2. [double free when load bmp image #184](https://github.com/dtschump/CImg/issues/184)

[**Description**](https://github.com/dtschump/CImg/issues/184)

An issue was discovered in CImg v.220. A double free in load_bmp in CImg.h occurs when loading a crafted bmp image.

[**Patch code:**](https://github.com/dtschump/CImg/commit/8447076ef22322a14a0ce130837e44c5ba8095f4)

```diff
@@ -48333,9 +48333,9 @@ namespace cimg_library_suffixed {
      const int
        dx_bytes = (bpp==1)?(dx/8 + (dx%8?1:0)):((bpp==4)?(dx/2 + (dx%2)):(dx*bpp/8)),
        align_bytes = (4 - dx_bytes%4)%4;
-      const longT
-        cimg_iobuffer = (longT)24*1024*1024,
-        buf_size = std::min((longT)cimg::abs(dy)*(dx_bytes + align_bytes),(longT)file_size - offset);
+      const ulongT
+        cimg_iobuffer = (ulongT)24*1024*1024,
+        buf_size = std::min((ulongT)cimg::abs(dy)*(dx_bytes + align_bytes),(ulongT)file_size - offset);
       CImg<intT> colormap;
      if (bpp<16) { if (!nb_colors) nb_colors = 1<<bpp; } else nb_colors = 0;
@@ -48368,7 +48368,7 @@ namespace cimg_library_suffixed {
      case 1 : { // Monochrome
        for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
-            cimg::fread(ptrs=buffer._data,dx_bytes,nfile);
+            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
          }
          unsigned char mask = 0x80, val = 0;
@@ -48386,7 +48386,7 @@ namespace cimg_library_suffixed {
      case 4 : { // 16 colors
        for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
-            cimg::fread(ptrs=buffer._data,dx_bytes,nfile);
+            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
          }
          unsigned char mask = 0xF0, val = 0;
@@ -48405,7 +48405,7 @@ namespace cimg_library_suffixed {
      case 8 : { //  256 colors
        for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
-            cimg::fread(ptrs=buffer._data,dx_bytes,nfile);
+            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
          }
          cimg_forX(*this,x) {
@@ -48420,7 +48420,7 @@ namespace cimg_library_suffixed {
      case 16 : { // 16 bits colors
        for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
-            cimg::fread(ptrs=buffer._data,dx_bytes,nfile);
+            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
          }
          cimg_forX(*this,x) {
@@ -48436,7 +48436,7 @@ namespace cimg_library_suffixed {
      case 24 : { // 24 bits colors
        for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
-            cimg::fread(ptrs=buffer._data,dx_bytes,nfile);
+            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
          }
          cimg_forX(*this,x) {
@@ -48450,7 +48450,7 @@ namespace cimg_library_suffixed {
      case 32 : { // 32 bits colors
        for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
-            cimg::fread(ptrs=buffer._data,dx_bytes,nfile);
+            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
          }
          cimg_forX(*this,x) {
```

[**Full function:**](https://github.com/dtschump/CImg/commit/8447076ef22322a14a0ce130837e44c5ba8095f4)

too long, see [here](https://github.com/dtschump/CImg/commit/8447076ef22322a14a0ce130837e44c5ba8095f4)

**Comments**:

---

<a name="a heap overflow when load a bmp image #183">

### 3. [a heap overflow when load a bmp image #183]()

[**Description**](https://github.com/dtschump/CImg/issues/183)

An issue was discovered in CImg v.220. A heap-based buffer over-read in load_bmp in CImg.h occurs when loading a crafted bmp image.

[**Patch code:**](https://github.com/dtschump/CImg/commit/8447076ef22322a14a0ce130837e44c5ba8095f4)

```diff
@@ -48333,9 +48333,9 @@ namespace cimg_library_suffixed {
      const int
        dx_bytes = (bpp==1)?(dx/8 + (dx%8?1:0)):((bpp==4)?(dx/2 + (dx%2)):(dx*bpp/8)),
        align_bytes = (4 - dx_bytes%4)%4;
-      const longT
-        cimg_iobuffer = (longT)24*1024*1024,
-        buf_size = std::min((longT)cimg::abs(dy)*(dx_bytes + align_bytes),(longT)file_size - offset);
+      const ulongT
+        cimg_iobuffer = (ulongT)24*1024*1024,
+        buf_size = std::min((ulongT)cimg::abs(dy)*(dx_bytes + align_bytes),(ulongT)file_size - offset);
       CImg<intT> colormap;
      if (bpp<16) { if (!nb_colors) nb_colors = 1<<bpp; } else nb_colors = 0;
@@ -48368,7 +48368,7 @@ namespace cimg_library_suffixed {
      case 1 : { // Monochrome
        for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
-            cimg::fread(ptrs=buffer._data,dx_bytes,nfile);
+            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
          }
          unsigned char mask = 0x80, val = 0;
@@ -48386,7 +48386,7 @@ namespace cimg_library_suffixed {
      case 4 : { // 16 colors
        for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
-            cimg::fread(ptrs=buffer._data,dx_bytes,nfile);
+            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
          }
          unsigned char mask = 0xF0, val = 0;
@@ -48405,7 +48405,7 @@ namespace cimg_library_suffixed {
      case 8 : { //  256 colors
        for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
-            cimg::fread(ptrs=buffer._data,dx_bytes,nfile);
+            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
          }
          cimg_forX(*this,x) {
@@ -48420,7 +48420,7 @@ namespace cimg_library_suffixed {
      case 16 : { // 16 bits colors
        for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
-            cimg::fread(ptrs=buffer._data,dx_bytes,nfile);
+            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
          }
          cimg_forX(*this,x) {
@@ -48436,7 +48436,7 @@ namespace cimg_library_suffixed {
      case 24 : { // 24 bits colors
        for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
-            cimg::fread(ptrs=buffer._data,dx_bytes,nfile);
+            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
          }
          cimg_forX(*this,x) {
@@ -48450,7 +48450,7 @@ namespace cimg_library_suffixed {
      case 32 : { // 32 bits colors
        for (int y = height() - 1; y>=0; --y) {
          if (buf_size>=cimg_iobuffer) {
-            cimg::fread(ptrs=buffer._data,dx_bytes,nfile);
+            if (!cimg::fread(ptrs=buffer._data,dx_bytes,nfile)) break;
            cimg::fseek(nfile,align_bytes,SEEK_CUR);
          }
          cimg_forX(*this,x) {
```

[**Full function:**](https://github.com/dtschump/CImg/commit/8447076ef22322a14a0ce130837e44c5ba8095f4)

too long, see [here](https://github.com/dtschump/CImg/commit/8447076ef22322a14a0ce130837e44c5ba8095f4)

**Comments**:

---

<a name="ImageMagick">

### Project Name: [ImageMagick](https://github.com/ImageMagick/ImageMagick)

<a name="heap-buffer-overflow in SVGStripString of svg.c #1336">

### 1. [heap-buffer-overflow in SVGStripString of svg.c #1336](https://github.com/ImageMagick/ImageMagick/issues/1336)

[**Description**](https://github.com/ImageMagick/ImageMagick/issues/1336)

> In ImageMagick 7.0.8-13 Q16, there is a heap-based buffer over-read in the SVGStripString function of coders/svg.c, which allows attackers to cause a denial of service via a crafted SVG image file.

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
            {
              p+=2;
              break;
            }
        if (*p == '\0')
          break;
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

### 2. [heap-buffer-overflow in EncodeImage of pict.c #1335](https://github.com/ImageMagick/ImageMagick/issues/1335)

[**Description**](https://github.com/ImageMagick/ImageMagick/issues/1335)

> In ImageMagick 7.0.8-13 Q16, there is a heap-based buffer over-read in the EncodeImage function of coders/pict.c, which allows attackers to cause a denial of service via a crafted SVG image file.

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


### 3. [heap-buffer-overflow in MagickCore #1156](https://github.com/ImageMagick/ImageMagick/issues/1156)

[**Description**](https://github.com/ImageMagick/ImageMagick/issues/1156)

> In ImageMagick 7.0.7-37 Q16, SetGrayscaleImage in the quantize.c file allows attackers to cause a heap-based buffer over-read via a crafted file.

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

<a name="heap-buffer-overflow #1009">

### 4. [heap-buffer-overflow #1009](https://github.com/ImageMagick/ImageMagick/issues/1009)

[**Description**](https://github.com/ImageMagick/ImageMagick/issues/1009)

In ImageMagick 7.0.7-24 Q16, there is a heap-based buffer over-read in IsWEBPImageLossless in coders/webp.c.

[**Patch code:**](https://github.com/ImageMagick/ImageMagick/commit/4f7196b0b7539b113f2580b6a77aa496813d8899)

```diff
@@ -181,6 +181,8 @@ static MagickBooleanType IsWEBPImageLossless(const unsigned char *stream,
  /*
    Read simple header.
  */
+  if (length <= VP8_CHUNK_INDEX)
+    return(MagickFalse);
```

[**Full function:**](https://github.com/ImageMagick/ImageMagick/commit/4f7196b0b7539b113f2580b6a77aa496813d8899)

```c
 static MagickBooleanType IsWEBPImageLossless(const unsigned char *stream,
   const size_t length)
 {
 #define VP8_CHUNK_INDEX  15
 #define LOSSLESS_FLAG  'L'
 #define EXTENDED_HEADER  'X'
 #define VP8_CHUNK_HEADER  "VP8"
 #define VP8_CHUNK_HEADER_SIZE  3
 #define RIFF_HEADER_SIZE  12
 #define VP8X_CHUNK_SIZE  10
 #define TAG_SIZE  4
 #define CHUNK_SIZE_BYTES  4
 #define CHUNK_HEADER_SIZE  8
 #define MAX_CHUNK_PAYLOAD  (~0U-CHUNK_HEADER_SIZE-1)
 
   ssize_t
     offset;
 
  /*
    Read simple header.
  */
  if (length <= VP8_CHUNK_INDEX)
    return(MagickFalse);
  if (stream[VP8_CHUNK_INDEX] != EXTENDED_HEADER)
    return(stream[VP8_CHUNK_INDEX] == LOSSLESS_FLAG ? MagickTrue : MagickFalse);
  /*
     Read extended header.
   */
   offset=RIFF_HEADER_SIZE+TAG_SIZE+CHUNK_SIZE_BYTES+VP8X_CHUNK_SIZE;
   while (offset <= (ssize_t) (length-TAG_SIZE))
   {
     uint32_t
       chunk_size,
       chunk_size_pad;
 
     chunk_size=ReadWebPLSBWord(stream+offset+TAG_SIZE);
     if (chunk_size > MAX_CHUNK_PAYLOAD)
       break;
     chunk_size_pad=(CHUNK_HEADER_SIZE+chunk_size+1) & ~1;
     if (memcmp(stream+offset,VP8_CHUNK_HEADER,VP8_CHUNK_HEADER_SIZE) == 0)
       return(*(stream+offset+VP8_CHUNK_HEADER_SIZE) == LOSSLESS_FLAG ?
         MagickTrue : MagickFalse);
     offset+=chunk_size_pad;
   }
   return(MagickFalse);
 }
```

**Comments**:

---

<a name="Stack over-read in MagickCore/accelerate.c due to type mismatch #967">

### 5. [Stack over-read in MagickCore/accelerate.c due to type mismatch #967](#Stack over-read in MagickCore/accelerate.c due to type mismatch #967)

[**Description**](https://github.com/ImageMagick/ImageMagick/issues/967)

A stack-based buffer over-read in the ComputeResizeImage function in the MagickCore/accelerate.c file of ImageMagick 7.0.7-22 allows a remote attacker to cause a denial of service (application crash) via a maliciously crafted pict file.

[**Patch code:**](https://github.com/ImageMagick/ImageMagick/commit/6aa7d5d9a39b6d42a4f6c7eacd6ad2169b68fc4f)

```diff
@@ -4325,7 +4325,7 @@ static Image *ComputeResizeImage(const Image* image,MagickCLEnv clEnv,
  for (i = 0; i < 7; i++)
    coefficientBuffer[i]=(float) resizeFilterCoefficient[i];
  cubicCoefficientsBuffer=CreateOpenCLBuffer(device,CL_MEM_COPY_HOST_PTR |
-    CL_MEM_READ_ONLY,7*sizeof(*cubicCoefficientsBuffer),&coefficientBuffer);
+    CL_MEM_READ_ONLY,sizeof(coefficientBuffer),&coefficientBuffer);
```

[**Full function:**](https://github.com/ImageMagick/ImageMagick/commit/6aa7d5d9a39b6d42a4f6c7eacd6ad2169b68fc4f)

too long, see [here](https://github.com/ImageMagick/ImageMagick/commit/6aa7d5d9a39b6d42a4f6c7eacd6ad2169b68fc4f#diff-8368336e30a67e0e3c22fec282b6baccR4263), it has a lot of comparisons.

**Comments**:


---

<a name="ArduinoJson">

### Project Name: [ArduinoJson](https://github.com/bblanchon/ArduinoJson)


<a name="Update QuotedString.cpp #81">

### 1. [Update QuotedString.cpp #81](https://github.com/bblanchon/ArduinoJson/pull/81)

[**Description**](https://github.com/bblanchon/ArduinoJson/pull/81)

> The extractFrom function in Internals/QuotedString.cpp in Arduino JSON before 4.5 allows remote attackers to cause a denial of service (crash) via a JSON string with a \ (backslash) followed by a terminator, as demonstrated by "\\\0", which triggers a buffer overflow and over-read.

[**Patch code:**](https://github.com/bblanchon/ArduinoJson/commit/5e7b9ec688d79e7b16ec7064e1d37e8481a31e72)

```diff
@@ -58,46 +58,44 @@ static char unescapeChar(char c) {
static inline bool isQuote(char c) { return c == '\"' || c == '\''; }
- char *QuotedString::extractFrom(char *input, char **endPtr) {
-  char firstChar = *input;
-   if (!isQuote(firstChar)) {
-    // must start with a quote
-    return NULL;
-  }
-   char stopChar = firstChar;  // closing quote is the same as opening quote
   char *startPtr = input + 1;  // skip the quote
  char *readPtr = startPtr;
  char *writePtr = startPtr;
  char c;
+   char firstChar = *input;
+  char stopChar = firstChar;  // closing quote is the same as opening quote
+   if (!isQuote(firstChar)) goto ERROR_OPENING_QUOTE_MISSING;
   for (;;) {
    c = *readPtr++;
-     if (c == '\0') {
-      // premature ending
-      return NULL;
-    }
+    if (c == '\0') goto ERROR_CLOSING_QUOTE_MISSING;
-     if (c == stopChar) {
-      // closing quote
-      break;
-    }
+    if (c == stopChar) goto SUCCESS;
     if (c == '\\') {
      // replace char
      c = unescapeChar(*readPtr++);
+      if (c == '\0') goto ERROR_ESCAPE_SEQUENCE_INTERRUPTED;
    }
     *writePtr++ = c;
  }
+ SUCCESS:
  // end the string here
  *writePtr = '\0';
   // update end ptr
  *endPtr = readPtr;
+   // return pointer to unquoted string
  return startPtr;
+ ERROR_OPENING_QUOTE_MISSING:
+ ERROR_CLOSING_QUOTE_MISSING:
+ ERROR_ESCAPE_SEQUENCE_INTERRUPTED:
+   return NULL;
}
```

[**Full function:**](https://github.com/bblanchon/ArduinoJson/commit/5e7b9ec688d79e7b16ec7064e1d37e8481a31e72)

```c
char *QuotedString::extractFrom(char *input, char **endPtr) {
  char firstChar = *input;
   if (!isQuote(firstChar)) {
    // must start with a quote
    return NULL;
  }
   char stopChar = firstChar;  // closing quote is the same as opening quote
   char *startPtr = input + 1;  // skip the quote
  char *readPtr = startPtr;
  char *writePtr = startPtr;
  char c;
   for (;;) {
    c = *readPtr++;
     if (c == '\0') {
      // premature ending
      return NULL;
    }
     if (c == stopChar) {
      // closing quote
      break;
    }
     if (c == '\\') {
      // replace char
      c = unescapeChar(*readPtr++);
    }
     *writePtr++ = c;
  }
  // end the string here
  *writePtr = '\0';
   // update end ptr
  *endPtr = readPtr;
  return startPtr;
}
```

**Comments**:


---



<a name="get<String> returns -0 for 0 #808">

### 2. [get<String> returns -0 for 0 #808](https://github.com/bblanchon/ArduinoJson/issues/808)

[**Description**](https://github.com/bblanchon/ArduinoJson/issues/808)

> get<String> returns different outputs of 0 for v6.3.0-beta and v6.2.3-beta. In case of v6.3.0-beta it returns "-0" (minus occurs before 0), but in case of v6.2.3-beta it returns "0".

> Example:

```
char json[] = "{\"x\":0}";
StaticJsonDocument<256> doc;
deserializeJson(doc, json);
JsonObject object = doc.as<JsonObject>();
obj["x_str"] = object.get<String>("x");
obj["x_uint"] = object.get<unsigned int>("x");
```

> Output in case of v6.3.0-beta:

```
x_str = "-0"
x_uint = 0
```

> Output in case of v6.2.3-beta:

```
x_str = "0"
x_uint = 0
```

[**Patch code:**](https://github.com/bblanchon/ArduinoJson/commit/98c8e8e35a19c7b41ca7b97008867f98415480bc)

```diff
@@ -30,13 +30,6 @@ struct JsonVariantData {
    content.asFloat = value;
  }
-   void setInteger(JsonInteger value) {
-    if (value > 0)
-      setPostiveInteger(static_cast<JsonUInt>(value));
-    else
-      setNegativeInteger(static_cast<JsonUInt>(-value));
-  }
   void setNegativeInteger(JsonUInt value) {
    type = JSON_NEGATIVE_INTEGER;
    content.asInteger = value;
```

[**Full function:**](https://github.com/bblanchon/ArduinoJson/commit/98c8e8e35a19c7b41ca7b97008867f98415480bc)

```c
  void setInteger(JsonInteger value) {
    if (value > 0)
      setPostiveInteger(static_cast<JsonUInt>(value));
    else
      setNegativeInteger(static_cast<JsonUInt>(-value));
  }
```

**Comments**:


---

<a name="out-of-bounds read in coders/sun.c:582:57 #375">

### 1. [out-of-bounds read in coders/sun.c:582:57 #375](https://github.com/ImageMagick/ImageMagick/issues/375)

[**Description**](https://github.com/ImageMagick/ImageMagick/issues/375)

An issue was discovered in ImageMagick 6.9.7. A specially crafted sun file triggers a heap-based buffer over-read.

[**Patch code:**](https://github.com/ImageMagick/ImageMagick/commit/3007531bfd326c5c1e29cd41d2cd80c166de8528)

```diff
@@ -458,7 +458,7 @@ static Image *ReadSUNImage(const ImageInfo *image_info,ExceptionInfo *exception)
        ThrowReaderException(ResourceLimitError,"ImproperImageHeader");
      }
    pixels_length=height*bytes_per_line;
    sun_pixels=(unsigned char *) AcquireQuantumMemory(pixels_length,
    sun_pixels=(unsigned char *) AcquireQuantumMemory(pixels_length+image->rows,
```

[**Full function:**](https://github.com/ImageMagick/ImageMagick/commit/3007531bfd326c5c1e29cd41d2cd80c166de8528)

too long, see [here](https://github.com/ImageMagick/ImageMagick/commit/3007531bfd326c5c1e29cd41d2cd80c166de8528#diff-faffa511c4f3a41db200d63cb3cadd9bR303)

**Comments**:


---


<a name="FFmpeg">

### Project Name: [FFmpeg](https://github.com/FFmpeg/FFmpeg)

<a name="integer overflow and out of array access">

### 1. [integer overflow and out of array access](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1999011)

[**Description**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1999011)

> Buffer Overflow vulnerability in asf_o format demuxer that can result in heap-buffer-overflow that may result in remote code execution. This attack appears to be exploitable via specially crafted ASF file that has to be provided as input to FFmpeg.

[**Patch code:**](https://github.com/FFmpeg/FFmpeg/commit/2b46ebdbff1d8dec7a3d8ea280a612b91a582869)

```diff
@@ -706,7 +706,8 @@ static int parse_video_info(AVIOContext *pb, AVStream *st)
    st->codecpar->codec_id  = ff_codec_get_id(ff_codec_bmp_tags, tag);
    size_bmp = FFMAX(size_asf, size_bmp);
-    if (size_bmp > BMP_HEADER_SIZE) {
+    if (size_bmp > BMP_HEADER_SIZE &&
+        size_bmp < INT_MAX - AV_INPUT_BUFFER_PADDING_SIZE) {
        int ret;
        st->codecpar->extradata_size  = size_bmp - BMP_HEADER_SIZE;
        if (!(st->codecpar->extradata = av_malloc(st->codecpar->extradata_size +
```

[**Full function:**](https://github.com/FFmpeg/FFmpeg/commit/2b46ebdbff1d8dec7a3d8ea280a612b91a582869)

```c
 static int parse_video_info(AVIOContext *pb, AVStream *st)
 {
     uint16_t size_asf; // ASF-specific Format Data size
     uint32_t size_bmp; // BMP_HEADER-specific Format Data size
     unsigned int tag;
 
     st->codecpar->width  = avio_rl32(pb);
     st->codecpar->height = avio_rl32(pb);
     avio_skip(pb, 1); // skip reserved flags
     size_asf = avio_rl16(pb);
     tag = ff_get_bmp_header(pb, st, &size_bmp);
     st->codecpar->codec_tag = tag;
    st->codecpar->codec_id  = ff_codec_get_id(ff_codec_bmp_tags, tag);
    size_bmp = FFMAX(size_asf, size_bmp);
    if (size_bmp > BMP_HEADER_SIZE &&
        size_bmp < INT_MAX - AV_INPUT_BUFFER_PADDING_SIZE) {
        int ret;
        st->codecpar->extradata_size  = size_bmp - BMP_HEADER_SIZE;
        if (!(st->codecpar->extradata = av_malloc(st->codecpar->extradata_size +
                                                AV_INPUT_BUFFER_PADDING_SIZE))) {
             st->codecpar->extradata_size = 0;
             return AVERROR(ENOMEM);
         }
         memset(st->codecpar->extradata + st->codecpar->extradata_size , 0,
                AV_INPUT_BUFFER_PADDING_SIZE);
         if ((ret = avio_read(pb, st->codecpar->extradata,
                              st->codecpar->extradata_size)) < 0)
             return ret;
     }
     return 0;
 }
```

**Comments**:


---



<a name="Fix multiple runtime error: index 256 out of bounds">

### 2. [Fix multiple runtime error: index 256 out of bounds](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-9995)

[**Description**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-9995)

libavcodec/scpr.c in FFmpeg 3.3 before 3.3.1 does not properly validate height and width data, which allows remote attackers to cause a denial of service (heap-based buffer overflow and application crash) or possibly have unspecified other impact via a crafted file.


[**Patch code:**](https://github.com/FFmpeg/FFmpeg/commit/2171dfae8c065878a2e130390eb78cf2947a5b69)

```diff
+    if (x >= 16 || c >= 256) {
+        return AVERROR_INVALIDDATA;
+    }
```

[**Full function:**](https://github.com/FFmpeg/FFmpeg/commit/2171dfae8c065878a2e130390eb78cf2947a5b69)

```c
 static int decode_unit(SCPRContext *s, PixelModel *pixel, unsigned step, unsigned *rval)
 {
     GetByteContext *gb = &s->gb;
     RangeCoder *rc = &s->rc;
     unsigned totfr = pixel->total_freq;
     unsigned value, x = 0, cumfr = 0, cnt_x = 0;
     int i, j, ret, c, cnt_c;
 
     if ((ret = s->get_freq(rc, totfr, &value)) < 0)
         return ret;
 
     while (x < 16) {
         cnt_x = pixel->lookup[x];
         if (value >= cumfr + cnt_x)
             cumfr += cnt_x;
         else
             break;
         x++;
     }
 
     c = x * 16;
     cnt_c = 0;
     while (c < 256) {
         cnt_c = pixel->freq[c];
         if (value >= cumfr + cnt_c)
             cumfr += cnt_c;
         else
            break;
        c++;
    }
    if (x >= 16 || c >= 256) {
        return AVERROR_INVALIDDATA;
    }
     if ((ret = s->decode(gb, rc, cumfr, cnt_c, totfr)) < 0)
        return ret;
 
     pixel->freq[c] = cnt_c + step;
     pixel->lookup[x] = cnt_x + step;
     totfr += step;
     if (totfr > BOT) {
         totfr = 0;
         for (i = 0; i < 256; i++) {
             unsigned nc = (pixel->freq[i] >> 1) + 1;
             pixel->freq[i] = nc;
             totfr += nc;
         }
         for (i = 0; i < 16; i++) {
             unsigned sum = 0;
             unsigned i16_17 = i << 4;
             for (j = 0; j < 16; j++)
                 sum += pixel->freq[i16_17 + j];
             pixel->lookup[i] = sum;
         }
     }
     pixel->total_freq = totfr;
 
     *rval = c & s->cbits;
 
     return 0;
 }
```

**Comments**:


---



<a name="http: make length/offset-related variables unsigned.">

### 3. [http: make length/offset-related variables unsigned.](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-10190)

[**Description**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-10190)

Heap-based buffer overflow in libavformat/http.c in FFmpeg before 2.8.10, 3.0.x before 3.0.5, 3.1.x before 3.1.6, and 3.2.x before 3.2.2 allows remote web servers to execute arbitrary code via a negative chunk size in an HTTP response.

[**Patch code:**](https://github.com/FFmpeg/FFmpeg/commit/2a05c8f813de6f2278827734bf8102291e7484aa)

Too many files edited, see [here](https://github.com/FFmpeg/FFmpeg/commit/2a05c8f813de6f2278827734bf8102291e7484aa)

[**Full function:**](https://github.com/FFmpeg/FFmpeg/commit/2a05c8f813de6f2278827734bf8102291e7484aa)

Too many files edited, see [here](https://github.com/FFmpeg/FFmpeg/commit/2a05c8f813de6f2278827734bf8102291e7484aa)

**Comments**:


---

<a name="FFmpeg before 2017-01-24 has an out-of-bounds write caused by a heap-based buffer overflow">

### 4. [FFmpeg before 2017-01-24 has an out-of-bounds write caused by a heap-based buffer overflow]()

[**Description**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-7865)

FFmpeg before 2017-01-24 has an out-of-bounds write caused by a heap-based buffer overflow related to the ipvideo_decode_block_opcode_0xA function in libavcodec/interplayvideo.c and the avcodec_align_dimensions2 function in libavcodec/utils.c.

[**Patch code:**](https://github.com/FFmpeg/FFmpeg/commit/2080bc33717955a0e4268e738acf8c1eeddbf8cb)

```diff
@@ -376,6 +376,10 @@ void avcodec_align_dimensions2(AVCodecContext *s, int *width, int *height,
            w_align = 4;
            h_align = 4;
        }
+        if (s->codec_id == AV_CODEC_ID_INTERPLAY_VIDEO) {
+            w_align = 8;
+            h_align = 8;
+        }
        break;
    case AV_PIX_FMT_PAL8:
    case AV_PIX_FMT_BGR8:
@@ -385,7 +389,8 @@ void avcodec_align_dimensions2(AVCodecContext *s, int *width, int *height,
            w_align = 4;
            h_align = 4;
        }
-        if (s->codec_id == AV_CODEC_ID_JV) {
+        if (s->codec_id == AV_CODEC_ID_JV ||
+            s->codec_id == AV_CODEC_ID_INTERPLAY_VIDEO) {
            w_align = 8;
            h_align = 8;
        }
```

[**Full function:**](https://github.com/FFmpeg/FFmpeg/commit/2080bc33717955a0e4268e738acf8c1eeddbf8cb#diff-d7031e4f689033d5546668b25eb9dd30R260)

too long, see [here](https://github.com/FFmpeg/FFmpeg/commit/2080bc33717955a0e4268e738acf8c1eeddbf8cb#diff-d7031e4f689033d5546668b25eb9dd30R260), it has a lot of comparisons.

**Comments**:


---

<a name="FFmpeg before 2017-01-23 has an out-of-bounds write caused by a stack-based buffer overflow">

### 5. [FFmpeg before 2017-01-23 has an out-of-bounds write caused by a stack-based buffer overflow]()

[**Description**](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-7866)

FFmpeg before 2017-01-23 has an out-of-bounds write caused by a stack-based buffer overflow related to the decode_zbuf function in libavcodec/pngdec.c.
References

[**Patch code:**](https://github.com/FFmpeg/FFmpeg/commit/e371f031b942d73e02c090170975561fabd5c264)

```diff
@@ -437,13 +437,13 @@ static int decode_zbuf(AVBPrint *bp, const uint8_t *data,
    av_bprint_init(bp, 0, -1);
     while (zstream.avail_in > 0) {
-        av_bprint_get_buffer(bp, 1, &buf, &buf_size);
-        if (!buf_size) {
+        av_bprint_get_buffer(bp, 2, &buf, &buf_size);
+        if (buf_size < 2) {
            ret = AVERROR(ENOMEM);
            goto fail;
        }
        zstream.next_out  = buf;
-        zstream.avail_out = buf_size;
+        zstream.avail_out = buf_size - 1;
        ret = inflate(&zstream, Z_PARTIAL_FLUSH);
        if (ret != Z_OK && ret != Z_STREAM_END) {
```

[**Full function:**](https://github.com/FFmpeg/FFmpeg/commit/e371f031b942d73e02c090170975561fabd5c264#diff-1205c376797026cb2296bd451f341c5eR422)

```c
static int decode_zbuf(AVBPrint *bp, const uint8_t *data,
                        const uint8_t *data_end)
 {
     z_stream zstream;
     unsigned char *buf;
     unsigned buf_size;
     int ret;
 
     zstream.zalloc = ff_png_zalloc;
     zstream.zfree  = ff_png_zfree;
     zstream.opaque = NULL;
     if (inflateInit(&zstream) != Z_OK)
         return AVERROR_EXTERNAL;
     zstream.next_in  = (unsigned char *)data;
     zstream.avail_in = data_end - data;
    av_bprint_init(bp, 0, -1);
     while (zstream.avail_in > 0) {
        av_bprint_get_buffer(bp, 1, &buf, &buf_size);
        if (!buf_size) {
        av_bprint_get_buffer(bp, 2, &buf, &buf_size);
        if (buf_size < 2) {
            ret = AVERROR(ENOMEM);
            goto fail;
        }
        zstream.next_out  = buf;
        zstream.avail_out = buf_size;
        zstream.avail_out = buf_size - 1;
        ret = inflate(&zstream, Z_PARTIAL_FLUSH);
        if (ret != Z_OK && ret != Z_STREAM_END) {
            ret = AVERROR_EXTERNAL;
             goto fail;
         }
         bp->len += zstream.next_out - buf;
         if (ret == Z_STREAM_END)
             break;
     }
     inflateEnd(&zstream);
     bp->str[bp->len] = 0;
     return 0;
 
 fail:
     inflateEnd(&zstream);
     av_bprint_finalize(bp, NULL);
     return ret;
 }
```

**Comments**:


---

<a name="OpenCV">

### Project Name: [OpenCV](https://github.com/opencv/opencv)

<a name="Out of bounds write causes Segmentation Fault #9723">

### 1. [Out of bounds write causes Segmentation Fault #9723](https://github.com/opencv/opencv/issues/9309)

[**Description**](https://github.com/opencv/opencv/issues/9723)

In opencv/modules/imgcodecs/src/utils.cpp, functions FillUniColor and FillUniGray do not check the input length, which can lead to integer overflow. If the image is from remote, may lead to remote code execution or denial of service. This affects Opencv 3.3 and earlier.

[**Patch code:**](https://github.com/opencv/opencv/pull/9726/files)

```diff
@@ -375,6 +375,9 @@ decode_rle4_bad: ;
                                                gray_palette[code] );
                         line_end_flag = y - prev_y;
+                         if( y >= m_height )
+                            break;
                    }
                    else if( code > 2 ) // absolute mode
                    {
```

[**Full function:**](https://github.com/opencv/opencv/pull/9726/files#diff-236c3294512b9353649b64ad8385e984R194)

too long, see [here](https://github.com/opencv/opencv/pull/9726/files#diff-236c3294512b9353649b64ad8385e984R194)

**Comments**:


---



<a name="A heap based buffer overflow happens in cv::Jpeg2KDecoder::readComponent8u #10541">

### 1. [A heap based buffer overflow happens in cv::Jpeg2KDecoder::readComponent8u #10541](https://github.com/opencv/opencv/issues/10541)

[**Description**](https://github.com/opencv/opencv/issues/10541)

In OpenCV 3.3.1, a heap-based buffer overflow happens in cv::Jpeg2KDecoder::readComponent8u in modules/imgcodecs/src/grfmt_jpeg2000.cpp when parsing a crafted image file.

[**Patch code:**]()

```diff
@@ -77,7 +77,8 @@ static JasperInitializer initialize_jasper;
 Jpeg2KDecoder::Jpeg2KDecoder()
{
-    m_signature = '\0' + String() + '\0' + String() + '\0' + String("\x0cjP  \r\n\x87\n");
+    static const unsigned char signature_[12] = { 0, 0, 0, 0x0c, 'j', 'P', ' ', ' ', 13, 10, 0x87, 10};
+    m_signature = String((const char*)signature_, (const char*)signature_ + sizeof(signature_));
    m_stream = 0;
    m_image = 0;
}
@@ -121,6 +122,8 @@ bool  Jpeg2KDecoder::readHeader()
        jas_image_t* image = jas_image_decode( stream, -1, 0 );
        m_image = image;
        if( image ) {
+            CV_Assert(0 == (jas_image_tlx(image)) && "not supported");
+            CV_Assert(0 == (jas_image_tly(image)) && "not supported");
            m_width = jas_image_width( image );
            m_height = jas_image_height( image );
 @@ -130,14 +133,31 @@ bool  Jpeg2KDecoder::readHeader()
            for( int i = 0; i < numcmpts; i++ )
            {
                int depth_i = jas_image_cmptprec( image, i );
+                CV_Assert(depth == 0 || depth == depth_i); // component data type mismatch
                depth = MAX(depth, depth_i);
                if( jas_image_cmpttype( image, i ) > 2 )
                    continue;
+                int sgnd = jas_image_cmptsgnd(image, i);
+                int xstart = jas_image_cmpttlx(image, i);
+                int xend = jas_image_cmptbrx(image, i);
+                int xstep = jas_image_cmpthstep(image, i);
+                int ystart = jas_image_cmpttly(image, i);
+                int yend = jas_image_cmptbry(image, i);
+                int ystep = jas_image_cmptvstep(image, i);
+                CV_Assert(sgnd == 0 && "not supported");
+                CV_Assert(xstart == 0 && "not supported");
+                CV_Assert(ystart == 0 && "not supported");
+                CV_Assert(xstep == 1 && "not supported");
+                CV_Assert(ystep == 1 && "not supported");
+                CV_Assert(xend == m_width);
+                CV_Assert(yend == m_height);
                cntcmpts++;
            }
             if( cntcmpts )
            {
+                CV_Assert(depth == 8 || depth == 16);
+                CV_Assert(cntcmpts == 1 || cntcmpts == 3);
                m_type = CV_MAKETYPE(depth <= 8 ? CV_8U : CV_16U, cntcmpts > 1 ? 3 : 1);
                result = true;
            }
@@ -150,9 +170,14 @@ bool  Jpeg2KDecoder::readHeader()
    return result;
}
+ static void Jpeg2KDecoder_close(Jpeg2KDecoder* ptr)
+ {
+    ptr->close();
+ }
 bool  Jpeg2KDecoder::readData( Mat& img )
{
+    Ptr<Jpeg2KDecoder> close_this(this, Jpeg2KDecoder_close);
    bool result = false;
    int color = img.channels() > 1;
    uchar* data = img.ptr();
@@ -204,11 +229,16 @@ bool  Jpeg2KDecoder::readData( Mat& img )
                    result = true;
                }
                else
-                    fprintf(stderr, "JPEG 2000 LOADER ERROR: cannot convert colorspace\n");
+                {
+                     jas_cmprof_destroy(clrprof);
+                     CV_Error(Error::StsError, "JPEG 2000 LOADER ERROR: cannot convert colorspace");
+                }
                jas_cmprof_destroy( clrprof );
            }
            else
-                fprintf(stderr, "JPEG 2000 LOADER ERROR: unable to create colorspace\n");
+            {
+                CV_Error(Error::StsError, "JPEG 2000 LOADER ERROR: unable to create colorspace");
+            }
        }
        else
            result = true;
@@ -257,8 +287,8 @@ bool  Jpeg2KDecoder::readData( Mat& img )
                                result = readComponent16u( ((unsigned short *)data) + i, buffer, validateToInt(step / 2), cmptlut[i], maxval, offset, ncmpts );
                            if( !result )
                            {
-                                i = ncmpts;
-                                result = false;
+                                jas_matrix_destroy( buffer );
+                                CV_Error(Error::StsError, "JPEG2000 LOADER ERROR: failed to read component");
                            }
                        }
                        jas_matrix_destroy( buffer );
@@ -267,10 +297,12 @@ bool  Jpeg2KDecoder::readData( Mat& img )
            }
        }
        else
-            fprintf(stderr, "JPEG2000 LOADER ERROR: colorspace conversion failed\n" );
+        {
+            CV_Error(Error::StsError, "JPEG2000 LOADER ERROR: colorspace conversion failed");
+        }
    }
-     close();
+    CV_Assert(result == true);
 #ifndef _WIN32
    if (!clr.empty())
```

[**Full function:**]()

```c

```

**Comments**:


---

<a name="json-c">

### Project Name: [json-c](https://github.com/json-c/json-c)

<a name="Empty strings and unicode zero values break json parsing. #53">

### 1. [Empty strings and unicode zero values break json parsing. #53](https://github.com/json-c/json-c/issues/53)

[**Description**](https://github.com/json-c/json-c/issues/53)

Package: libjson0
Version: 0.10-1.1
Severity: important

If the input JSON contains empty value (i.e. "") The internal string
buffer is unterminated and unexpected behaviour occours.

If the unicode value \u0000 appears in the input the string is
terminated early and the string is truncated.

[**Patch code:**](https://github.com/json-c/json-c/commit/4e4af93d667ae0d3cb9779f5a3c3f964cc9d7d81)

```diff
json_object.c
@@ -620,8 +620,9 @@ struct json_object* json_object_new_string_len(const char *s, int len)
  if(!jso) return NULL;
  jso->_delete = &json_object_string_delete;
  jso->_to_json_string = &json_object_string_to_json_string;
-  jso->o.c_string.str = (char*)malloc(len);
+  jso->o.c_string.str = (char*)malloc(len + 1);
  memcpy(jso->o.c_string.str, (void *)s, len);
+  jso->o.c_string.str[len] = '\0';
  jso->o.c_string.len = len;
  return jso;
}
json_tokener.c
@@ -393,7 +393,7 @@ struct json_object* json_tokener_parse_ex(struct json_tokener *tok,
	while(1) {
	  if(c == tok->quote_char) {
	    printbuf_memappend_fast(tok->pb, case_start, str-case_start);
-	    current = json_object_new_string(tok->pb->buf);
+	    current = json_object_new_string_len(tok->pb->buf, tok->pb->bpos);
	    saved_state = json_tokener_state_finish;
	    state = json_tokener_state_eatws;
	    break;
```

[**Full function:**](https://github.com/json-c/json-c/commit/4e4af93d667ae0d3cb9779f5a3c3f964cc9d7d81)

multiple functions edited, see [here](https://github.com/json-c/json-c/commit/4e4af93d667ae0d3cb9779f5a3c3f964cc9d7d81)

**Comments**:


---

<a name="jansson">

### Project Name: [jansson](https://github.com/akheron/jansson)

<a name="Stack exhaustion parsing a JSON file #282">

### 1. [Stack exhaustion parsing a JSON file #282](https://github.com/akheron/jansson/issues/282)

[**Description**](https://github.com/akheron/jansson/issues/282)

Jansson 2.7 and earlier allows context-dependent attackers to cause a denial of service (deep recursion, stack consumption, and crash) via crafted JSON data.

[**Patch code:**](https://github.com/akheron/jansson/pull/284/files)

```diff
android/jansson_config.h
@@ -36,4 +36,8 @@
   otherwise to 0. */
#define JSON_HAVE_LOCALECONV 0
+ /* Maximum recursion depth for parsing JSON input.
+   This limits the depth of e.g. array-within-array constructions. */
+ #define JSON_PARSER_MAX_DEPTH 2048
src/load.c
@@ -62,6 +62,7 @@ typedef struct {
    stream_t stream;
    strbuffer_t saved_text;
    size_t flags;
+    size_t depth;
    int token;
    union {
        struct {
@@ -803,6 +804,12 @@ static json_t *parse_value(lex_t *lex, size_t flags, json_error_t *error)
{
    json_t *json;
+   lex->depth++;
+   if(lex->depth > JSON_PARSER_MAX_DEPTH) {
+       error_set(error, lex, "maximum parsing depth reached");
+       return NULL;
+   }
     switch(lex->token) {
        case TOKEN_STRING: {
            const char *value = lex->value.string.val;
@@ -865,13 +872,16 @@ static json_t *parse_value(lex_t *lex, size_t flags, json_error_t *error)
    if(!json)
        return NULL;
+   lex->depth--;
    return json;
}
 static json_t *parse_json(lex_t *lex, size_t flags, json_error_t *error)
{
    json_t *result;
+    lex->depth = 0;
    lex_scan(lex, error);
    if(!(flags & JSON_DECODE_ANY)) {
        if(lex->token != '[' && lex->token != '{') {
```

[**Full function:**](https://github.com/akheron/jansson/pull/284/commits/64ce0ad3731ebd77e02897b07920eadd0e2cc318#diff-04323737e1efd784854c30ab83651c9cR803)

```c
 static json_t *parse_value(lex_t *lex, size_t flags, json_error_t *error)
{
    json_t *json;
     lex->depth++;
    if(lex->depth > JSON_PARSER_MAX_DEPTH) {
        error_set(error, lex, "maximum parsing depth reached");
        return NULL;
    }
     switch(lex->token) {
        case TOKEN_STRING: {
            const char *value = lex->value.string.val;
             size_t len = lex->value.string.len;
 
             if(!(flags & JSON_ALLOW_NUL)) {
                 if(memchr(value, '\0', len)) {
                     error_set(error, lex, "\\u0000 is not allowed without JSON_ALLOW_NUL");
                     return NULL;
                 }
             }
 
             json = jsonp_stringn_nocheck_own(value, len);
             if(json) {
                 lex->value.string.val = NULL;
                 lex->value.string.len = 0;
             }
             break;
         }
 
         case TOKEN_INTEGER: {
             json = json_integer(lex->value.integer);
             break;
         }
 
         case TOKEN_REAL: {
             json = json_real(lex->value.real);
             break;
         }
 
         case TOKEN_TRUE:
             json = json_true();
             break;
 
         case TOKEN_FALSE:
             json = json_false();
             break;
 
         case TOKEN_NULL:
             json = json_null();
             break;
 
         case '{':
             json = parse_object(lex, flags, error);
             break;
 
         case '[':
             json = parse_array(lex, flags, error);
             break;
 
         case TOKEN_INVALID:
             error_set(error, lex, "invalid token");
             return NULL;
 
         default:
             error_set(error, lex, "unexpected token");
             return NULL;
     }
 
    if(!json)
        return NULL;
     lex->depth--;
    return json;
}
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