# mdview

Linux 上预览 Markdown 的小工具。

## 安装

需要 Python 3、GTK 3、WebKit2GTK 4.1、pandoc。

```bash
git clone https://github.com/mingyangqianli2357/md-viewer.git
cd md-viewer
git clone --depth 1 https://github.com/sindresorhus/github-markdown-css
```

## 用法

```bash
python mdview.py --path note.md
```

```bash
python mdview.py --path note.md --width 700
python mdview.py --path note.md --css /path/to/github-markdown-light.css
```
