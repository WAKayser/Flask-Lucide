"""Single File plugin for Lucide icons."""
import re

from dataclasses import dataclass
from flask import current_app, Flask
from io import StringIO
from markupsafe import Markup
from pathlib import Path
from typing import Optional, Any
from xml.dom import minidom

from .icons import i as icons


class Lucide(object):
    """Lucide Class object represents the plugin."""

    def __init__(self, app: Flask, import_dir: Optional[Path] = None):
        """Initialize plugin and read extra files from import dir.

        Args:
            app (Flask): flask app
            import_dir (Optional[Path]): potentiall allow a pathlob path
        """
        if app is not None:
            self.init_app(app)
        if import_dir:
            print(f"Attempting to import custom svg from {import_dir}")
            files = import_dir.glob('**/*.svg')
            for file in files:
                icon_name = file.stem.replace('-', '_')
                print(f"Parsing {icon_name}")
                svg = file.read_text()
                svg = re.sub(r'\n', r' ', svg)
                svg = re.sub(r'\s+', r' ', svg)
                svg = svg.replace('> <', '><').replace(' />', '/>')
                svg = ('><').join(svg.split('><')[1:-1])
                icons[icon_name] = svg

    def init_app(self, app: Flask):
        """Initialize plugin.

        Args:
            app (Flask): flask entity
        """
        if not hasattr(app, 'extensions'):
            app.extensions = {}
        app.extensions['lucide'] = _lucide
        app.context_processor(self.context_processor)

    @staticmethod
    def context_processor() -> dict:
        """Set the extensions.

        Returns:
            dict: what to add to context of app.
        """
        return {'lucide': current_app.extensions['lucide']}


class _lucide(object):
    @staticmethod
    def icon(icon_name: str, **kwargs: Any) -> Markup:
        """Attempt to render the icon icon_name with attributes as listed.

        Args:
            icon_name (str): The name of the lucide icon
            **kwargs (Any): arguments to set for the icons.

        Returns:
            Markup: markup safe string of xml
        """
        icon_name = icon_name.replace('-', '_')
        if not icon_name:
            return Markup('')

        start = "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"24\""\
                " height=\"24\" viewBox=\"0 0 24 24\" fill=\"none\" stroke="\
                "\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\""\
                " stroke-linejoin=\"round\" ><"

        end = "></svg>"

        svg = start + icons[icon_name] + end

        doc = minidom.parseString(svg)
        for attr, val in kwargs.items():
            attr = attr.replace('_', '-')
            doc.documentElement.setAttribute(attr, str(val))

        writer = StringIO()
        for node in doc.childNodes:
            node.writexml(writer, "", "", "")

        return Markup(writer.getvalue())
