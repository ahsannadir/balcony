import streamlit as st
from ultralytics import YOLO
from PIL import Image, ImageOps

st.set_page_config(
    page_title = 'Balcony Detection',
    page_icon = "🪟",
    #layout = 'wide'
)

st.markdown("""
    <style>

    .stApp a:first-child {
        display: none;
    }

    .css-15zrgzn {display: none}
    .css-eczf16 {display: none}
    .css-jn99sy {display: none}
    
    .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
    </style>
    """, unsafe_allow_html = True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.css-hi6a2p {padding-top: 0rem;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model = YOLO("model/best.pt")
    return model

st.title("Altnova Balconies Detection")

# st.markdown("#### Detect Different types of Balconies")

# st.text('Drag and drop or upload a file')
image = st.file_uploader(label='Upload a file',type=['jpg', 'jpeg', 'png'],
                         help='Drag and drop or Upload a Picture for Detection',
                         label_visibility='hidden')
# picture = st.camera_input("Take a picture", help='Take A Picture')


predicted_class = 0

if image:
    model = load_model()
    names = model.model.names
    img = Image.open(image)
    img = ImageOps.exif_transpose(img)
    
    detection = model.predict(source=img)
    
    # boxes = detection[0].boxes.xywh.cpu()
    clss = detection[0].boxes.cls.cpu().tolist()
    # confs = detection[0].boxes.conf.float().cpu().tolist()

    if len(clss) != 0:
        predicted_class = names[int(clss[0])]
    else:
        predicted_class = 404

    #for box, cls, conf in zip(boxes, clss, confs):
        #predicted_class = names[int(cls)]
        # break

#if picture:
#    st.image(picture)

def display_info(predicted_class):

    if predicted_class == 'Nestor-Martin-N-3158-R':
        st.markdown("Detected Balocony:  **ALTNOVA-09 (RN) Nestor Martin (=10-RNS0)**")
        st.write("Nestor Martin, straight panel with one face, style Renaissance Flamande, nr 3158")
        st.image('resources/1.png')

    elif predicted_class == 'Nestor-Martin-N-3130-B':
        st.markdown("Detected Balcony: **10-BNS1 Nestor Martin N° 3130**")
        st.write("Nestor Martin, model with « belly » Style Renaissance Flamande N° 3130.")
        st.image("resources/1B.png")

    elif predicted_class == 'Cruls-de-Zeelhem-N-1191':
        st.markdown("Detected Balcony: **15-BNS0 Cruls de Zeelhem N°1191 | 43-RNS0 Cruls de Zeelhem N°1191**")
        st.write("""De Zeelhem Cruls N° 1191 Série R” for standard width panels – the leafs on the corners of the balcony have N°1170.
                The original commercial catalogue mentions that this was “a modèle de réclame” (a publicity model). De Zeelhem Cruls N° 1191 Série R” 
                for standard width panels –. The original commercial catalogue mentions that this panel exists in straight and bellied 
                configuration. It was “often asked for”. It also exists in bellied panels (43-RNS0)""")
        st.image("resources/2.png")

    elif predicted_class == 'Nestor-Martin-2748':
        st.markdown("Detected Balcony: **31-BNS0 Nestor Martin N°2748**")
        st.write("Nestor Martin, model with “belly” N° 2748")
        st.image("resources/3.png")

    elif predicted_class == 'Nestor-Martin-N-3211':
        st.markdown("Detected Balcony: **24-BNS0 Nestor Martin motief = 3211 (R)**")
        st.write("""Nestor Martin N°3211 Style Flemish Renaissance” for standard width panels –
                The illustration from the original commercial catalogue shows a flat panel, 
                but the picture shows that there has been a bellied execution as well""")
        st.image("resources/4.png")

    elif predicted_class == 'Nestor-Martin-N-3181-R':
        st.markdown("Detected Balcony: **45-RNS0 Nestor Martin N° 3181**")
        st.write("""Nestor Martin N°3181 Style Flemish Renaissance” for standard width panels –
                The illustration from the original commercial catalogue shows a flat panel,
                but the picture shows that there has been a bellied execution as well.""")
        st.image("resources/5.png")

    elif predicted_class == 'Nestor-Martin-N-3181-B':
        st.markdown("Detected Balcony: **GDEBALU2-N (B) Nestor Martin (motief = 3181 R)**")
        st.write("""Nestor Martin N°3181 Style Flemish Renaissance” for standard width panels – 
                The illustration from the original commercial catalogue shows a flat panel,
                but the picture shows that there has been a bellied execution as well.""")
        st.image("resources/5B.png")

    elif predicted_class == 'Cruls-1235':
        st.markdown("Detected Balcony: **ALTNOVA-10 (R) Cruls N° 1235 – Série A**")
        st.write("""The illustration from the original commercial catalogue shows a flat panel,
                but the picture shows that there has been a bellied execution as well""")
        st.image("resources/6.png")

    elif predicted_class == 'Nestor-Martin-3064':
        st.markdown("Detected Balcony: **44-RNS0 Nestor martin N°3064 | 14-BNS0 Nestor martin N°3064**")
        st.write("""Nestor Martin N°3064 for standard width panels – 
                The illustration from the original commercial catalogue shows a bellied panel, 
                we did not find the straight panel illustration in the catalogue (so far)""")
        st.image("resources/7.png")

    elif predicted_class == 'Nestor-Martin-3345':
        st.markdown("Detected Balcony: **09-RNS0 Nestor Martin N°3281 | DUJAR-01 (B) Nestor Martin N°3345**")
        st.write("""The illustration from the original Nestor Martin’s commercial catalogue shows a flat panel N° 3281
                “Style Esthétique” – esthetic style. Nestor Martin N°3064 for standard width panels""")
        st.image("resources/8.png")

    elif predicted_class == 'Cruls-1194':
        st.markdown("Detected Balcony: **GDEBALU-3 Cruls N°1194 – Série R | ALTNOVA-17 (N) (B) Cruls N°1194 – Série R**")
        st.write("""The illustration from the original catalogue from the casting company Cruls de Zeelhem.
                The catalogue mentions that the model exists in straight and belly execution and that it is being frequently asked
                for (i.e. it is a popular model)""")
        st.image("resources/9.png")

    elif predicted_class == 404:
            st.error("Sorry unable to detect any Balconies in the Image.")


display_info(predicted_class)