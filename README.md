# VISUALISASI TRAFFIC DENGAN OPENGL

## HOW TO RUN THE PROGRAM?
#### CLONE REPOSITORY
<code>git clone https://github.com/unormiesable/OpenGL_Traffic.git</code>

#### PYTHON VIRTUAL ENVIRONMENT
###### WINDOWS :
<pre>
    <code>python -m venv virtual</code>
    <code>source virtual/Scripts/activate</code>
</pre>

###### LINUX :
<pre>
    <code>python -m venv virtual</code>
    <code>source virtual/bin/activate</code>
</pre>

#### INSTALL DEPENDENCIES
<pre>
    <code>python install -r requirements.txt</code>
</pre>

#### JALANKAN PROGRAM
<pre>
    <code>python main.py</code>
</pre>

## KAMUS DASAR OPENGL
### VBO (Vertex Buffer Object)
* Vertex Coordinate
* Color Data
* Texture Coordinate
* Normal Vector
* (Dan beberapa data lain misalnya seperti "Weight" pada vertex)

** Main : Hold data raw di GPU

### VAO (Vertex Array Object)
* Referesi/Penunjuk ke VBO yang digunakan
* Layout Attr Vertex
* Bindng State

** Main : Cara baca VBO

### FBO (Frame Buffer)
* Texture and Color Buffer (sebagai output image)
* Depth Buffer (z-testing)
* Stencil buffer DKK

** Main : Konfig render target (Selain layar utama)

### GBUFFER (Geometry Buffer) -Belum Implementasi
* Position
* Normal
* Albedo
* Specular
* Depth

** Main : Sekumpulan texture dalam FBO untuk deferred shading (Menyimpan data per pixel)