import streamlit as st
from PIL import Image

st.title('《诗云》读书会~')
# 写一段关于《诗云》读书会的欢迎语句，用markdown格式，带上丰富的emoji表情
st.markdown("- 《诗云》是刘慈欣的一部短篇科幻小说，讲述了一个未来的世界，诗云是一个神级文明创造的神奇设备，它可以将任何思想和情感转化为诗歌，并在空中呈现出来。🌥️")
st.markdown("- 诗云是神级文明的化身，它试图写出超越李白的诗歌，但却发现无法从无穷无尽的诗句中找出最好的一首。😲")
st.markdown("- 这是一个充满了诗意和想象力的故事，在去年11月底chatgpt卷起一波又一波浪潮的当下，对书中主题的探讨显得很有意义 🤔")
st.markdown("- 让我们开始叭~👏")
            
# 加粗的分割线

st.markdown('---')


st.markdown("""
            《诗云》在维基百科上的英文简介的第一句话是:
            
            Yiyi, a poet, Big-tooth, an ambassador, and Li Bai, also a poet, are travelling on a yacht to the South Pole. 
            Ten years ago, Big-tooth went with Yiyi to meet the "god" that had recently appeared in the solar system.

            下面的图是我把上面这句话发给midjourney画出来的😂""")

# 读取图片 开头.png 并居中显示

image = Image.open('开头.png')
st.image(image, caption='', use_column_width=True)




