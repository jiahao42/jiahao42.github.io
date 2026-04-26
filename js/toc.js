document.addEventListener("DOMContentLoaded", function () {
  var content = document.getElementById("post-content");
  if (!content) return;

  var headings = content.querySelectorAll("h2, h3, h4");
  if (headings.length < 2) return;

  var toc = document.createElement("div");
  toc.className = "toc";

  var label = document.createElement("p");
  label.className = "toc-label";
  label.textContent = "Outline";
  toc.appendChild(label);

  var list = document.createElement("ul");
  list.className = "toc-list";

  headings.forEach(function (h) {
    var li = document.createElement("li");
    li.className = "toc-" + h.tagName.toLowerCase();
    var a = document.createElement("a");
    a.href = "#" + h.id;
    a.textContent = h.textContent;
    li.appendChild(a);
    list.appendChild(li);
  });

  toc.appendChild(list);
  content.insertBefore(toc, content.firstChild);
});
