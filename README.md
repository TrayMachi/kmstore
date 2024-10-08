
# KMStore

Store for keyboard & mouse.





## Tugas 2
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
## Tugas 3
## Data Delivery dalam Sebuah Platform
Dalam platform tentu kita perlu data delivery yang bertujuan untuk membuat client berinteraksi dengan data yang dibutuhkan. Tanpa data delivery, platform yang kita buat rasanya akan mati karena tidak ada proses pertukaran data yang dibutuhkan sehingga fungsi sebuah platform tersebut tidak berjalan secara maksimal
## XML atau JSON?
Menurut saya, JSON lebih populer dan lebih dipilih oleh para pengembang (termasuk saya) karena formatnya yang mudah dipahami dan diprosesnya yang lebih mudah dibanding XML, selain itu JSON juga lebih ringan dan lebih cepat dalam segi peforma, sehingga untuk web skala besar akan cenderung memilih JSON karena alasan peforma tersebut.
## Method is_valid() pada Form Django
Method is_valid() berguna untuk menvalidasi input user yang dimasukan ke dalam form yang buat, method ini juga dapat mengirim error apabila ada input yang kosong karena tidak dianggap valid oleh method tersebut.
## csrf_token di Django
`csrf_token` diperlukan guna menghindari serangan CSRF di web yang berbasiskan Django. Serangan CSRF dapat terjadi dengan cara sebuah situs berbahaya me-request ke web yang berisi authenticated user. Nantinya hal ini menyebabkan kebocoran data. Sehingga, untuk menghindari request aneh dari luar, csrf_token diperlukan guna menyortir request mana yang sah untuk diberikan akses me-request.
## Checklist Step by Step
- Membuat forms.py
Saya membuat file bernamakan forms.py di directory main, nantinya file ini akan berisi meta data perihal model apa yang saya ingin jadikan form, fields yang saya perlukan untuk dbuat form (berdasarkan model yang telah saya buat), dan yang terakhir penamaan label.
```
from django.forms import ModelForm
from main.models import Keyboard, Mouse


class KeyboardForm(ModelForm):
    class Meta:
        model = Keyboard
        fields = ["name", "price", "stock", "switch", "brand", "image", "description"]
        labels = {
            "name": "Name",
            "price": "Price",
            "description": "Description",
            "stock": "Stock",
            "switch": "Switch",
            "brand": "Brand",
            "image": "Image",
        }

```
- Menambahkan forms ke dalam views
Setelah itu, saya membuat views yang berisikan validasi form tersebut dan sebuah render yang nantinya akan merender ui dari form tersebut
```
def create_keyboard(request):
    form = KeyboardForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")
    
    return render(request, "keyboard_form.html", {"form": form}) 
```

- Views untuk melihat objek dalam format XML, JSON, XML by ID, dan JSON by ID
Untuk yang bukan berdasarkan id, saya dapat menggunakan method `all()` untuk mengambil semua object yang ada pada model tersebut. Lalu saya akan mengembalikan `HttpResponse` berupa serializers dalam bentuk XML atau JSON tergantung dengan request yang diminta. Untuk yang by ID saya menggunakan method `get(id=id)` dimana ID didapatkan melalui parameter dari sebuah request url.

#### Tanpa ID (semua)
```
def show_json_keyboard(request):
    data = Keyboard.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_keyboard(request):
    data = Keyboard.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

#### Dengan ID
```
def show_json_by_id_keyboard(request, id):
    data = Keyboard.objects.get(id=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id_keyboard(request, id):
    data = Keyboard.objects.get(id=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

- Routing GET request
Routing saya tambahkan pada file urls.py yang dimana untuk yang tanpa ID (semua) dapat diakses pada route `json/keyboard/` dan `xml/keyboard/` sedangkan untuk yang dengan ID saya buat pada route `json/keyboard/<str:id>` dan `xml/keyboard/<str:id>` yang dimana `<str:id>` mengartikan sebuah parameter dengan nama variable id dengan tipe data string. Jadinya nanti hanya menampilkan data yang memiliki id tersebut.

#### Tanpa ID (semua)
```
path('json/keyboard/', show_json_keyboard, name='show_json_keyboard')
path('xml/keyboard/', show_xml_keyboard, name='show_xml_keyboard')
```

#### Dengan ID
```
path('json/mouse/<str:id>/', show_json_by_id_mouse, name='show_json_by_id_mouse')
path('xml/keyboard/<str:id>/', show_xml_by_id_keyboard, name='show_xml_by_id_keyboard')
```





## API Reference

#### Get all keyboard items JSON promise

```http
  GET /json/keyboard
```
#### Get all keyboard items XML promise

```http
  GET /json/keyboard
```


#### Get item by id JSON promise

```http
  GET /json/keyboard/<str:id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |



#### Get item by id XML promise

```http
  GET /xml/keyboard/<str:id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |






## Tugas 4
## Perbedaan HttpResponseRedirect() dan redirect()
- `HttpResponseRedirect()` 
Berfungsi sebagai mengembalikan respons HTTP yang nantinya akan melakukan redirect ke URL yang ditentukan melalui parameter dalam bentuk string

Contoh:
```
return HttpResponseRedirect('/example/url/')
```

- `redirect()`
Memiliki fungsi yang sama seperti `HttpResponseRedirect()` hanya saja terdapat tambahan yaitu mengalihkan client ke dalam views. fungsi `redirect()` dalam pembuatannya terdapat `HttpResponseRedirect()` di dalamnya, yang artinya `redirect()` merupakan shortcut dari `HttpResponseRedirect()`.

Contoh:
```
return redirect('my_view_name')
```
## Cara Kerja Penghubungan Model Product dengan User
Cara menghubungkan User dengan Model yang kita buat adalah dengan cara membuat attribute pada model yang mengandung Foreign Key di dalamnya. Nantinya Foreign Key ini akan mereferensikan kepada Primary Key User.

Contoh:
```
class Keyboard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
```

Penjelasan:
- Attribute author menyimpan Foreign Key User, Foreign Key ini berfungsi untuk mengidentifikasi object Keyboard ini dimiliki oleh siapa.
- Terjadi relasi one-to-many antara User dengan model Keyboard yang artinya User dapat memiliki banyak Keyboard yang nantinya kita dapat me-filter berdasarkan id User.

## Perbedaan antara Authentication dan Authorization
- Authentication
Adalah proses untuk mengidentifikasi dan mengverifikasi username/email ada di dalam database atau tidak. Jika ada maka akan mengecek apakah password yang diberikan valid atau tidak, jika valid maka proses Authentication selesai yang artinya User berhasi melakukan login.
- Authorization
Adalah metode untuk mengatur akses yang diberikan ke User. Contohnya seperti User tidak dapat mendapatkan akses yang hanya boleh dilakukan oleh admin. Ketidakbolehan itu adalah penyebab dari Authorization apa saja yang User punya dan tidak punya.

- Implementasi di Django
Di Django terdapat metode bawaan untuk Authentication, salah satunya adalah `login()`, fungsi ini akan mengverifikasi username dan password yang user masukan di dalam form. Bagusnya metode bawaan ini adalah password user sebelum disimpan dilakukan hashing terlebih dahulu.

Untuk Authorization terdapat decorator yang dapat digunakan pada views, contohnya seperti 
```
@login_required(login_url="/login")
def show_json_by_author(request):
    keyboard_listings = Keyboard.objects.filter(author=request.user)
    mouse_listings = Mouse.objects.filter(author=request.user)
    data = list(chain(keyboard_listings, mouse_listings))
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )
``` 
decorator ini menandakan bahwa fungsi `show_json_by_author` dapat diakses hanya kepada user yang sudah mmelakukan login.
## Bagaimana Django Mengingat Pengguna yang Telah Login?
Di Django terdapat sessionId yang disimpan melalui cookies. sessionId ini akan mengingat user mana yang sedang login berdasarkan sessionId tersebut. sessionId yang di dalam cookies nantinya akan dihapus apabila user melakukan logout.
- Kegunaan Lain dari Cookies
Kegunaan lain dari Cookies adalah dapat tidak hilang walaupun kita keluar dari website tersebut. Cookies tersebut akan terus ada di dalam device user selama user tidak melakukan logout, menghapus Cookies secara manual, dan tidak expired. Selain itu, Cookies juga dapat membantu menyimpan data yang sifatnya sementara dan tidak diperlukan disimpan di dalam database, tetapi disarankan untuk tidak menaruh data sensitif di dalam Cookies.
- Apakah Semua Cookies Aman digunakan?
Terdapat Cookies yang tidak aman, yaitu jika seseorang sengaja melakukan Cross Site Scripting (XSS) untuk mencuri data Cookies orang lain. Maka dari itu kita sebagai developer tidak boleh asal menaruh data sensitif yang ada di dalam Cookies. Selain itu, kita juga harus melakukan perlindungan terhadap Cookies yaitu dengan mengatur
`HttpOnly` pada Cookies untuk mencegah pengaksesan Cookies melalui javascript sehingga terhindar dari serangan XSS.
## Step by Step Tugas 4
- Mengimplementasi Login, Register, dan Logout
Mula - mula saya menambahkan fungsi pada views.py, saya menggunakan method bawaan python untuk Login, Register, dan Logout.
- Register
Untuk register saya membutuhkan form melalui `UserCreationForm(request.POST)` untuk meminta input pengguna yang ingin mendaftar, setelah valid maka saya akan mengembalikan pesan sukses dan mengembalikan halaman ke login. Views ini nantinya akan dapat diakses melalui url `path("register/", register, name="register")` dan merender template `register.html`
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:login")
    context = {"form": form}
    return render(request, "register.html", context)

```
- Login
Untuk login saya juga membutuhkan form dengan menggunakan method bawaan `AuthenticationForm(data=request.POST)` jika form valid dan method `login(request, user)` berhasil, maka user berhasil logindan akan menyimpan cookies berupa sessionId.
``` 
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {"form": form}
    return render(request, "login.html", context)
```
- Logout
Akan menghapus sessionId dari cookies dan mengembalikan ke halaman login.
```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie("last_login")
    return response
```
- Menghubungkan Model dengan User
Untuk menghubungkan model dengan user saya menambahkan Foreign Key pada setiap model yang saya mau, yang nantinya ketika user membuat object pada model tersebut, di dalam attribute author akan terdapat id user sebagai referensi dari Foreign Key.
```
class Keyboard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ....
```
- Menampilkan Informasi User yang sedang Login
Untuk menampilkan informasi User saya dapat melakukan pada request pada view show_main saya. Saya melakukan request juga terhadap cookies yang sudah saya buat untuk menyimpan last login User. Saya juga menambahkan variable `your_listing` yang berisi setiap object yang telah dibuat oleh User.
```
@login_required(login_url="/login")
def show_main(request):
    keyboard_listings = Keyboard.objects.filter(author=request.user)
    mouse_listings = Mouse.objects.filter(author=request.user)
    your_listing = list(chain(keyboard_listings, mouse_listings))
    context = {
        .....
        "current_user": request.user.username,
        "your_listing": your_listing,
        "last_login": request.COOKIES["last_login"],
        ....
    }

    return render(request, "main.html", context)
```


# Tugas 5

## CSS selector untuk suatu elemen HTML
Pada CSS terdapat banyak selector yang bisa kita gunakan untuk men-styling elemen HTML. Berikut urutan prioritas selector yang ada pada CSS:

- Properti `!important`
Jika terdapat properti !important pada sebuah selector, maka hal tersebut akan menjadi prioritas paling tinggi dalam penge-style-nya

- Inline Selector `style`
Selector ini terdapat di dalam sebuah elemen HTML atau yang biasa disebut sebagai attribute dari elemen HTML itu sendiri. Selector ini akan diprioritaskan dibandingkan yang ada di file CSS (kecuali jika ada `!important`)

- ID Selector `#id`
Selector ini biasanya ditandai dengan pagar `#example` yang artinya itu merupakan style dari elemen HTML dengan id `example`

- Class Selector `.class`
Selector ini biasanya ditandai dengan attribute dari elemen HTML seperti `class=yourClass`

- Tag Selector
Selector ini akan mempengaruhi tag yang di-style contohnya seperti `p, h1, h2, span, dll`

- Universal Selector `*`
Selector ini merupakan prioritas paling rendah yang dimana selector ini akan mempengaruhi styling dari semua elemen HTML

## Responsive Design
Responsive Design berguna agar seluruh kalangan device pengguna dapat merasakan pengalaman pengguna yang nyaman. Selain itu, Responsive Design juga menjual daya tarik yang dimiliki oleh sebuah aplikasi agar aplikasi tersebut lebih dilirik dan dipadati pengguna.

- Contoh aplikasi dengan Responsive Design:
Web - web yang terdapat di repo github ini

- Contoh aplikasi yang belum Responsive Design:
pws
## Perbedaan antara Margin, Border, dan Padding

Terdapat 3 Layer dalam sebuah container, yaitu `Margin`, `Border`, dan `Padding`

- Margin: Ruang di luar elemen, memisahkan elemen dari elemen lainnya. Dapat diatur dengan `margin: 10px;` untuk semua sisi atau margin-top, margin-right, margin-bottom, margin-left untuk sisi tertentu.

- Border: Garis yang mengelilingi elemen, memberikan batas visual. Dapat diimplementasikan dengan `border: 2px solid black;`, yang mengatur ketebalan, style, dan warna border.

- Padding: Ruang di dalam elemen, antara konten dan border. Diatur dengan `padding: 10px;` untuk semua sisi, atau dengan cara yang sama seperti margin untuk sisi tertentu.
## Flex Box dan Grid Layout 
Flex Box dan Grid Layout adalah metode untuk melakukan pengaturan tata letak sebuah elemen atau kontainer agar lebih responsif.

- Flex Box: model tata letak satu dimensi yang dirancang untuk mengatur elemen dalam satu baris (horizontal) atau satu kolom (vertikal). Ini memudahkan penataan elemen dalam suatu kontainer dengan mengatur ruang dan ukuran elemen secara otomatis.

- Grid Layout: model tata letak dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom. Ini memberikan lebih banyak kontrol atas 
ukuran dan posisi elemen dalam grid yang dibentuk.

Untuk menentukan menggunakan Grid atau Flex tergantung dari kebutuhan yang kita perlukan. Jika kita hanya perlu model tata letak satu dimensi layaknya sebuah navbar, maka disarankan menggunakan Flex. Tetapi, jika kita ingin membuat sebuah dashboard yang disebut dengan bento dashboard, maka memerlukan model tata letak dua dimensi seperti Grid.

## Step-by-Step Tugas 5
- Fungsi Delete dan Edit
Untuk fungsi delete saya menggunakan metode bawaan python yaitu delete() yang berguna untuk menghapus sebuah objek yang dimana objek yang saya miliki sudah saya `request` berdasarkan `id` yang didapat.

Untuk Edit mirip seperti create biasa dan bahkan saya menggunakan url create saya, hanya sajaa saya menambahkan instance atau default value untuk form tersebut yang dimana default value berasalkan dari value yang mau di-edit.

- Desain pada Template HTML

Untuk desain saya menggunakan `Tailwind Play CDN`, tetapi saya juga menggunakan Vanilla CSS untuk default style. Pada form desain yang saya buat lumayan mirip, saya menggunakan `for loop` untuk mengiterasi `form field` yang mendesignnya dengan responsif.

Untuk bagian hero saya menambahkan animasi pulse dan beberapa responsiveness dari `hover:`. Saya juga menerapkan flex dan grid agar website tetap terlihat bagus di device apapun.

Untuk bagian Card saya menggunakan border dan flex vertical untuk mengatur isi dari card tersebut. Untuk mengatur kumpulan dari Card saya menggunakan grid dengan jumlah kolom maksimal 4, tetapi pada saat mobile jumlah kolomnya hanya 1.

Untuk navbar saya menggunakan `fixed` yang dimana akan tetap di atas selama kita meng-scroll. Saya juga menambahkan sentuhan `backdrop-blur` yang dimana akan memberikan glass effect kepada background navbar saya.

# Tugas 6
## Manfaat JavaScript
Manfaat JavaScript untuk pengembangan aplikasi web adalah untuk mendukung interaktifitas website. Selain itu, JavaScript juga dapat berguna untuk membuat website kita menjadi dynamic.
## Fungsi await
Fungsi `await` terutama saat menggunakan `fetch()` adalah agar memastikan bahwa `fetching` yang kita lakukan selesai terlebih dahulu sebelum menjalankan command selanjutnya. Jika kita tidak memakai `await`, maka akan bertabrakan dengan command selanjutnya yang dimana memungkinkan bahwa command selanjutnya membutuhkan hasil `fetching` yang kita mau, sehingga jika `fetching` belum selesai, akan menimbulkan kekeliruan.
## csrf_exempt pada View
Penggunaan decorator `csrf_exempt` pada view yang akan digunakan untuk AJAX POST di framework seperti Django umumnya diperlukan untuk menangani `CSRF (Cross-Site Request Forgery)`, yaitu sebuah mekanisme keamanan yang memastikan bahwa permintaan POST datang dari sumber yang terpercaya (yaitu dari aplikasi atau situs yang sama). Namun, pada beberapa kasus tertentu, kita perlu menggunakan decorator ini untuk mengecualikan view tersebut dari perlindungan `CSRF`.
## Pembersihan Data Input di Backend
Backend dapat membuat proses validasi tanpa diganggu oleh pengguna melalui front-end, jika pada front-end validasi dapat dilewati oleh pengguna yang memanipulasi request menggunakan query-query atau dengan menonaktifkan JavaScript.
## Step-by-Step Tugas 6
- AJAX GET
Untuk melakukannya, saya menambahkan tag script di bagian kedua paling bawah pada `main.html`. Saya membuat fungsi yang dapat meng-fetching method `GET` yang sudah saya buat, setelah itu saya membuat fungsi refresh yang nantinya akan mengiterasi hasil dari fungsi `fetching` yang sudah saya buat, sehingga produk yang saya buat dapat ditampilkan secara realtime.

- AJAX POST
Saya membuat komponen modal dengan memanfaatkan class `hidden` dan dapat juga di-show dengan memanfaatkan JavaScript. Akan ada tombol yang dimana jika dipencet akan mengarah kepada fungsi untuk membuka modal dengan cara menghapus class `hidden` yang saya taruh pada modal. Setelah modal muncul akan ada form `POST` yang mengarah ke api ke views yang sudah buat khusus untuk `AJAX`. Setelah melakukan `POST` akan melakukan fungsi refresh agar user tidak perlu reload page untuk mendapatkan info produk yang baru, lalu modal akan menghapus semua input.