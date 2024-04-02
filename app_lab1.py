import streamlit as st



# This should be the first command executed.
st.set_page_config(page_title="My Personal Website", page_icon=":tada:", layout="wide")

# Adding a header and a subheader
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

.custom-google-font {
    font-family: 'Roboto', sans-serif;
    font-size: 80px;
    font-weight: 700; /* Bold */
    color: #2E8B57; /* SeaGreen */
}
</style>
<div class="custom-google-font">Welcome to Xinyi Zhou's Website!</div>
""", unsafe_allow_html=True)
st.write("Here you'll find information about me, my projects, and how to get in touch.")

st.image('./images/me.png', width=400)

# Using columns to add an about section
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

.custom-google-font {
    font-family: 'Roboto', sans-serif;
    font-size: 45px;
    font-weight: 700; /* Bold */
    color: #2E8B57; /* SeaGreen */
}
</style>
<div class="custom-google-font">About me</div>
""", unsafe_allow_html=True)
st.write("Xinyi Zhou, from the MSTI program at the University of Washington, is focusing on novel XR-based interfaces for human-robot interaction, aiming to develop new interaction patterns through AR technologies. With three years of prior experience in XR, AI technologies, startups, and investments. I enjoy sports like climbing, hiking, swimming, and basketball, and have a keen interest in backpacking and exploring. Additionally, my continuous curiosity has led me to learn and explore areas like psychology, innovative education, regional politics, and multimedia art.")

# Adding a section for Projects
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

.custom-google-font {
    font-family: 'Roboto', sans-serif;
    font-size: 45px;
    font-weight: 700; /* Bold */
    color: #2E8B57; /* SeaGreen */
}
</style>
<div class="custom-google-font">Projects</div>
""", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.subheader("AeroNex")
    st.write("AeroNex pioneers in revolutionizing hazardous environment man- agement through cutting-edge aerial intelligence, integrating drone technology with advanced image processing. Our mission is to enhance operational safety and efficiency in industries like construction and warehousing, where environmental hazards and inventory management pose significant challenges..")
    st.image("./images/abstract graphic2.png", caption="Project 1 visualization")

with col2:
    st.subheader("Nvidia Cloud XR ")
    st.write("this projectproposes a new workflow by NVIDlA CloudXR streaming technology toachieve high-precision visualization and a rich interactive experience onhand-held devices. Such heritage can be promoted and popularised moreconveniently.")
    st.image("./images/XR.png", caption="Project 2 visualization")

with col1:
    st.subheader("Project 3")
    st.write("Waitting for update.")
    st.image("./images/test1.png", caption="Project 3 visualization")

with col2:
    st.subheader("Project 4")
    st.write("Waitting for update.")
    st.image("./images/test1.png", caption="Project 4 visualization")


# Contact Form
st.header("Contact Me")
contact_form = """
<form action="https://formsubmit.co/your-email-address" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)


# Footer
st.write("Thank you for visiting my personal website!")





# Update the geometry of the cube to make it bigger
webgl_html = """
<!DOCTYPE html>
<html>
<head>
  <title>Interactive WebGL with Streamlit</title>
  <style>
    canvas { width: 100%; height: 100% }
  </style>
</head>
<body>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script>
    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    var renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);
    
    // Parameters for the BoxGeometry have been increased to make the cube larger
    var geometry = new THREE.BoxGeometry(3, 3, 3); // Width, Height, Depth increased from 1 to 2
    var material = new THREE.MeshBasicMaterial({ color: 0xffffff });
    var cube = new THREE.Mesh(geometry, material);
    scene.add(cube);
    
    camera.position.z = 5;
    
    var mouse = { x: 0, y: 0 };
    
    document.addEventListener('mousemove', onDocumentMouseMove, false);
    
    function onDocumentMouseMove(event) {
      event.preventDefault();
      mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
      mouse.y = - (event.clientY / window.innerHeight) * 2 + 1;
    }
    
    function animate() {
      requestAnimationFrame(animate);
      
      cube.rotation.x += (mouse.y * 0.05);
      cube.rotation.y += (mouse.x * 0.05);
      
      renderer.render(scene, camera);
    }
    animate();
  </script>
</body>
</html>
"""

# Use Streamlit's HTML component to display the interactive WebGL content
st.components.v1.html(webgl_html, height=350)
