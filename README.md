# VISUALISASI TRAFFIC DENGAN OPENGL

## HOW TO RUN THE PROGRAM ?
#### CLONE REPOSITORY
<pre>
    <code>git clone https://github.com/unormiesable/OpenGL_Traffic.git</code>
    <code>cd OpenGL_Traffic</code>
</pre>

#### PYTHON VIRTUAL ENVIRONMENT
###### WINDOWS :
<pre>
    <code>python -m venv virtual</code>
    <code>virtual\Scripts\activate</code>
</pre>

###### LINUX :
<pre>
    <code>python -m venv virtual</code>
    <code>source virtual/bin/activate</code>
</pre>

#### INSTALL DEPENDENCIES
<pre>
    <code>pip install -r requirements.txt</code>
</pre>

#### JALANKAN PROGRAM
<pre>
    <code>python main.py</code>
</pre>

## CARA MENGGUNAKAN ?
#### KONTROL KAMERA

* Tekan "TAB" untuk mengubah mode kamera

###### FLY MODE (DEFAULT)
<pre>
* W                     =       MAJU
* A                     =       GERAK KE KIRI
* D                     =       GERAK KE KANAN
* S                     =       MUNDUR
* Q                     =       GERAK KE BAWAH
* E                     =       GERAK KE ATAS
* MOUSE                 =       MENGUBAH ARAH PANDANG
* SHIFT                 =       BERGERAK LEBIH CEPAT
* CTRL                  =       BERGERAK LEBIH LAMBAT
</pre>

* Pergerakan kamera akan bergerak dengan koordinat lokal

###### ORBIT MODE
<pre>
* ↑ (PANAH ATAS)        =       MENGORBIT KE ATAS
* ← (PANAH KIRI)        =       MENGORBIT KE KIRI
* → (PANAH KANAN)       =       MENGORBIT KE KANAN
* ↓ (PANAH BAWAH)       =       MENGORBIT KE BAWAH
* MOUSE                 =       MENGORBIT SESUAI DENGAN ARAH MOUSE
* SHIFT                 =       BERGERAK LEBIH CEPAT
* CTRL                  =       BERGERAK LEBIH LAMBAT
</pre>

#### PENGATURAN SCENE
###### SPAWN MOBIL
* Pada scene default disediakan 4 mobil untuk setiap lanenya 
<pre>
* 1                     =       MENAMBAH MOBIL PADA LANE 1
* 2                     =       MENAMBAH MOBIL PADA LANE 2
* 3                     =       MENAMBAH MOBIL PADA LANE 3
* 4                     =       MENAMBAH MOBIL PADA LANE 4
</pre>

###### DELETE MOBIL
* Pada scene default disediakan 4 mobil untuk setiap lanenya 
<pre>
* 6                     =       MENGHAPUS MOBIL PADA LANE 1
* 7                     =       MENGHAPUS MOBIL PADA LANE 2
* 8                     =       MENGHAPUS MOBIL PADA LANE 3
* 9                     =       MENGHAPUS MOBIL PADA LANE 4
</pre>
* Jumlah mobil minimum adalah 4 untuk setiap lane
* Jumlah mobil maksimum adalah 7 untuk setiap lane

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
