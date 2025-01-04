import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from ultralytics import YOLO
from PIL import Image, ImageOps

st.set_page_config(
    page_title = 'Balcony Detection',
    page_icon = "🪟",
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
st.markdown(hide_streamlit_style, unsafe_allow_html = True)

@st.cache_resource
def load_model():
    model = YOLO("model/best.pt")
    return model

st.title("Altnova Balconies Detection")

image = st.file_uploader(label='Upload a file',type=['jpg', 'jpeg', 'png'],
                         help='Drag and drop or Upload a Picture for Detection',
                         label_visibility='hidden')

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

if image:
    st.image(image)

def perform_next_steps():
    if st.button('**PROCEED TO NEXT STEPS**', use_container_width = True):
        switch_page('next-steps')
    
    st.markdown("<p style='padding-top:10px'> </p>", unsafe_allow_html=True)

def display_info(predicted_class):

    if predicted_class == '01-RN':
        st.markdown("Detected Balocony:  **01-RNS0 NM C0M10**")
        st.write("Nestor Martin, straight panel with one face, style Renaissance Flamande, nr 3158")
        st.image('resources/1.png')
        perform_next_steps()

    elif predicted_class == '01-BN':
        st.markdown("Detected Balcony: **01-BNS1 NM C0M0**")
        st.write("Nestor Martin, model with « belly » Style Renaissance Flamande N° 3130.")
        st.image("resources/1B.png")
        perform_next_steps()

    elif predicted_class == '02-RN':
        st.markdown("Detected Balcony: **02-RNS0 CR C0M0**")
        st.write(""" “De Zeelhem Cruls N° 1191 Série R” for standard width panels –. The original commercial catalogue mentions that this 
                 panel exists in straight and bellied configuration. It was “often asked for”. It also exists in bellied panels (43-RNS0). 
                 The catalogue mentions furthermore that “this model is very nice and often asked for”.""")
        st.image("resources/2.png")
        perform_next_steps()

    elif predicted_class == '02-BN':
        st.markdown("Detected Balcony: **02-BNS0 CR C0M0**")
        st.write(""" “De Zeelhem Cruls N° 1191 Série R” for standard width panels – the leafs on the corners of the balcony have N°1170. 
                 The original commercial catalogue mentions that this was “a modèle de réclame” (a publicity model). 
                 It also exists in bellied panels (43-RNS0). The catalogue mentions furthermore that “this model is very nice and often asked".""")
        st.image("resources/2B.png")
        perform_next_steps()

    elif predicted_class == '03-RN':
        st.markdown("Detected Balcony: **03-RNS0 NM C0M0**")
        st.write("Nestor Martin, model with “belly” N° 2748")
        st.image("resources/3.png")
        perform_next_steps()

    elif predicted_class == '04-RN':
        st.markdown("Detected Balcony: **04-RNS0 NM C0M0**")
        st.write(""" “Nestor Martin N°3211 Style Flemish Renaissance” for standard width panels – The illustration from the original commercial 
                 catalogue shows a flat panel, but the picture shows that there has been a bellied execution as well. We did not find the 
                 picture of the bellied panel in the catalogueso far.""")
        st.image("resources/4.png")
        perform_next_steps()

    elif predicted_class == '05-RN':
        st.markdown("Detected Balcony: **05-RNS1 NM C0M0**")
        st.write("""Nestor Martin N°3181 Style Flemish Renaissance” for standard width panels –
                The illustration from the original commercial catalogue shows a flat panel,
                but the picture shows that there has been a bellied execution as well.""")
        st.image("resources/5.png")
        perform_next_steps()

    elif predicted_class == '05-BN':
        st.markdown("Detected Balcony: **05-BNS1 NM C0M10**")
        st.write("""Nestor Martin N°3181 Style Flemish Renaissance” for standard width panels –
                The illustration from the original commercial catalogue shows a flat panel,
                but the picture shows that there has been a bellied execution as well.""")
        st.image("resources/5.png")
        perform_next_steps()

    elif predicted_class == '06-RN':
        st.markdown("Detected Balcony: **06-RNS0 CR C0M0**")
        st.write("""The illustration from the original commercial catalogue shows a flat panel,
                but the picture shows that there has been a bellied execution as well""")
        st.image("resources/6.png")
        perform_next_steps()

    elif predicted_class == '07-RN':
        st.markdown("Detected Balcony: **07-RNS0 NM C0M0**")
        st.write("""Nestor Martin N°3064 for standard width panels – 
                The illustration from the original commercial catalogue shows a bellied panel, 
                we did not find the straight panel illustration in the catalogue (so far)""")
        st.image("resources/7.png")
        perform_next_steps()

    elif predicted_class == '07-BN':
        st.markdown("Detected Balcony: **07-BNS0 NM C0M0**")
        st.write("""Nestor Martin N°3064 for standard width
                panels – The illustration from the original
                commercial catalogue shows a bellied panel""")
        st.image("resources/7.png")
        perform_next_steps()

    elif predicted_class == '08-RN':
        st.markdown("Detected Balcony: **08-RNS0 NM C0M0**")
        st.write("""The illustration from the original Nestor Martin’s commercial catalogue shows a flat panel N° 3281
                “Style Esthétique” – esthetic style. Nestor Martin N°3064 for standard width panels""")
        st.image("resources/8.png")
        perform_next_steps()

    elif predicted_class == '08-BN':
        st.markdown("Detected Balcony: **08-BNS1 NM C0M10**")
        st.write("""The illustration from the original Nestor Martin’s commercial catalogue shows a bellied panel N° 3345""")
        st.image("resources/8.png")
        perform_next_steps()

    elif predicted_class == '09-RN':
        st.markdown("Detected Balcony: **09-RNS0 CR C0M0**")
        st.write("""The illustration from the original catalogue from the casting company Cruls de Zeelhem. 
                 The catalogue mentions that the model exists in straight and belly execution and that it is being 
                 frequently asked for (i.e. it is a popular model)""")
        st.image("resources/9.png")
        perform_next_steps()

    elif predicted_class == '09-BN':
        st.markdown("Detected Balcony: **09-BNS1 CR C1M11**")
        st.write("""The illustration from the original catalogue from the casting company Cruls de Zeelhem. 
                 The catalogue mentions that the model exists in straight and belly execution and that it is being 
                 frequently asked for (i.e. it is a popular model)""")
        st.image("resources/9B.png")
        perform_next_steps()

    elif predicted_class == '12-RN':
        st.markdown("Detected Balcony: **12-RNS1 G0 C0M0**")
        st.error("Sorry no historical information for this Balcony found.")
        perform_next_steps()

    elif predicted_class == '12-BNS1 G0 C1M11':
        st.markdown("Detected Balcony: **12-BNS1 G0 C1M11**")
        st.error("Sorry no historical information for this Balcony found.")
        perform_next_steps()

    elif predicted_class == '13-RN':
        st.markdown("Detected Balcony: **13-RNS0 G0 C0M11**")
        st.error("Sorry no historical information for this Balcony found.")
        perform_next_steps()

    elif predicted_class == '15-RN':
        st.markdown("Detected Balcony: **15-RNS0 CR C0M0**")
        st.image("resources/15.png")
        perform_next_steps()

    elif predicted_class == '16-RN':
        st.markdown("Detected Balcony: **16-RNS0 G0 C0M11**")
        st.error("Sorry no historical information for this Balcony found.")
        perform_next_steps()

    elif predicted_class == 404:
            st.error("Sorry unable to detect any Balconies in the Image.")

            if st.button('**REPORT ERROR**', use_container_width = True):
                switch_page('next-steps')


display_info(predicted_class)