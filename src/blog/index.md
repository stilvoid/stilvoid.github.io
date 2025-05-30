# Blog

{{- range .Site.Blogs}}
[{{.Title}}]({{.Uri}})
: {{.Date}}
{{end -}}
