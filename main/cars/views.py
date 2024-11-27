from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

data = [
    {
        "id": "1",
        "title": "Toyota Corolla",
        "description": "A reliable compact sedan known for its efficiency and comfort.",
        "image": "https://scene7.toyota.eu/is/image/toyotaeurope/cors0001a_web_2023:Medium-Landscape?ts=0&resMode=sharp2&op_usm=1.75,0.3,2,0",
    },
    {
        "id": "2",
        "title": "Honda Civic",
        "description": "A popular compact car with sporty design and advanced features.",
        "image": "https://media.ed.edmunds-media.com/honda/civic/2025/oem/2025_honda_civic_sedan_si_fq_oem_1_1280.jpg",
    },
    {
        "id": "3",
        "title": "Ford Mustang",
        "description": "An iconic American muscle car delivering power and performance.",
        "image": "https://m.atcdn.co.uk/ect/media/%7Bresize%7D/3e7dbe41afea4891a15e05034e6360e1.jpg",
    },
    {
        "id": "4",
        "title": "Tesla Model 3",
        "description": "An all-electric sedan with cutting-edge technology and impressive range.",
        "image": "https://res.cloudinary.com/unix-center/image/upload/c_limit,dpr_3.0,f_auto,fl_progressive,g_center,h_240,q_auto:good,w_385/eghq9ct3evxunl27bkhl.jpg",
    },
    {
        "id": "5",
        "title": "BMW 3 Series",
        "description": "A luxury sedan offering a blend of performance and sophistication.",
        "image": "https://www.topgear.com/sites/default/files/cars-car/inline-gallery/2023/09/1-BMW-M3-CS.jpg",
    },
]


def index(request):

    return render(request, 'cars/index.html', {'data': data})


def add(request):

    content = {}

    if request.method == 'POST':
        # Get form data from POST request
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.POST.get('image')

        content = {
            "id": str(len(data) + 1),
            "title": title,
            "description": description,
            "image": image,
        }

        data.append(content)

    return render(request, 'cars/add.html', {"content": content})


def detail(request, id):

    car = data[id-1]

    return render(request, 'cars/detail.html', {"car": car})


def tezefunc(request):

    arr = ["test1sdgsdgsdgsdgsdgsdg", "test2sdgsdgsdg", "tsdgsdgest3"]

    date = datetime.now()

    title = "Teze Page"

    num = 234.56

    my_data = {
        "arr": arr,
        "title": title,
        "date": date,
        "num": num,
    }

    return render(request, "cars/teze.html", my_data)


def errorPage(request, exception):
    return HttpResponseNotFound("Sehife yoxdu")


def testPage(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    return HttpResponse(f"Ad={name}, age={age}")
