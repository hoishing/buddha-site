import streamlit as st
from data import cn
from utils import sidebar, content, config


title = "认识佛教"

config(title)

sidebar(cn)

f"""
### {title}
###### 华语有声书
---
"""

content(cn)
