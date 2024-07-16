import streamlit as st  # 1.31.1
import os
import sys
import time
import streamlit.components.v1 as components


def main():
    # 设置标题,图标等
    st.set_page_config(layout="centered", page_title="HLS播放", page_icon=":shark:")

    st.write("演示HLS播放")
    html_content = '''
<html> 
<head>
    <meta charset="utf-8">
    <style>
        .video-js {
            width: 100%;
            height: 100%;
        }
    </style>
    <script src="https://unpkg.com/hls.js@0.14.17/dist/hls.js"></script>
    <body>
        <h1>hahahhah</h1>
    </body>
    <script>
    var video = document.getElementById('videoPlayer');
    var hls = new Hls();
    if (Hls.isSupported()) {
      hls.loadSource('http://localhost:8000/playlist.m3u8');
      hls.attachMedia(video);
      hls.on(Hls.Events.MANIFEST_PARSED, function() {
        video.play();
      });
    }
    </script>
</html>
    '''
    components.html(html_content, height=400)
    st.button("按钮")


if __name__ == "__main__":
    main()
