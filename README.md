
# KMStore

Store for keyboard & mouse.

## Demo

Cek tautan ini untuk melihat website [KMStore](http://tristan-agra-kmstore.pbp.cs.ui.ac.id/)


## Implementation

- Membuat proyek django bernama `kmstore`. 
Di dalam directory ini kita dapat mengatur semua aplikasi kita mulai dari routing dan settings yang dapat kita atur melalui `settings.py` dan `urls.py`
```bash
django-admin startproject kmstore .
```

- Membuat aplikasi dengan nama `main`
Di directory ini kita akan memulai membuat model kita, yaitu `keyboard` dan `mouse`
```bash
python manage.py startapp main
```

- Routing main ke dalam proyek
Untuk routing ke main kita dapat menambahkan path pada proyek di `urls.py` dengan `URLconf`
```bash
urlpatterns = [
    # ... snip ...
    path('', include('main.urls')),
    # ... snip ...
]
```

- Modelling produk keyboard dan mouse
Kita dapat membuka `models.py` pada aplikasi main dan mulai mendefinisikan class model kita mulai dari menamai atribut pada setiap class dengan `nama`, `deskripsi`, dan `harga`. Lalu, saya memakai tambahan `imageField` disini, sehingga membutuhkan library `pillow` install pillow dengan
```bash
pip install pillow
```

- Membuat fungsi show_main pada `views.py` yang berisi `title`, `name`, `npm`, dan `class` lalu mengembalikan `render` dengan template name `main.html` dan mulai mengedit tampilan sederhana menggunakan [Tailwind Play CDN](https://tailwindcss.com/docs/installation/play-cdn)

- Menambahkan routing di `urls.py` dengan function views agar fungsi yang kita buat pada `views.py` dapat dijalankan
```bash
urlpatterns = [
    # ... snip ...
    path('', show_main, name='show_main'),
    # ... snip ...
]
```

- Melakukan deployment di Pacil Web Service (PWS)

## Alur Bagan Django
Alur kerja Django dimulai ketika client mengirimkan request ke server. Request ini pertama kali diproses oleh `urls.py`, yang bertugas mencocokkan URL yang diminta dengan pola yang sesuai. Setelah pola URL ditemukan, request diteruskan ke `views.py`, yang menangani logika sesuai dengan permintaan tersebut.

Di dalam `views.py`, jika diperlukan, akan ada interaksi dengan models.py untuk operasi read or write data. Selain itu, `views.py` juga memproses data yang diperoleh dan kemudian menggunakan `templates` untuk merender halaman HTML atau memberikan respons lain yang sesuai.

Hasil akhirnya, baik itu halaman web yang dirender atau data dalam format lain, akan dikirimkan kembali ke client sebagai response.

## What is Git
Git adalah version controller system yang dapat digunakan oleh para pengembang perangkat lunak untuk melacak perubahan yang telah dibuat. Selain itu Git juga dapat mengatur proyek yang kita buat. Kita dapat berkolaborasi dengan pengembang lain, membuat branch baru untuk sebuah proyek, mengrollback proyek apabila ada kesalahan, dan masih banyak lagi. Hal ini bertujuan untuk meningkatkan efisiensi di dalam pengembangan perangkat lunak, khususnya jika kita mempunyai proyek yang kompleks dan membutuhkan kerja sama team.

## Django untuk Pemula
Menurut saya Django cocok untuk memulai pembelajaran perangkat lunak dikarenakan Django digunakan untuk rapid development yang dimana sudah disediakan template untuk dipenuhi agar menjadi website, selain itu Django juga framework fullstack yang mendukung hubungan Front-end dan Back-end dalam satu framework, sehingga pemula dapat mudah mempelajari pengembangan perangkat lunak.

## ORM Pada Model Django
Singkatnya ORM adalah intrepeter yang menginteprete sebuah bahasa ke dalam bahasa SQL melalui migration. Pada model di Django kita hanya perlu mendeskripsikan model beserta attributenya dengan syntax python, nantinya model tersebut akan di migration menjadi bahasa SQL yang akan di simpen pada folder `migrations`.