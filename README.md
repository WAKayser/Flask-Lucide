# Flask Lucide


A simple Tag (`{% icon "name" %}`) to implement [Lucide Icons](https://lucide.dev) in Flask. 
This is completely copied of the library [Flask Feather](https://github.com/thetomcat/flask-feather) by TheTomcat
This is largely based of the library [django_feather](https://github.com/jnsdrtlf/django-feather) by [Jonas Drotleff](https://github.com/jnsdrtlf/).

## Install

Install `flask-lucide` using `pip`.

```bash
pip install flask-lucide
```  

## Quick Start

Firstly, initialise the extension within your Flask context

```python
from flask_feather import Feather
feather = Feather(app)
```

This extension also supports the [Flask application factory pattern](http://flask.pocoo.org/docs/latest/patterns/appfactories/) by allowing you to create a Feather object and then initialised it separately for an app:

```python
feather = Feather()

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    feather.init_app(app)
```

### Advanced setup

In addition to the wonderful icons provided in the feather set, you can supply your own svg icons, to attempt to parse them and use them in the same format. Simply initialise the extension with a directory containing .svg files that are similar in style to the feather ones. They should resemble the feather icon style as near as possible - any significant differences in formatting/structure may result in unexpected errors.

```python
feather = Feather(import_dir='app\\static\\customsvg')

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    feather.init_app(app)
```

## Usage

It's pretty simple to use this package. From within a jinja template:

```html
<p>{{ lucide.icon('icon-name', width=32, height=32) }}</p>
```

If the property you're modifying has a hyphen, use an underscore instead. You can refer to icon names with either hyphens or underscores.

```html
<p>{{ lucide.icon('icon-name', stroke_width=2) }}</p>
```

The `icon` function takes the SVG source from the Feather project, applies additional attributes and return the SVG tag.

## Performance

`flask-lucide` borrows the application structure from `django-feather` and does not read the `.svg`
files each time an icon is rendered. Instead, on installation, all the icons are written to a `.py` file.
All icons are rendered on the server side, avoiding the need to call `feather.replace()` after the page has loaded.

Any custom icons are parsed each time the server is restarted, and not every time they're loaded.

## License

Lucide is licensed under the [ISC License](https://github.com/lucide-icons/lucide/blob/master/LICENSE).

`flask-lucide` is a derivative work of `flask-feather` and `django-feather`,  are licensed under the Apache License, Version 2.0:


```license
    Modifications Copyright 2020 Tom Vos <tjvos1@gmail.com>
    
    Original Django-feather Copyright 2020 Jonas Drotleff <j.drotleff@desk-lab.de>
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
       http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
```
