import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# -----------------------------------
st.title('Streamlit 門')
st.header('This is a header')
st.write('DataFrame')
df=pd.DataFrame({
'1列目':[1,2,3,4],
'2列目':[10,20,40,30]
})
st.write(df)
st.dataframe(width=100,height=100)

# -----------------------------------
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

# -----------------------------------
df=pd.DataFrame(
np.random.rand(20,3),
columns=['a','b','c']
)
st.write(df)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

# -----------------------------------
# 100個2行
df=pd.DataFrame(
np.random.rand(100,2)/[50,50] + [35.69,139.70],
columns=['lat','lon']
)
st.write(df)
st.map(df)

# -----------------------------------
st.write('Display Image')
img = Image.open('C:/Users/hiramatu/Desktop/pythonwk/Test.jpg')
#ブラウザの横幅に合わせるuse_column_width
st.image(img, caption='aiueo',use_column_width='true')

