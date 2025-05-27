# Blog

<nav class="blog">
{{- range .Site.Blogs}}
[{{.Title}}]({{.Uri}})
<br />
<span class="date">{{.Date}}</span>
{{end -}}
</nav>
