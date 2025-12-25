!pip install transformers torch streamlit

import streamlit as st
from transformers import pipeline

# تحميل نموذج توليدي (GPT-2)
@st.cache_resource
def load_generator():
    return pipeline("text-generation", model="gpt2")

generator = load_generator()

# وظيفة توليد خطة التعلم
def generate_learning_plan(topic):
    prompt = f"اعطني خطة تعلم مفصلة لتعلم {topic} من الصفر إلى مستوى متقدم:"
    result = generator(prompt, max_length=300, num_return_sequences=1)
    return result[0]['generated_text']

# واجهة Streamlit
st.title("مولّد خطط التعلم بالذكاء الاصطناعي")
st.write("ادخل موضوع التعلم للحصول على خطة مفصلة:")

topic = st.text_input("موضوع التعلم:")

if st.button("توليد الخطة"):
    if not topic.strip():
        st.warning("من فضلك أدخل موضوع التعلم!")
    else:
        with st.spinner("جاري توليد الخطة..."):
            plan = generate_learning_plan(topic)
        st.subheader("خطة التعلم الناتجة:")
        st.write(plan)
