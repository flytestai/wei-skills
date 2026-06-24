# API usage

本 skill 采用 OpenAI 兼容接口风格。

## 配置来源
从本地私有 JSON 配置文件读取：
- `base_url`
- `api_key`
- `model`

## 默认接口
- POST `{base_url}/images/generations`

## 请求体
```json
{
  "model": "gpt-image-2",
  "prompt": "用户提示词",
  "size": "1024x1024",
  "n": 1,
  "quality": "high"
}
```

## 兼容处理
脚本兼容以下常见返回格式：
- `data[].b64_json`
- `data[].url`（仅下载为本地文件后发送，不直接转发 URL）

如果接口不支持 `quality` 字段，脚本会自动去掉该字段并重试。

## 失败处理
- 配置缺失：退出并返回错误
- 接口非 200：返回状态码与简短响应片段
- 返回结构无法识别：返回结构错误
