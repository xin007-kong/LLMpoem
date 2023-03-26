import streamlit as st
from PIL import Image

st.title('《诗云》读书会~')
# 写一段关于《诗云》读书会的欢迎语句，用markdown格式，带上丰富的emoji表情
st.markdown("""


    《诗云》是刘慈欣的一部短篇科幻小说。
   
      小说讲述了一个高等外星文明为了写出超越李白的诗歌，穷尽了太阳系的大部分能量，列举出了所有可能的字词组合，最终，他们“借助伟大的技术，我写出了诗词的巅峰之作”，却还是选择了认输，因为他们“不可能把它们从诗云中检索出来”。😲
    
      在去年11月底自从chatgpt发布以来，人类迎来了又一波工业革命，一波又一波颠覆人们想象的浪潮滚滚袭来，此时再看《诗云》，显得很有意义 🤔
   
    这是一个充满了诗意和想象力的故事，让我们开始叭~👏""")
            
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




st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)