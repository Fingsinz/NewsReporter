# NewsReporter

NewsReporter 是一个功能强大的智能信息收集与分析系统，支持从RSS源和邮箱自动收集信息，并通过AI Agent生成报告。

Tech:

- **Python 3.10+**
- **Pydantic**: 数据验证和配置管理
- **Feedparser**: RSS/Atom 源解析
- **APScheduler**: 定时任务调度
- **Python-Markdown**: Markdown转HTML转换
- **OpenAI/Anthropic/DeepSeek SDK**: AI模型接口
- **PyYAML**: 配置文件处理

env:

```env
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

MIT License
