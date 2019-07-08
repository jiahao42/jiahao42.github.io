---
layout: term
title: Jiahao Cai Home Page @University of Virginia
cmd: cat about.txt
description: Jiahao Cai, Ph.D. Student, Department of Computer Science, University of Virginia.
---

# Jiahao Cai

## Who?

I am currently a Ph.D. candidate in the Department of Computer Science, Univeristy of Virginia. I am advised by [Prof. Yonghwi Kwon](https://yonghwi-kwon.github.io) and my research interest lies in Software Security and Programming Language. 

Previously, I spent three years (2014-2017) in Beijing, China, and one year (2017-2018) in Halmstad, Sweden.

## Contact
+ e-mail: (dot (at jc4mf virginia) edu)

## Teaching
+ Teaching Assistant: [CS4414: Operating Systems](https://www.cs.virginia.edu/~cr4bd/4414/S2019/) - Spring 2019

## Elsewhere
+ <a class = "dir" href="https://github.com/jiahao42">Github</a>
+ <a class = "dir" href="https://stackoverflow.com/users/story/5685664">Stack Overflow</a>
<!-- + <a class = "dir" href="https://twitter.com/caterpillarous">Twitter</a> -->
+ <a class = "dir" href="https://linkedin.com/in/jiahao-cai/">LinkedIn</a>



<script>
$.getJSON("quote.json", function(json) {
  index = Math.floor(Math.random() * json.length);
  var _quote = json[index];
  console.log(index);
  console.log(_quote); // this will show the info it in firebug console
  var quote = document.createElement("div"); 
  quote.innerHTML = '<i>' + _quote.saying + '</i><br><p align="right"> --' + _quote.author + '</p>';
  quote.style.cssText = "width:15%;margin-top: 20px;position: absolute;margin-left: 70%;margin-right: 4%;height:0;";
  var site = document.getElementsByClassName("site")[0];
  document.body.insertBefore(quote, site);
});
</script>