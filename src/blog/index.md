# Blog

A collection of things that I decided to write. Here are the most recent of them...

{{range slice .Site.Blogs 0 5}}
- [{{.Title}}]({{.Uri}})
(<span class="date">{{.Date}}</span>)

> {{.Preview}}
{{end}}
