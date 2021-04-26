import streamlit as st
from PIL import Image

st.title('Streamlit Text Sizing')
st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')

st.write('This is a st.write call')
st.caption('This is small text')

st.markdown('---')
st.title('Markdown Heading Sizes')

st.markdown('# Heading Level One')
st.markdown('## Heading Level Two')
st.markdown('### Heading Level Three')
st.markdown('#### Heading Level Four')
st.markdown('##### Heading Level Five')
st.markdown('###### Heading Level Six')
st.caption('This is small text')

st.markdown('---')
image = Image.open('dog.jpg')
st.image(image, caption='This is the default image caption: Photo by Marliese Streefland on Unsplash')
st.caption('Photo by Marliese Streefland on Unsplash') 
st.write('Above: A caption without any tags')



st.markdown('---')
st.write('Below: st.caption supports inline markdown')
with st.echo():
    st.caption('Photo by [Marliese Streefland](https://unsplash.com/@marliesebrandsma?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/dog?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)')

st.write('Italic and Bold')
with st.echo():
    st.caption('This is small text and _italic_ and **bold**')
    st.markdown('This is normal markdown text and _italic_ and **bold**', unsafe_allow_html=False)

st.markdown('---')

st.header('Multi-line strings')

st.code("""st.caption('''<small>
Hello _world_

test

1. One item
2. another

</small>''')""")

st.caption('''<small>
Hello _world_

test

1. One item
2. another

</small>''')

st.markdown('---')

st.write('How st.markdown handles the same situation')

st.code("""st.markdown('''<small>
Hello _world_

test

1. One item
2. another

</small>''')""")

st.markdown('''<small>
Hello _world_

test

1. One item
2. another

</small>''', unsafe_allow_html=False)

st.markdown('---')

st.write('How st.subheader handles the same situation')

st.code("""st.subheader('''<small>
Hello _world_

test

1. One item
2. another

</small>''')""")

st.subheader('''<small>
Hello _world_

test

1. One item
2. another

</small>''')

st.subheader('''<small>
Hello _world_

# test


1. One item
2. another

</small>''')

st.markdown('Photo by <a href="https://unsplash.com/@marliesebrandsma?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Marliese Streefland</a> on <a href="https://unsplash.com/s/photos/dog?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>')