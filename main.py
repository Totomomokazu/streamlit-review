import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("streamlit 超入門")
st.write("Dataframe")


st.sidebar.write("Interactive Widgets")
text = st.sidebar.text_input("text入力")
condition=st.sidebar.slider("今の調子は？",0,100,50)
"textの入力内容", text
"コンディション", condition

# プログレスバーのコード
latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f"読み込み中{i+1}")
    bar.progress(i+1)
    time.sleep(0.01)
# プログレスバーのコード


"""
### 表の確認
"""
df = pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[10,20,30,40]
})

df

st.dataframe(df.style.highlight_max(axis=0),width=100,height=500)
# dataframeを使うと引数を指定できる

"""
### テーブルの確認
"""
st.table(df.style.highlight_max(axis=0))
# dataframeを使うと引数を指定できる

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

"""
### Mapの表示確認
"""

map_df=pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,137.70],
    columns=["lat","lon"]
)


st.write("地図表示")
st.map(map_df)

st.write("緯度経度情報")
if st.checkbox("Show table"):
    st.table(map_df)


img= Image.open("sample.png")
st.image(img, caption="img_python", use_column_width=True)

left_column,right_column=st.columns(2)
button=left_column.button("右にカラムが表示されます。")
if button:
    right_column.image(img, caption="img_python", use_column_width=True)
    right_column.text_input("text入力してください")

expander1=st.expander("問い合わせ内容を入力")
expander_output=expander1.text_input("")

expander_output