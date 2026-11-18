import subprocess
import pathlib
import gi
import argparse

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.1")
from gi.repository import Gtk, WebKit2

ap = argparse.ArgumentParser()
ap.add_argument("--style", default="breezedark")
ap.add_argument("--css", default="./github-markdown-css/github-markdown-dark.css")
ap.add_argument("--path", required=True)
ap.add_argument("--width", default="900")
args = ap.parse_args()

md = pathlib.Path(args.path).absolute()
css = pathlib.Path(args.css)
if not css.is_absolute():
    css = pathlib.Path(__file__).resolve().parent / css

p = subprocess.run(
    [
        "pandoc",
        str(md),
        "-f",
        "gfm",
        "-t",
        "html5",
        "--standalone",
        "--mathml",
        "--highlight-style",
        args.style,
        "--css",
        css.as_uri(),
    ],
    capture_output=True,
    text=True,
    check=False,
)


LAYOUT = f"<style>body.markdown-body {{ max-width: {args.width}px; margin: 0 auto; padding: 45px 24px; }}</style>"

html = p.stdout.replace("<body", '<body class="markdown-body"', 1)
html = html.replace("</head>", LAYOUT + "</head>")

Gtk.Settings.get_default().set_property("gtk-application-prefer-dark-theme", True)

view = WebKit2.WebView()
view.get_settings().set_allow_file_access_from_file_urls(True)
view.load_html(html, md.parent.as_uri() + "/")

win = Gtk.Window()
win.set_decorated(False)
win.add(view)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
