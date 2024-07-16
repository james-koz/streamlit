import streamlit as st
import pandas as pd
import numpy as np
import datetime






# st.sidebar("喀什地方据了解")

st.error('错误信息')

st.warning('警告信息')

st.info('提示信息')

st.success('成功信息')

st.exception('异常信息')

birthday = st.date_input(label='请输入您的出生年月',
                         value=None,
                         min_value=None,
                         max_value=datetime.date.today(),
                         help='请输入您的出生年月')

st.write('您的生日是：', birthday)


text = st.text_area(label='请输入文本',
                    value='请输入...',
                    height=5,
                    max_chars=200,
                    help='最大长度限制为200')

st.write('您的输入是', text)

age = st.number_input(label='请输入您的年龄',
                      min_value=0,
                      max_value=100,
                      value=0,
                      step=1,
                      help='请输入您的年龄'
                      )
st.write('您的年龄是', age)

name = st.text_input('请输入用户名', max_chars=100, help='最大长度为100字符')

# 根据用户输入进行操作
st.write('您的用户名是', name)

age = st.slider(label='请输入您的年龄',
                min_value=0,
                max_value=800,
                value=0,
                step=1,
                help="请输入您的年龄"
                )

st.write('您的年龄是', age)

options = st.multiselect(
    label='请问您喜欢吃什么水果',
    options=('橘子', '苹果', '香蕉', '草莓', '葡萄'),
    default=None,
    format_func=str,
    help='选择您喜欢吃的水果'
)

st.write('您喜欢吃的是', options)

sex = st.radio(
    label='请输入您的性别',
    options=('男', '女', '保密'),
    index=2,
    format_func=str,
    help='如果您不想透露，可以选择保密'
)

if sex == '男':
    st.write('男士您好!')
elif sex == '女':
    st.write('女士您好!')
else:
    st.write('您好!')

if st.button('点我'):
    st.write('今天是个好日子！')



cb = st.checkbox('确认', value=False)

if cb:
    st.write('确认成功')
else:
    st.write('没有确认')


file_path = r'C:\Users\James\Desktop\mypython\pythonProject2\赛宁机器信息.xlsx'   # r对路径进行转义，windows需要
raw_data = pd.read_excel(file_path, header=0)  # header=0表示第一行是表头，就自动去除了
print(raw_data)



df = pd.DataFrame(raw_data)

st.dataframe(df)
st.table(df)


st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})
data = {
    'latitude': [37.7749, 34.0522, 40.7128],
    'longitude': [-122.4194, -118.2437, -74.0060],
    'name': ['beijing', 'tokyo', 'New York']
}

st.map(data, zoom=4, use_container_width=True)

df2 = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(df2)



# 网络视频
st.video("https://youtu.be/uLhNVExSu_4?si=y6liVItXCBvF48jw")

