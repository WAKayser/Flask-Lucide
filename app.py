from flask import Flask, render_template_string
from flask_lucide import Lucide

app = Flask(__name__)
lucide = Lucide(app)

@app.route('/')
def hello_world():
    return render_template_string("""<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Page Title</title>
</head>
<body>
    {{ lucide.icon('user-plus') }}
    {{ lucide.icon('user-minus', width=100, height=100) }}
    {{ lucide.icon('aperture', stroke_width=0.1) }}
</body>
</html> 
    """)