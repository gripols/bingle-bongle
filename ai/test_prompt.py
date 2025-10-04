import json
from promptKit import analyze_mistakes

# 测试一段错误的笔记
result = analyze_mistakes("The limt of sin(x)/x as x -> 0 is 0")
print(json.dumps(result, indent=2, ensure_ascii=False))
