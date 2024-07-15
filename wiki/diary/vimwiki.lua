require("string")

Writer = pandoc.scaffolding.Writer

Writer.Block.Para = function(para)
    return {Writer.Inlines(para.content), pandoc.layout.blankline}
end

Writer.Inline.Str = function(str)
    return str.text
end

Writer.Inline.Space = function(str)
    return " "
end

Writer.Inline.Link = function(link)
    return "[[" .. link.target .. "|" .. Writer.Inlines(link.content) .. "]]"
end

Writer.Inline.Code = function(code)
    return "`" .. code.text .. "`"
end

Writer.Block.Header = function(header)
    return string.rep("=", header.level) .. Writer.Inlines(header.content) .. string.rep("=", header.level)
end

Writer.Block.Figure = function(figure)
    return Writer.Blocks(figure.content)
end

Writer.Block.Plain = function(plain)
    return Writer.Inlines(plain.content)
end

Writer.Inline.Image = function(image)
    return "{{" .. image.src .. "|" .. Writer.Inlines(image.caption) .. "}}"
end

Writer.Inline.Quoted = function(quoted)
    return "\"" .. Writer.Inlines(quoted.content) .. "\""
end

Writer.Block.CodeBlock = function(codeblock)
    return "{{{\n" .. codeblock.text .. "\n}}}"
end

Writer.Inline.Emph = function(emph)
    return "_" .. Writer.Inlines(emph.content) .. "_"
end

Writer.Block.BulletList = function(bl)
    out = {}

    for i, b in ipairs(bl.content) do
        out[i] = "* " .. Writer.Blocks(b) .. "\n"
    end

    return out
end

Writer.Block.OrderedList = function(ol)
    out = {}

    for i, o in ipairs(ol.content) do
        out[i] = "# " .. Writer.Blocks(o) .. "\n"
    end

    return out
end

Writer.Block.HorizontalRule = function(rule)
    return "----"
end

Writer.Block.RawBlock = function(raw)
    return raw.text
end

Writer.Inline.Strong = function(strong)
    return "*" .. Writer.Inlines(strong.content) .. "*"
end

Writer.Block.BlockQuote = function(quote)
    out = {}

    for i, q in ipairs(quote) do
        out[i] = "    " .. Writer.Blocks(q)
    end

    return out
end

Writer.Inline.RawInline = function(raw)
    return raw.text
end
