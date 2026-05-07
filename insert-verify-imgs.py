import os

path = r'C:\Projects\signal-how\content\guides\signal-verification-code-not-received.md'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace(
    '## 1. 检查手机号格式（最常见的原因）',
    '## 1. 检查手机号格式（最常见的原因）\n\n![Signal手机号正确格式示例](/images/guides/signal-verification/phone-format.jpg)'
)
c = c.replace(
    '## 3. 使用语音验证码',
    '## 3. 使用语音验证码\n\n![Signal语音验证码操作步骤](/images/guides/signal-verification/voice-verify.jpg)'
)
c = c.replace(
    '## 7. 检查手机短信拦截设置',
    '## 7. 检查手机短信拦截设置\n\n![手机短信拦截设置检查](/images/guides/signal-verification/intercept-settings.jpg)'
)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)
print("3 body images inserted")
