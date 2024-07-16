
import os
import streamlit as st

def get_file_list(suffix,path):
    input_template_all = []
    input_template_all_path = []

    for root, dirs, files in os.walk(path,topdown=False):
        for name in files:
            if os.path.splitext(name)[1] == suffix:
                input_template_all.append(name)
                input_template_all_path.append(os.path.join(root, name))

    return input_template_all,input_template_all_path


st.title('数据分析工具')

input_folder = st.sidebar.text_input(
    "s输入数据所在的目录：（默认为所在脚本的目录）， 可输入新的路径回车更新",
    value=os.path.abspath('.'),key=None
)

path=input_folder
_, file_list_xlsx = get_file_list(".xlsx",path)
file_list = file_list_xlsx


if file_list:
    select_file=st.sidebar.selectbox(
            'aaa',
            file_list
    )
    st.write('you selected:',select_file)
else:
    st.title('没找到合适的文件')