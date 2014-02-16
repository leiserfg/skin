# -*- coding: utf-8 -*-
import sys
# sys.path.append('./3rd')
from app import app
app.run(debug=True, port=8080, host='0.0.0.0')
