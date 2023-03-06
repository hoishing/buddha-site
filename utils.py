import streamlit as st
from pathlib import Path
from data import base_url

TOC = dict[str, dict[str, list[str]]]


def sidebar(src: TOC) -> None:
    with st.sidebar:
        for section in src:
            st.write(f"#### {section}")
            for book in src[section]:
                title = book.split("-")[0]
                st.markdown(f"&nbsp;&nbsp;[{title}](#{title})")


def content(src: TOC) -> None:
    for section in src:
        for book in src[section]:
            title, author = book.split("-")
            st.subheader("", anchor=title)
            st.markdown(f"##### {title} - {author}")
            for file in src[section][book]:
                path = Path(file)
                name = path.stem.split("-")[1] + path.suffix
                url = base_url + file
                icon = "🎙️" if path.suffix == ".mp3" else "📜"
                st.write(
                    f"&nbsp;&nbsp;&nbsp;&nbsp;{icon}&nbsp;&nbsp;&nbsp;[{name}]({url})"
                )
            st.write("---")


def config(zh: bool) -> None:
    title = "認識佛教" if zh else "认识佛教"
    desc = "歡迎複製流通" if zh else "欢迎复制流通"
    st.set_page_config(
        page_title=title,
        page_icon="🙏",
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items={
            "Get help": "https://github.com/hoishing/buddha-site",
            "Report a bug": "https://github.com/hoishing/buddha-site/issues",
            "About": f"#### {title} \n {desc}",
        },
    )
