import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
legacy = Image.open("images/legacy.png")
garochaa = Image.open("images/garochaa.png")
safal = load_lottieurl("https://lottie.host/4f7fdd17-ebb3-4d53-8836-eb55e0ced4d9/TxwTgo1hft.json")    

st.write("##")
# ---- HEADER SECTION ----
st.markdown("<style> .circle-frame { border-radius: 55%; width: 120px; height: 120px; background-color: white; text-align: center; float: right; margin-left: 20px; margin-top: -100px; } .circle-frame img { border-radius: 50%; width: 120px; height: 120px; object-fit: cover; } </style>", unsafe_allow_html=True)
st.markdown('<div class="circle-frame"><img src="https://t.ly/hJlHn" alt="Your Name" /><p>Safal Poudel</p></div>', unsafe_allow_html=True)

st.write("##")

with st.container():
    st.title("Hi, I am Safal  :wave:")
    st.subheader('Versatile musician and Python programmer, harmonizing melodies and code.  #MusicAndCode')

    st.subheader("""Multifaceted musician and Python maestro, seamlessly blending the world of music and code. 
Crafting symphonies with melodies and algorithms, I bridge the realms of creativity and precision. MusicAndCode""")
    


# ... (rest of your code)

    

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            "As a musician and Python programmer, I find joy in the fusion of two worlds. Music is my artistic canvas, and Python is my technical palette. Crafting harmonious melodies and elegant code are my dual passions. In both realms, I seek the perfect balance of creativity and precision, striving for elegance and efficiency. Whether composing a musical masterpiece or writing a complex algorithm, I'm driven by the artistry of structure and rhythm. This creative duality fuels my endless exploration of possibilities, reminding me that the synergy between music and code is where my true passion thrives, shaping a unique path of endless discovery."
            
            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/@SSAIZY)")
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Recent songs")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(garochaa)
    with text_column:
        st.subheader("Saizy collaborates with Aadesh in 'Garo Chaa,' a track inspired by personal experiences, exuding a cool and enjoyable vibe.")
        st.write(
            """
        "Saizy and Aadesh join forces in 'Garo Chaa,' a composition drawn from personal encounters, emanating a pleasing and relaxed ambiance. This collaboration encapsulates their harmonious synergy, weaving a melodious tale that resonates with authenticity and enjoyment. Through candid storytelling and harmonious arrangements, 'Garo Chaa' invites listeners to a unique auditory experience, rich with their shared experiences and an effortlessly cool atmosphere, making it a compelling addition to their artistic journey."
           """
        )
        st.markdown("[Watch Video...](https://youtu.be/QLMkB_Uo2Rw?si=f_w14zzoSvwpBVf7)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(legacy)
    with text_column:
        st.subheader("Legacy' is a resonant reflection of growth, resilience, and purpose, inspiring listeners to embrace challenges and live authentically.")
        st.write(
            """
            "Recently released 'Legacy,' a musical reflection of my personality and life perspective. The song resonates with the essence of growth, resilience, and the pursuit of leaving a lasting impact. Its lyrics and melodies intertwine to convey a message of embracing challenges as opportunities, forging a path of purpose and significance. 'Legacy' encapsulates my journey, an artistic testament to the idea that every moment and choice shapes the narrative we leave behind. With its powerful storytelling and captivating rhythm, the song invites listeners to contemplate their own legacy, inspiring them to live with intention and authenticity.".
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/wKEsV8zicyo?si=WpTV7vSxZJIWpXoK)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/info1.saizy@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

#stay connected with me

    st.header("Connect with Me!")

# Calculate approximate width and height for 1 cm² area based on display resolution (adjust as needed)
logo_width = 35  # in pixels
logo_height = 35  # in pixels

# Display social media links with logos as clickable links
social_media_columns = st.columns(4)

with social_media_columns[0]:
    st.markdown(f'<a href="https://www.facebook.com/safal.poudel205" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Facebook_logo_%28square%29.png/800px-Facebook_logo_%28square%29.png" width="{logo_width}" height="{logo_height}" alt="Facebook"></a>', unsafe_allow_html=True)

with social_media_columns[1]:
    st.markdown(f'<a href="https://www.instagram.com/safalpoudel77/" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/600px-Instagram_icon.png?20200512141346" width="{logo_width}" height="{logo_height}" alt="Instagram"></a>', unsafe_allow_html=True)

with social_media_columns[2]:
    st.markdown(f'<a href="https://www.linkedin.com/in/safal-poudel-93b0b827b" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/600px-LinkedIn_logo_initials.png?20140125013055" width="{logo_width}" height="{logo_height}" alt="LinkedIn"></a>', unsafe_allow_html=True)

with social_media_columns[3]:
    st.markdown(f'<a href="https://www.youtube.com/@SSAIZY" target="_blank"><img src="https://pngimg.com/d/youtube_PNG102351.png" width="{logo_width}" height="{logo_height}" alt="YouTube"></a>', unsafe_allow_html=True)

