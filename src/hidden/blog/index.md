# Blog

{{- range .Site.Blogs}}
[{{.Title}}]({{.Uri}})
: {{.Blog.Date}}
{{end -}}
