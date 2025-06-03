# Blog

{{- range .Site.Blogs}}
[{{.Title}}]({{.Uri}})
: {{.BlogData.Date}}
{{end -}}
